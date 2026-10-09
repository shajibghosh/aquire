'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
const root = path.resolve(__dirname, '..');
const atlas = JSON.parse(fs.readFileSync(path.join(root, 'data/atlas.json'), 'utf8'));

(async () => {
  const executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
  fs.mkdirSync(path.join(root, 'test-results'), {recursive: true});
  const browser = await chromium.launch({headless: true, ...(executablePath ? {executablePath} : {})});
  try {
    const context = await browser.newContext({viewport: {width: 1440, height: 1100}, acceptDownloads: true});
    const page = await context.newPage();
    const errors = [];
    const networkRequests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', request => {
      if (/^https?:/.test(request.url())) networkRequests.push(request.url());
    });
    await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
    await page.waitForSelector('.resource');
    assert.equal(await page.locator('h1').textContent(), 'AQuIRE');
    assert.ok((await page.title()).includes('Awesome Quantum Information Research Explorer'));
    assert.ok((await page.locator('meta[http-equiv="Content-Security-Policy"]').getAttribute('content')).includes("connect-src 'none'"));
    const blocked = await page.evaluate(() => {
      window.unapprovedScriptExecuted = false;
      const injected = document.createElement('script');
      injected.textContent = 'window.unapprovedScriptExecuted = true;';
      document.head.appendChild(injected);
      injected.remove();
      return !window.unapprovedScriptExecuted;
    });
    assert.ok(blocked, 'Browser policy should block unapproved inline scripts');
    const filtered = () => page.evaluate(() => window.atlasTest.getFiltered());
    const records = async () => {
      const ids = new Set(await filtered());
      return atlas.resources.filter(r => ids.has(r.id));
    };
    assert.equal((await filtered()).length, atlas.resources.length);
    await page.screenshot({path: path.join(root, 'test-results', 'desktop.png')});

    await page.locator('#q').fill('"surface code"');
    assert.ok((await filtered()).length > 0, 'Phrase search should match resources');
    await page.locator('#type').selectOption('Journal article');
    await page.locator('#from').fill('2020');
    const combined = await records();
    assert.ok(combined.length > 0, 'Combined phrase/type/year query should match');
    assert.ok(combined.every(r => r.type === 'Journal article' && r.year >= 2020));

    await page.locator('#reset').click();
    await page.locator('#domain').selectOption('D10');
    await page.locator('#topic').selectOption('D10T02');
    const topic = await records();
    assert.ok(topic.length > 0);
    assert.ok(topic.every(r => r.assignments.some(a => a.topic_id === 'D10T02')));
    await page.locator('#reset').click();
    await page.locator('#dated').selectOption('unknown');
    const undated = await records();
    assert.ok(undated.length > 0);
    assert.ok(undated.every(r => r.year === null));
    for (const type of ['Book', 'Conference paper', 'Tutorial']) {
      await page.locator('#reset').click();
      await page.locator('#type').selectOption(type);
      const list = await records();
      assert.ok(list.length > 0);
      assert.ok(list.every(r => r.type === type));
    }

    await page.locator('#reset').click();
    await page.locator('[data-save]').first().click();
    await page.locator('#saved').check();
    assert.equal((await filtered()).length, 1);
    await page.reload();
    assert.equal((await page.evaluate(() => atlasTest.getSaved())).length, 1);
    await page.locator('#saved').check();
    const downloading = page.waitForEvent('download');
    await page.locator('#json').click();
    const download = await downloading;
    assert.equal(download.suggestedFilename(), 'AQuIRE_Filtered.json');
    const destination = path.join(root, 'test-results', 'filtered.json');
    await download.saveAs(destination);
    const exported = JSON.parse(fs.readFileSync(destination, 'utf8'));
    assert.equal(exported.length, 1);
    assert.equal(exported[0].id, (await filtered())[0]);
    assert.ok(!Object.hasOwn(exported[0], 'searchText'), 'Export excludes runtime index');

    await page.locator('#reset').click();
    await page.locator('[data-tab="taxonomy"]').click();
    await page.locator('#taxSearch').fill('GKP');
    assert.equal(await page.locator('.domain').count(), 1);
    await page.locator('[data-tab="paths"]').click();
    assert.equal(await page.locator('.path').count(), atlas.paths.length);
    await page.locator('[data-tab="methods"]').click();
    assert.equal(await page.locator('#domainTable tr').count(), atlas.taxonomy.length);
    await page.locator('[data-tab="catalog"]').click();
    await page.locator('#theme').click();
    assert.ok(await page.locator('body').evaluate(body => body.classList.contains('dark')));
    await page.locator('#theme').click();
    await page.setViewportSize({width: 390, height: 844});
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 2));
    await page.screenshot({path: path.join(root, 'test-results', 'mobile.png')});
    assert.deepEqual(errors, []);
    assert.deepEqual(networkRequests, [], 'The explorer must not issue outbound HTTP requests during local search and exports');
    // Existing saved resources migrate once; subsequent AQuIRE preferences take priority.
    const migrationContext = await browser.newContext();
    const migrationPage = await migrationContext.newPage();
    const expectedId = atlas.resources[0].id;
    await migrationPage.addInitScript(id => {
      localStorage.setItem('quantum-atlas-saved', JSON.stringify([id]));
      localStorage.setItem('quantum-atlas-dark', 'true');
    }, expectedId);
    await migrationPage.goto(pathToFileURL(path.join(root, 'index.html')).href);
    assert.deepEqual(await migrationPage.evaluate(() => atlasTest.getSaved()), [expectedId]);
    assert.equal(await migrationPage.evaluate(() => localStorage.getItem('aquire-saved')), JSON.stringify([expectedId]));
    assert.ok(await migrationPage.locator('body').evaluate(body => body.classList.contains('dark')));
    await migrationPage.locator('#theme').click();
    await migrationPage.reload();
    assert.equal(await migrationPage.evaluate(() => localStorage.getItem('aquire-dark')), 'false');
    assert.ok(!await migrationPage.locator('body').evaluate(body => body.classList.contains('dark')));
    await migrationContext.close();
    console.log(`Browser smoke checks passed for ${atlas.resources.length} resources.`);
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error); process.exitCode = 1;});
