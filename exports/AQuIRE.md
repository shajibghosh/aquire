# AQuIRE

**Awesome Quantum Information Research Explorer**

1,600 unique resources across 30 major categories, 164 topics, and 792 fine subcategories. Snapshot date: 8 October 2026.

This atlas supports systematic exploration of quantum computing, quantum machine learning, hardware, fault tolerance, software, and related technologies. Use the taxonomy to locate a question, then inspect the associated resource records and their source links. The catalog contains authentic retrieved metadata and official pages; classification is title screened and does not replace reading the papers.

## How to use this package

Open the interactive HTML in a browser for combined search and filters. Use the DOCX or PDF for sequential reading. The Markdown contains the full taxonomy and catalog. CSV and JSON support reuse. Resource identifiers such as Q0001 match across all formats.

## Catalog composition

| Resource type | Unique records |
| --- | ---: |
| Book | 20 |
| Book chapter | 148 |
| Conference paper | 296 |
| Course | 6 |
| Documentation | 13 |
| Edited book | 3 |
| Institutional resource | 4 |
| Journal article | 1005 |
| Lecture notes | 1 |
| Posted content | 56 |
| Reference book | 4 |
| Report | 14 |
| Software repository | 20 |
| Standard | 3 |
| Tutorial | 7 |

1,546 records have registered DOI metadata; 54 official pages were retrieved. Supplied years span 1966 to 2026. Undated web resources are retained as undated.

## Sources and verification

### Scope and taxonomy

This is a broad research and learning map, not a claim to enumerate every possible topic or every available resource. The hierarchy contains major categories, topics, and fine subcategories. Networking, sensing, and classical post quantum cryptography are explicitly included as adjacent areas. These areas should not be conflated with quantum computation.

### Authentic source records

Scholarly entries were retrieved from the Crossref REST API using publisher deposited metadata and identifiable DOIs. Official web entries were retrieved from first party institutions, software projects, or providers and required a successful HTTP response and an identifiable page title. Failed or unrelated sources were excluded. The catalog is a metadata based bibliography, not a full text systematic review or a ranking of research quality.

### Subject assignments and finer tags

Topic searches were screened using title wording and subject context. Ambiguous results received editorial corrections or exclusion. Multiple supported discovery paths are retained as related topics. Fine subcategory tags are conservative lexical assignments from titles. Topic level only means that no precise fine tag was established; the full vocabulary shown in the taxonomy is not automatically assigned to every resource.

### Dates and publication types

Years and publication types follow retrieved bibliographic metadata. Posted content is kept separate from journal articles because peer review cannot be inferred from a DOI. Books and book chapters are distinct resource types, and separate editions can be retained when their years differ. Undated official pages stay undated; the retrieval year is not substituted for a publication year. Conference names are shown only when the source supplies an event or a proceedings venue.

### Deduplication and selection

DOIs and canonical web URLs were deduplicated. Identical normalized titles with matching lead author and publication year were also merged, preferring a journal or conference record over posted content when a match was clear. The selection balances topic coverage and retains curated foundational material. The same stable Q identifiers and resource records are used in HTML, DOCX, Markdown, PDF, CSV, and JSON.

### What the verification status means

Registered DOI means that a corresponding bibliographic record was retrieved from Crossref. It does not mean that every DOI resolver or full text download was individually tested. Page retrieved means that the official web page and its title were successfully retrieved on the snapshot date. Links can redirect, change, require authentication, or lead to paywalled content after delivery. No publication year, author, venue, or review status was invented to fill missing fields.

### Coverage and limitations

Coverage is selective and varies by topic, especially standards, economics, and specialized engineering. Bibliographic identity is stronger evidence than an unverified reference string, but it is not a guarantee of scientific validity, peer review quality, or practical advantage. Metadata can contain publisher errors or incomplete fields. Papers were not systematically screened for retractions and corrections across all external databases. Use the source record and paper itself when a claim is important.

### Offline use and exports

The HTML is self contained and uses no external scripts or fonts. Search, topic browsing, sorting, saved resources, and exports operate locally. External resource links need internet access. Browser saved resources use local storage and are not sent to a server. Search supports words combined with AND and quoted phrases. Journal, conference, author, publisher, year, type, topic, and verification filters can be combined. Exports contain all filtered results, while printing prints the currently displayed page of cards.

Primary source documentation: [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/), [NIST quantum information science](https://www.nist.gov/quantum-information-science), [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning), and [MIT OpenCourseWare](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/).

## Reading paths

### Foundations to algorithms

Build the mathematical and algorithmic vocabulary needed to read quantum computing research.

1. Review Hilbert spaces, tensor products, and unitary operators. Topic D01T01.
2. Work with states, density matrices, and partial traces. Topic D01T02.
3. Understand gates, circuits, and universal models. Topic D03T01.
4. Implement a small quantum Fourier transform. Topic D05T01.
5. Study phase estimation with explicit precision and overlap assumptions. Topic D05T02.
6. Compare oracle query cost with complete implementation cost. Topic D04T02.

Suggested output: A tested notebook for small algorithms, with input assumptions and classical comparisons.

### Quantum machine learning and hybrid AI

Connect classical ML experience to defensible quantum learning experiments.

1. Account for the cost of encoding the dataset. Topic D10T01.
2. Compare a quantum kernel with classical kernels on the same split. Topic D10T02.
3. Build a variational classifier with a reproducible training loop. Topic D10T03.
4. Measure gradients and investigate trainability. Topic D09T04.
5. Read generalization and sample complexity results. Topic D10T06.
6. Evaluate GPU simulation cost and memory before scaling experiments. Topic D24T04.

Suggested output: A benchmark report with held out metrics, uncertainty, encoding cost, and strong classical baselines.

### Quantum chemistry and simulation

Follow a physical problem from model definition to algorithm and resource estimate.

1. Choose the basis, active space, observable, and accuracy. Topic D08T01.
2. Map fermionic operators to qubits and use valid symmetries. Topic D08T02.
3. Run a small VQE study with reference energies. Topic D09T01.
4. Compare digital simulation methods and error budgets. Topic D07T01.
5. Study block encoding and qubitization access assumptions. Topic D06T01.
6. Translate the algorithm into logical and physical resources. Topic D08T04.

Suggested output: A small molecule or lattice demonstration and a transparent resource estimate.

### Error correction to fault tolerant architecture

Connect code properties to a complete logical computing system.

1. Construct stabilizer checks and logical operators. Topic D19T01.
2. Simulate syndrome extraction under an explicit noise model. Topic D19T02.
3. Measure decoder accuracy and latency. Topic D20T06.
4. Map logical operations through lattice surgery or another stated method. Topic D20T03.
5. Include non Clifford resources and factory scheduling. Topic D20T02.
6. Combine distance, hardware, and runtime assumptions in an estimate. Topic D20T05.

Suggested output: Logical error scaling plots and an architecture aware cost model.

### Hardware and experimental reliability

Evaluate one hardware platform using control and characterization evidence.

1. Select a platform and understand its physical qubit model. Topic D12T01.
2. Study control pulses and parameter constraints. Topic D18T01.
3. Review calibration and drift tracking. Topic D18T05.
4. Interpret benchmarking with its model assumptions. Topic D22T02.
5. Investigate leakage, crosstalk, and correlated errors. Topic D18T04.
6. Assess mitigation with sampling overhead and bias. Topic D21T01.

Suggested output: A platform comparison that distinguishes device metrics from logical performance.

### Quantum software and GPU systems

Build an executable workflow and understand its full software stack.

1. Learn one supported programming framework. Topic D23T01.
2. Inspect intermediate representation and classical control semantics. Topic D23T02.
3. Measure the effect of mapping and routing. Topic D23T04.
4. Estimate state vector and density matrix memory. Topic D24T01.
5. Benchmark CPU, GPU, and distributed simulation where available. Topic D24T04.
6. Add semantic and statistical checks to the workflow. Topic D23T06.

Suggested output: A versioned project with circuit definitions, environment details, and performance measurements.

### Networking and security

Separate quantum networking protocols from classical post quantum security.

1. Understand teleportation and the required classical communication. Topic D26T01.
2. Study repeaters and memory and loss constraints. Topic D26T02.
3. Analyze entanglement distribution and routing. Topic D26T03.
4. Read QKD security with finite size and device assumptions. Topic D27T01.
5. Compare delegation, blindness, and verifiability. Topic D27T03.
6. Study classical post quantum cryptography as a distinct deployment path. Topic D27T05.

Suggested output: A protocol comparison with explicit trust models, costs, and deployment requirements.

### Sensing and scientific applications

Choose a scientific target and distinguish computational from sensing claims.

1. Define an estimation task and attainable measurement strategy. Topic D28T01.
2. Read sensing performance with bandwidth and spatial resolution. Topic D28T02.
3. Identify a concrete scientific or engineering observable. Topic D29T04.
4. Evaluate numerical algorithm assumptions and conditioning. Topic D06T06.
5. Specify what can be verified with the available measurements. Topic D22T06.
6. Prepare a reproducible comparison with complete uncertainty reporting. Topic D30T04.

Suggested output: An application study with a specified observable, validation plan, and practical cost accounting.

## Questions to take to every resource

1. What task, input model, observable, and accuracy are specified?
2. Is this a theorem, simulation, experiment, review, tutorial, or roadmap?
3. Does the reported cost include preparation, oracles, compilation, shots, and classical processing?
4. What strong classical baseline is appropriate?
5. Which noise and trust assumptions support the conclusion?
6. Can the reported result be reproduced from the available record?

## Detailed taxonomy and complete resource catalog

## D01 Foundations and mathematical tools

The language of quantum information connects linear algebra, probability, physical states, and measurements. These resources build the prerequisites needed to read algorithm and hardware papers.

Prerequisites: Linear algebra, probability, and introductory quantum mechanics.

Assessment focus: State normalization, operator properties, measurement definitions, and physical interpretation.

Primary catalog resources in this category: 42.

### D01T01 Linear algebra and Hilbert spaces

Hilbert spaces provide the state space for quantum systems; tensor products describe composition. Linear algebra is also the implementation language of gates and many simulators.

Fine subcategories: State vectors; inner products; tensor products; eigenvalues; spectral decomposition; unitary operators.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0001 Hilbert space in quantum mechanics

Wenbing MENG, Pan ZHOU.
Journal article | 2024 | Region - Educational Research and Reviews | vol. 6 | no. 7 | pp. 93.
Identifier and resource: [10.32629/rerr.v6i7.2344](https://doi.org/10.32629/rerr.v6i7.2344).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.32629%2Frerr.v6i7.2344); retrieved 2026-10-08.

#### Q0002 Algebra and Hilbert space structures induced by quantum probes

Go Kato, Masaki Owari, Koji Maruyama.
Journal article | 2020 | Annals of Physics | vol. 412 | pp. 168046 | article 168046.
Identifier and resource: [10.1016/j.aop.2019.168046](https://doi.org/10.1016/j.aop.2019.168046).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.aop.2019.168046); retrieved 2026-10-08.

#### Q0003 Quantum Information Science I | Physics | MIT OpenCourseWare

Author metadata not supplied.
Course | 2018 | MIT OpenCourseWare.
Identifier and resource: [Official resource](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/); retrieved 2026-10-08.

#### Q0004 Hilbert space representations of the quantum *-algebra $\mathcal{U}_q(su_{1,1})$

David Dubray.
Journal article | 2015 | Banach Journal of Mathematical Analysis | vol. 9 | no. 3 | pp. 261-277.
Identifier and resource: [10.15352/bjma/09-3-19](https://doi.org/10.15352/bjma/09-3-19).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15352%2Fbjma%2F09-3-19); retrieved 2026-10-08.

#### Q0005 Quantum Mechanics in Hilbert Space

Author metadata not supplied.
Book chapter | 2015 | Hilbert Space and Quantum Mechanics | pp. 611-696.
Identifier and resource: [10.1142/9789814635844_0019](https://doi.org/10.1142/9789814635844_0019).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2F9789814635844_0019); retrieved 2026-10-08.

#### Q0006 A class of Hilbert space representations of the quantum plane and the quantum algebra Uq(sl2)

Asao Arai.
Journal article | 2008 | Reports on Mathematical Physics | vol. 61 | no. 2 | pp. 171-180.
Identifier and resource: [10.1016/s0034-4877(08)00013-x](https://doi.org/10.1016/s0034-4877(08)00013-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fs0034-4877%2808%2900013-x); retrieved 2026-10-08.

#### Q0007 Hilbert space representation of an algebra of observables forq-deformed relativistic quantum mechanics

W. Zippold.
Journal article | 1995 | Zeitschrift f�r Physik C Particles and Fields | vol. 67 | no. 4 | pp. 681-686.
Identifier and resource: [10.1007/bf01553995](https://doi.org/10.1007/bf01553995).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbf01553995); retrieved 2026-10-08.

#### Q0008 Quantum diffusions on the algebra of all bounded operators on a hilbert space

RL Hudson.
Book chapter | 1989 | Lecture Notes in Mathematics | pp. 256-269.
Identifier and resource: [10.1007/bfb0083556](https://doi.org/10.1007/bfb0083556).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbfb0083556); retrieved 2026-10-08.

### D01T02 Quantum states and density operators

Density operators represent both pure states and statistical mixtures. Reduced states are essential when only part of a larger system is measured or controlled.

Fine subcategories: Pure states; mixed states; Bloch sphere; partial trace; reduced states; purification.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q0009 Geometry of Quantum States

Ingemar Bengtsson, Karol Życzkowski.
Book | 2017 | Cambridge University Press.
Identifier and resource: [10.1017/9781139207010](https://doi.org/10.1017/9781139207010).
ISBN: 9781107026254; 9781139207010; 9781107656147.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781139207010); retrieved 2026-10-08.

#### Q0010 Quantum Computation and Quantum Information

Michael A. Nielsen, Isaac L. Chuang.
Book | 2012 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511976667](https://doi.org/10.1017/cbo9780511976667).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2FCBO9780511976667); retrieved 2026-10-08.

#### Q0011 Geometry of Quantum States

Ingemar Bengtsson, Karol Zyczkowski.
Book | 2006 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511535048](https://doi.org/10.1017/cbo9780511535048).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2FCBO9780511535048); retrieved 2026-10-08.

#### Q0012 Ph219/CS219 Quantum Computation

Author metadata not supplied.
Course | 2026 | Caltech John Preskill.
Identifier and resource: [Official resource](https://preskill.caltech.edu/ph219/ph219_2026.html).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://preskill.caltech.edu/ph219/ph219_2026.html); retrieved 2026-10-08.

#### Q0013 Feynman Path Integral and Landau Density Matrix in Probability Representation of Quantum States

Olga V. Man’ko.
Journal article | 2025 | Physics | vol. 7 | no. 4 | pp. 66.
Identifier and resource: [10.3390/physics7040066](https://doi.org/10.3390/physics7040066).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fphysics7040066); retrieved 2026-10-08.

#### Q0014 Measuring the Density Matrix of Quantum-Modeled Cognitive States

Wendy Xiomara Chavarría-Garza, Osvaldo Aquines-Gutiérrez, Ayax Santos-Guevara, Humberto Martínez-Huerta, Jose Ruben Morones-Ibarra, Jonathan Rincon Saucedo.
Journal article | 2024 | Quantum Reports | vol. 6 | no. 2 | pp. 156-171.
Identifier and resource: [10.3390/quantum6020013](https://doi.org/10.3390/quantum6020013).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fquantum6020013); retrieved 2026-10-08.

#### Q0015 Density matrix renormalization group algorithm for mixed quantum states

Chu Guo.
Journal article | 2022 | Physical Review B | vol. 105 | no. 19 | article 195152.
Identifier and resource: [10.1103/physrevb.105.195152](https://doi.org/10.1103/physrevb.105.195152).
Fine tags: mixed states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.105.195152); retrieved 2026-10-08.

#### Q0016 Neutral excitations of quantum Hall states: A density matrix renormalization group study

Prashant Kumar, F. D. M. Haldane.
Journal article | 2022 | Physical Review B | vol. 106 | no. 7 | article 075116.
Identifier and resource: [10.1103/physrevb.106.075116](https://doi.org/10.1103/physrevb.106.075116).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.106.075116); retrieved 2026-10-08.

#### Q0017 Physics 219 Course Information

Author metadata not supplied.
Lecture notes | Undated | Caltech John Preskill.
Identifier and resource: [Official resource](https://preskill.caltech.edu/ph229/index.html).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://preskill.caltech.edu/ph229/index.html); retrieved 2026-10-08.

### D01T03 Quantum measurements

Measurements convert quantum states into classical outcomes according to a specified measurement model. General measurements require POVMs and instruments rather than only orthogonal projectors.

Fine subcategories: Projective measurements; POVMs; weak measurement; quantum instruments; measurement disturbance.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0018 Implementing positive-operator-valued-measurement elements in photonic circuits for performing minimum quantum state tomography of path qudits

W. R. Cardoso, D. F. Barros, M. R. Barros, S. Pádua.
Journal article | 2019 | Physical Review A | vol. 99 | no. 6 | article 062324.
Identifier and resource: [10.1103/physreva.99.062324](https://doi.org/10.1103/physreva.99.062324).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.99.062324); retrieved 2026-10-08.

#### Q0019 A Measure of Quantum Correlation Based on von Neumann Entropy and Positive Operator-Valued Measurement

Yang Leng, Wen-Juan Li.
Journal article | 2018 | International Journal of Theoretical Physics | vol. 57 | no. 11 | pp. 3480-3484.
Identifier and resource: [10.1007/s10773-018-3862-8](https://doi.org/10.1007/s10773-018-3862-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10773-018-3862-8); retrieved 2026-10-08.

#### Q0020 Research on Deep Space Optical Quantum OFDM System Based on Positive Operator Valued Measurement Detection

Xiao Zhao, Xiaolin Zhou, Chongbin Xu, Xin Wang.
Book chapter | 2018 | Communications in Computer and Information Science | pp. 307-317.
Identifier and resource: [10.1007/978-981-10-7877-4_28](https://doi.org/10.1007/978-981-10-7877-4_28).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-10-7877-4_28); retrieved 2026-10-08.

#### Q0021 Realization of Single-Qubit Positive-Operator-Valued Measurement via a One-Dimensional Photonic Quantum Walk

Zhihao Bian, Jian Li, Hao Qin, Xiang Zhan, Rong Zhang, Barry C. Sanders, Peng Xue.
Journal article | 2015 | Physical Review Letters | vol. 114 | no. 20 | article 203602.
Identifier and resource: [10.1103/physrevlett.114.203602](https://doi.org/10.1103/physrevlett.114.203602).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.114.203602); retrieved 2026-10-08.

#### Q0022 QUANTUM THREE-QUBIT W-STATE SHARING VIA POSITIVE OPERATOR-VALUED MEASUREMENT AND PROJECTIVE MEASUREMENT

MING-QIANG BAI, ZHI-WEN MO.
Journal article | 2012 | Modern Physics Letters B | vol. 26 | no. 31 | pp. 1250208.
Identifier and resource: [10.1142/s0217984912502089](https://doi.org/10.1142/s0217984912502089).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0217984912502089); retrieved 2026-10-08.

#### Q0023 Quantum Tasks with Non-maximally Quantum Channels via Positive Operator-Valued Measurement

Jia-Yin Peng, Ming-Xing Luo, Zhi-Wen Mo.
Journal article | 2012 | International Journal of Theoretical Physics | vol. 52 | no. 1 | pp. 253-265.
Identifier and resource: [10.1007/s10773-012-1328-y](https://doi.org/10.1007/s10773-012-1328-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10773-012-1328-y); retrieved 2026-10-08.

#### Q0024 Symmetric Remote Single-Qubit State Preparation via Positive Operator-Valued Measurement

Zhang-Yin Wang.
Journal article | 2010 | International Journal of Theoretical Physics | vol. 49 | no. 6 | pp. 1357-1369.
Identifier and resource: [10.1007/s10773-010-0316-3](https://doi.org/10.1007/s10773-010-0316-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10773-010-0316-3); retrieved 2026-10-08.

#### Q0025 Positive-operator and projection valued measurements in quantum key distribution

Howard E. Brandt.
Journal article | 2007 | Journal of Modern Optics | vol. 54 | no. 16-17 | pp. 2357-2363.
Identifier and resource: [10.1080/09500340701639557](https://doi.org/10.1080/09500340701639557).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F09500340701639557); retrieved 2026-10-08.

### D01T04 Quantum channels and open systems

Quantum channels describe physical transformations including noise and discarded subsystems. Open system models connect microscopic dynamics to experimentally observed decoherence.

Fine subcategories: Kraus representations; completely positive maps; Lindblad equations; Stinespring dilation; non Markovian dynamics.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0026 An Open-Quantum-Systems Theory of Quantum-Biological Communication Channels

Liang Dong.
Journal article | 2026 | IEEE Transactions on Molecular, Biological, and Multi-Scale Communications | vol. 12 | pp. 858-874.
Identifier and resource: [10.1109/tmbmc.2026.3716243](https://doi.org/10.1109/tmbmc.2026.3716243).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftmbmc.2026.3716243); retrieved 2026-10-08.

#### Q0027 Efficient simulation of open quantum systems coupled to a reservoir through multiple channels

Hanggai Nuomin, Jiaxi Wu, Peng Zhang, David N. Beratan.
Journal article | 2024 | The Journal of Chemical Physics | vol. 161 | no. 12 | article 124114.
Identifier and resource: [10.1063/5.0226183](https://doi.org/10.1063/5.0226183).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0226183); retrieved 2026-10-08.

#### Q0028 Transport in open quantum systems in the presence of lossy channels

Katha Ganguly, Manas Kulkarni, Bijay Kumar Agarwalla.
Journal article | 2024 | Physical Review B | vol. 110 | no. 23 | article 235425.
Identifier and resource: [10.1103/physrevb.110.235425](https://doi.org/10.1103/physrevb.110.235425).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.110.235425); retrieved 2026-10-08.

#### Q0029 Quantum Systems, Channels, Information

Alexander S. Holevo.
Edited book | 2019 | De Gruyter.
Identifier and resource: [10.1515/9783110642490](https://doi.org/10.1515/9783110642490).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1515%2F9783110642490); retrieved 2026-10-08.

#### Q0030 Quantum speed-up capacity in different types of quantum channels for two-qubit open systems

Wei Wu, Xin Liu, Chao Wang.
Journal article | 2018 | Chinese Physics B | vol. 27 | no. 6 | pp. 060302.
Identifier and resource: [10.1088/1674-1056/27/6/060302](https://doi.org/10.1088/1674-1056/27/6/060302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2F27%2F6%2F060302); retrieved 2026-10-08.

#### Q0031 The decay of quantum systems with a small number of open channels

F Dittes.
Journal article | 2000 | Physics Reports | vol. 339 | no. 4 | pp. 215-316.
Identifier and resource: [10.1016/s0370-1573(00)00065-x](https://doi.org/10.1016/s0370-1573(00)00065-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fs0370-1573%2800%2900065-x); retrieved 2026-10-08.

#### Q0032 GitHub - qutip/qutip: QuTiP: Quantum Toolbox in Python · GitHub

Author metadata not supplied.
Software repository | Undated | QuTiP.
Identifier and resource: [Official resource](https://github.com/qutip/qutip).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/qutip/qutip); retrieved 2026-10-08.

#### Q0033 QuTiP: Quantum Toolbox in Python — QuTiP 5.3 Documentation

Author metadata not supplied.
Documentation | Undated | QuTiP.
Identifier and resource: [Official resource](https://qutip.readthedocs.io/en/stable/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://qutip.readthedocs.io/en/stable/); retrieved 2026-10-08.

### D01T05 Quantum entropy and information measures

Information measures quantify uncertainty, correlations, and distinguishability. Operational meanings depend on the coding, estimation, or security task being studied.

Fine subcategories: Von Neumann entropy; relative entropy; mutual information; min entropy; data processing inequalities.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q0034 The Theory of Quantum Information

John Watrous.
Book | 2018 | Cambridge University Press.
Identifier and resource: [10.1017/9781316848142](https://doi.org/10.1017/9781316848142).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781316848142); retrieved 2026-10-08.

#### Q0035 Quantum Information Theory

Mark M. Wilde.
Book | 2016 | Cambridge University Press.
Identifier and resource: [10.1017/9781316809976](https://doi.org/10.1017/9781316809976).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781316809976); retrieved 2026-10-08.

#### Q0036 Quantum Information Theory

Mark M. Wilde.
Book | 2013 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9781139525343](https://doi.org/10.1017/cbo9781139525343).
ISBN: 9781107034259; 9781139525343.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2Fcbo9781139525343); retrieved 2026-10-08.

#### Q0037 Quantum Accessible Information and Classical Entropy Inequalities

A. S. Holevo, A. V. Utkin.
Journal article | 2026 | Lobachevskii Journal of Mathematics | vol. 47 | no. 6 | pp. 2499-2527.
Identifier and resource: [10.1134/s1995080226617704](https://doi.org/10.1134/s1995080226617704).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1995080226617704); retrieved 2026-10-08.

#### Q0038 Quantum dynamical entropy and dissipative information flows

Anonymous.
Journal article | 2026 | APS Open Science.
Identifier and resource: [10.1103/6hlj-9t5r](https://doi.org/10.1103/6hlj-9t5r).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F6hlj-9t5r); retrieved 2026-10-08.

#### Q0039 Quantum-inspired information entropy in multifield turbulence

Go Yatomi, Motoki Nakata.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 2 | article 023212.
Identifier and resource: [10.1103/physrevresearch.7.023212](https://doi.org/10.1103/physrevresearch.7.023212).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.023212); retrieved 2026-10-08.

#### Q0040 Quantum Entropy and Correlations in Quantum Information

Reinhold A. Bertlmann, Nicolai Friis.
Book chapter | 2023 | Modern Quantum Theory | pp. 659-703.
Identifier and resource: [10.1093/oso/9780199683338.003.0020](https://doi.org/10.1093/oso/9780199683338.003.0020).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Foso%2F9780199683338.003.0020); retrieved 2026-10-08.

#### Q0041 Quantum Information Dimension and Geometric Entropy

Fabio Anza, James P. Crutchfield.
Journal article | 2022 | PRX Quantum | vol. 3 | no. 2 | article 020355.
Identifier and resource: [10.1103/prxquantum.3.020355](https://doi.org/10.1103/prxquantum.3.020355).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.3.020355); retrieved 2026-10-08.

#### Q0042 Quantum Information Science | Media Arts and Sciences | MIT OpenCourseWare

Author metadata not supplied.
Course | 2006 | MIT OpenCourseWare.
Identifier and resource: [Official resource](https://ocw.mit.edu/courses/mas-865j-quantum-information-science-spring-2006/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://ocw.mit.edu/courses/mas-865j-quantum-information-science-spring-2006/); retrieved 2026-10-08.

## D02 Entanglement and quantum resources

Entanglement and other nonclassical resources supply capabilities that must be characterized separately from hardware size. Resource theory studies what operations can generate or consume each resource.

Prerequisites: Density operators, composite systems, and basic information measures.

Assessment focus: Allowed operations, resource monotones, witness validity, and operational task.

Primary catalog resources in this category: 42.

### D02T01 Entanglement detection and quantification

Entanglement criteria test whether a state is separable, while monotones quantify particular resources. Different measures need not order mixed states in the same way.

Fine subcategories: Witnesses; separability criteria; negativity; concurrence; entanglement entropy.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0043 Data-Driven Quantification of Quantum k-Entanglement via Machine Learning

Jie Guo, Jinchuan Hou, Xiaofei Qi, Kan He.
Journal article | 2026 | Entropy | vol. 28 | no. 7 | pp. 832.
Identifier and resource: [10.3390/e28070832](https://doi.org/10.3390/e28070832).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe28070832); retrieved 2026-10-08.

#### Q0044 Detection of quantum entanglement across the event horizon

Patryk Michalski, Andrzej Dragan.
Journal article | 2026 | Physical Review A | vol. 114 | no. 1 | article 012420.
Identifier and resource: [10.1103/1mch-w3zx](https://doi.org/10.1103/1mch-w3zx).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F1mch-w3zx); retrieved 2026-10-08.

#### Q0045 Entanglement detection via subsystem quantum Fisher information

Jiawei Zang, Wei Wu, Pingxing Chen.
Journal article | 2026 | Physical Review A | vol. 114 | no. 3 | article 032443.
Identifier and resource: [10.1103/kxxy-llb2](https://doi.org/10.1103/kxxy-llb2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fkxxy-llb2); retrieved 2026-10-08.

#### Q0046 Entanglement detection with quantum-inspired kernels and SVMs

Ana Martínez-Sabiote, Michalis Skotiniotis, Jara J. Bermejo-Vega, Daniel Manzano, Carlos Cano.
Journal article | 2026 | The Journal of Supercomputing | vol. 82 | no. 2 | article 100.
Identifier and resource: [10.1007/s11227-026-08229-7](https://doi.org/10.1007/s11227-026-08229-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11227-026-08229-7); retrieved 2026-10-08.

#### Q0047 Reliable entanglement detection via quantum generative adversarial model

Li Xu, Fengting Zhou, Jing Wang, Jin-Min Liang, Zongqiang Chen, Ming Li.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 26 | pp. 265103.
Identifier and resource: [10.1088/1402-4896/ae7e63](https://doi.org/10.1088/1402-4896/ae7e63).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae7e63); retrieved 2026-10-08.

#### Q0048 Quantification of Entanglement and Coherence with Purity Detection

He Lu, Ting Zhang, Graemn Smith, John Smolin, Lu Liu, Xu-Jie Peng, Qi Zhao, Davide Girolami et al..
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-3844047/v1](https://doi.org/10.21203/rs.3.rs-3844047/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-3844047%2Fv1); retrieved 2026-10-08.

#### Q0049 Quantification of entanglement and coherence with purity detection

Ting Zhang, Graeme Smith, John A. Smolin, Lu Liu, Xu-Jie Peng, Qi Zhao, Davide Girolami, Xiongfeng Ma et al..
Journal article | 2024 | npj Quantum Information | vol. 10 | no. 1 | article 60.
Identifier and resource: [10.1038/s41534-024-00857-2](https://doi.org/10.1038/s41534-024-00857-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-024-00857-2); retrieved 2026-10-08.

#### Q0050 Detection and quantification of entanglement with measurement-device-independent and universal entanglement witness*

Zhi-Jin Ke, Yi-Tao Wang, Shang Yu, Wei Liu, Yu Meng, Zhi-Peng Li, Hang Wang, Qiang Li et al..
Journal article | 2020 | Chinese Physics B | vol. 29 | no. 8 | pp. 080301.
Identifier and resource: [10.1088/1674-1056/ab9288](https://doi.org/10.1088/1674-1056/ab9288).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fab9288); retrieved 2026-10-08.

### D02T02 Bell nonlocality and contextuality

Bell nonlocality concerns correlations incompatible with local hidden variable models. Contextuality concerns dependence on measurement context and requires its own experimental assumptions.

Fine subcategories: Bell inequalities; loopholes; device independence; contextuality inequalities; self testing.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0051 Revealing hidden nonlocality and preparation contextuality for an arbitrary input Bell inequality

Asmita Kumari, Saikat Patra.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 34 | pp. 345101.
Identifier and resource: [10.1088/1402-4896/ae9993](https://doi.org/10.1088/1402-4896/ae9993).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae9993); retrieved 2026-10-08.

#### Q0052 Trade-off relations between Bell nonlocality and local Kochen–Specker contextuality in generalized Bell scenarios

Lucas E A Porto, Gabriel Ruffolo, Rafael Rabelo, Marcelo Terra Cunha, Paweł Kurzyński.
Journal article | 2024 | New Journal of Physics | vol. 26 | no. 8 | pp. 083028.
Identifier and resource: [10.1088/1367-2630/ad7167](https://doi.org/10.1088/1367-2630/ad7167).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fad7167); retrieved 2026-10-08.

#### Q0053 Contextuality or Nonlocality: What Would John Bell Choose Today?

Marian Kupczynski.
Journal article | 2023 | Entropy | vol. 25 | no. 2 | pp. 280.
Identifier and resource: [10.3390/e25020280](https://doi.org/10.3390/e25020280).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe25020280); retrieved 2026-10-08.

#### Q0054 Synchronous Observation of Bell Nonlocality and State-Dependent Contextuality

Peng Xue, Lei Xiao, G. Ruffolo, A. Mazzari, T. Temistocles, M. Terra Cunha, R. Rabelo.
Journal article | 2023 | Physical Review Letters | vol. 130 | no. 4 | article 040201.
Identifier and resource: [10.1103/physrevlett.130.040201](https://doi.org/10.1103/physrevlett.130.040201).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.130.040201); retrieved 2026-10-08.

#### Q0055 Assumption-Free Derivation of the Bell-Type Criteria of Contextuality/Nonlocality

Ehtibar N. Dzhafarov.
Journal article | 2021 | Entropy | vol. 23 | no. 11 | pp. 1543.
Identifier and resource: [10.3390/e23111543](https://doi.org/10.3390/e23111543).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe23111543); retrieved 2026-10-08.

#### Q0056 Classical causal models cannot faithfully explain Bell nonlocality or Kochen-Specker contextuality in arbitrary scenarios

J. C. Pearl, E. G. Cavalcanti.
Journal article | 2021 | Quantum | vol. 5 | pp. 518 | article 518.
Identifier and resource: [10.22331/q-2021-08-05-518](https://doi.org/10.22331/q-2021-08-05-518).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2021-08-05-518); retrieved 2026-10-08.

#### Q0057 Experimental observation of quantum contextuality beyond Bell nonlocality

Zheng-Hao Liu, Hui-Xian Meng, Zhen-Peng Xu, Jie Zhou, Sheng Ye, Qiang Li, Kai Sun, Hong-Yi Su et al..
Journal article | 2019 | Physical Review A | vol. 100 | no. 4 | article 042118.
Identifier and resource: [10.1103/physreva.100.042118](https://doi.org/10.1103/physreva.100.042118).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.100.042118); retrieved 2026-10-08.

#### Q0058 Sharing nonlocality and nontrivial preparation contextuality using the same family of Bell expressions

Asmita Kumari, A. K. Pan.
Journal article | 2019 | Physical Review A | vol. 100 | no. 6 | article 062130.
Identifier and resource: [10.1103/physreva.100.062130](https://doi.org/10.1103/physreva.100.062130).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.100.062130); retrieved 2026-10-08.

### D02T03 Coherence and resource theories

Resource theories specify free states and operations before defining a resource. Coherence, asymmetry, and entanglement are related but distinct examples.

Fine subcategories: Incoherent operations; asymmetry; conversion rates; resource monotones; coherence distillation.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0059 One-shot manipulation of coherence in dynamic quantum resource theory

Yu Luo.
Journal article | 2025 | Physical Review A | vol. 111 | no. 2 | article 022447.
Identifier and resource: [10.1103/physreva.111.022447](https://doi.org/10.1103/physreva.111.022447).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.022447); retrieved 2026-10-08.

#### Q0060 Generic aspects of the resource theory of quantum coherence

Fabio Deelan Cunden, Paolo Facchi, Giuseppe Florio, Giovanni Gramegna.
Journal article | 2021 | Physical Review A | vol. 103 | no. 2 | article 022401.
Identifier and resource: [10.1103/physreva.103.022401](https://doi.org/10.1103/physreva.103.022401).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.103.022401); retrieved 2026-10-08.

#### Q0061 Resource theory of quantum coherence with probabilistically nondistinguishable pointers and corresponding wave-particle duality

Chirag Srivastava, Sreetama Das, Ujjwal Sen.
Journal article | 2021 | Physical Review A | vol. 103 | no. 2 | article 022417.
Identifier and resource: [10.1103/physreva.103.022417](https://doi.org/10.1103/physreva.103.022417).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.103.022417); retrieved 2026-10-08.

#### Q0062 Dynamical resource theory of quantum coherence

Gaurav Saxena, Eric Chitambar, Gilad Gour.
Journal article | 2020 | Physical Review Research | vol. 2 | no. 2 | article 023298.
Identifier and resource: [10.1103/physrevresearch.2.023298](https://doi.org/10.1103/physrevresearch.2.023298).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.2.023298); retrieved 2026-10-08.

#### Q0063 The resource theory of coherence for quantum channels

F. H. Kamin, F. T. Tabesh, S. Salimi, F. Kheirandish.
Journal article | 2020 | Quantum Information Processing | vol. 19 | no. 7 | article 210.
Identifier and resource: [10.1007/s11128-020-02702-9](https://doi.org/10.1007/s11128-020-02702-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-020-02702-9); retrieved 2026-10-08.

#### Q0064 General resource theory of quantum coherence in multipartite system

Feng Liu, Dong-Mei Gao, Xiao-Qiu Cai.
Journal article | 2019 | Acta Physica Sinica | vol. 68 | no. 23 | pp. 230301.
Identifier and resource: [10.7498/aps.68.20190966](https://doi.org/10.7498/aps.68.20190966).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.68.20190966); retrieved 2026-10-08.

#### Q0065 Operational resource theory of total quantum coherence

Si-ren Yang, Chang-shui Yu.
Journal article | 2018 | Annals of Physics | vol. 388 | pp. 305-314.
Identifier and resource: [10.1016/j.aop.2017.11.028](https://doi.org/10.1016/j.aop.2017.11.028).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.aop.2017.11.028); retrieved 2026-10-08.

#### Q0066 Structure of the Resource Theory of Quantum Coherence

Alexander Streltsov, Swapan Rana, Paul Boes, Jens Eisert.
Journal article | 2017 | Physical Review Letters | vol. 119 | no. 14 | article 140402.
Identifier and resource: [10.1103/physrevlett.119.140402](https://doi.org/10.1103/physrevlett.119.140402).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.119.140402); retrieved 2026-10-08.

### D02T04 Magic and stabilizer resources

Magic characterizes resources outside stabilizer computation. It matters both for non Clifford computation and for the cost of classical simulation.

Fine subcategories: Nonstabilizer states; mana; robustness of magic; stabilizer rank; simulation costs.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0067 No-cost Bell nonlocality certification from quantum tomography and its applications in quantum-magic-resource witnessing

Paweł Cieśliński, Lukas Knips, Harald Weinfurter, Wiesław Laskowski.
Journal article | 2026 | Physical Review A | vol. 113 | no. 5 | article 052404.
Identifier and resource: [10.1103/1nkl-sphd](https://doi.org/10.1103/1nkl-sphd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F1nkl-sphd); retrieved 2026-10-08.

#### Q0068 Qualia from quantum magic: a quantum resource approach to phenomenal consciousness

Gandhimohan M. Viswanathan.
Journal article | 2026 | Frontiers in Physics | vol. 13 | article 1715825.
Identifier and resource: [10.3389/fphy.2025.1715825](https://doi.org/10.3389/fphy.2025.1715825).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffphy.2025.1715825); retrieved 2026-10-08.

#### Q0069 Stabilizer Ranks, Barnes Wall Lattices and Magic Monotones

Amolak Ratan Kalra, Pulkit Sinha.
Journal article | 2026 | Quantum | vol. 10 | pp. 2179 | article 2179.
Identifier and resource: [10.22331/q-2026-07-29-2179](https://doi.org/10.22331/q-2026-07-29-2179).
Fine tags: stabilizer rank.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-07-29-2179); retrieved 2026-10-08.

#### Q0070 Stabilizer entanglement enhances magic injection

Zong-Yue Hou, ChunJun Cao, Zhi-Cheng Yang.
Journal article | 2026 | npj Quantum Information | vol. 12 | no. 1 | article 113.
Identifier and resource: [10.1038/s41534-026-01265-4](https://doi.org/10.1038/s41534-026-01265-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-026-01265-4); retrieved 2026-10-08.

#### Q0071 Leveraging magic resources for quantum channel capacity enhancement under stabilizer convolution

Wenlong Sun, Yuanfeng Jin.
Journal article | 2025 | Physical Review A | vol. 112 | no. 5 | article 052412.
Identifier and resource: [10.1103/qnz3-4fsc](https://doi.org/10.1103/qnz3-4fsc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fqnz3-4fsc); retrieved 2026-10-08.

#### Q0072 Stabilizer Testing and Magic Entropy via Quantum Fourier Analysis

Kaifeng Bu, Weichen Gu, Arthur Jaffe.
Journal article | 2025 | Communications in Mathematical Physics | vol. 406 | no. 10 | article 236.
Identifier and resource: [10.1007/s00220-025-05421-3](https://doi.org/10.1007/s00220-025-05421-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00220-025-05421-3); retrieved 2026-10-08.

#### Q0073 Stabilizer entropies are monotones for magic-state resource theory

Lorenzo Leone, Lennart Bittel.
Journal article | 2024 | Physical Review A | vol. 110 | no. 4 | article L040403.
Identifier and resource: [10.1103/physreva.110.l040403](https://doi.org/10.1103/physreva.110.l040403).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.l040403); retrieved 2026-10-08.

### D02T05 Entanglement distillation

Distillation converts noisy shared resources into fewer high quality ones. Rates and achievable fidelities depend on allowed communication and operation classes.

Fine subcategories: Purification; hashing; bound entanglement; one shot protocols; network resource conversion.

Primary resources: 11. Additional related assignments can be found in the interactive HTML.

#### Q0074 Improving entanglement resilience in quantum memories with error-detection-based distillation

Huidan Zheng, Gunsik Min, Ilkwon Sohn, Jun Heo.
Journal article | 2026 | Scientific Reports.
Identifier and resource: [10.1038/s41598-026-72375-4](https://doi.org/10.1038/s41598-026-72375-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-026-72375-4); retrieved 2026-10-08.

#### Q0075 Nonlocality Distillation Can Outperform Entanglement Distillation

Peter Høyer, Jibran Rashid, Razeen Ud Din.
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 291-297.
Identifier and resource: [10.1109/qcnc69040.2026.00049](https://doi.org/10.1109/qcnc69040.2026.00049).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00049); retrieved 2026-10-08.

#### Q0076 Constant-Rate Entanglement Distillation for Fast Quantum Interconnects

Christopher Pattison, Gefen Baranes, Juan Pablo Bonilla Ataides, Mikhail D. Lukin, Hengyun Zhou.
Conference paper | 2025 | Proceedings of the 52nd Annual International Symposium on Computer Architecture | pp. 257-270.
Identifier and resource: [10.1145/3695053.3731069](https://doi.org/10.1145/3695053.3731069).
Conference metadata: ISCA '25: Proceedings of the 52nd Annual International Symposium on Computer Architecture.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3695053.3731069); retrieved 2026-10-08.

#### Q0077 Entanglement Distribution Delay Optimization in Quantum Networks With Distillation

Mahdi Chehimi, Kenneth Goodenough, Walid Saad, Don Towsley, Tony X. Zhou.
Journal article | 2025 | IEEE Journal on Selected Areas in Communications | vol. 43 | no. 5 | pp. 1871-1886.
Identifier and resource: [10.1109/jsac.2025.3543485](https://doi.org/10.1109/jsac.2025.3543485).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjsac.2025.3543485); retrieved 2026-10-08.

#### Q0078 Quantum Code-Assisted Entanglement Distillation Under Bit-Flip Noise

Huidan Zheng, Gunsik Min, Yujin Kang, Youshin Chung, Hyelyn Kwak, Jun Heo.
Conference paper | 2025 | 2025 International Conference on Mobile, Military, Maritime IT Convergence (ICMIC) | pp. 317-320.
Identifier and resource: [10.1109/icmic66299.2025.11257738](https://doi.org/10.1109/icmic66299.2025.11257738).
Conference metadata: 2025 International Conference on Mobile, Military, Maritime IT Convergence (ICMIC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficmic66299.2025.11257738); retrieved 2026-10-08.

#### Q0079 Quantum change point and entanglement distillation

Abhishek Banerjee, Pratapaditya Bej, Somshubhro Bandyopadhyay.
Journal article | 2024 | Physical Review A | vol. 109 | no. 4 | article 042407.
Identifier and resource: [10.1103/physreva.109.042407](https://doi.org/10.1103/physreva.109.042407).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.042407); retrieved 2026-10-08.

#### Q0080 Entanglement Distillation Optimization Using Fuzzy Relations for Quantum State Tomography

Timothy Ganesan, Irraivan Elamvazuthi.
Journal article | 2023 | Algorithms | vol. 16 | no. 7 | pp. 313.
Identifier and resource: [10.3390/a16070313](https://doi.org/10.3390/a16070313).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fa16070313); retrieved 2026-10-08.

#### Q0081 Learning Quantum Entanglement Distillation With Noisy Classical Communications

Hari Hara Suthan Chittoor, Osvaldo Simeone.
Conference paper | 2023 | ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) | pp. 1-5.
Identifier and resource: [10.1109/icassp49357.2023.10097202](https://doi.org/10.1109/icassp49357.2023.10097202).
Conference metadata: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficassp49357.2023.10097202); retrieved 2026-10-08.

#### Q0082 Optimal Entanglement Distillation Policies for Quantum Switches

Vivek Kumar, Nitish K. Chandra, Kaushik P. Seshadreesan, Alan Scheller-Wolf, Sridhar Tayur.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1198-1204.
Identifier and resource: [10.1109/qce57702.2023.00135](https://doi.org/10.1109/qce57702.2023.00135).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00135); retrieved 2026-10-08.

#### Q0083 Trapped Ion Quantum Repeaters with Entanglement Distillation based on Quantum LDPC Codes

Ann Kang, Saikat Guha, Narayanan Rengaswamy, Kaushik P. Seshadreesan.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1165-1171.
Identifier and resource: [10.1109/qce57702.2023.00131](https://doi.org/10.1109/qce57702.2023.00131).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00131); retrieved 2026-10-08.

#### Q0084 Multi-User Distillation of Common Randomness and Entanglement From Quantum States

Farzin Salek, Andreas Winter.
Journal article | 2022 | IEEE Transactions on Information Theory | vol. 68 | no. 2 | pp. 976-988.
Identifier and resource: [10.1109/tit.2021.3124965](https://doi.org/10.1109/tit.2021.3124965).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftit.2021.3124965); retrieved 2026-10-08.

## D03 Models of quantum computation

Different models specify the available operations and how an algorithm is executed. Equivalence of models does not imply identical engineering costs or noise tolerance.

Prerequisites: Qubits, unitary operations, and measurement.

Assessment focus: Model assumptions, universality, resource generation, and noise constraints.

Primary catalog resources in this category: 71.

### D03T01 Circuit and universal gate models

A circuit is an ordered composition of gates and measurements. Universality describes what transformations can be approximated, while compilation determines their actual cost.

Fine subcategories: Universal gate sets; reversible circuits; qudit gates; multi controlled gates; universality proofs.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0085 Quantum Computing for Computer Scientists

Noson S. Yanofsky, Mirco A. Mannucci.
Book | 2008 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511813887](https://doi.org/10.1017/cbo9780511813887).
ISBN: 9780521879965; 9780511813887.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2Fcbo9780511813887); retrieved 2026-10-08.

#### Q0086 Quantum Computer Science

N. David Mermin.
Book | 2007 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511813870](https://doi.org/10.1017/cbo9780511813870).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2FCBO9780511813870); retrieved 2026-10-08.

#### Q0087 Quantum theory, the Church–Turing principle and the universal quantum computer

David Deutsch.
Journal article | 1985 | Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences | vol. 400 | no. 1818 | pp. 97-117.
Identifier and resource: [10.1098/rspa.1985.0070](https://doi.org/10.1098/rspa.1985.0070).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1098%2Frspa.1985.0070); retrieved 2026-10-08.

#### Q0088 Time-optimal universal quantum gates on superconducting circuits

Ze Li, Ming-Jie Liang, Zheng-Yuan Xue.
Journal article | 2023 | Physical Review A | vol. 108 | no. 4 | article 042617.
Identifier and resource: [10.1103/physreva.108.042617](https://doi.org/10.1103/physreva.108.042617).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.108.042617); retrieved 2026-10-08.

#### Q0089 Quantum-Dot Cellular Automata-Based Encoder Circuit Using Layered Universal Gates

Birinderjit Singh Kalyan, Balwinder Singh.
Book chapter | 2021 | Nanoelectronic Devices for Hardware and Software Security | pp. 217-230.
Identifier and resource: [10.1201/9781003126645-11](https://doi.org/10.1201/9781003126645-11).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003126645-11); retrieved 2026-10-08.

#### Q0090 Electric circuits for universal quantum gates and quantum Fourier transformation

Motohiko Ezawa.
Journal article | 2020 | Physical Review Research | vol. 2 | no. 2 | article 023278.
Identifier and resource: [10.1103/physrevresearch.2.023278](https://doi.org/10.1103/physrevresearch.2.023278).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.2.023278); retrieved 2026-10-08.

#### Q0091 Experimental Implementation of Universal Nonadiabatic Geometric Quantum Gates in a Superconducting Circuit

Y. Xu, Z. Hua, Tao Chen, X. Pan, X. Li, J. Han, W. Cai, Y. Ma et al..
Journal article | 2020 | Physical Review Letters | vol. 124 | no. 23 | article 230503.
Identifier and resource: [10.1103/physrevlett.124.230503](https://doi.org/10.1103/physrevlett.124.230503).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.124.230503); retrieved 2026-10-08.

#### Q0092 Fast universal quantum gates on microwave photons with all-resonance operations in circuit QED

Ming Hua, Ming-Jie Tao, Fu-Guo Deng.
Journal article | 2015 | Scientific Reports | vol. 5 | no. 1 | article 9274.
Identifier and resource: [10.1038/srep09274](https://doi.org/10.1038/srep09274).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fsrep09274); retrieved 2026-10-08.

### D03T02 Measurement based computing

Measurement based computation processes an entangled resource state through adaptive local measurements. Classical feed forward and resource generation are part of the computation.

Fine subcategories: Cluster states; graph states; adaptive measurements; feed forward; one way computing.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0093 MCBGD: Multi-Path Cluster-Based Graph Distribution for Scalable Measurement-Based Quantum Computation

Guanting Yu, Yongzhe Lin, Yiyang Yu, Zisen Wei, Xiaofeng Jiang.
Conference paper | 2026 | 2026 28th International Conference on Advanced Communications Technology (ICACT) | pp. 309-315.
Identifier and resource: [10.23919/icact68090.2026.11431344](https://doi.org/10.23919/icact68090.2026.11431344).
Conference metadata: 2026 28th International Conference on Advanced Communications Technology (ICACT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Ficact68090.2026.11431344); retrieved 2026-10-08.

#### Q0094 One- and two-dimensional cluster states for topological phase simulation and measurement-based quantum computation

Tao Jiang, Jianbin Cai, Junxiang Huang, Naibin Zhou, Yukun Zhang, Jiahao Bei, Guoqing Cai, Sirui Cao et al..
Journal article | 2026 | Nature Physics | vol. 22 | no. 3 | pp. 430-438.
Identifier and resource: [10.1038/s41567-026-03179-6](https://doi.org/10.1038/s41567-026-03179-6).
Fine tags: Cluster states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-026-03179-6); retrieved 2026-10-08.

#### Q0095 FMCC: Flexible Measurement-based Quantum Computation over Cluster State

Yingheng Li, Aditya Pawar, Zewei Mo, Youtao Zhang, Jun Yang, Xulong Tang.
Conference paper | 2024 | Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 4 | pp. 111-126.
Identifier and resource: [10.1145/3622781.3674185](https://doi.org/10.1145/3622781.3674185).
Conference metadata: ASPLOS '24: 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 4.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3622781.3674185); retrieved 2026-10-08.

#### Q0096 Universal hardware-efficient topological measurement-based quantum computation via color-code-based cluster states

Seok-Hyung Lee, Hyunseok Jeong.
Journal article | 2022 | Physical Review Research | vol. 4 | no. 1 | article 013010.
Identifier and resource: [10.1103/physrevresearch.4.013010](https://doi.org/10.1103/physrevresearch.4.013010).
Fine tags: Cluster states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.4.013010); retrieved 2026-10-08.

#### Q0097 Temporal-mode continuous-variable three-dimensional cluster state for topologically protected measurement-based quantum computation

Kosuke Fukui, Warit Asavanant, Akira Furusawa.
Journal article | 2020 | Physical Review A | vol. 102 | no. 3 | article 032614.
Identifier and resource: [10.1103/physreva.102.032614](https://doi.org/10.1103/physreva.102.032614).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.102.032614); retrieved 2026-10-08.

#### Q0098 Constraints on Measurement-Based Quantum Computation in Effective Cluster States

Daniel Klagges, Kai Phillip Schmidt.
Journal article | 2012 | Physical Review Letters | vol. 108 | no. 23 | article 230508.
Identifier and resource: [10.1103/physrevlett.108.230508](https://doi.org/10.1103/physrevlett.108.230508).
Fine tags: Cluster states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.108.230508); retrieved 2026-10-08.

#### Q0099 MEASUREMENT-BASED QUANTUM COMPUTATION WITH CLUSTER STATES

ROBERT RAUßENDORF.
Journal article | 2009 | International Journal of Quantum Information | vol. 07 | no. 06 | pp. 1053-1203.
Identifier and resource: [10.1142/s0219749909005699](https://doi.org/10.1142/s0219749909005699).
Fine tags: Cluster states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0219749909005699); retrieved 2026-10-08.

#### Q0100 Efficient measurement-based quantum computation with cluster states in quantum-bit fixed systems

Da-Sheng Diao, Yong-Sheng Zhang, Xiang-Fa Zhou, Guang-Can Guo.
Journal article | 2008 | Physical Review A | vol. 77 | no. 4 | article 044301.
Identifier and resource: [10.1103/physreva.77.044301](https://doi.org/10.1103/physreva.77.044301).
Fine tags: Cluster states.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.77.044301); retrieved 2026-10-08.

### D03T03 Adiabatic quantum computing

Adiabatic computation evolves a Hamiltonian along a path whose low energy states encode the answer. Gap behavior and schedule assumptions determine the required runtime.

Fine subcategories: Spectral gaps; adiabatic theorems; schedule design; universality; diabatic effects.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0101 Adiabatic Quantum Computing and Quantum Annealing

Bastien Chopard, Marco Tomassini.
Book chapter | 2026 | Natural Computing Series | pp. 265-275.
Identifier and resource: [10.1007/978-981-95-6216-9_15](https://doi.org/10.1007/978-981-95-6216-9_15).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-6216-9_15); retrieved 2026-10-08.

#### Q0102 Quantum Zeno effect versus adiabatic quantum computing and quantum annealing

Naser Ahmadiniaz, Dennis Kraft, Gernot Schaller, Ralf Schützhold.
Journal article | 2026 | New Journal of Physics | vol. 28 | no. 6 | pp. 064502.
Identifier and resource: [10.1088/1367-2630/ae6e68](https://doi.org/10.1088/1367-2630/ae6e68).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fae6e68); retrieved 2026-10-08.

#### Q0103 Adiabatic Quantum Computing

Christian Bauckhage, Rafet Sifa.
Book chapter | 2025 | Cognitive Technologies | pp. 253-276.
Identifier and resource: [10.1007/978-3-031-99402-9_12](https://doi.org/10.1007/978-3-031-99402-9_12).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-99402-9_12); retrieved 2026-10-08.

#### Q0104 Adiabatic Quantum Computing

Ray LaPierre.
Book chapter | 2025 | The Materials Research Society Series | pp. 341-344.
Identifier and resource: [10.1007/978-3-031-90731-9_23](https://doi.org/10.1007/978-3-031-90731-9_23).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-90731-9_23); retrieved 2026-10-08.

#### Q0105 Bayesian Update Step Using Adiabatic Quantum Computing

Rheinische Friedrich- Wilhelms-Universität, Norman Bunk, Felix Govaers, Fraunhofer FKIE.
Conference paper | 2025 | Computer Science Research Notes.
Identifier and resource: [10.24132/csrn.2025-a23](https://doi.org/10.24132/csrn.2025-a23).
Conference metadata: Computer Science Research Notes.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.24132%2Fcsrn.2025-a23); retrieved 2026-10-08.

#### Q0106 Determining probability density functions with adiabatic quantum computing

Matteo Robbiati, Juan M. Cruz-Martinez, Stefano Carrazza.
Journal article | 2025 | Quantum Machine Intelligence | vol. 7 | no. 1 | article 5.
Identifier and resource: [10.1007/s42484-024-00228-2](https://doi.org/10.1007/s42484-024-00228-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-024-00228-2); retrieved 2026-10-08.

#### Q0107 Exploiting adiabatic quantum computing in deep space missions

Rebecca Casati, Enrico Prati.
Journal article | 2025 | Journal of Physics: Conference Series | vol. 3017 | no. 1 | pp. 012042.
Identifier and resource: [10.1088/1742-6596/3017/1/012042](https://doi.org/10.1088/1742-6596/3017/1/012042).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F3017%2F1%2F012042); retrieved 2026-10-08.

#### Q0108 Filter-enhanced adiabatic quantum computing on a digital quantum processor

Erenay Karacan, Conor Mc Keever, Michael Foss-Feig, David Hayes, Michael Lubasch.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 3 | article 033153.
Identifier and resource: [10.1103/x2v8-jx1h](https://doi.org/10.1103/x2v8-jx1h).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fx2v8-jx1h); retrieved 2026-10-08.

#### Q0109 Non-adiabatic holonomies for photonic quantum computing

Vera Neef, Julien Pinske, Tom A. W. Wolterink, Karo Becker, Matthias Heinrich, Stefan Scheel, Alexander Szameit.
Journal article | 2025 | Optica Quantum | vol. 3 | no. 1 | pp. 93.
Identifier and resource: [10.1364/opticaq.530855](https://doi.org/10.1364/opticaq.530855).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fopticaq.530855); retrieved 2026-10-08.

#### Q0110 Solving Portfolio Optimization Problems using Adiabatic Quantum Computing

Bartlomiej Kolodziejczyk.
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-6986668/v1](https://doi.org/10.21203/rs.3.rs-6986668/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-6986668%2Fv1); retrieved 2026-10-08.

#### Q0111 Adiabatic Quantum Computing

Bernard Zygelman.
Book chapter | 2024 | Undergraduate Topics in Computer Science | pp. 241-273.
Identifier and resource: [10.1007/978-3-031-66425-0_10](https://doi.org/10.1007/978-3-031-66425-0_10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-66425-0_10); retrieved 2026-10-08.

#### Q0112 Quantum annealing and adiabatic quantum computing

Charles R. Giardina.
Book chapter | 2024 | Many-Sorted Algebras for Deep Learning and Quantum Technology | pp. 103-129.
Identifier and resource: [10.1016/b978-0-443-13697-9.00021-7](https://doi.org/10.1016/b978-0-443-13697-9.00021-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-13697-9.00021-7); retrieved 2026-10-08.

#### Q0113 Quantum-Assisted Machine Learning by Means of Adiabatic Quantum Computing

Leonardo Tomazeli Duarte, Yannick Deville.
Conference paper | 2024 | 2024 IEEE Mediterranean and Middle-East Geoscience and Remote Sensing Symposium (M2GARSS) | pp. 371-375.
Identifier and resource: [10.1109/m2garss57310.2024.10537323](https://doi.org/10.1109/m2garss57310.2024.10537323).
Conference metadata: 2024 IEEE Mediterranean and Middle-East Geoscience and Remote Sensing Symposium (M2GARSS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fm2garss57310.2024.10537323); retrieved 2026-10-08.

#### Q0114 Simulating adiabatic quantum computing with parameterized quantum circuits

Ioannis Kolotouros, Ioannis Petrongonas, Miloš Prokop, Petros Wallden.
Journal article | 2024 | Quantum Science and Technology | vol. 10 | no. 1 | pp. 015003.
Identifier and resource: [10.1088/2058-9565/ad80c0](https://doi.org/10.1088/2058-9565/ad80c0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad80c0); retrieved 2026-10-08.

#### Q0115 Towards Adiabatic Quantum Computing Using Compressed Quantum Circuits

Conor Mc Keever, Michael Lubasch.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 2 | article 020362.
Identifier and resource: [10.1103/prxquantum.5.020362](https://doi.org/10.1103/prxquantum.5.020362).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.020362); retrieved 2026-10-08.

#### Q0116 Training neural networks with universal adiabatic quantum computing

Steve Abel, Juan Carlos Criado, Michael Spannowsky.
Journal article | 2024 | Frontiers in Artificial Intelligence | vol. 7 | article 1368569.
Identifier and resource: [10.3389/frai.2024.1368569](https://doi.org/10.3389/frai.2024.1368569).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffrai.2024.1368569); retrieved 2026-10-08.

### D03T04 Quantum annealing

Annealing seeks low energy solutions of an encoded optimization problem. Embedding, temperature, open system dynamics, and solution sampling distinguish hardware annealers from ideal adiabatic algorithms.

Fine subcategories: Ising encoding; QUBO; minor embedding; anneal offsets; reverse annealing.

Primary resources: 14. Additional related assignments can be found in the interactive HTML.

#### Q0117 QUANTUM ANNEALING

STEVE ABEL, LUCA A. NUTRICATI.
Book chapter | 2026 | Machine Learning Tutorials for Pure Mathematics and Theoretical Physics | pp. 59-79.
Identifier and resource: [10.1142/9781807290016_0004](https://doi.org/10.1142/9781807290016_0004).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2F9781807290016_0004); retrieved 2026-10-08.

#### Q0118 Quantum Annealing

Michael Tsesmelis.
Book chapter | 2025 | Quantum Technologies | pp. 65-72.
Identifier and resource: [10.1007/978-3-031-90727-2_7](https://doi.org/10.1007/978-3-031-90727-2_7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-90727-2_7); retrieved 2026-10-08.

#### Q0119 Quantum Annealing

Ryo Maezono.
Book chapter | 2025 | Essentials for Deeper Understanding of Quantum Computing | pp. 199-214.
Identifier and resource: [10.1007/978-981-96-5646-2_8](https://doi.org/10.1007/978-981-96-5646-2_8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-96-5646-2_8); retrieved 2026-10-08.

#### Q0120 Quantum error mitigation in quantum annealing

Jack Raymond, Mohammad H. Amin, Andrew D. King, Richard Harris, William Bernoudy, Andrew J. Berkley, Kelly Boothby, Anatoly Smirnov et al..
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 38.
Identifier and resource: [10.1038/s41534-025-00977-3](https://doi.org/10.1038/s41534-025-00977-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-00977-3); retrieved 2026-10-08.

#### Q0121 Quantum Annealing

Chuck Easttom.
Book chapter | 2024 | Hardware for Quantum Computing | pp. 101-112.
Identifier and resource: [10.1007/978-3-031-66477-9_9](https://doi.org/10.1007/978-3-031-66477-9_9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-66477-9_9); retrieved 2026-10-08.

#### Q0122 Quantum Annealing

Carleton Coffrin, Marc Vuffray.
Book chapter | 2024 | Encyclopedia of Optimization | pp. 1-8.
Identifier and resource: [10.1007/978-3-030-54621-2_855-1](https://doi.org/10.1007/978-3-030-54621-2_855-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-54621-2_855-1); retrieved 2026-10-08.

#### Q0123 Quantum annealing and computation

Bikas K Chakrabarti, Sudip Mukherjee.
Book chapter | 2024 | Encyclopedia of Condensed Matter Physics | pp. 536-542.
Identifier and resource: [10.1016/b978-0-323-90800-9.00057-3](https://doi.org/10.1016/b978-0-323-90800-9.00057-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-323-90800-9.00057-3); retrieved 2026-10-08.

#### Q0124 Reverse Quantum Annealing Assisted by Forward Annealing

Manpreet Singh Jattana.
Journal article | 2024 | Quantum Reports | vol. 6 | no. 3 | pp. 452-464.
Identifier and resource: [10.3390/quantum6030030](https://doi.org/10.3390/quantum6030030).
Fine tags: reverse annealing.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fquantum6030030); retrieved 2026-10-08.

#### Q0125 Quantum Annealing with Ocean

Rafael Pereira da Silva.
Posted content | 2023 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.4526152](https://doi.org/10.2139/ssrn.4526152).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.4526152); retrieved 2026-10-08.

#### Q0126 Quantum Topology Optimization via Quantum Annealing

Zisheng Ye, Xiaoping Qian, Wenxiao Pan.
Journal article | 2023 | IEEE Transactions on Quantum Engineering | vol. 4 | pp. 1-15.
Identifier and resource: [10.1109/tqe.2023.3266410](https://doi.org/10.1109/tqe.2023.3266410).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2023.3266410); retrieved 2026-10-08.

#### Q0127 Customized Quantum Annealing Schedules

Mostafa Khezri, Xi Dai, Rui Yang, Tameem Albash, Adrian Lupascu, Daniel A. Lidar.
Journal article | 2022 | Physical Review Applied | vol. 17 | no. 4 | article 044005.
Identifier and resource: [10.1103/physrevapplied.17.044005](https://doi.org/10.1103/physrevapplied.17.044005).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.17.044005); retrieved 2026-10-08.

#### Q0128 Guaranteed-accuracy quantum annealing

Takashi Imoto, Yuya Seki, Yuichiro Matsuzaki, Shiro Kawabata.
Journal article | 2022 | Physical Review A | vol. 106 | no. 4 | article 042615.
Identifier and resource: [10.1103/physreva.106.042615](https://doi.org/10.1103/physreva.106.042615).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.106.042615); retrieved 2026-10-08.

#### Q0129 Parallel quantum annealing

Elijah Pelofske, Georg Hahn, Hristo N. Djidjev.
Journal article | 2022 | Scientific Reports | vol. 12 | no. 1 | article 4499.
Identifier and resource: [10.1038/s41598-022-08394-8](https://doi.org/10.1038/s41598-022-08394-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-022-08394-8); retrieved 2026-10-08.

#### Q0130 Quantum annealing: an overview

Atanu Rajak, Sei Suzuki, Amit Dutta, Bikas K. Chakrabarti.
Journal article | 2022 | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences | vol. 381 | no. 2241 | article 20210417.
Identifier and resource: [10.1098/rsta.2021.0417](https://doi.org/10.1098/rsta.2021.0417).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1098%2Frsta.2021.0417); retrieved 2026-10-08.

### D03T05 Continuous variable computing

Continuous variable systems encode information in modes with continuous quadratures. Universal computation generally needs suitable non Gaussian resources as well as Gaussian control.

Fine subcategories: Quadratures; Gaussian states; non Gaussian operations; squeezing; continuous variable universality.

Primary resources: 17. Additional related assignments can be found in the interactive HTML.

#### Q0131 Continuous-variable quantum communication

Vladyslav C. Usenko, Antonio Acín, Romain Alléaume, Ulrik L. Andersen, Eleni Diamanti, Tobias Gehring, Adnan A. E. Hajomer, Florian Kanitschar et al..
Journal article | 2026 | Reviews of Modern Physics | vol. 98 | no. 1 | article 015003.
Identifier and resource: [10.1103/mgj7-t6d3](https://doi.org/10.1103/mgj7-t6d3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fmgj7-t6d3); retrieved 2026-10-08.

#### Q0132 Experimental memory control in continuous-variable optical quantum reservoir computing

Iris Paparelle, Johan Henaff, Jorge García-Beni, Émilie Gillet, Daniel Montesinos, Gian Luca Giorgi, Miguel C. Soriano, Roberta Zambrini et al..
Journal article | 2026 | Nature Photonics | vol. 20 | no. 4 | pp. 413-420.
Identifier and resource: [10.1038/s41566-026-01880-9](https://doi.org/10.1038/s41566-026-01880-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41566-026-01880-9); retrieved 2026-10-08.

#### Q0133 Interplay of resources for universal continuous-variable quantum computing

Varun Upreti, Ulysse Chabaud.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033379.
Identifier and resource: [10.1103/2str-dhrg](https://doi.org/10.1103/2str-dhrg).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F2str-dhrg); retrieved 2026-10-08.

#### Q0134 Neonatal EEG Seizure Prediction with Quantum-Inspired Continuous-Variable (Bosonic) Reservoir Computing

Krishna Bhatia, Chun-Yu Lin.
Conference paper | 2026 | ICASSP 2026 - 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) | pp. 22057-22061.
Identifier and resource: [10.1109/icassp55912.2026.11460556](https://doi.org/10.1109/icassp55912.2026.11460556).
Conference metadata: ICASSP 2026 - 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficassp55912.2026.11460556); retrieved 2026-10-08.

#### Q0135 Continuous Variable Quantum Distance Bounding

Kevin Bogner, Aysajan Abidin, Dave Singelée.
Conference paper | 2025 | IEEE INFOCOM 2025 - IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS) | pp. 1-6.
Identifier and resource: [10.1109/infocomwkshps65812.2025.11153001](https://doi.org/10.1109/infocomwkshps65812.2025.11153001).
Conference metadata: IEEE INFOCOM 2025 - IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Finfocomwkshps65812.2025.11153001); retrieved 2026-10-08.

#### Q0136 Continuous-variable quantum computing on a trapped ion: neural network applications

Alexandre C Ricardo, Gubio G de Lima, Amanda G Valério, Tiago de S Farias, Celso J Villas-Boas.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 12 | pp. 125109.
Identifier and resource: [10.1088/1402-4896/ae2164](https://doi.org/10.1088/1402-4896/ae2164).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae2164); retrieved 2026-10-08.

#### Q0137 Integrated continuous-variable quantum light sources for quantum computing

Xuezhi Zhu, Siyu Ren, Yunyun Cao, Xiaolong Su.
Journal article | 2025 | Advanced Photonics | vol. 7 | no. 06 | pp. 1-8.
Identifier and resource: [10.1117/1.ap.7.6.064005](https://doi.org/10.1117/1.ap.7.6.064005).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F1.ap.7.6.064005); retrieved 2026-10-08.

#### Q0138 Measurement-based continuous-variable quantum reservoir computing

Iris Paparelle, Johan Henaff, Jorge Garcia-Beni, Roberta Zambrini, Valentina Parigi.
Conference paper | 2025 | Quantum Communications and Quantum Imaging XXIII | pp. 21.
Identifier and resource: [10.1117/12.3063922](https://doi.org/10.1117/12.3063922).
Conference metadata: Quantum Communications and Quantum Imaging XXIII.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3063922); retrieved 2026-10-08.

#### Q0139 Programmable Continuous-Variable Photonic Quantum Computing in the Time Domain

Shuntaro Takeda.
Conference paper | 2025 | 2025 European Conference on Optical Communications (ECOC) | pp. 1-2.
Identifier and resource: [10.1109/ecoc66593.2025.11263362](https://doi.org/10.1109/ecoc66593.2025.11263362).
Conference metadata: 2025 European Conference on Optical Communications (ECOC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fecoc66593.2025.11263362); retrieved 2026-10-08.

#### Q0140 Quantum reservoir computing with nonlinear optics: experimental continuous variable memory control

Iris Paparelle, Johan Henaff, Jorge Garcia-Beni, Roberta Zambrini, Valentina Parigi.
Conference paper | 2025 | Emerging Topics in Artificial Intelligence (ETAI) 2025 | pp. 15.
Identifier and resource: [10.1117/12.3063910](https://doi.org/10.1117/12.3063910).
Conference metadata: Emerging Topics in Artificial Intelligence (ETAI) 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3063910); retrieved 2026-10-08.

#### Q0141 Towards a Measurement-Based Quantum Computing Architecture Using Continuous-Variable Optical Qubits

Ryosuke Matsuo, Junichiro Kadomoto.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 657-658.
Identifier and resource: [10.1109/qce65121.2025.10493](https://doi.org/10.1109/qce65121.2025.10493).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10493); retrieved 2026-10-08.

#### Q0142 Continuous-variable Quantum Boltzmann Machine

Shikha Bangar, Leanto Sunny, Kubra Yeter-Aydeniz, George Siopsis.
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-4485601/v1](https://doi.org/10.21203/rs.3.rs-4485601/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-4485601%2Fv1); retrieved 2026-10-08.

#### Q0143 Programmable Continuous-Variable Photonic Quantum Computing in the Time Domain

Shuntaro Takeda.
Conference paper | 2024 | 2024 Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR) | pp. 1-1.
Identifier and resource: [10.1109/cleo-pr60912.2024.10676435](https://doi.org/10.1109/cleo-pr60912.2024.10676435).
Conference metadata: 2024 Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcleo-pr60912.2024.10676435); retrieved 2026-10-08.

#### Q0144 Time-Multiplexed Programmable Continuous-Variable Photonic Quantum Computing

Shuntaro Takeda.
Conference paper | 2024 | Advanced Photonics Congress 2024 | pp. SpW2H.1.
Identifier and resource: [10.1364/sppcom.2024.spw2h.1](https://doi.org/10.1364/sppcom.2024.spw2h.1).
Conference metadata: Signal Processing in Photonic Communications.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fsppcom.2024.spw2h.1); retrieved 2026-10-08.

#### Q0145 Flow conditions for continuous variable measurement-based quantum computing

Robert I. Booth, Damian Markham.
Journal article | 2023 | Quantum | vol. 7 | pp. 1146 | article 1146.
Identifier and resource: [10.22331/q-2023-10-19-1146](https://doi.org/10.22331/q-2023-10-19-1146).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-10-19-1146); retrieved 2026-10-08.

#### Q0146 Time-multiplexed programmable continuous-variable photonic quantum computing

Shuntaro Takeda.
Conference paper | 2023 | Quantum Communications and Quantum Imaging XXI | pp. 27.
Identifier and resource: [10.1117/12.2672528](https://doi.org/10.1117/12.2672528).
Conference metadata: Quantum Communications and Quantum Imaging XXI.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2672528); retrieved 2026-10-08.

#### Q0147 Xanadu | Welcome to Xanadu

Author metadata not supplied.
Documentation | Undated | Xanadu Strawberry Fields.
Identifier and resource: [Official resource](https://strawberryfields.ai/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://strawberryfields.ai/); retrieved 2026-10-08.

### D03T06 Topological computation and anyons

Topological schemes encode and manipulate information using anyonic degrees of freedom. Mathematical universality and experimental identification of the required excitations are separate questions.

Fine subcategories: Braiding; fusion rules; non Abelian statistics; topological gates; Majorana proposals.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0148 Fault-tolerant quantum computation by anyons

A.Yu. Kitaev.
Journal article | 2003 | Annals of Physics | vol. 303 | no. 1 | pp. 2-30.
Identifier and resource: [10.1016/s0003-4916(02)00018-0](https://doi.org/10.1016/s0003-4916(02)00018-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2FS0003-4916%2802%2900018-0); retrieved 2026-10-08.

#### Q0149 Fluctuating Charge Disproportionation in Doped La₃Ni₂O₇: Ambient-Pressure Fibonacci Anyons for Universal Topological Quantum Computation

Fanyuy Fai, Lukong Fai, Afungchui David.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-10108629/v1](https://doi.org/10.21203/rs.3.rs-10108629/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-10108629%2Fv1); retrieved 2026-10-08.

#### Q0150 Universal quantum computation using Ising anyons from a non-semisimple topological quantum field theory

Filippo Iulianelli, Sung Kim, Joshua Sussan, Aaron D. Lauda.
Journal article | 2025 | Nature Communications | vol. 16 | no. 1 | article 6408.
Identifier and resource: [10.1038/s41467-025-61342-8](https://doi.org/10.1038/s41467-025-61342-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-025-61342-8); retrieved 2026-10-08.

#### Q0151 Anyons and Topological Quantum Computation

Tudor D. Stanescu.
Book chapter | 2024 | Introduction to Topological Quantum Matter & Quantum Computation | pp. 365-392.
Identifier and resource: [10.1201/9781003226048-12](https://doi.org/10.1201/9781003226048-12).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003226048-12); retrieved 2026-10-08.

#### Q0152 Compiling single-qubit braiding gate for Fibonacci anyons topological quantum computation

M T Rouabah, N E Belaloui, A Tounsi.
Journal article | 2021 | Journal of Physics: Conference Series | vol. 1766 | no. 1 | pp. 012029.
Identifier and resource: [10.1088/1742-6596/1766/1/012029](https://doi.org/10.1088/1742-6596/1766/1/012029).
Fine tags: Braiding.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F1766%2F1%2F012029); retrieved 2026-10-08.

#### Q0153 Isolating Kondo anyons for topological quantum computation

Yashar Komijani.
Journal article | 2020 | Physical Review B | vol. 101 | no. 23 | article 235131.
Identifier and resource: [10.1103/physrevb.101.235131](https://doi.org/10.1103/physrevb.101.235131).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.101.235131); retrieved 2026-10-08.

#### Q0154 Introduction to topological quantum computation with non-Abelian anyons

Bernard Field, Tapio Simula.
Journal article | 2018 | Quantum Science and Technology | vol. 3 | no. 4 | pp. 045004.
Identifier and resource: [10.1088/2058-9565/aacad2](https://doi.org/10.1088/2058-9565/aacad2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faacad2); retrieved 2026-10-08.

#### Q0155 Topological Quantum Computation with Non-Abelian Anyons in Fractional Quantum Hall States

Lachezar S. Georgiev.
Book chapter | 2017 | Progress in Theoretical Chemistry and Physics | pp. 75-94.
Identifier and resource: [10.1007/978-3-319-50255-7_5](https://doi.org/10.1007/978-3-319-50255-7_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-319-50255-7_5); retrieved 2026-10-08.

## D04 Quantum complexity and limitations

Complexity theory identifies conditional speedups and lower bounds. It also explains why a problem being quantum does not automatically make it efficiently solvable.

Prerequisites: Algorithms, asymptotic analysis, and discrete mathematics.

Assessment focus: Oracle model, complexity assumptions, lower bounds, and input access.

Primary catalog resources in this category: 34.

### D04T01 Quantum complexity classes

Complexity classes formalize efficiently solvable and verifiable quantum problems. A class inclusion or separation should be read together with its error and oracle model.

Fine subcategories: BQP; QMA; QCMA; interactive proofs; promise problems; oracle separations.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0156 Quantum Computing since Democritus

Scott Aaronson.
Book | 2013 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511979309](https://doi.org/10.1017/cbo9780511979309).
ISBN: 9780521199568; 9780511979309.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2Fcbo9780511979309); retrieved 2026-10-08.

#### Q0157 Quantum computational complexity

Daowen Qiu.
Book chapter | 2026 | Theoretical Foundations of Quantum Computing | pp. 207-237.
Identifier and resource: [10.1016/b978-0-44-327704-7.00012-8](https://doi.org/10.1016/b978-0-44-327704-7.00012-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-44-327704-7.00012-8); retrieved 2026-10-08.

#### Q0158 Comparing quantum complexity and quantum fidelity

Anonymous.
Journal article | 2025 | Physical Review B.
Identifier and resource: [10.1103/qccp-sgvb](https://doi.org/10.1103/qccp-sgvb).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fqccp-sgvb); retrieved 2026-10-08.

#### Q0159 On quantum complexity

Mohsen Alishahiha.
Journal article | 2023 | Physics Letters B | vol. 842 | pp. 137979 | article 137979.
Identifier and resource: [10.1016/j.physletb.2023.137979](https://doi.org/10.1016/j.physletb.2023.137979).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.physletb.2023.137979); retrieved 2026-10-08.

#### Q0160 Quantum Complexity

Helmut Satz.
Book chapter | 2022 | More than the Sum of the Parts | pp. 127-135.
Identifier and resource: [10.1093/oso/9780192864178.003.0015](https://doi.org/10.1093/oso/9780192864178.003.0015).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Foso%2F9780192864178.003.0015); retrieved 2026-10-08.

#### Q0161 Quantum Complexity and Quantum Chaos

Author metadata not supplied.
Book chapter | 2022 | Quantum Mechanics | pp. 384-392.
Identifier and resource: [10.1017/9781108976299.040](https://doi.org/10.1017/9781108976299.040).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781108976299.040); retrieved 2026-10-08.

#### Q0162 Quantum Hamiltonian Complexity

Sevag Gharibian, Yichen Huang, Zeph Landau, Seung Woo Shin.
Journal article | 2015 | Foundations and Trends® in Theoretical Computer Science | vol. 10 | no. 3 | pp. 159-282.
Identifier and resource: [10.1561/0400000066](https://doi.org/10.1561/0400000066).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1561%2F0400000066); retrieved 2026-10-08.

#### Q0163 Quantum Computational Complexity of the N -Representability Problem: QMA Complete

Yi-Kai Liu, Matthias Christandl, F. Verstraete.
Journal article | 2007 | Physical Review Letters | vol. 98 | no. 11 | article 110503.
Identifier and resource: [10.1103/physrevlett.98.110503](https://doi.org/10.1103/physrevlett.98.110503).
Fine tags: QMA.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.98.110503); retrieved 2026-10-08.

### D04T02 Query complexity and lower bounds

Query complexity counts accesses to an input oracle. This isolates useful theoretical questions but does not include the physical cost of constructing that oracle.

Fine subcategories: Polynomial method; adversary method; oracle models; decision trees; bounded error queries.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0164 THEORETICAL FOUNDATIONS OF CLASSICAL AND QUANTUM QUERY MODELS: COMPLEXITY, LOWER BOUNDS, AND POLYNOMIAL-SPECTRAL INTERPLAY

Medak Srinivas.
Book chapter | 2026 | IIP Series | pp. 139-150.
Identifier and resource: [10.58532/nbennur3146c10](https://doi.org/10.58532/nbennur3146c10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.58532%2Fnbennur3146c10); retrieved 2026-10-08.

#### Q0165 Permutation Superposition Oracles for Quantum Query Lower Bounds

Christian Majenz, Giulio Malavolta, Michael Walter.
Conference paper | 2025 | Proceedings of the 57th Annual ACM Symposium on Theory of Computing | pp. 1508-1519.
Identifier and resource: [10.1145/3717823.3718266](https://doi.org/10.1145/3717823.3718266).
Conference metadata: STOC '25: 57th Annual ACM Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3717823.3718266); retrieved 2026-10-08.

#### Q0166 Quantum Lower Bounds by Sample-to-Query Lifting

Qisheng Wang, Zhicheng Zhang.
Journal article | 2025 | SIAM Journal on Computing | vol. 54 | no. 5 | pp. 1294-1334.
Identifier and resource: [10.1137/24m1638616](https://doi.org/10.1137/24m1638616).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F24m1638616); retrieved 2026-10-08.

#### Q0167 Quantum Query Complexity for Nonstandard Oracles with Tight Bounds and Tradeoffs Beyond Grover

Yalla Jnan Devi Satya Prasad.
Posted content | 2025 | Wiley.
Identifier and resource: [10.22541/au.176616158.89278653/v1](https://doi.org/10.22541/au.176616158.89278653/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22541%2Fau.176616158.89278653%2Fv1); retrieved 2026-10-08.

#### Q0168 Explicit relation between all lower bound techniques for quantum query complexity

Loïck Magnin, Jérémie Roland.
Journal article | 2015 | International Journal of Quantum Information | vol. 13 | no. 04 | pp. 1350059.
Identifier and resource: [10.1142/s0219749913500597](https://doi.org/10.1142/s0219749913500597).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0219749913500597); retrieved 2026-10-08.

#### Q0169 Lower Bounds on Quantum Query Complexity for Read-Once Formulas with XOR and MUX Operators

Hideaki FUKUHARA, Eiji TAKIMOTO.
Journal article | 2010 | IEICE Transactions on Information and Systems | vol. E93-D | no. 2 | pp. 280-289.
Identifier and resource: [10.1587/transinf.e93.d.280](https://doi.org/10.1587/transinf.e93.d.280).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1587%2Ftransinf.e93.d.280); retrieved 2026-10-08.

#### Q0170 Lower Bounds for Randomized and Quantum Query Complexity Using Kolmogorov Arguments

Sophie Laplante, Frédéric Magniez.
Journal article | 2008 | SIAM Journal on Computing | vol. 38 | no. 1 | pp. 46-62.
Identifier and resource: [10.1137/050639090](https://doi.org/10.1137/050639090).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F050639090); retrieved 2026-10-08.

#### Q0171 An Algorithmic Argument for Nonadaptive Query Complexity Lower Bounds on Advised Quantum Computation

Harumichi Nishimura, Tomoyuki Yamakami.
Book chapter | 2004 | Lecture Notes in Computer Science | pp. 827-838.
Identifier and resource: [10.1007/978-3-540-28629-5_65](https://doi.org/10.1007/978-3-540-28629-5_65).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-540-28629-5_65); retrieved 2026-10-08.

### D04T03 Quantum communication complexity

Communication complexity asks how much information must be exchanged to solve a distributed task. Prior entanglement and classical side channels change the model.

Fine subcategories: One way communication; simultaneous messages; entanglement assisted protocols; lower bounds.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0172 Quantum Communication Complexity of Regularized Linear Regression Protocols

Sayaki Matsushita.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 3103012-3103012.
Identifier and resource: [10.1109/tqe.2026.3687237](https://doi.org/10.1109/tqe.2026.3687237).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3687237); retrieved 2026-10-08.

#### Q0173 Hybrid Quantum Cryptography from Communication Complexity

Francesco Mazzoncini, Balthazar Bauer, Peter Brown, Romain Alléaume.
Journal article | 2025 | Quantum | vol. 9 | pp. 1862 | article 1862.
Identifier and resource: [10.22331/q-2025-09-24-1862](https://doi.org/10.22331/q-2025-09-24-1862).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-09-24-1862); retrieved 2026-10-08.

#### Q0174 Quantum Communication Complexity and Raz's Problem

Nipun Agarwal.
Posted content | 2024 | Institute of Electrical and Electronics Engineers (IEEE).
Identifier and resource: [10.36227/techrxiv.171779455.51487026/v1](https://doi.org/10.36227/techrxiv.171779455.51487026/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.36227%2Ftechrxiv.171779455.51487026%2Fv1); retrieved 2026-10-08.

#### Q0175 Quantum Communication Complexity of Linear Regression

Ashley Montanaro, Changpeng Shao.
Journal article | 2024 | ACM Transactions on Computation Theory | vol. 16 | no. 1 | pp. 1-30.
Identifier and resource: [10.1145/3625225](https://doi.org/10.1145/3625225).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3625225); retrieved 2026-10-08.

#### Q0176 Quantum Contextuality Provides Communication Complexity Advantage

Shashank Gupta, Debashis Saha, Zhen-Peng Xu, Adán Cabello, A. S. Majumdar.
Journal article | 2023 | Physical Review Letters | vol. 130 | no. 8 | article 080802.
Identifier and resource: [10.1103/physrevlett.130.080802](https://doi.org/10.1103/physrevlett.130.080802).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.130.080802); retrieved 2026-10-08.

#### Q0177 Bounds on Oblivious Multiparty Quantum Communication Complexity

François Le Gall, Daiki Suruga.
Book chapter | 2022 | Lecture Notes in Computer Science | pp. 641-657.
Identifier and resource: [10.1007/978-3-031-20624-5_39](https://doi.org/10.1007/978-3-031-20624-5_39).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-20624-5_39); retrieved 2026-10-08.

#### Q0178 Entanglement-based quantum communication complexity beyond Bell nonlocality

Joseph Ho, George Moreno, Samuraí Brito, Francesco Graffitti, Christopher L. Morrison, Ranieri Nery, Alexander Pickston, Massimiliano Proietti et al..
Journal article | 2022 | npj Quantum Information | vol. 8 | no. 1 | article 13.
Identifier and resource: [10.1038/s41534-022-00520-8](https://doi.org/10.1038/s41534-022-00520-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-022-00520-8); retrieved 2026-10-08.

#### Q0179 Quantum versus Randomized Communication Complexity, with Efficient Players

Uma Girish, Ran Raz, Avishay Tal.
Journal article | 2022 | computational complexity | vol. 31 | no. 2 | article 17.
Identifier and resource: [10.1007/s00037-022-00232-7](https://doi.org/10.1007/s00037-022-00232-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00037-022-00232-7); retrieved 2026-10-08.

### D04T04 Quantum advantage and sampling hardness

Sampling advantage compares specified quantum distributions with classical algorithms under stated assumptions. A sampling demonstration is not by itself evidence of useful application advantage.

Fine subcategories: Circuit sampling; complexity assumptions; classical baselines; verification gaps; asymptotic advantage.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0180 Quantum supremacy using a programmable superconducting processor

Frank Arute, Kunal Arya, Ryan Babbush, Dave Bacon, Joseph C. Bardin, Rami Barends, Rupak Biswas, Sergio Boixo et al..
Journal article | 2019 | Nature | vol. 574 | no. 7779 | pp. 505-510.
Identifier and resource: [10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-019-1666-5); retrieved 2026-10-08.

#### Q0181 Predicting sampling advantage of stochastic Ising machines for quantum simulations

Rutger J.L.F. Berns, Davi R. Rodrigues, Giovanni Finocchio, Johan H. Mentink.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 2 | article 024085.
Identifier and resource: [10.1103/xl6n-dlq6](https://doi.org/10.1103/xl6n-dlq6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fxl6n-dlq6); retrieved 2026-10-08.

#### Q0182 Quantum energetic advantage before computational advantage in Boson Sampling

Anonymous.
Journal article | 2026 | Physical Review Letters.
Identifier and resource: [10.1103/8jyg-m72v](https://doi.org/10.1103/8jyg-m72v).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8jyg-m72v); retrieved 2026-10-08.

#### Q0183 Unconditional Quantum Advantage for Sampling with Shallow Circuits

Adam Bene Watts, Natalie Parham.
Journal article | 2026 | Quantum | vol. 10 | pp. 2188 | article 2188.
Identifier and resource: [10.22331/q-2026-08-12-2188](https://doi.org/10.22331/q-2026-08-12-2188).
Fine tags: Circuit sampling.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-08-12-2188); retrieved 2026-10-08.

#### Q0184 Instantaneous Quantum Polynomial-Time Sampling and Verifiable Quantum Advantage: Stabilizer Scheme and Classical Security

Michael J. Bremner, Bin Cheng, Zhengfeng Ji.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 2 | article 020315.
Identifier and resource: [10.1103/prxquantum.6.020315](https://doi.org/10.1103/prxquantum.6.020315).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.6.020315); retrieved 2026-10-08.

#### Q0185 Quantum Computational Advantage of Noisy Boson Sampling with Partially Distinguishable Photons

Byeongseon Go, Changhun Oh, Hyunseok Jeong.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 3 | article 030362.
Identifier and resource: [10.1103/rflv-gc66](https://doi.org/10.1103/rflv-gc66).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Frflv-gc66); retrieved 2026-10-08.

#### Q0186 Quantum-Advantage Cryptography via Lemniscate-Orbit Sampling and Distributional Hardness

Ralph Vince.
Posted content | 2025 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.5488706](https://doi.org/10.2139/ssrn.5488706).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.5488706); retrieved 2026-10-08.

#### Q0187 Robust quantum computational advantage with programmable 3050-photon Gaussian boson sampling

Chao-Yang Lu, Hua-Liang Liu, Hao Su, Si-Qiu Gong, Yi-Chao Gu, Hao-Yang Tang, Meng-Hao Jia, Qian Wei et al..
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-7435859/v1](https://doi.org/10.21203/rs.3.rs-7435859/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-7435859%2Fv1); retrieved 2026-10-08.

### D04T05 Dequantization and classical limitations

Dequantization identifies classical algorithms that reproduce a claimed benefit under comparable access assumptions. Input preparation and low rank structure often determine the comparison.

Fine subcategories: Sample query access; low rank assumptions; classical emulation; input access costs; quantum inspired algorithms.

Primary resources: 2. Additional related assignments can be found in the interactive HTML.

#### Q0188 Quantum Algorithms for Trading: A Survey of Speedups, Thresholds, and Dequantization

Luigi Laura, Marco Parrillo, Alessio Pascucci, Marco Rossi, Valerio Rughetti.
Journal article | 2026 | Information | vol. 17 | no. 9 | pp. 908.
Identifier and resource: [10.3390/info17090908](https://doi.org/10.3390/info17090908).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Finfo17090908); retrieved 2026-10-08.

#### Q0189 Quantum-inspired career guidance without quantum advantage: A dequantization-aware hybrid architecture, critical benchmarking, and readiness assessment

Kondeti Vinay Kumar, Chandra Shekar N, Meeravali Shaik, Savanam Chandra Sekhar.
Journal article | 2026 | International Journal of Computing and Artificial Intelligence | vol. 7 | no. 8 | pp. 52-64.
Identifier and resource: [10.33545/27076571.2026.v7.i8a.371](https://doi.org/10.33545/27076571.2026.v7.i8a.371).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.33545%2F27076571.2026.v7.i8a.371); retrieved 2026-10-08.

## D05 Core quantum algorithms

Primitive algorithms form reusable components of larger workflows. Their complexity must include data preparation, oracle construction, accuracy, and measurement costs.

Prerequisites: Quantum circuits, probability, and eigenvalue problems.

Assessment focus: Oracle construction, precision, state overlap, and output readout.

Primary catalog resources in this category: 72.

### D05T01 Quantum Fourier transform

The quantum Fourier transform changes between computational and Fourier bases. It is a primitive in phase estimation and order finding rather than a general replacement for classical FFT output.

Fine subcategories: Phase kickback; approximate transforms; semiclassical transforms; arithmetic circuits; Fourier sampling.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q0190 A review on quantum Fourier transform

Tomás Barros, Pablo Álvarez, Bárbara Vidal, Mauricio Solar.
Journal article | 2026 | Quantum Information Processing | vol. 25 | no. 2 | article 41.
Identifier and resource: [10.1007/s11128-026-05067-7](https://doi.org/10.1007/s11128-026-05067-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-026-05067-7); retrieved 2026-10-08.

#### Q0191 Algorithms Using Quantum Fourier Transform

Author metadata not supplied.
Book chapter | 2025 | Quantum Computing for Programmers | pp. 244-292.
Identifier and resource: [10.1017/9781009548519.012](https://doi.org/10.1017/9781009548519.012).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781009548519.012); retrieved 2026-10-08.

#### Q0192 Quantum Fourier Transform

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 155-158.
Identifier and resource: [10.1007/978-3-032-03325-3_19](https://doi.org/10.1007/978-3-032-03325-3_19).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_19); retrieved 2026-10-08.

#### Q0193 Quantum Fourier Transform

Cheng Hsiao Wu.
Book chapter | 2025 | Nonlocal Quantum Computing Theory | pp. 25-35.
Identifier and resource: [10.1201/9781003542032-2](https://doi.org/10.1201/9781003542032-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003542032-2); retrieved 2026-10-08.

#### Q0194 Quantum Fourier Transform and Applications

Eduardo R. Mucciolo.
Book chapter | 2025 | Introduction to Quantum Information Processing | pp. 97-118.
Identifier and resource: [10.1201/9781003485124-8](https://doi.org/10.1201/9781003485124-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003485124-8); retrieved 2026-10-08.

#### Q0195 Quantum Fourier Transform with Leakage Control

US Department of Energy, D. Kurkcuoglu, Fermi National Accelerator Laboratory (FNAL), Batavia, IL (United States), M. Alam, J. Job, A. Li, A. Macridin, G. Perdue et al..
Report | 2025 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3019156](https://doi.org/10.2172/3019156).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3019156); retrieved 2026-10-08.

#### Q0196 Quantum Fourier transform

Author metadata not supplied.
Book chapter | 2025 | Quantum Algorithms | pp. 225-227.
Identifier and resource: [10.1017/9781009639651.015](https://doi.org/10.1017/9781009639651.015).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781009639651.015); retrieved 2026-10-08.

#### Q0197 Short-time quantum Fourier transform processing

Sreeraj Rajindran Nair, Benjamin Southwell, Christopher Ferrie.
Conference paper | 2025 | ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) | pp. 1-5.
Identifier and resource: [10.1109/icassp49660.2025.10890646](https://doi.org/10.1109/icassp49660.2025.10890646).
Conference metadata: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficassp49660.2025.10890646); retrieved 2026-10-08.

#### Q0198 Quantum Fourier Transform Using Dynamic Circuits

Elisa Bäumer, Vinay Tripathi, Alireza Seif, Daniel Lidar, Derek S. Wang.
Journal article | 2024 | Physical Review Letters | vol. 133 | no. 15 | article 150602.
Identifier and resource: [10.1103/physrevlett.133.150602](https://doi.org/10.1103/physrevlett.133.150602).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.133.150602); retrieved 2026-10-08.

#### Q0199 Circuit of Quantum Fractional Fourier Transform

Tieyu Zhao, Yingying Chi.
Journal article | 2023 | Fractal and Fractional | vol. 7 | no. 10 | pp. 743.
Identifier and resource: [10.3390/fractalfract7100743](https://doi.org/10.3390/fractalfract7100743).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Ffractalfract7100743); retrieved 2026-10-08.

#### Q0200 Entanglement Parallelization via Quantum Fourier Transform

Mario Mastriani.
Journal article | 2023 | Advanced Quantum Technologies | vol. 6 | no. 10 | article 2300022.
Identifier and resource: [10.1002/qute.202300022](https://doi.org/10.1002/qute.202300022).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202300022); retrieved 2026-10-08.

#### Q0201 Quantum Fourier Transform

Andreas Wichert.
Book chapter | 2023 | Quantum Artificial Intelligence with Qiskit | pp. 246-254.
Identifier and resource: [10.1201/9781003374404-19](https://doi.org/10.1201/9781003374404-19).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003374404-19); retrieved 2026-10-08.

#### Q0202 Quantum Fourier Transform Has Small Entanglement

Jielun Chen, E.M. Stoudenmire, Steven R. White.
Journal article | 2023 | PRX Quantum | vol. 4 | no. 4 | article 040318.
Identifier and resource: [10.1103/prxquantum.4.040318](https://doi.org/10.1103/prxquantum.4.040318).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.4.040318); retrieved 2026-10-08.

#### Q0203 Quantum Fourier Transform I

Hiu Yung Wong.
Book chapter | 2023 | Introduction to Quantum Computing | pp. 243-253.
Identifier and resource: [10.1007/978-3-031-36985-8_25](https://doi.org/10.1007/978-3-031-36985-8_25).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-36985-8_25); retrieved 2026-10-08.

#### Q0204 Quantum Fourier Transform II

Hiu Yung Wong.
Book chapter | 2023 | Introduction to Quantum Computing | pp. 255-264.
Identifier and resource: [10.1007/978-3-031-36985-8_26](https://doi.org/10.1007/978-3-031-36985-8_26).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-36985-8_26); retrieved 2026-10-08.

### D05T02 Phase estimation

Phase estimation extracts eigenphase information from controlled dynamics. Precision, coherent evolution time, and state overlap control its cost and success probability.

Fine subcategories: Iterative estimation; Bayesian estimation; robust estimation; spectral resolution; controlled evolution.

Primary resources: 14. Additional related assignments can be found in the interactive HTML.

#### Q0205 Filtered quantum phase estimation

Gwonhak Lee, Minhyeok Kang, Jungsoo Hong, Stepan Fomichev, Joonsuk Huh.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 4 | pp. 045053.
Identifier and resource: [10.1088/2058-9565/aea127](https://doi.org/10.1088/2058-9565/aea127).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faea127); retrieved 2026-10-08.

#### Q0206 Measuring the non-abelian quantum phase with the algorithm of quantum phase estimation

Seng Ghee Tan, Son-Hsien Chen, Ying-Cheng Yang, Yen-Fu Chen, Yen-Lin Chen, Jia-Hsiu Hsieh.
Journal article | 2026 | Physics Letters A | vol. 593 | pp. 132019 | article 132019.
Identifier and resource: [10.1016/j.physleta.2026.132019](https://doi.org/10.1016/j.physleta.2026.132019).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.physleta.2026.132019); retrieved 2026-10-08.

#### Q0207 Optimal Coherent Quantum Phase Estimation [Slides]

USDOE National Nuclear Security Administration (NNSA), Yigit Subasi, USDOE Office of Science (SC), Advanced Scientific Computing Research (ASCR), USDOE Laboratory Directed Research and Development (LDRD) Program, Los Alamos National Laboratory (LANL), Los Alamos, NM (United States), National Quantum Information Science (QIS) Research Centers (United States). The Quantum Science Center (QSC), Andrew Sornborger.
Report | 2026 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3097329](https://doi.org/10.2172/3097329).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3097329); retrieved 2026-10-08.

#### Q0208 Quantum Phase Estimation Without Controlled Unitaries

Laura Clinton, Toby S. Cubitt, Raul Garcia-Patron, Ashley Montanaro, Stasja Stanisic, Maarten Stroeks.
Journal article | 2026 | PRX Quantum | vol. 7 | no. 1 | article 010345.
Identifier and resource: [10.1103/7qcr-znl2](https://doi.org/10.1103/7qcr-znl2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F7qcr-znl2); retrieved 2026-10-08.

#### Q0209 Quantumness of quantum phase estimation algorithms

Ugo Marzolino.
Journal article | 2026 | Annals of Physics | vol. 493 | pp. 170599 | article 170599.
Identifier and resource: [10.1016/j.aop.2026.170599](https://doi.org/10.1016/j.aop.2026.170599).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.aop.2026.170599); retrieved 2026-10-08.

#### Q0210 Agnostic phase estimation for quantum sensing and quantum computation

Flavio Salvati, Xingrui Song, Chandrashekhar Gaikwad, Nicole Y. Halpern, David R. M. Arvidsson-Shukur, Kater Murch.
Conference paper | 2025 | Quantum Sensing, Imaging, and Precision Metrology III | pp. 178.
Identifier and resource: [10.1117/12.3053679](https://doi.org/10.1117/12.3053679).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology III.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3053679); retrieved 2026-10-08.

#### Q0211 Nonlinear Spectroscopy via Generalized Quantum Phase Estimation

Ignacio Loaiza, Danial Motlagh, Kasra Hejazi, Modjtaba Shokrian Zini, Alain Delgado, Juan Miguel Arrazola.
Journal article | 2025 | Quantum | vol. 9 | pp. 1822 | article 1822.
Identifier and resource: [10.22331/q-2025-08-07-1822](https://doi.org/10.22331/q-2025-08-07-1822).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-08-07-1822); retrieved 2026-10-08.

#### Q0212 Quantum Phase Estimation

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 159-163.
Identifier and resource: [10.1007/978-3-032-03325-3_20](https://doi.org/10.1007/978-3-032-03325-3_20).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_20); retrieved 2026-10-08.

#### Q0213 Quantum phase estimation

Author metadata not supplied.
Book chapter | 2025 | Quantum Algorithms | pp. 228-234.
Identifier and resource: [10.1017/9781009639651.016](https://doi.org/10.1017/9781009639651.016).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781009639651.016); retrieved 2026-10-08.

#### Q0214 Quantum phase estimation-enabled phase tracking for coexisting quantum/classical metropolitan networks

Jabir Marakkarakath Vadakkepurayil, Daehyun H. Ahn, Nur Fajar R. Annafianto, Ivan Burenkov, Abdella Battou, Sergey Polyakov.
Conference paper | 2025 | Quantum Sensing, Imaging, and Precision Metrology III | pp. 144.
Identifier and resource: [10.1117/12.3043163](https://doi.org/10.1117/12.3043163).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology III.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3043163); retrieved 2026-10-08.

#### Q0215 Special Functions in Quantum Phase Estimation

Masahito Hayashi.
Book chapter | 2025 | CRM Series in Mathematical Physics | pp. 81-92.
Identifier and resource: [10.1007/978-3-031-90135-5_5](https://doi.org/10.1007/978-3-031-90135-5_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-90135-5_5); retrieved 2026-10-08.

#### Q0216 A differentiable quantum phase estimation algorithm

Davide Castaldo, Soran Jahangiri, Agostino Migliore, Juan Miguel Arrazola, Stefano Corni.
Journal article | 2024 | Quantum Science and Technology | vol. 9 | no. 4 | pp. 045026.
Identifier and resource: [10.1088/2058-9565/ad69bc](https://doi.org/10.1088/2058-9565/ad69bc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad69bc); retrieved 2026-10-08.

#### Q0217 Learning Quantum Phase Estimation by Variational Quantum Circuits

Chen-Yu Liu, Kuan-Cheng Chen, Chu-Hsuan Abraham Lin.
Conference paper | 2024 | 2024 International Joint Conference on Neural Networks (IJCNN) | pp. 1-6.
Identifier and resource: [10.1109/ijcnn60899.2024.10651206](https://doi.org/10.1109/ijcnn60899.2024.10651206).
Conference metadata: 2024 International Joint Conference on Neural Networks (IJCNN).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fijcnn60899.2024.10651206); retrieved 2026-10-08.

#### Q0218 Reductive quantum phase estimation

Nicholas J. C. Papadopoulos, Jarrod T. Reilly, John Drew Wilson, Murray J. Holland.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 3 | article 033051.
Identifier and resource: [10.1103/physrevresearch.6.033051](https://doi.org/10.1103/physrevresearch.6.033051).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.033051); retrieved 2026-10-08.

### D05T03 Amplitude amplification and search

Amplitude amplification raises the probability of a marked outcome. Search speedups are measured in oracle queries and must include the implementation of the marking operation.

Fine subcategories: Grover search; fixed point amplification; search lower bounds; unknown success probability.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0219 A fast quantum mechanical algorithm for database search

Lov K. Grover.
Conference paper | 1996 | Proceedings of the twenty-eighth annual ACM symposium on Theory of computing - STOC '96 | pp. 212-219.
Identifier and resource: [10.1145/237814.237866](https://doi.org/10.1145/237814.237866).
Conference metadata: Proceedings of the twenty-eighth annual ACM symposium on Theory of computing - STOC '96.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F237814.237866); retrieved 2026-10-08.

#### Q0220 Distributed exact quantum amplitude amplification algorithm for arbitrary quantum states

Xu Zhou, Wenxuan Tao, Keren Li, Shenggen Zheng.
Journal article | 2026 | Science China Information Sciences | vol. 69 | no. 8 | article 180506.
Identifier and resource: [10.1007/s11432-026-5020-7](https://doi.org/10.1007/s11432-026-5020-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11432-026-5020-7); retrieved 2026-10-08.

#### Q0221 QUANTUM SEARCH DYNAMICS: A COMPREHENSIVE ANALYSIS OF GROVER’S ALGORITHM AND AMPLITUDE AMPLIFICATION

Sripada Saipriya, Dr. Mahender Veshala.
Book chapter | 2026 | IIP Series | pp. 126-138.
Identifier and resource: [10.58532/nbennur3146c9](https://doi.org/10.58532/nbennur3146c9).
Fine tags: Grover search.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.58532%2Fnbennur3146c9); retrieved 2026-10-08.

#### Q0222 The Single-Rotation Quantum Search Algorithm: Amplitude Amplification with One Oracle Call

Ying Liu.
Journal article | 2026 | Journal of Quantum Information Science | vol. 16 | no. 02 | pp. 161-190.
Identifier and resource: [10.4236/jqis.2026.162006](https://doi.org/10.4236/jqis.2026.162006).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4236%2Fjqis.2026.162006); retrieved 2026-10-08.

#### Q0223 Limitations of quantum counting, nested quantum search and amplitude amplification and their potential to solve discrete optimization problems

Stefan Creemers, Luis Fernando Pérez Armas.
Journal article | 2025 | Philosophical Transactions of the Royal Society A Mathematical Physical and Engineering Sciences | vol. 383 | no. 2310 | article 20240561.
Identifier and resource: [10.1098/rsta.2024.0561](https://doi.org/10.1098/rsta.2024.0561).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1098%2Frsta.2024.0561); retrieved 2026-10-08.

#### Q0224 Optimized Amplitude Amplification for Quantum State Preparation

A. A. Chernikov, K. R. Zakharova, S. S. Sysoev.
Journal article | 2025 | Lobachevskii Journal of Mathematics | vol. 46 | no. 7 | pp. 3522-3526.
Identifier and resource: [10.1134/s1995080225606666](https://doi.org/10.1134/s1995080225606666).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1995080225606666); retrieved 2026-10-08.

#### Q0225 Quantum amplitude amplification operators: exact quantum search

Hyeokjea Kwon, Joonwoo Bae.
Conference paper | 2022 | Quantum Communications and Quantum Imaging XX | pp. 11.
Identifier and resource: [10.1117/12.2626449](https://doi.org/10.1117/12.2626449).
Conference metadata: Quantum Communications and Quantum Imaging XX.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2626449); retrieved 2026-10-08.

#### Q0226 Search by Quantum Walks on Two-Dimensional Grid without Amplitude Amplification

Andris Ambainis, Artūrs Bačkurs, Nikolajs Nahimovs, Raitis Ozols, Alexander Rivosh.
Book chapter | 2013 | Lecture Notes in Computer Science | pp. 87-97.
Identifier and resource: [10.1007/978-3-642-35656-8_7](https://doi.org/10.1007/978-3-642-35656-8_7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-642-35656-8_7); retrieved 2026-10-08.

### D05T04 Amplitude estimation

Amplitude estimation estimates a probability or expectation using structured quantum access. Near term variants trade coherent depth for sampling and inference.

Fine subcategories: Monte Carlo estimation; maximum likelihood estimation; iterative methods; confidence intervals.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0227 Component-wise Validation of Amplitude Encoding within Quantum Amplitude Estimation

Farhat Zargoun, Marwa Swidan.
Journal article | 2026 | AlQalam Journal of Medical and Applied Sciences.
Identifier and resource: [10.54361/ajmas.269746](https://doi.org/10.54361/ajmas.269746).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.54361%2Fajmas.269746); retrieved 2026-10-08.

#### Q0228 Entropic optimal transport with quantum amplitude estimation

Francisco Orts.
Journal article | 2026 | Future Generation Computer Systems | vol. 183 | pp. 108570 | article 108570.
Identifier and resource: [10.1016/j.future.2026.108570](https://doi.org/10.1016/j.future.2026.108570).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.future.2026.108570); retrieved 2026-10-08.

#### Q0229 Hardware-Efficient Quantum Grid Sampling for Low-Latency Amplitude Estimation

Yu-Ting Kao, Hao-Yu Lu, Yeong-Jar Chang, Jason Gemsun Young, Chao-Hung Wang, Darsen D. Lu.
Conference paper | 2026 | 2026 IEEE 19th Dallas Circuits and Systems Conference (DCAS) | pp. 1-5.
Identifier and resource: [10.1109/dcas69364.2026.11544432](https://doi.org/10.1109/dcas69364.2026.11544432).
Conference metadata: 2026 IEEE 19th Dallas Circuits and Systems Conference (DCAS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fdcas69364.2026.11544432); retrieved 2026-10-08.

#### Q0230 Harnessing Bayesian Statistics to Accelerate Iterative Quantum Amplitude Estimation

Qilin Li, Atharva Vidwans, Yazhen Wang, Micheline B. Soley.
Journal article | 2026 | Quantum | vol. 10 | pp. 1962 | article 1962.
Identifier and resource: [10.22331/q-2026-01-14-1962](https://doi.org/10.22331/q-2026-01-14-1962).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-01-14-1962); retrieved 2026-10-08.

#### Q0231 Quantum Amplitude Estimation in Practice: A Case Study in Option Pricing

Nouhaila Innan, Muhammad Kashif, Alberto Marchisio, Muhammad Moonis Usman, Muhammad Shafique.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 348-358.
Identifier and resource: [10.1007/978-3-032-13852-1_35](https://doi.org/10.1007/978-3-032-13852-1_35).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-13852-1_35); retrieved 2026-10-08.

#### Q0232 An efficient quantum computing based structural reliability analysis method using quantum amplitude estimation

Jingran He.
Journal article | 2025 | Structural Safety | vol. 114 | pp. 102555 | article 102555.
Identifier and resource: [10.1016/j.strusafe.2024.102555](https://doi.org/10.1016/j.strusafe.2024.102555).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.strusafe.2024.102555); retrieved 2026-10-08.

#### Q0233 Bayesian Quantum Amplitude Estimation

Alexandra Ramôa, Luis Paulo Santos.
Journal article | 2025 | Quantum | vol. 9 | pp. 1856 | article 1856.
Identifier and resource: [10.22331/q-2025-09-11-1856](https://doi.org/10.22331/q-2025-09-11-1856).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-09-11-1856); retrieved 2026-10-08.

#### Q0234 Classical postprocessing approach for quantum amplitude estimation

Yongdan Yang, Ruyu Yang.
Journal article | 2025 | Physical Review A | vol. 112 | no. 1 | article 012625.
Identifier and resource: [10.1103/z9hk-f37h](https://doi.org/10.1103/z9hk-f37h).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fz9hk-f37h); retrieved 2026-10-08.

#### Q0235 Evaluating Quantum Amplitude Estimation for Pricing Multi-Asset Basket Options

Muhammad Kashif, Shaf Khalid, Nouhaila Innan, Alberto Marchisio, Muhammad Shafique.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Artificial Intelligence (QAI) | pp. 451-458.
Identifier and resource: [10.1109/qai63978.2025.00076](https://doi.org/10.1109/qai63978.2025.00076).
Conference metadata: 2025 IEEE International Conference on Quantum Artificial Intelligence (QAI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqai63978.2025.00076); retrieved 2026-10-08.

#### Q0236 Quantum phase estimation and quantum amplitude estimation

Steven Herbert.
Book chapter | 2025 | Quantum Computing | pp. 155-175.
Identifier and resource: [10.1093/9780191964381.003.0009](https://doi.org/10.1093/9780191964381.003.0009).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2F9780191964381.003.0009); retrieved 2026-10-08.

#### Q0237 Adaptive measurement strategy for noisy quantum amplitude estimation with variational quantum circuits

Kohei Oshio, Yohichi Suzuki, Kaito Wada, Keigo Hisanaga, Shumpei Uno, Naoki Yamamoto.
Journal article | 2024 | Physical Review A | vol. 110 | no. 6 | article 062423.
Identifier and resource: [10.1103/physreva.110.062423](https://doi.org/10.1103/physreva.110.062423).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.062423); retrieved 2026-10-08.

#### Q0238 An Efficient Quantum Computing Based Reliability Analysis Method Using Quantum Amplitude Estimation

Jingran He.
Posted content | 2024 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.4870890](https://doi.org/10.2139/ssrn.4870890).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.4870890); retrieved 2026-10-08.

#### Q0239 Carbon market risk estimation using quantum conditional generative adversarial network and amplitude estimation

Xiyuan Zhou, Huan Zhao, Yuji Cao, Xiang Fei, Gaoqi Liang, Junhua Zhao.
Journal article | 2024 | Energy Conversion and Economics | vol. 5 | no. 4 | pp. 193-210.
Identifier and resource: [10.1049/enc2.12122](https://doi.org/10.1049/enc2.12122).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1049%2Fenc2.12122); retrieved 2026-10-08.

#### Q0240 Noise-Aware Quantum Amplitude Estimation

Steven Herbert, Ifan Williams, Roland Guichard, Darren Ng.
Journal article | 2024 | IEEE Transactions on Quantum Engineering | vol. 5 | pp. 1-23.
Identifier and resource: [10.1109/tqe.2024.3476929](https://doi.org/10.1109/tqe.2024.3476929).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2024.3476929); retrieved 2026-10-08.

#### Q0241 On the bias in iterative quantum amplitude estimation

Koichi Miyamoto.
Journal article | 2024 | EPJ Quantum Technology | vol. 11 | no. 1 | article 42.
Identifier and resource: [10.1140/epjqt/s40507-024-00253-x](https://doi.org/10.1140/epjqt/s40507-024-00253-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjqt%2Fs40507-024-00253-x); retrieved 2026-10-08.

#### Q0242 Quantum multi-programming for maximum likelihood amplitude estimation

Pooja Rao, Sua Choi, Kwangmin Yu.
Conference paper | 2024 | Quantum Computing, Communication, and Simulation IV | pp. 33.
Identifier and resource: [10.1117/12.3002854](https://doi.org/10.1117/12.3002854).
Conference metadata: Quantum Computing, Communication, and Simulation IV.
Fine tags: maximum likelihood estimation.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3002854); retrieved 2026-10-08.

### D05T05 Quantum walks

Quantum walks use interference in graph or configuration space to design algorithms. Walk dynamics, graph access, and hitting or detection tasks need separate definitions.

Fine subcategories: Discrete time walks; continuous time walks; hitting times; graph search; spatial search.

Primary resources: 11. Additional related assignments can be found in the interactive HTML.

#### Q0243 Boomerang quantum walks

A. R. C. Buarque, W. S. Dias, Ernesto P. Raposo.
Journal article | 2026 | Quantum Information Processing | vol. 25 | no. 6 | article 199.
Identifier and resource: [10.1007/s11128-026-05222-0](https://doi.org/10.1007/s11128-026-05222-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-026-05222-0); retrieved 2026-10-08.

#### Q0244 Quantum Computing and Quantum Walks

Fei Yan, Wen Liang, Fangyan Dong.
Book chapter | 2025 | Exploring Complex Networks with Quantum Walks | pp. 3-32.
Identifier and resource: [10.1201/9781003683902-2](https://doi.org/10.1201/9781003683902-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003683902-2); retrieved 2026-10-08.

#### Q0245 Quantum Walks

Peng Xue.
Book chapter | 2025 | Reference Module in Materials Science and Materials Engineering.
Identifier and resource: [10.1016/b978-0-443-33965-3.00003-1](https://doi.org/10.1016/b978-0-443-33965-3.00003-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-33965-3.00003-1); retrieved 2026-10-08.

#### Q0246 Asynchronous Quantum Random Walks

Manfred Harringer.
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-3372215/v5](https://doi.org/10.21203/rs.3.rs-3372215/v5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-3372215%2Fv5); retrieved 2026-10-08.

#### Q0247 A Crossover Between Open Quantum Random Walks to Quantum Walks

Norio Konno, Kaname Matsue, Etsuo Segawa.
Journal article | 2023 | Journal of Statistical Physics | vol. 190 | no. 12 | article 202.
Identifier and resource: [10.1007/s10955-023-03211-6](https://doi.org/10.1007/s10955-023-03211-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10955-023-03211-6); retrieved 2026-10-08.

#### Q0248 Irrational Quantum Walks

Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, Reinhard Werner.
Journal article | 2023 | SIAM Journal on Applied Algebra and Geometry | vol. 7 | no. 3 | pp. 567-584.
Identifier and resource: [10.1137/22m1521262](https://doi.org/10.1137/22m1521262).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F22m1521262); retrieved 2026-10-08.

#### Q0249 Multidimensional Quantum Walks

Stacey Jeffery, Sebastian Zur.
Conference paper | 2023 | Proceedings of the 55th Annual ACM Symposium on Theory of Computing | pp. 1125-1130.
Identifier and resource: [10.1145/3564246.3585158](https://doi.org/10.1145/3564246.3585158).
Conference metadata: STOC '23: 55th Annual ACM Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3564246.3585158); retrieved 2026-10-08.

#### Q0250 Quantum walks

Steven Duplij, Raimund Vogl.
Book chapter | 2023 | Innovative Quantum Computing | pp. 6-1-6-29.
Identifier and resource: [10.1088/978-0-7503-5281-9ch6](https://doi.org/10.1088/978-0-7503-5281-9ch6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F978-0-7503-5281-9ch6); retrieved 2026-10-08.

#### Q0251 Geodesic quantum walks

Giuseppe Di Molfetta, Victor Deng.
Journal article | 2022 | Physical Review A | vol. 105 | no. 6 | article 062420.
Identifier and resource: [10.1103/physreva.105.062420](https://doi.org/10.1103/physreva.105.062420).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.105.062420); retrieved 2026-10-08.

#### Q0252 On Quantum Algorithms for Random Walks in the Nonnegative Quarter Plane

Vasileios Kalantzis, Mark S. Squillante, Shashanka Ubaru, Lior Horesh.
Journal article | 2022 | ACM SIGMETRICS Performance Evaluation Review | vol. 50 | no. 2 | pp. 42-44.
Identifier and resource: [10.1145/3561074.3561089](https://doi.org/10.1145/3561074.3561089).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3561074.3561089); retrieved 2026-10-08.

#### Q0253 QUANTUM AI FRAMEWORKS: ENHANCING MACHINE LEARNING AND OPTIMIZATION THROUGH QUANTUM NEURAL NETWORKS, VARIATIONAL ALGORITHMS, AND QUANTUM WALKS

Narayana Gaddam.
Journal article | 2022 | INTERNATIONAL JOURNAL OF ADVANCED RESEARCH IN ENGINEERING AND TECHNOLOGY | vol. 13 | no. 6 | pp. 59-72.
Identifier and resource: [10.34218/ijaret_13_06_006](https://doi.org/10.34218/ijaret_13_06_006).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.34218%2Fijaret_13_06_006); retrieved 2026-10-08.

### D05T06 Hidden subgroup and factoring algorithms

Order finding underlies Shor factoring and discrete logarithm algorithms. Hidden subgroup methods generalize the structure, but non abelian cases have additional obstacles.

Fine subcategories: Shor algorithm; order finding; discrete logarithms; abelian subgroups; non abelian challenges.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0254 Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

Peter W. Shor.
Journal article | 1997 | SIAM Journal on Computing | vol. 26 | no. 5 | pp. 1484-1509.
Identifier and resource: [10.1137/s0097539795293172](https://doi.org/10.1137/s0097539795293172).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2FS0097539795293172); retrieved 2026-10-08.

#### Q0255 Shor Factoring Algorithm and the Quantum Fourier Transform

Alice Flarend, Robert Hilborn.
Book chapter | 2026 | Quantum Computing and Quantum Physics | pp. 272-293.
Identifier and resource: [10.1093/oso/9780197904930.003.0015](https://doi.org/10.1093/oso/9780197904930.003.0015).
Fine tags: Shor algorithm.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Foso%2F9780197904930.003.0015); retrieved 2026-10-08.

#### Q0256 Contributions of Quantum Factoring on Quantum Research

Clayton Ferner.
Journal article | 2022 | Computer | vol. 55 | no. 8 | pp. 5-7.
Identifier and resource: [10.1109/mc.2022.3178307](https://doi.org/10.1109/mc.2022.3178307).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmc.2022.3178307); retrieved 2026-10-08.

#### Q0257 Factoring Using Quantum Computers

Kristian Gjøsteen.
Book chapter | 2022 | Practical Mathematical Cryptography | pp. 137-146.
Identifier and resource: [10.1201/9781003149422-5](https://doi.org/10.1201/9781003149422-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003149422-5); retrieved 2026-10-08.

#### Q0258 Variational Quantum Factoring

Eric Anschuetz, Jonathan Olson, Alán Aspuru-Guzik, Yudong Cao.
Book chapter | 2019 | Lecture Notes in Computer Science | pp. 74-85.
Identifier and resource: [10.1007/978-3-030-14082-3_7](https://doi.org/10.1007/978-3-030-14082-3_7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-14082-3_7); retrieved 2026-10-08.

#### Q0259 Quantum Algorithm for Factoring

Sean Hallgren.
Book chapter | 2016 | Encyclopedia of Algorithms | pp. 1651-1652.
Identifier and resource: [10.1007/978-1-4939-2864-4_307](https://doi.org/10.1007/978-1-4939-2864-4_307).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-1-4939-2864-4_307); retrieved 2026-10-08.

#### Q0260 Quantum Computation | Mathematics | MIT OpenCourseWare

Author metadata not supplied.
Course | 2003 | MIT OpenCourseWare.
Identifier and resource: [Official resource](https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/); retrieved 2026-10-08.

#### Q0261 Quantum factoring, discrete logarithms, and the hidden subgroup problem

R. Jozsa.
Journal article | 2001 | Computing in Science & Engineering | vol. 3 | no. 2 | pp. 34-43.
Identifier and resource: [10.1109/5992.909000](https://doi.org/10.1109/5992.909000).
Fine tags: discrete logarithms.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2F5992.909000); retrieved 2026-10-08.

## D06 Advanced algorithm design

Modern algorithm frameworks organize linear algebra, simulation, and optimization around carefully controlled access models. Resource estimates depend strongly on how operators are encoded.

Prerequisites: Linear algebra, core quantum algorithms, and approximation theory.

Assessment focus: Block encoding normalization, conditioning, polynomial degree, and total cost.

Primary catalog resources in this category: 76.

### D06T01 Block encoding and qubitization

Block encodings embed an operator into a larger unitary, and qubitization builds controlled spectral transformations. Normalization and oracle construction are central resource assumptions.

Fine subcategories: Signal oracles; normalization factors; quantum walks; Hamiltonian access; projected unitary encodings.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0262 Quantum Möbius Transform via Block Encoding

Cezary Pilaszewicz.
Conference paper | 2026 | 2026 IEEE Conference on Artificial Intelligence (CAI) | pp. 1968-1972.
Identifier and resource: [10.1109/cai68641.2026.11536229](https://doi.org/10.1109/cai68641.2026.11536229).
Conference metadata: 2026 IEEE Conference on Artificial Intelligence (CAI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcai68641.2026.11536229); retrieved 2026-10-08.

#### Q0263 Quantum block encoding for one-pair semiseparable matrices

Giacomo Antonioli, Paola Boito, Gianna Maria Del Corso, Margherita Porcelli.
Journal article | 2026 | Numerical Algorithms.
Identifier and resource: [10.1007/s11075-026-02479-5](https://doi.org/10.1007/s11075-026-02479-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11075-026-02479-5); retrieved 2026-10-08.

#### Q0264 Quantum simulation of wave optics in weakly inhomogeneous media using block-encoding

Anonymous.
Journal article | 2026 | Physical Review Research.
Identifier and resource: [10.1103/snzq-fp39](https://doi.org/10.1103/snzq-fp39).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fsnzq-fp39); retrieved 2026-10-08.

#### Q0265 An efficient quantum circuit for block encoding a pairing Hamiltonian

Diyi Liu, Weijie Du, Lin Lin, James P. Vary, Chao Yang.
Journal article | 2025 | Journal of Computational Science | vol. 85 | pp. 102480 | article 102480.
Identifier and resource: [10.1016/j.jocs.2024.102480](https://doi.org/10.1016/j.jocs.2024.102480).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.jocs.2024.102480); retrieved 2026-10-08.

#### Q0266 Block encoding bosons by signal processing

Christopher F. Kane, Siddharth Hariprakash, Neel S. Modi, Michael Kreshchuk, Christian W Bauer.
Journal article | 2025 | Quantum | vol. 9 | pp. 1747 | article 1747.
Identifier and resource: [10.22331/q-2025-05-15-1747](https://doi.org/10.22331/q-2025-05-15-1747).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-05-15-1747); retrieved 2026-10-08.

#### Q0267 Classical optimization with imaginary-time block encoding on quantum computers: The MaxCut problem

Dawei Zhong, Akhil Francis, Ermal Rrapaj.
Journal article | 2025 | Physical Review A | vol. 112 | no. 4 | article 042420.
Identifier and resource: [10.1103/gtq3-j37b](https://doi.org/10.1103/gtq3-j37b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fgtq3-j37b); retrieved 2026-10-08.

#### Q0268 Exact block encoding of imaginary time evolution with universal quantum neural networks

Ermal Rrapaj, Evan Rule.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 1 | article 013306.
Identifier and resource: [10.1103/physrevresearch.7.013306](https://doi.org/10.1103/physrevresearch.7.013306).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.013306); retrieved 2026-10-08.

#### Q0269 GitHub - quantumlib/Qualtran: Qᴜᴀʟᴛʀᴀɴ is a Python library for expressing and analyzing Fault Tolerant Quantum algorithms. · GitHub

Author metadata not supplied.
Software repository | Undated | Google Quantum AI Qualtran.
Identifier and resource: [Official resource](https://github.com/quantumlib/Qualtran).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/quantumlib/Qualtran); retrieved 2026-10-08.

### D06T02 Quantum signal processing

Quantum signal processing implements constrained polynomial transformations through phase sequences. Polynomial degree, phase synthesis, and approximation error determine algorithm costs.

Fine subcategories: Polynomial transformations; phase factor synthesis; parity constraints; approximation error.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0270 An adversary bound for quantum signal processing

Lorenzo Laneve.
Journal article | 2026 | Quantum | vol. 10 | pp. 2025 | article 2025.
Identifier and resource: [10.22331/q-2026-03-13-2025](https://doi.org/10.22331/q-2026-03-13-2025).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-03-13-2025); retrieved 2026-10-08.

#### Q0271 Fast Phase Factor Finding for Quantum Signal Processing

Hongkang Ni, Lexing Ying.
Journal article | 2026 | SIAM Journal on Scientific Computing | vol. 48 | no. 4 | pp. B651-B670.
Identifier and resource: [10.1137/24m1705214](https://doi.org/10.1137/24m1705214).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F24m1705214); retrieved 2026-10-08.

#### Q0272 Mathematical and Numerical Analysis of Quantum Signal Processing

Lin Lin.
Conference paper | 2026 | Proceedings of the International Congress of Mathematicians 2026 - Volume 7: Invited Lectures (Sections 15–20) | pp. 57-74.
Identifier and resource: [10.1137/25m1806120](https://doi.org/10.1137/25m1806120).
Conference metadata: International Congress of Mathematicians 2026.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F25m1806120); retrieved 2026-10-08.

#### Q0273 Arbeitsgemeinschaft: Quantum Signal Processing and Nonlinear Fourier Analysis

András Gilyén, Lin Lin, Christoph Thiele.
Journal article | 2025 | Oberwolfach Reports | vol. 21 | no. 4 | pp. 2671-2750.
Identifier and resource: [10.4171/owr/2024/46](https://doi.org/10.4171/owr/2024/46).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4171%2Fowr%2F2024%2F46); retrieved 2026-10-08.

#### Q0274 Complementary Polynomials in Quantum Signal Processing

Bjorn K. Berntson, Christoph Sünderhauf.
Journal article | 2025 | Communications in Mathematical Physics | vol. 406 | no. 7 | article 161.
Identifier and resource: [10.1007/s00220-025-05302-9](https://doi.org/10.1007/s00220-025-05302-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00220-025-05302-9); retrieved 2026-10-08.

#### Q0275 Modular quantum signal processing in many variables

Zane M. Rossi, Jack L. Ceroni, Isaac L. Chuang.
Journal article | 2025 | Quantum | vol. 9 | pp. 1776 | article 1776.
Identifier and resource: [10.22331/q-2025-06-18-1776](https://doi.org/10.22331/q-2025-06-18-1776).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-06-18-1776); retrieved 2026-10-08.

#### Q0276 Parallel Quantum Signal Processing Via Polynomial Factorization

John M. Martyn, Zane M. Rossi, Kevin Z. Cheng, Yuan Liu, Isaac L. Chuang.
Journal article | 2025 | Quantum | vol. 9 | pp. 1834 | article 1834.
Identifier and resource: [10.22331/q-2025-08-27-1834](https://doi.org/10.22331/q-2025-08-27-1834).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-08-27-1834); retrieved 2026-10-08.

#### Q0277 Private Quantum Signal Processing

Akinori KAWACHI, Yuto NISHIKUBO.
Journal article | 2025 | IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences | vol. E108.A | no. 9 | pp. 1105-1113 | article 2024DMP0017.
Identifier and resource: [10.1587/transfun.2024dmp0017](https://doi.org/10.1587/transfun.2024dmp0017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1587%2Ftransfun.2024dmp0017); retrieved 2026-10-08.

#### Q0278 Prospects of quantum error mitigation for quantum signal processing

Ugnė Liaubaitė, S E Skelton.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 12 | pp. 125119.
Identifier and resource: [10.1088/1402-4896/ae216a](https://doi.org/10.1088/1402-4896/ae216a).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae216a); retrieved 2026-10-08.

#### Q0279 Quantum Machine Learning for Enhancing Signal Processing Applications

Kamineni Sairam, Shashikant Deepak, Rekha Chakravarthi, Saumendra Ku. Mohanty, P.S. Raghavendra Rao, Varsha Choudhary, Ankit Punia.
Journal article | 2025 | International Journal of Engineering, Science and Information Technology | vol. 5 | no. 2 | pp. 508-512.
Identifier and resource: [10.52088/ijesty.v5i2.1375](https://doi.org/10.52088/ijesty.v5i2.1375).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.52088%2Fijesty.v5i2.1375); retrieved 2026-10-08.

#### Q0280 Quantum signal processing and the quantum singular value transformation

Steven Herbert.
Book chapter | 2025 | Quantum Computing | pp. 253-276.
Identifier and resource: [10.1093/9780191964381.003.0014](https://doi.org/10.1093/9780191964381.003.0014).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2F9780191964381.003.0014); retrieved 2026-10-08.

#### Q0281 Qubitization and Quantum Signal Processing

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 179-183.
Identifier and resource: [10.1007/978-3-032-03325-3_23](https://doi.org/10.1007/978-3-032-03325-3_23).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_23); retrieved 2026-10-08.

#### Q0282 Statistical Signal Processing for Quantum Error Mitigation

Kausthubh Chandramouli, Kelly Mae Allen, Christopher Mori, Dror Baron, Mário A. T. Figueiredo.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 269-275.
Identifier and resource: [10.1109/qce65121.2025.00038](https://doi.org/10.1109/qce65121.2025.00038).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00038); retrieved 2026-10-08.

#### Q0283 Derivative Pricing using Quantum Signal Processing

Nikitas Stamatopoulos, William J. Zeng.
Journal article | 2024 | Quantum | vol. 8 | pp. 1322 | article 1322.
Identifier and resource: [10.22331/q-2024-04-30-1322](https://doi.org/10.22331/q-2024-04-30-1322).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-04-30-1322); retrieved 2026-10-08.

#### Q0284 Generalized Quantum Signal Processing

Danial Motlagh, Nathan Wiebe.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 2 | article 020368.
Identifier and resource: [10.1103/prxquantum.5.020368](https://doi.org/10.1103/prxquantum.5.020368).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.020368); retrieved 2026-10-08.

#### Q0285 Infinite quantum signal processing

Yulong Dong, Lin Lin, Hongkang Ni, Jiasu Wang.
Journal article | 2024 | Quantum | vol. 8 | pp. 1558 | article 1558.
Identifier and resource: [10.22331/q-2024-12-10-1558](https://doi.org/10.22331/q-2024-12-10-1558).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-12-10-1558); retrieved 2026-10-08.

### D06T03 Quantum singular value transformation

Singular value transformation applies polynomial functions to the singular values of a block encoded matrix. It unifies many algorithms while making access assumptions explicit.

Fine subcategories: Matrix functions; singular value thresholds; pseudoinverses; spectral filtering; polynomial degree.

Primary resources: 18. Additional related assignments can be found in the interactive HTML.

#### Q0286 Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics

András Gilyén, Yuan Su, Guang Hao Low, Nathan Wiebe.
Conference paper | 2019 | Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing | pp. 193-204.
Identifier and resource: [10.1145/3313276.3316366](https://doi.org/10.1145/3313276.3316366).
Conference metadata: Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3313276.3316366); retrieved 2026-10-08.

#### Q0287 Avoiding Singular Value Thresholding in Quantum Low-Rank Recovery

Angshul Majumdar.
Journal article | 2026 | IEEE Signal Processing Letters | vol. 33 | pp. 2820-2824.
Identifier and resource: [10.1109/lsp.2026.3710103](https://doi.org/10.1109/lsp.2026.3710103).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Flsp.2026.3710103); retrieved 2026-10-08.

#### Q0288 Improved Performance of Quantum Search via Quantum Singular Value Transformation

Zheng Zhang, Minzhong Luo.
Conference paper | 2026 | Proceedings of the 2026 7th International Conference on Computer Information and Big Data Applications | pp. 240-244.
Identifier and resource: [10.1145/3813822.3813860](https://doi.org/10.1145/3813822.3813860).
Conference metadata: CIBDA 2026: 2026 7th International Conference on Computer Information and Big Data Applications.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3813822.3813860); retrieved 2026-10-08.

#### Q0289 SIGNAL DENOISING BASED ON QUANTUM ADAPTIVE TRANSFORMATION AND SINGULAR VALUE DECOMPOSITION

YingYing Sun, MengYao Lv, ChenLin Wu, WeiXian Xie, ZiYuan Fang, RuiTong Zhao.
Journal article | 2026 | Journal of Computer Science and Electrical Engineering | vol. 8 | no. 3 | pp. 27-33.
Identifier and resource: [10.61784/jcsee3134](https://doi.org/10.61784/jcsee3134).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.61784%2Fjcsee3134); retrieved 2026-10-08.

#### Q0290 Simple Harmonic Motion Analysis of Elastic Structures Using Hamiltonian Simulation via Quantum Singular Value Transformation

Koya Wagatsuma, Katsuhiro Endo, Kenjiro Terada.
Journal article | 2026 | International Journal for Numerical Methods in Engineering | vol. 127 | no. 16 | article e70407.
Identifier and resource: [10.1002/nme.70407](https://doi.org/10.1002/nme.70407).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fnme.70407); retrieved 2026-10-08.

#### Q0291 Singular value transformation for unknown quantum channels

Ryotaro Niwa, Zane Marius Rossi, Philip Taranto, Mio Murao.
Journal article | 2026 | Physical Review A | vol. 114 | no. 3 | article L030401.
Identifier and resource: [10.1103/321q-k5dh](https://doi.org/10.1103/321q-k5dh).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F321q-k5dh); retrieved 2026-10-08.

#### Q0292 Correction: Robust dequantization of the quantum singular value transformation and quantum machine learning algorithms

François Le Gall.
Journal article | 2025 | computational complexity | vol. 34 | no. 1 | article 5.
Identifier and resource: [10.1007/s00037-025-00265-8](https://doi.org/10.1007/s00037-025-00265-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00037-025-00265-8); retrieved 2026-10-08.

#### Q0293 Implementing Credit Risk Analysis with Quantum Singular Value Transformation

Davide Veronelli, Francesca Cibrario, Emanuele Dri, Valeria Zaffaroni, Giacomo Ranieri, Davide Corbelletto, Bartolomeo Montrucchio.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 2228-2237.
Identifier and resource: [10.1109/qce65121.2025.00243](https://doi.org/10.1109/qce65121.2025.00243).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00243); retrieved 2026-10-08.

#### Q0294 Improved quantum power method and numerical integration using a quantum singular-value transformation

Nhat A. Nghiem, Hiroki Sukeno, Shuyu Zhang, Tzu-Chieh Wei.
Journal article | 2025 | Physical Review A | vol. 111 | no. 1 | article 012434.
Identifier and resource: [10.1103/physreva.111.012434](https://doi.org/10.1103/physreva.111.012434).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.012434); retrieved 2026-10-08.

#### Q0295 Matrix Encoding Method in Variational Quantum Singular Value Decomposition

Alexander I. Zenchuk, Wentao Qi, Junde Wu.
Journal article | 2025 | Quantum Information &amp; Computation | vol. 25 | no. 4 | pp. 356-368.
Identifier and resource: [10.2478/qic-2025-0020](https://doi.org/10.2478/qic-2025-0020).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2478%2Fqic-2025-0020); retrieved 2026-10-08.

#### Q0296 Robust Dequantization of the Quantum Singular Value Transformation and Quantum Machine Learning Algorithms

François Le Gall.
Journal article | 2025 | computational complexity | vol. 34 | no. 1 | article 2.
Identifier and resource: [10.1007/s00037-024-00262-3](https://doi.org/10.1007/s00037-024-00262-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00037-024-00262-3); retrieved 2026-10-08.

#### Q0297 A CS guide to the quantum singular value transformation

Ewin Tang, Kevin Tian.
Book chapter | 2024 | 2024 Symposium on Simplicity in Algorithms (SOSA) | pp. 121-143.
Identifier and resource: [10.1137/1.9781611977936.13](https://doi.org/10.1137/1.9781611977936.13).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F1.9781611977936.13); retrieved 2026-10-08.

#### Q0298 An Improved Classical Singular Value Transformation for Quantum Machine Learning

Ainesh Bakshi, Ewin Tang.
Book chapter | 2024 | Proceedings of the 2024 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | pp. 2398-2453.
Identifier and resource: [10.1137/1.9781611977912.86](https://doi.org/10.1137/1.9781611977912.86).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F1.9781611977912.86); retrieved 2026-10-08.

#### Q0299 Nonlinear transformation of complex amplitudes via quantum singular value transformation

Naixu Guo, Kosuke Mitarai, Keisuke Fujii.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 4 | article 043227.
Identifier and resource: [10.1103/physrevresearch.6.043227](https://doi.org/10.1103/physrevresearch.6.043227).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.043227); retrieved 2026-10-08.

#### Q0300 Recursive quantum eigenvalue and singular-value transformation: Analytic construction of matrix sign function by Newton iteration

Kaoru Mizuta, Keisuke Fujii.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 1 | article L012007.
Identifier and resource: [10.1103/physrevresearch.6.l012007](https://doi.org/10.1103/physrevresearch.6.l012007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.l012007); retrieved 2026-10-08.

#### Q0301 Singular Value Decomposition Quantum Algorithm for Quantum Biology

Emily K. Oh, Timothy J. Krogmeier, Anthony W. Schlimgen, Kade Head-Marsden.
Journal article | 2024 | ACS Physical Chemistry Au | vol. 4 | no. 4 | pp. 393-399.
Identifier and resource: [10.1021/acsphyschemau.4c00018](https://doi.org/10.1021/acsphyschemau.4c00018).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facsphyschemau.4c00018); retrieved 2026-10-08.

#### Q0302 Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture

Sevag Gharibian, François Le Gall.
Journal article | 2023 | SIAM Journal on Computing | vol. 52 | no. 4 | pp. 1009-1038.
Identifier and resource: [10.1137/22m1513721](https://doi.org/10.1137/22m1513721).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F22m1513721); retrieved 2026-10-08.

#### Q0303 Simulation of Linear Non-Hermitian Boundary-Value Problems with Quantum Singular-Value Transformation

I. Novikau, I.Y. Dodin, E.A. Startsev.
Journal article | 2023 | Physical Review Applied | vol. 19 | no. 5 | article 054012.
Identifier and resource: [10.1103/physrevapplied.19.054012](https://doi.org/10.1103/physrevapplied.19.054012).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.19.054012); retrieved 2026-10-08.

### D06T04 Linear combination of unitaries

Linear combinations of unitaries implement operators using coherent selection and state preparation. Success probability and amplification overhead affect the final resource estimate.

Fine subcategories: PREPARE and SELECT oracles; oblivious amplification; Taylor series simulation; success probability.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0304 Efficient Quantum Circuit Implementations of The qDRIFT Algorithm via Linear Combinations of Unitaries and Quantum Forking

I. J. David, I. Sinayskiy, F. Petruccione.
Journal article | 2025 | Journal of Physics: Conference Series | vol. 2970 | no. 1 | pp. 012004.
Identifier and resource: [10.1088/1742-6596/2970/1/012004](https://doi.org/10.1088/1742-6596/2970/1/012004).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F2970%2F1%2F012004); retrieved 2026-10-08.

#### Q0305 Hamiltonian dynamics simulation using linear combination of unitaries on an ion trap quantum computer

Michelle Wynne Sze, Yao Tang, Silas Dilkes, David Muñoz Ramo, Ross Duncan, Nathan Fitzpatrick.
Journal article | 2025 | Quantum Science and Technology | vol. 11 | no. 1 | pp. 015023.
Identifier and resource: [10.1088/2058-9565/ae2292](https://doi.org/10.1088/2058-9565/ae2292).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae2292); retrieved 2026-10-08.

#### Q0306 Majorana tensor decomposition: a unifying framework for decompositions of fermionic Hamiltonians to linear combination of unitaries

Ignacio Loaiza, Aritra Sankar Brahmachari, Artur F Izmaylov.
Journal article | 2025 | Quantum Science and Technology | vol. 10 | no. 3 | pp. 035035.
Identifier and resource: [10.1088/2058-9565/add9c1](https://doi.org/10.1088/2058-9565/add9c1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fadd9c1); retrieved 2026-10-08.

#### Q0307 An Optimal Linear-combination-of-unitaries-based Quantum Linear System Solver

Sander Gribling, Iordanis Kerenidis, Dániel Szilágyi.
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 2 | pp. 1-23.
Identifier and resource: [10.1145/3649320](https://doi.org/10.1145/3649320).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3649320); retrieved 2026-10-08.

#### Q0308 Implementing any Linear Combination of Unitaries on Intermediate-term Quantum Computers

Shantanav Chakraborty.
Journal article | 2024 | Quantum | vol. 8 | pp. 1496 | article 1496.
Identifier and resource: [10.22331/q-2024-10-10-1496](https://doi.org/10.22331/q-2024-10-10-1496).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-10-10-1496); retrieved 2026-10-08.

#### Q0309 Programmable silicon-photonic quantum simulator based on a linear combination of unitaries

Yue Yu, Yulin Chi, Chonghao Zhai, Jieshan Huang, Qihuang Gong, Jianwei Wang.
Journal article | 2024 | Photonics Research | vol. 12 | no. 8 | pp. 1760.
Identifier and resource: [10.1364/prj.517294](https://doi.org/10.1364/prj.517294).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fprj.517294); retrieved 2026-10-08.

#### Q0310 Efficient Application of the Factorized form of the Unitary Coupled-Cluster Ansatz for the Variational Quantum Eigensolver Algorithm by Using Linear Combination of Unitaries

Luogen Xu, James K. Freericks.
Journal article | 2023 | Symmetry | vol. 15 | no. 7 | pp. 1429.
Identifier and resource: [10.3390/sym15071429](https://doi.org/10.3390/sym15071429).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fsym15071429); retrieved 2026-10-08.

#### Q0311 Fast black-box quantum state preparation based on linear combination of unitaries

Shengbin Wang, Zhimin Wang, Guolong Cui, Shangshang Shi, Ruimin Shang, Lixin Fan, Wendong Li, Zhiqiang Wei et al..
Journal article | 2021 | Quantum Information Processing | vol. 20 | no. 8 | article 270.
Identifier and resource: [10.1007/s11128-021-03203-z](https://doi.org/10.1007/s11128-021-03203-z).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-021-03203-z); retrieved 2026-10-08.

### D06T05 Quantum linear systems

Quantum linear systems algorithms prepare a state related to a linear system solution. Extracting every solution component can remove the intended advantage.

Fine subcategories: HHL; condition numbers; sparse access; solution observables; preconditioning.

Primary resources: 10. Additional related assignments can be found in the interactive HTML.

#### Q0312 A VARIATIONAL QUANTUM ALGORITHM FOR SOLVING LINEAR SYSTEMS FOR DECISION SUPPORT SYSTEMS

Author metadata not supplied.
Journal article | 2026 | Telecommunication and information technologies | vol. 92 | no. 3 | pp. 46-51.
Identifier and resource: [10.31673/2412-4338.2026.039705](https://doi.org/10.31673/2412-4338.2026.039705).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.31673%2F2412-4338.2026.039705); retrieved 2026-10-08.

#### Q0313 Quantum algorithm for linear systems

Yunah Choi, Jeihee Cho, Shiho Kim.
Book chapter | 2026 | Advances in Computers | pp. 1-26.
Identifier and resource: [10.1016/bs.adcom.2025.11.001](https://doi.org/10.1016/bs.adcom.2025.11.001).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fbs.adcom.2025.11.001); retrieved 2026-10-08.

#### Q0314 Resource-efficient quantum algorithm for linear systems of equations

Francesco Ghisoni, Francesco Scala, Daniele Bajoni, Dario Gerace.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032405.
Identifier and resource: [10.1103/gwzg-4pls](https://doi.org/10.1103/gwzg-4pls).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fgwzg-4pls); retrieved 2026-10-08.

#### Q0315 A mixed-precision quantum-classical algorithm for solving linear systems

Océane Koska, Marc Baboulin, Arnaud Gazda.
Conference paper | 2025 | 2025 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW) | pp. 501-508.
Identifier and resource: [10.1109/ipdpsw66978.2025.00081](https://doi.org/10.1109/ipdpsw66978.2025.00081).
Conference metadata: 2025 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fipdpsw66978.2025.00081); retrieved 2026-10-08.

#### Q0316 Quantum Iterative Algorithm for Linear Systems of Equation

Debasish Roy, Sambo Raj Chandra.
Book chapter | 2024 | Lecture Notes in Networks and Systems | pp. 560-575.
Identifier and resource: [10.1007/978-3-031-62281-6_38](https://doi.org/10.1007/978-3-031-62281-6_38).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-62281-6_38); retrieved 2026-10-08.

#### Q0317 Quantum multirow iteration algorithm for linear systems with nonsquare coefficient matrices

Weitao Lin, Guojing Tian, Xiaoming Sun.
Journal article | 2024 | Physical Review A | vol. 110 | no. 2 | article 022438.
Identifier and resource: [10.1103/physreva.110.022438](https://doi.org/10.1103/physreva.110.022438).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.022438); retrieved 2026-10-08.

#### Q0318 Coherence dynamics in quantum algorithm for linear systems of equations

Linlin Ye, Zhaoqi Wu, Shao-Ming Fei.
Journal article | 2023 | Physica Scripta | vol. 98 | no. 12 | pp. 125104.
Identifier and resource: [10.1088/1402-4896/ad0584](https://doi.org/10.1088/1402-4896/ad0584).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fad0584); retrieved 2026-10-08.

#### Q0319 Enhancing the Quantum Linear Systems Algorithm Using Richardson Extrapolation

Almudena Carrera Vazquez, Ralf Hiptmair, Stefan Woerner.
Journal article | 2022 | ACM Transactions on Quantum Computing | vol. 3 | no. 1 | pp. 1-37.
Identifier and resource: [10.1145/3490631](https://doi.org/10.1145/3490631).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3490631); retrieved 2026-10-08.

#### Q0320 Quantum linear system algorithm applied to communication systems

Jeonghoon Park, Jun Heo.
Journal article | 2022 | Quantum Information Processing | vol. 21 | no. 7 | article 267.
Identifier and resource: [10.1007/s11128-022-03598-3](https://doi.org/10.1007/s11128-022-03598-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-022-03598-3); retrieved 2026-10-08.

#### Q0321 Solving Large‐Scale Linear Systems of Equations by a Quantum Hybrid Algorithm

M. R. Perelshtein, A. I. Pakhomchik, A. A. Melnikov, A. A. Novikov, A. Glatz, G. S. Paraoanu, V. M. Vinokur, G. B. Lesovik.
Journal article | 2022 | Annalen der Physik | vol. 534 | no. 7 | article 2200082.
Identifier and resource: [10.1002/andp.202200082](https://doi.org/10.1002/andp.202200082).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fandp.202200082); retrieved 2026-10-08.

### D06T06 Quantum differential equations

Differential equation algorithms encode time evolution or discretized solution vectors. Stability, conditioning, boundary conditions, and output observables all enter the analysis.

Fine subcategories: Ordinary differential equations; partial differential equations; stability; boundary conditions; solution readout.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0322 Fast-forwarding quantum algorithms for linear dissipative differential equations

Dong An, Akwum Onwunta, Gengzhi Yang.
Journal article | 2026 | Quantum | vol. 10 | pp. 1986 | article 1986.
Identifier and resource: [10.22331/q-2026-01-27-1986](https://doi.org/10.22331/q-2026-01-27-1986).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-01-27-1986); retrieved 2026-10-08.

#### Q0323 H-DES: a quantum–classical hybrid differential equation solver

Hamza Jaffali, Jonas Bastos de Araujo, Nadia Milazzo, Marta Reina, Henri de Boutray, Karla Baumann, Frédéric Holweck, Youcef Mohdeb et al..
Journal article | 2026 | Physica Scripta | vol. 101 | no. 21 | pp. 215107.
Identifier and resource: [10.1088/1402-4896/ae6404](https://doi.org/10.1088/1402-4896/ae6404).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae6404); retrieved 2026-10-08.

#### Q0324 Compact quantum algorithms for time-dependent differential equations

Sachin S. Bharadwaj, Katepalli R. Sreenivasan.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 2 | article 023262.
Identifier and resource: [10.1103/physrevresearch.7.023262](https://doi.org/10.1103/physrevresearch.7.023262).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.023262); retrieved 2026-10-08.

#### Q0325 Quantum Algorithms for Stochastic Differential Equations: A Schrödingerisation Approach

Shi Jin, Nana Liu, Wei Wei.
Journal article | 2025 | Journal of Scientific Computing | vol. 104 | no. 2 | article 56.
Identifier and resource: [10.1007/s10915-025-02970-6](https://doi.org/10.1007/s10915-025-02970-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10915-025-02970-6); retrieved 2026-10-08.

#### Q0326 Quantum Differential Equation Solvers: Limitations and Fast-Forwarding

Dong An, Jin-Peng Liu, Daochen Wang, Qi Zhao.
Journal article | 2025 | Communications in Mathematical Physics | vol. 406 | no. 8 | article 189.
Identifier and resource: [10.1007/s00220-025-05358-7](https://doi.org/10.1007/s00220-025-05358-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00220-025-05358-7); retrieved 2026-10-08.

#### Q0327 Quantum Ordinary Differential Equation Algorithms: Block-Matrix Algorithms

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 259-265.
Identifier and resource: [10.1007/978-3-032-03325-3_32](https://doi.org/10.1007/978-3-032-03325-3_32).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_32); retrieved 2026-10-08.

#### Q0328 Quantum Ordinary Differential Equation Algorithms: Time-Marching Algorithms

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 267-269.
Identifier and resource: [10.1007/978-3-032-03325-3_33](https://doi.org/10.1007/978-3-032-03325-3_33).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_33); retrieved 2026-10-08.

#### Q0329 Quantum Partial Differential Equation Algorithms

Osama M. Raisuddin, Suvranu De.
Book chapter | 2025 | Quantum Computing for Engineers | pp. 271-275.
Identifier and resource: [10.1007/978-3-032-03325-3_34](https://doi.org/10.1007/978-3-032-03325-3_34).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03325-3_34); retrieved 2026-10-08.

#### Q0330 Variational Quantum Algorithms for Differential Equations on a Noisy Quantum Computer

Niclas Schillo, Andreas Sturm.
Journal article | 2025 | IEEE Transactions on Quantum Engineering | vol. 6 | pp. 1-16.
Identifier and resource: [10.1109/tqe.2025.3532017](https://doi.org/10.1109/tqe.2025.3532017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2025.3532017); retrieved 2026-10-08.

#### Q0331 Variational Quantum Framework for Partial Differential Equation Constrained Optimization

Amit Surana, Abeynaya Gnanasekaran.
Journal article | 2025 | ACM Transactions on Quantum Computing | vol. 7 | no. 1 | pp. 1-36.
Identifier and resource: [10.1145/3762671](https://doi.org/10.1145/3762671).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3762671); retrieved 2026-10-08.

#### Q0332 Diffusion-Based Quantum Error Mitigation Using Stochastic Differential Equation

Joo Yong Shim, Joongheon Kim.
Conference paper | 2024 | 2024 IEEE VTS Asia Pacific Wireless Communications Symposium (APWCS) | pp. 1-5.
Identifier and resource: [10.1109/apwcs61586.2024.10679306](https://doi.org/10.1109/apwcs61586.2024.10679306).
Conference metadata: 2024 VTS Asia Pacific Wireless Communications Symposium (APWCS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fapwcs61586.2024.10679306); retrieved 2026-10-08.

#### Q0333 Quantum Algorithms for Multiscale Partial Differential Equations

Junpeng Hu, Shi Jin, Lei Zhang.
Journal article | 2024 | Multiscale Modeling & Simulation | vol. 22 | no. 3 | pp. 1030-1067.
Identifier and resource: [10.1137/23m1566340](https://doi.org/10.1137/23m1566340).
Fine tags: partial differential equations.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F23m1566340); retrieved 2026-10-08.

#### Q0334 Quantum Computing Solution to Sturm-Liouville Differential Equation

Author metadata not supplied.
Journal article | 2024 | International Journal of Innovative Research in Physics | vol. 5 | no. 2.
Identifier and resource: [10.15864/ijiip.5203](https://doi.org/10.15864/ijiip.5203).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15864%2Fijiip.5203); retrieved 2026-10-08.

#### Q0335 Quantum algorithm for dynamic mode decomposition integrated with a quantum differential equation solver

Yuta Mizuno, Tamiki Komatsuzaki.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 4 | article 043031.
Identifier and resource: [10.1103/physrevresearch.6.043031](https://doi.org/10.1103/physrevresearch.6.043031).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.043031); retrieved 2026-10-08.

#### Q0336 Quantum algorithms for nonlinear partial differential equations

Shi Jin, Nana Liu.
Journal article | 2024 | Bulletin des Sciences Mathématiques | vol. 194 | pp. 103457 | article 103457.
Identifier and resource: [10.1016/j.bulsci.2024.103457](https://doi.org/10.1016/j.bulsci.2024.103457).
Fine tags: partial differential equations.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.bulsci.2024.103457); retrieved 2026-10-08.

#### Q0337 Quantum Algorithms for Nonlinear Partial Differential Equations

Shi Jin, Nana Liu.
Posted content | 2023 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.4353562](https://doi.org/10.2139/ssrn.4353562).
Fine tags: partial differential equations.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.4353562); retrieved 2026-10-08.

## D07 Hamiltonian simulation and many body physics

Quantum simulation targets the evolution and observables of physical systems. Digital, analog, and hybrid approaches have different error budgets and verification methods.

Prerequisites: Quantum mechanics, Hamiltonians, and many body physics.

Assessment focus: Simulation error, model truncation, observables, and classical verification.

Primary catalog resources in this category: 56.

### D07T01 Digital Hamiltonian simulation

Digital simulation approximates Hamiltonian evolution with a programmable sequence of gates. The comparison should include accuracy, sparsity, simulation time, and compilation cost.

Fine subcategories: Trotter formulas; error bounds; interaction picture; sparse Hamiltonians; time dependent evolution.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0338 Diagonal-Budgeted Trotterization for Efficient Quantum Hamiltonian Simulation

Srikar Chundury, Blake Burgstahler, Jiajia Li, In-Saeng Suh, Frank Mueller.
Conference paper | 2026 | Proceedings of the 40th ACM International Conference on Supercomputing | pp. 1350-1362.
Identifier and resource: [10.1145/3797905.3807869](https://doi.org/10.1145/3797905.3807869).
Conference metadata: ICS '26: 2026 International Conference on Supercomputing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3797905.3807869); retrieved 2026-10-08.

#### Q0339 Practical limitations on Hamiltonian simulation using quantum processors

Abhishek Sadhu, Mandira Dey, Debashree Ghosh.
Journal article | 2026 | Electronic Structure | vol. 8 | no. 3 | pp. 035006.
Identifier and resource: [10.1088/2516-1075/ae97a8](https://doi.org/10.1088/2516-1075/ae97a8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2516-1075%2Fae97a8); retrieved 2026-10-08.

#### Q0340 Snapshot-QAOA: Extending QAOA to Quantum Hamiltonian Simulation

Reuben Tate, Quinn Langfitt, Elijah Pelofske, Ammar Kirmani, Andreas Bärtschi, John Golden, Stephan Eidenbenz.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-9171925/v1](https://doi.org/10.21203/rs.3.rs-9171925/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-9171925%2Fv1); retrieved 2026-10-08.

#### Q0341 Quantum Hamiltonian Simulation of Time-Domain Electromagnetic Fields

E. Colella, L. Bastianelli, V. Mariani Primiani, F. Moglie, G. Gradoni.
Conference paper | 2025 | 2025 International Conference on Electromagnetics in Advanced Applications (ICEAA) | pp. 1-1.
Identifier and resource: [10.1109/iceaa65662.2025.11305881](https://doi.org/10.1109/iceaa65662.2025.11305881).
Conference metadata: 2025 International Conference on Electromagnetics in Advanced Applications (ICEAA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficeaa65662.2025.11305881); retrieved 2026-10-08.

#### Q0342 A Mathematical Framework for Quantum Hamiltonian Simulation and Duality

Harriet Apel, Toby Cubitt.
Journal article | 2024 | Annales Henri Poincaré | vol. 26 | no. 1 | pp. 317-364.
Identifier and resource: [10.1007/s00023-024-01432-3](https://doi.org/10.1007/s00023-024-01432-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00023-024-01432-3); retrieved 2026-10-08.

#### Q0343 Parallel Quantum Algorithm for Hamiltonian Simulation

Zhicheng Zhang, Qisheng Wang, Mingsheng Ying.
Journal article | 2024 | Quantum | vol. 8 | pp. 1228 | article 1228.
Identifier and resource: [10.22331/q-2024-01-15-1228](https://doi.org/10.22331/q-2024-01-15-1228).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-01-15-1228); retrieved 2026-10-08.

#### Q0344 Quantum computing of reacting flows via Hamiltonian simulation

Zhen Lu, Yue Yang.
Journal article | 2024 | Proceedings of the Combustion Institute | vol. 40 | no. 1-4 | pp. 105440 | article 105440.
Identifier and resource: [10.1016/j.proci.2024.105440](https://doi.org/10.1016/j.proci.2024.105440).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.proci.2024.105440); retrieved 2026-10-08.

#### Q0345 Riemannian quantum circuit optimization for Hamiltonian simulation

Ayse Kotil, Rahul Banerjee, Qunsheng Huang, Christian B Mendl.
Journal article | 2024 | Journal of Physics A: Mathematical and Theoretical | vol. 57 | no. 13 | pp. 135303.
Identifier and resource: [10.1088/1751-8121/ad2d6e](https://doi.org/10.1088/1751-8121/ad2d6e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1751-8121%2Fad2d6e); retrieved 2026-10-08.

### D07T02 Analog quantum simulation

Analog simulators engineer a physical Hamiltonian to approximate a target model. Calibration and validation are especially important when universal digital corrections are unavailable.

Fine subcategories: Hamiltonian engineering; cold atoms; trapped ions; spin models; simulator calibration.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0346 Simulating physics with computers

Richard P. Feynman.
Journal article | 1982 | International Journal of Theoretical Physics | vol. 21 | no. 6-7 | pp. 467-488.
Identifier and resource: [10.1007/bf02650179](https://doi.org/10.1007/bf02650179).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2FBF02650179); retrieved 2026-10-08.

#### Q0347 Analog quantum simulation of chiral magnetic dynamics using optical superlattices

Sabhyata Gupta, Luis Santos.
Journal article | 2026 | Physical Review A | vol. 114 | no. 3 | article 033321.
Identifier and resource: [10.1103/hr8d-ttj8](https://doi.org/10.1103/hr8d-ttj8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fhr8d-ttj8); retrieved 2026-10-08.

#### Q0348 Hamiltonian simulation with explicit formulas for digital-analog quantum computing

Mikel Garcia de Andoin, Thorge Müller, Gonzalo Camacho.
Journal article | 2026 | Physical Review A | vol. 113 | no. 6 | article 062607.
Identifier and resource: [10.1103/nzxg-5lbg](https://doi.org/10.1103/nzxg-5lbg).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fnzxg-5lbg); retrieved 2026-10-08.

#### Q0349 Accuracy Guarantees and Quantum Advantage in Analog Open Quantum Simulation with and without Noise

Vikram Kashyap, Georgios Styliaris, Sara Mouradian, J. Ignacio Cirac, Rahul Trivedi.
Journal article | 2025 | Physical Review X | vol. 15 | no. 2 | article 021017.
Identifier and resource: [10.1103/physrevx.15.021017](https://doi.org/10.1103/physrevx.15.021017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.15.021017); retrieved 2026-10-08.

#### Q0350 Analog Quantum Simulation via Rydberg Dressing

Arinjoy De, Majd Hamdan, Milan Kornjaca, Alexei Bylinskii.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 520-521.
Identifier and resource: [10.1109/qce65121.2025.10425](https://doi.org/10.1109/qce65121.2025.10425).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10425); retrieved 2026-10-08.

#### Q0351 Analog quantum simulation of coupled electron-nuclear dynamics in molecules

Jong-Kwon Ha, Ryan J. MacDonell.
Journal article | 2025 | Chemical Science | vol. 16 | no. 41 | pp. 19423-19435.
Identifier and resource: [10.1039/d5sc04076k](https://doi.org/10.1039/d5sc04076k).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1039%2Fd5sc04076k); retrieved 2026-10-08.

#### Q0352 Analog simulation of noisy quantum circuits

Etienne Granet, Kévin Hémery, Henrik Dreyer.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 1 | article 013213.
Identifier and resource: [10.1103/physrevresearch.7.013213](https://doi.org/10.1103/physrevresearch.7.013213).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.013213); retrieved 2026-10-08.

#### Q0353 Compact quantum dot models for analog microwave co-simulation

Lorenzo Peri, Alberto Gomez-Saiz, Christopher J. B. Ford, M. Fernando Gonzalez-Zalba.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 194.
Identifier and resource: [10.1038/s41534-025-01140-8](https://doi.org/10.1038/s41534-025-01140-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01140-8); retrieved 2026-10-08.

#### Q0354 Progress towards neutron-scattering simulation on an analog quantum processor

Nora Bauer, Victor Ale, Pontus Laurell, Serena Huang, Seth Watabe, David Alan Tennant, George Siopsis.
Journal article | 2025 | Physical Review A | vol. 111 | no. 2 | article 022442.
Identifier and resource: [10.1103/physreva.111.022442](https://doi.org/10.1103/physreva.111.022442).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.022442); retrieved 2026-10-08.

#### Q0355 QTurbo: A Robust and Efficient Compiler for Analog Quantum Simulation

Junyu Zhou, Yuhao Liu, Shize Che, Anupam Mitra, Efekan Kökcü, Ermal Rrapaj, Costin Iancu, Gushu Li.
Conference paper | 2025 | Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1 | pp. 203-218.
Identifier and resource: [10.1145/3760250.3762227](https://doi.org/10.1145/3760250.3762227).
Conference metadata: ASPLOS '26:31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3760250.3762227); retrieved 2026-10-08.

#### Q0356 Analog quantum simulation of partial differential equations

Shi Jin, Nana Liu.
Journal article | 2024 | Quantum Science and Technology | vol. 9 | no. 3 | pp. 035047.
Identifier and resource: [10.1088/2058-9565/ad49cf](https://doi.org/10.1088/2058-9565/ad49cf).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad49cf); retrieved 2026-10-08.

#### Q0357 Multipurpose platform for analog quantum simulation

Shuwei Jin, Kunlun Dai, Joris Verstraten, Maxime Dixmerias, Ragheed Alhyder, Christophe Salomon, Bruno Peaudecerf, Tim de Jongh et al..
Journal article | 2024 | Physical Review Research | vol. 6 | no. 1 | article 013158.
Identifier and resource: [10.1103/physrevresearch.6.013158](https://doi.org/10.1103/physrevresearch.6.013158).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.013158); retrieved 2026-10-08.

#### Q0358 SimuQ: A Framework for Programming Quantum Hamiltonian Simulation with Analog Compilation

Yuxiang Peng, Jacob Young, Pengyu Liu, Xiaodi Wu.
Journal article | 2024 | Proceedings of the ACM on Programming Languages | vol. 8 | no. POPL | pp. 2425-2455.
Identifier and resource: [10.1145/3632923](https://doi.org/10.1145/3632923).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3632923); retrieved 2026-10-08.

#### Q0359 Digital-Analog Quantum Simulation of Fermionic Models

Lucas C. Céleri, Daniel Huerga, Francisco Albarrán-Arriagada, Enrique Solano, Mikel Garcia de Andoin, Mikel Sanz.
Journal article | 2023 | Physical Review Applied | vol. 19 | no. 6 | article 064086.
Identifier and resource: [10.1103/physrevapplied.19.064086](https://doi.org/10.1103/physrevapplied.19.064086).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.19.064086); retrieved 2026-10-08.

#### Q0360 Measuring Arbitrary Physical Properties in Analog Quantum Simulation

Minh C. Tran, Daniel K. Mark, Wen Wei Ho, Soonwon Choi.
Journal article | 2023 | Physical Review X | vol. 13 | no. 1 | article 011049.
Identifier and resource: [10.1103/physrevx.13.011049](https://doi.org/10.1103/physrevx.13.011049).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.13.011049); retrieved 2026-10-08.

#### Q0361 Predicting molecular vibronic spectra using time-domain analog quantum simulation

Ryan J. MacDonell, Tomas Navickas, Tim F. Wohlers-Reichel, Christophe H. Valahu, Arjun D. Rao, Maverick J. Millican, Michael A. Currington, Michael J. Biercuk et al..
Journal article | 2023 | Chemical Science | vol. 14 | no. 35 | pp. 9439-9451.
Identifier and resource: [10.1039/d3sc02453a](https://doi.org/10.1039/d3sc02453a).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1039%2Fd3sc02453a); retrieved 2026-10-08.

### D07T03 Quantum lattice and spin models

Lattice and spin models provide structured many body targets. Geometry, interactions, symmetry, and observable selection specify the actual simulation problem.

Fine subcategories: Ising models; Heisenberg models; Hubbard models; phase diagrams; frustration.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0362 Probing confinement through dynamical quantum phase transitions: From quantum spin models to lattice gauge theories

Jesse J. Osborne, Ian P. McCulloch, Jad C. Halimeh.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 4 | article 043076.
Identifier and resource: [10.1103/rnv5-f32k](https://doi.org/10.1103/rnv5-f32k).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Frnv5-f32k); retrieved 2026-10-08.

#### Q0363 Quantum Simulating Continuum Field Theories with Large-Spin Lattice Models

Gabriele Calliari, Marco Di Liberto, Hannes Pichler, Torsten V. Zache.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 3 | article 030304.
Identifier and resource: [10.1103/nt76-ttmj](https://doi.org/10.1103/nt76-ttmj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fnt76-ttmj); retrieved 2026-10-08.

#### Q0364 Quantum simulation of spin-boson models with structured bath

Ke Sun, Mingyu Kang, Hanggai Nuomin, George Schwartz, David N. Beratan, Kenneth R. Brown, Jungsang Kim.
Journal article | 2025 | Nature Communications | vol. 16 | no. 1 | article 4042.
Identifier and resource: [10.1038/s41467-025-59296-y](https://doi.org/10.1038/s41467-025-59296-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-025-59296-y); retrieved 2026-10-08.

#### Q0365 Recipes for the digital quantum simulation of lattice spin systems

Guido Burkard.
Journal article | 2025 | SciPost Physics Core | vol. 8 | no. 1 | article 030.
Identifier and resource: [10.21468/scipostphyscore.8.1.030](https://doi.org/10.21468/scipostphyscore.8.1.030).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21468%2Fscipostphyscore.8.1.030); retrieved 2026-10-08.

#### Q0366 Real-space spectral simulation of quantum spin models: Application to generalized Kitaev models

Francisco M. O. Brito, Aires Ferreira.
Journal article | 2024 | SciPost Physics Core | vol. 7 | no. 1 | article 006.
Identifier and resource: [10.21468/scipostphyscore.7.1.006](https://doi.org/10.21468/scipostphyscore.7.1.006).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21468%2Fscipostphyscore.7.1.006); retrieved 2026-10-08.

#### Q0367 Thermal tensor renormalization group simulations of square-lattice quantum spin models

Han Li, Bin-Bin Chen, Ziyu Chen, Jan von Delft, Andreas Weichselbaum, Wei Li.
Journal article | 2019 | Physical Review B | vol. 100 | no. 4 | article 045110.
Identifier and resource: [10.1103/physrevb.100.045110](https://doi.org/10.1103/physrevb.100.045110).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.100.045110); retrieved 2026-10-08.

#### Q0368 Quantum Simulation of SU(4) Symmetric Spin Lattice Models

Bruno Uchoa.
Conference paper | 2018 | The First International Conference on Symmetry | pp. 39.
Identifier and resource: [10.3390/proceedings2010039](https://doi.org/10.3390/proceedings2010039).
Conference metadata: International Conference on Symmetry.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fproceedings2010039); retrieved 2026-10-08.

#### Q0369 Quantum simulation of spin models on an arbitrary lattice with trapped ions

S Korenblit, D Kafri, W C Campbell, R Islam, E E Edwards, Z-X Gong, G-D Lin, L-M Duan et al..
Journal article | 2012 | New Journal of Physics | vol. 14 | no. 9 | pp. 095024.
Identifier and resource: [10.1088/1367-2630/14/9/095024](https://doi.org/10.1088/1367-2630/14/9/095024).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2F14%2F9%2F095024); retrieved 2026-10-08.

### D07T04 Quantum thermal states

Thermal state algorithms prepare or characterize Gibbs states and finite temperature observables. Mixing, equilibration, and energy normalization can dominate costs.

Fine subcategories: Gibbs sampling; thermalization; imaginary time evolution; partition functions; finite temperature observables.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0370 Optimal Quantum Algorithm for Gibbs State Preparation

Cambyse Rouzé, Daniel Stilck França, Álvaro M. Alhambra.
Journal article | 2026 | Physical Review Letters | vol. 136 | no. 6 | article 060601.
Identifier and resource: [10.1103/lhht-svmn](https://doi.org/10.1103/lhht-svmn).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Flhht-svmn); retrieved 2026-10-08.

#### Q0371 Dissipative Variational Quantum Algorithms for Gibbs State Preparation

Yigal Ilin, Itai Arad.
Journal article | 2025 | IEEE Transactions on Quantum Engineering | vol. 6 | pp. 1-12.
Identifier and resource: [10.1109/tqe.2024.3511419](https://doi.org/10.1109/tqe.2024.3511419).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2024.3511419); retrieved 2026-10-08.

#### Q0372 Lindblad engineering for quantum Gibbs state preparation under the eigenstate thermalization hypothesis

Eric Brunner, Luuk Coopmans, Gabriel Matos, Matthias Rosenkranz, Frederic Sauvage, Yuta Kikuchi.
Journal article | 2025 | Quantum | vol. 9 | pp. 1843 | article 1843.
Identifier and resource: [10.22331/q-2025-08-29-1843](https://doi.org/10.22331/q-2025-08-29-1843).
Fine tags: thermalization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-08-29-1843); retrieved 2026-10-08.

#### Q0373 Resource Estimates for Lindbladian-Based Gibbs State Preparation on Fault-Tolerant Quantum Computers

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Eric Bobrow, Advanced Simulation and Computing, USDOE National Nuclear Security Administration (NNSA), Riley Chien, Alina Kononov, Lucas Kovalsky, Jacob Nelson et al..
Report | 2025 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3023927](https://doi.org/10.2172/3023927).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3023927); retrieved 2026-10-08.

#### Q0374 Variational Quantum Algorithms for Gibbs State Preparation

Mirko Consiglio.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 56-70.
Identifier and resource: [10.1007/978-3-031-81247-7_5](https://doi.org/10.1007/978-3-031-81247-7_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-81247-7_5); retrieved 2026-10-08.

#### Q0375 Variational Gibbs state preparation on noisy intermediate-scale quantum devices

Mirko Consiglio, Jacopo Settino, Andrea Giordano, Carlo Mastroianni, Francesco Plastina, Salvatore Lorenzo, Sabrina Maniscalco, John Goold et al..
Journal article | 2024 | Physical Review A | vol. 110 | no. 1 | article 012445.
Identifier and resource: [10.1103/physreva.110.012445](https://doi.org/10.1103/physreva.110.012445).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.012445); retrieved 2026-10-08.

#### Q0376 The Role of Initial Entanglement in Adaptive Gibbs State Preparation on Quantum Computers

Sophia E. Economou, Ada Warren, Edwin Barnes.
Conference paper | 2023 | ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) | pp. 1-5.
Identifier and resource: [10.1109/icassp49357.2023.10094697](https://doi.org/10.1109/icassp49357.2023.10094697).
Conference metadata: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficassp49357.2023.10094697); retrieved 2026-10-08.

#### Q0377 Variational Quantum Gibbs State Preparation with a Truncated Taylor Series

Youle Wang, Guangxi Li, Xin Wang.
Journal article | 2021 | Physical Review Applied | vol. 16 | no. 5 | article 054035.
Identifier and resource: [10.1103/physrevapplied.16.054035](https://doi.org/10.1103/physrevapplied.16.054035).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.16.054035); retrieved 2026-10-08.

### D07T05 Quantum dynamics and scrambling

Scrambling and transport characterize how information and operators spread through a system. Measured correlators need interpretation that accounts for noise and finite size.

Fine subcategories: OTOCs; operator spreading; transport; many body localization; dynamical phase transitions.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0378 Bridging Classical Sensitivity and Quantum Scrambling: A Tutorial on Out-of-Time-Ordered Correlators

Stephen Wiggins.
Journal article | 2026 | International Journal of Bifurcation and Chaos | vol. 36 | no. 12 | article 2650170.
Identifier and resource: [10.1142/s0218127426501701](https://doi.org/10.1142/s0218127426501701).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0218127426501701); retrieved 2026-10-08.

#### Q0379 Out of Time Order Correlators as Measures of Quantum Information Scrambling with Spectral Diagnostic

Bannishikha Banerjee.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-9329643/v1](https://doi.org/10.21203/rs.3.rs-9329643/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-9329643%2Fv1); retrieved 2026-10-08.

#### Q0380 Analyzing Information Scrambling in Simulated Quantum Systems Using Out-of-Time-Ordered Correlators

Bibiana Firmin R, Sathishkumar M.
Journal article | 2025 | International Journal For Multidisciplinary Research | vol. 7 | no. 6 | article 60321.
Identifier and resource: [10.36948/ijfmr.2025.v07i06.60321](https://doi.org/10.36948/ijfmr.2025.v07i06.60321).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.36948%2Fijfmr.2025.v07i06.60321); retrieved 2026-10-08.

#### Q0381 State estimation with quantum extreme learning machines beyond the scrambling time

Marco Vetrano, Gabriele Lo Monaco, Luca Innocenti, Salvatore Lorenzo, G. Massimo Palma.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 20.
Identifier and resource: [10.1038/s41534-024-00927-5](https://doi.org/10.1038/s41534-024-00927-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-024-00927-5); retrieved 2026-10-08.

#### Q0382 Scrambling Dynamics and Out-of-Time-Ordered Correlators in Quantum Many-Body Systems

Shenglong Xu, Brian Swingle.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 1 | article 010201.
Identifier and resource: [10.1103/prxquantum.5.010201](https://doi.org/10.1103/prxquantum.5.010201).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.010201); retrieved 2026-10-08.

#### Q0383 Imaginary components of out-of-time-order correlator and information scrambling for navigating the learning landscape of a quantum machine learning model

Manas Sajjan, Vinit Singh, Raja Selvarajan, Sabre Kais.
Journal article | 2023 | Physical Review Research | vol. 5 | no. 1 | article 013146.
Identifier and resource: [10.1103/physrevresearch.5.013146](https://doi.org/10.1103/physrevresearch.5.013146).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.5.013146); retrieved 2026-10-08.

#### Q0384 Author Correction: Unifying scrambling, thermalization and entanglement through measurement of fidelity out-of-time-order correlators in the Dicke model

R. J. Lewis-Swan, A. Safavi-Naini, J. J. Bollinger, A. M. Rey.
Journal article | 2019 | Nature Communications | vol. 10 | no. 1 | article 5007.
Identifier and resource: [10.1038/s41467-019-13016-5](https://doi.org/10.1038/s41467-019-13016-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-019-13016-5); retrieved 2026-10-08.

#### Q0385 Unifying scrambling, thermalization and entanglement through measurement of fidelity out-of-time-order correlators in the Dicke model

R. J. Lewis-Swan, A. Safavi-Naini, J. J. Bollinger, A. M. Rey.
Journal article | 2019 | Nature Communications | vol. 10 | no. 1 | article 1581.
Identifier and resource: [10.1038/s41467-019-09436-y](https://doi.org/10.1038/s41467-019-09436-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-019-09436-y); retrieved 2026-10-08.

### D07T06 Lattice gauge theory simulation

Gauge simulation encodes fields subject to local constraints. Truncation and gauge violation must be assessed along with gate noise and observable accuracy.

Fine subcategories: Gauge constraints; truncation; real time dynamics; link encodings; digital gauge simulation.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0386 Quantum Simulation of a $$\mathbb {Z}_2$$-Lattice Gauge Theory

Sebastian Saner.
Book chapter | 2026 | Springer Theses | pp. 141-168.
Identifier and resource: [10.1007/978-3-032-23775-0_8](https://doi.org/10.1007/978-3-032-23775-0_8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-23775-0_8); retrieved 2026-10-08.

#### Q0387 Quantum simulation of baryon scattering in SU(2) lattice gauge theory

João Barata, Juan Hormaza, Zhong-Bo Kang, Wenyang Qian.
Posted content | 2026 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.6760550](https://doi.org/10.2139/ssrn.6760550).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.6760550); retrieved 2026-10-08.

#### Q0388 ℤ2 lattice gauge theory on non-trivial topology and its quantum simulation

Jiaqi Hu, Shu Tian, Xiaopeng Cui, Rebing Wu, Man-Hong Yung, Yu Shi.
Journal article | 2026 | Journal of High Energy Physics | vol. 2026 | no. 7 | article 67.
Identifier and resource: [10.1007/jhep07(2026)067](https://doi.org/10.1007/jhep07(2026)067).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fjhep07%282026%29067); retrieved 2026-10-08.

#### Q0389 Quantum simulation with gauge fixing: From Ising lattice gauge theory to dynamical flux model

Junsen Wang, Xiangxiang Sun, Wei Zheng.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 1 | article 013311.
Identifier and resource: [10.1103/physrevresearch.7.013311](https://doi.org/10.1103/physrevresearch.7.013311).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.013311); retrieved 2026-10-08.

#### Q0390 Quantum simulation of gauge theory via orbifold lattice

Alexander J. Buser, Hrant Gharibyan, Masanori Hanada, Masazumi Honda, Junyu Liu.
Journal article | 2021 | Journal of High Energy Physics | vol. 2021 | no. 9 | article 34.
Identifier and resource: [10.1007/jhep09(2021)034](https://doi.org/10.1007/jhep09(2021)034).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fjhep09%282021%29034); retrieved 2026-10-08.

#### Q0391 Circuit-based digital adiabatic quantum simulation and pseudoquantum simulation as new approaches to lattice gauge theory

Xiaopeng Cui, Yu Shi, Ji-Chong Yang.
Journal article | 2020 | Journal of High Energy Physics | vol. 2020 | no. 8 | article 160.
Identifier and resource: [10.1007/jhep08(2020)160](https://doi.org/10.1007/jhep08(2020)160).
Fine tags: digital gauge simulation.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fjhep08%282020%29160); retrieved 2026-10-08.

#### Q0392 Trotter errors in digital adiabatic quantum simulation of quantum ℤ2 lattice gauge theory

Xiaopeng Cui, Yu Shi.
Journal article | 2020 | International Journal of Modern Physics B | vol. 34 | no. 30 | pp. 2050292.
Identifier and resource: [10.1142/s0217979220502926](https://doi.org/10.1142/s0217979220502926).
Fine tags: digital gauge simulation.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0217979220502926); retrieved 2026-10-08.

#### Q0393 Using Euclidean Lattice Field Theory for Efficient Quantum Simulation of a $Z_2$ Gauge Theory

Erik Gustafson.
Posted content | 2020 | Morressier.
Identifier and resource: [10.26226/morressier.5fa409874d4e91fe5c54b96b](https://doi.org/10.26226/morressier.5fa409874d4e91fe5c54b96b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.26226%2Fmorressier.5fa409874d4e91fe5c54b96b); retrieved 2026-10-08.

## D08 Quantum chemistry and materials

Electronic structure is a major application area because quantum states can encode correlated wavefunctions. Practical workflows require molecular mappings, controlled errors, and meaningful classical comparisons.

Prerequisites: Electronic structure, second quantization, and quantum algorithms.

Assessment focus: Basis set, active space, energy accuracy, mapping, and measured observables.

Primary catalog resources in this category: 39.

### D08T01 Electronic structure algorithms

Electronic structure algorithms estimate properties of interacting electrons in selected basis sets. The physical accuracy target and active space define the application.

Fine subcategories: Ground states; active spaces; basis sets; correlated wavefunctions; energy accuracy.

Primary resources: 12. Additional related assignments can be found in the interactive HTML.

#### Q0394 Quantum Computing Beyond Ground-State Electronic Structure: A Review of Progress Toward Quantum Chemistry Out of the Ground State

Alan Bidart, Prateek Vaish, Tilas Kabengele, Yaoqi Pang, Yuan Liu, Brenda M. Rubenstein.
Journal article | 2026 | Annual Review of Physical Chemistry | vol. 77 | no. 1 | pp. 417-441.
Identifier and resource: [10.1146/annurev-physchem-082624-084635](https://doi.org/10.1146/annurev-physchem-082624-084635).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1146%2Fannurev-physchem-082624-084635); retrieved 2026-10-08.

#### Q0395 Analyzing Common Electronic Structure Theory Algorithms for Distributed Quantum Computing

Grier M. Jones, Hans-Arno Jacobsen.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 368-373.
Identifier and resource: [10.1109/qce65121.2025.10351](https://doi.org/10.1109/qce65121.2025.10351).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10351); retrieved 2026-10-08.

#### Q0396 NOISY QUANTUM COMPUTING OF ELECTRONIC STRUCTURE OF CRYSTALS

Vojtěch VAŠINA, Ivana MIHÁLIKOVÁ, Martin FRIÁK.
Conference paper | 2025 | METAL Conference Proeedings | vol. 2025 | pp. 538-543.
Identifier and resource: [10.37904/metal.2025.5153](https://doi.org/10.37904/metal.2025.5153).
Conference metadata: METAL 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.37904%2Fmetal.2025.5153); retrieved 2026-10-08.

#### Q0397 Quantum computing of the electronic structure of crystals by the Variational Quantum Deflation algorithm

Michal Ďuriška, Ivana Miháliková, Martin Friák.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 4 | pp. 045105.
Identifier and resource: [10.1088/1402-4896/adbb29](https://doi.org/10.1088/1402-4896/adbb29).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fadbb29); retrieved 2026-10-08.

#### Q0398 SUPPRESING NOISE IN QUANTUM COMPUTING OF ELECTRONIC STRUCTURE OF CRYSTALS

Jan HOJAČ, Vojtěch VAŠINA, Martin FRIÁK.
Conference paper | 2025 | NANOCON Conference Proeedings | vol. 2025 | pp. 60-65.
Identifier and resource: [10.37904/nanocon.2025.5189](https://doi.org/10.37904/nanocon.2025.5189).
Conference metadata: NANOCON 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.37904%2Fnanocon.2025.5189); retrieved 2026-10-08.

#### Q0399 Electronic structure simulations in the cloud computing environment

Eric J. Bylaska, Ajay Panyala, Nicholas P. Bauman, Bo Peng, Himadri Pathak, Daniel Mejia-Rodriguez, Niranjan Govind, David B. Williams-Young et al..
Journal article | 2024 | The Journal of Chemical Physics | vol. 161 | no. 15 | article 150902.
Identifier and resource: [10.1063/5.0226437](https://doi.org/10.1063/5.0226437).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0226437); retrieved 2026-10-08.

#### Q0400 Quantum computing for electronic structure analysis: Ground state energy and molecular properties calculations

Nouhaila Innan, Muhammad Al-Zafar Khan, Mohamed Bennai.
Journal article | 2024 | Materials Today Communications | vol. 38 | pp. 107760 | article 107760.
Identifier and resource: [10.1016/j.mtcomm.2023.107760](https://doi.org/10.1016/j.mtcomm.2023.107760).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.mtcomm.2023.107760); retrieved 2026-10-08.

#### Q0401 Quantum computing quantum Monte Carlo with hybrid tensor network for electronic structure calculations

Shu Kanno, Hajime Nakamura, Takao Kobayashi, Shigeki Gocho, Miho Hatanaka, Naoki Yamamoto, Qi Gao.
Journal article | 2024 | npj Quantum Information | vol. 10 | no. 1 | article 56.
Identifier and resource: [10.1038/s41534-024-00851-8](https://doi.org/10.1038/s41534-024-00851-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-024-00851-8); retrieved 2026-10-08.

#### Q0402 Challenges in the Use of Quantum Computing Hardware-Efficient Ansätze in Electronic Structure Theory

Ruhee D’Cunha, T. Daniel Crawford, Mario Motta, Julia E. Rice.
Journal article | 2023 | The Journal of Physical Chemistry A | vol. 127 | no. 15 | pp. 3437-3448.
Identifier and resource: [10.1021/acs.jpca.2c08430](https://doi.org/10.1021/acs.jpca.2c08430).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jpca.2c08430); retrieved 2026-10-08.

#### Q0403 Quantum-computing study of the electronic structure of crystals: the case study of Si

Michal ĎURIŠKA, Ivana MIHÁLIKOVÁ, Martin FRIÁK.
Conference paper | 2023 | NANOCON Conference Proeedings | vol. 2023 | pp. 0-0.
Identifier and resource: [10.37904/nanocon.2023.4774](https://doi.org/10.37904/nanocon.2023.4774).
Conference metadata: NANOCON 2023.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.37904%2Fnanocon.2023.4774); retrieved 2026-10-08.

#### Q0404 GitHub - qiskit-community/qiskit-nature: Qiskit Nature is an open-source, quantum computing, framework for solving quantum mechanical natural science problems. · GitHub

Author metadata not supplied.
Software repository | Undated | Qiskit Nature.
Identifier and resource: [Official resource](https://github.com/qiskit-community/qiskit-nature).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/qiskit-community/qiskit-nature); retrieved 2026-10-08.

#### Q0405 GitHub - quantumlib/OpenFermion: Python package for compiling and analyzing quantum algorithms to simulate electronic structures. · GitHub

Author metadata not supplied.
Software repository | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://github.com/quantumlib/OpenFermion).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/quantumlib/OpenFermion); retrieved 2026-10-08.

### D08T02 Fermion to qubit mappings

Fermion mappings translate anticommutation relations into qubit operators. Operator locality, symmetry reduction, and measurement cost depend on the mapping.

Fine subcategories: Jordan Wigner; Bravyi Kitaev; parity mappings; symmetry tapering; fermionic encodings.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0406 Hidden Rotation Symmetry of the Jordan–Wigner Transformation and Its Application to Measurement in Quantum Computation

Grant Davis, James K. Freericks.
Journal article | 2026 | Symmetry | vol. 18 | no. 2 | pp. 251.
Identifier and resource: [10.3390/sym18020251](https://doi.org/10.3390/sym18020251).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fsym18020251); retrieved 2026-10-08.

#### Q0407 Extension of the Jordan-Wigner mapping to nonorthogonal spin orbitals for quantum computing application to valence bond approaches

Author metadata not supplied.
Book chapter | 2025 | Advances in Quantum Chemistry | pp. 245-266.
Identifier and resource: [10.1016/bs.aiq.2025.07.007](https://doi.org/10.1016/bs.aiq.2025.07.007).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fbs.aiq.2025.07.007); retrieved 2026-10-08.

#### Q0408 Jordan-Wigner mapping for nonorthogonal spin orbitals

Alessandro Genoni, Mosè Casalegno, Piero Macchi, Guido Raos.
Posted content | 2025 | American Chemical Society (ACS).
Identifier and resource: [10.26434/chemrxiv-2025-9cdvr](https://doi.org/10.26434/chemrxiv-2025-9cdvr).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.26434%2Fchemrxiv-2025-9cdvr); retrieved 2026-10-08.

#### Q0409 Simulation of quantum computation with magic states via Jordan-Wigner transformations

Michael Zurel, Lawrence Z. Cohen, Robert Raussendorf.
Journal article | 2025 | Physical Review A | vol. 112 | no. 4 | article 042602.
Identifier and resource: [10.1103/ng4l-96kd](https://doi.org/10.1103/ng4l-96kd).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fng4l-96kd); retrieved 2026-10-08.

#### Q0410 Geometric Algebra Jordan–Wigner Transformation for Quantum Simulation

Grégoire Veyrac, Zeno Toffano.
Journal article | 2024 | Entropy | vol. 26 | no. 5 | pp. 410.
Identifier and resource: [10.3390/e26050410](https://doi.org/10.3390/e26050410).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe26050410); retrieved 2026-10-08.

#### Q0411 Quaternary Jordan-Wigner mapping and topological extended-kink phase in the interacting Kitaev ring

Zhen-Yu Zheng, Han-Chuan Kou, Peng Li.
Journal article | 2019 | Physical Review B | vol. 100 | no. 23 | article 235127.
Identifier and resource: [10.1103/physrevb.100.235127](https://doi.org/10.1103/physrevb.100.235127).
Fine tags: Jordan Wigner.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.100.235127); retrieved 2026-10-08.

#### Q0412 A Comparison of the Bravyi–Kitaev and Jordan–Wigner Transformations for the Quantum Simulation of Quantum Chemistry

Andrew Tranter, Peter J. Love, Florian Mintert, Peter V. Coveney.
Journal article | 2018 | Journal of Chemical Theory and Computation | vol. 14 | no. 11 | pp. 5617-5630.
Identifier and resource: [10.1021/acs.jctc.8b00450](https://doi.org/10.1021/acs.jctc.8b00450).
Fine tags: Jordan Wigner; Bravyi Kitaev.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jctc.8b00450); retrieved 2026-10-08.

#### Q0413 OpenFermion | Google Quantum AI

Author metadata not supplied.
Documentation | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://quantumai.google/openfermion).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://quantumai.google/openfermion); retrieved 2026-10-08.

### D08T03 Excited states and spectroscopy

Excited state and response algorithms target spectra beyond the ground state. State preparation and transition observable estimation are separate resource demands.

Fine subcategories: Subspace methods; equation of motion; response functions; transition amplitudes.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0414 Folded Spectrum VQE: A Quantum Computing Method for the Calculation of Molecular Excited States

Lila Cadi Tazi, Alex J. W. Thom.
Journal article | 2024 | Journal of Chemical Theory and Computation | vol. 20 | no. 6 | pp. 2491-2504.
Identifier and resource: [10.1021/acs.jctc.3c01378](https://doi.org/10.1021/acs.jctc.3c01378).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jctc.3c01378); retrieved 2026-10-08.

#### Q0415 Computing molecular excited states on a D-Wave quantum annealer

Alexander Teplukhin, Brian K. Kendrick, Susan M. Mniszewski, Yu Zhang, Ashutosh Kumar, Christian F. A. Negre, Petr M. Anisimov, Sergei Tretiak et al..
Journal article | 2021 | Scientific Reports | vol. 11 | no. 1 | article 18796.
Identifier and resource: [10.1038/s41598-021-98331-y](https://doi.org/10.1038/s41598-021-98331-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-021-98331-y); retrieved 2026-10-08.

#### Q0416 Toward Quantum Computing for High-Energy Excited States in Molecular Systems: Quantum Phase Estimations of Core-Level States

Nicholas P. Bauman, Hongbin Liu, Eric J. Bylaska, Sriram Krishnamoorthy, Guang Hao Low, Christopher E. Granade, Nathan Wiebe, Nathan A. Baker et al..
Journal article | 2020 | Journal of Chemical Theory and Computation | vol. 17 | no. 1 | pp. 201-210.
Identifier and resource: [10.1021/acs.jctc.0c00909](https://doi.org/10.1021/acs.jctc.0c00909).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jctc.0c00909); retrieved 2026-10-08.

#### Q0417 Quantum Beat Spectroscopy of Excited Molecules.

Soji TSUCHIYA.
Journal article | 1992 | Journal of the Spectroscopical Society of Japan | vol. 41 | no. 1 | pp. 3-20.
Identifier and resource: [10.5111/bunkou.41.3](https://doi.org/10.5111/bunkou.41.3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5111%2Fbunkou.41.3); retrieved 2026-10-08.

#### Q0418 Photoelectron spectroscopy of excited molecular states

V. McKoy, M. Braunstein, H. Rudolph, J.A. Stephens, S.N. Dixit, D.L. Lynch.
Journal article | 1990 | Journal of Electron Spectroscopy and Related Phenomena | vol. 52 | pp. 597-612.
Identifier and resource: [10.1016/0368-2048(90)85051-a](https://doi.org/10.1016/0368-2048(90)85051-a).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2F0368-2048%2890%2985051-a); retrieved 2026-10-08.

#### Q0419 Quantum chemistry and spectroscopy of highly excited states of coordination compounds

A. V. Kondratenko, K. M. Neiman, G. L. Gutsev, G. M. Zhidomirov, S. F. Ruzankin.
Journal article | 1989 | Journal of Structural Chemistry | vol. 29 | no. 6 | pp. 899-910.
Identifier and resource: [10.1007/bf00748433](https://doi.org/10.1007/bf00748433).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbf00748433); retrieved 2026-10-08.

#### Q0420 Excited States in Quantum Chemistry

Author metadata not supplied.
Book | 1978 | Springer Netherlands.
Identifier and resource: [10.1007/978-94-009-9902-2](https://doi.org/10.1007/978-94-009-9902-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-94-009-9902-2); retrieved 2026-10-08.

### D08T04 Quantum chemistry resource estimates

Chemistry estimates translate an algorithm into logical and physical resources for a chosen accuracy. Molecular basis, code assumptions, and factory architecture should be stated.

Fine subcategories: Logical qubits; T counts; accuracy targets; molecule selection; runtime models.

Primary resources: 4. Additional related assignments can be found in the interactive HTML.

#### Q0421 QREChem: quantum resource estimation software for chemistry applications

Matthew Otten, Byeol Kang, Dmitry Fedorov, Joo-Hyoung Lee, Anouar Benali, Salman Habib, Stephen K. Gray, Yuri Alexeev.
Journal article | 2023 | Frontiers in Quantum Science and Technology | vol. 2 | article 1232624.
Identifier and resource: [10.3389/frqst.2023.1232624](https://doi.org/10.3389/frqst.2023.1232624).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffrqst.2023.1232624); retrieved 2026-10-08.

#### Q0422 Quantum Resource Estimation for Quantum Chemistry Algorithms

Dmitry Fedorov, Matthew Otten, Byeol Kang, Anouar Benali, Salman Habib, Stephen Gray, Yuri Alexeev.
Conference paper | 2022 | 2022 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 859-861.
Identifier and resource: [10.1109/qce53715.2022.00144](https://doi.org/10.1109/qce53715.2022.00144).
Conference metadata: 2022 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce53715.2022.00144); retrieved 2026-10-08.

#### Q0423 Resource-Optimized Fermionic Local-Hamiltonian Simulation on a Quantum Computer for Quantum Chemistry

Qingfeng Wang, Ming Li, Christopher Monroe, Yunseong Nam.
Journal article | 2021 | Quantum | vol. 5 | pp. 509 | article 509.
Identifier and resource: [10.22331/q-2021-07-26-509](https://doi.org/10.22331/q-2021-07-26-509).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2021-07-26-509); retrieved 2026-10-08.

#### Q0424 Accuracy and Resource Estimations for Quantum Chemistry on a Near-Term Quantum Computer

Michael Kühn, Sebastian Zanker, Peter Deglmann, Michael Marthaler, Horst Weiß.
Journal article | 2019 | Journal of Chemical Theory and Computation | vol. 15 | no. 9 | pp. 4764-4780.
Identifier and resource: [10.1021/acs.jctc.9b00236](https://doi.org/10.1021/acs.jctc.9b00236).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jctc.9b00236); retrieved 2026-10-08.

### D08T05 Quantum materials and condensed matter

Materials applications study strongly correlated phases and properties. A proposed workflow should identify observables that inform a materials decision and compare against suitable classical methods.

Fine subcategories: Strong correlation; superconductivity models; defects; electronic phases; materials observables.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0425 Condensed Matter Physics of Doped Materials: Theoretical Foundations, Electronic Structure, and Quantum Applications

MANJULA BHARATHI NAGULAPATI.
Journal article | 2025 | International Journal of Scientific Development and Research | vol. 10 | no. 11.
Identifier and resource: [10.56975/ijsdr.v10i11.306106](https://doi.org/10.56975/ijsdr.v10i11.306106).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.56975%2Fijsdr.v10i11.306106); retrieved 2026-10-08.

#### Q0426 Condensed Matter and Materials Theory (NSF)

Author metadata not supplied.
Journal article | 2025 | Federal Grants & Contracts | vol. 49 | no. 7 | pp. 3-3.
Identifier and resource: [10.1002/fgc.34235](https://doi.org/10.1002/fgc.34235).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Ffgc.34235); retrieved 2026-10-08.

#### Q0427 Condensed matter chemistry in polymer materials

Wenke Zhang, Yu Song.
Book chapter | 2024 | Introduction to Condensed Matter Chemistry | pp. 105-140.
Identifier and resource: [10.1016/b978-0-443-16140-7.00004-3](https://doi.org/10.1016/b978-0-443-16140-7.00004-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-16140-7.00004-3); retrieved 2026-10-08.

#### Q0428 Condensed Matter and Materials Theory (NSF)

Author metadata not supplied.
Journal article | 2023 | Federal Grants & Contracts | vol. 47 | no. 18 | pp. 3-4.
Identifier and resource: [10.1002/fgc.33196](https://doi.org/10.1002/fgc.33196).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Ffgc.33196); retrieved 2026-10-08.

#### Q0429 Condensed Matter and Materials Theory (NSF)

Author metadata not supplied.
Journal article | 2022 | Federal Grants & Contracts | vol. 46 | no. 16 | pp. 3-3.
Identifier and resource: [10.1002/fgc.32482](https://doi.org/10.1002/fgc.32482).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Ffgc.32482); retrieved 2026-10-08.

#### Q0430 Condensed Matter and Materials Theory (NSF)

Author metadata not supplied.
Journal article | 2020 | Federal Grants & Contracts | vol. 44 | no. 17 | pp. 2-2.
Identifier and resource: [10.1002/fgc.31210](https://doi.org/10.1002/fgc.31210).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Ffgc.31210); retrieved 2026-10-08.

#### Q0431 Condensed Matter and Materials Physics

Prafulla K. Jha, Arun Pratap, Ashvin R. Jani.
Book | 2013 | Advanced Materials Research.
Identifier and resource: [10.4028/b-fa150f](https://doi.org/10.4028/b-fa150f).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4028%2Fb-fa150f); retrieved 2026-10-08.

#### Q0432 Condensed-Matter and Materials Physics

Author metadata not supplied.
Edited book | 2007 | National Academies Press.
Identifier and resource: [10.17226/11967](https://doi.org/10.17226/11967).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.17226%2F11967); retrieved 2026-10-08.

## D09 Variational and hybrid quantum methods

Variational algorithms optimize a parameterized circuit with a classical loop. Trainability, sampling, noise, and optimizer costs must be evaluated along with the objective value.

Prerequisites: Optimization, parameterized circuits, and measurement statistics.

Assessment focus: Ansatz bias, trainability, shot cost, noise, and optimizer convergence.

Primary catalog resources in this category: 74.

### D09T01 Variational quantum eigensolvers

VQE minimizes measured energy with a parameterized circuit and classical optimization. Ansatz bias, shot noise, and optimizer convergence all affect the result.

Fine subcategories: VQE; energy measurement; UCC ansatz; adaptive ansatz; optimizer selection.

Primary resources: 18. Additional related assignments can be found in the interactive HTML.

#### Q0433 Variational quantum algorithms

M. Cerezo, Andrew Arrasmith, Ryan Babbush, Simon C. Benjamin, Suguru Endo, Keisuke Fujii, Jarrod R. McClean, Kosuke Mitarai et al..
Journal article | 2021 | Nature Reviews Physics | vol. 3 | no. 9 | pp. 625-644.
Identifier and resource: [10.1038/s42254-021-00348-9](https://doi.org/10.1038/s42254-021-00348-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42254-021-00348-9); retrieved 2026-10-08.

#### Q0434 A variational eigenvalue solver on a photonic quantum processor

Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong Yung, Xiao-Qi Zhou, Peter J. Love, Alán Aspuru-Guzik, Jeremy L. O’Brien.
Journal article | 2014 | Nature Communications | vol. 5 | no. 1 | article 4213.
Identifier and resource: [10.1038/ncomms5213](https://doi.org/10.1038/ncomms5213).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fncomms5213); retrieved 2026-10-08.

#### Q0435 Efficient variational quantum eigensolver methodologies on quantum processors

Tushar Pandey, Jason Saroni, Abdullah Kazi, Kartik Sharma.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 36 | pp. 365104.
Identifier and resource: [10.1088/1402-4896/ae9e06](https://doi.org/10.1088/1402-4896/ae9e06).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae9e06); retrieved 2026-10-08.

#### Q0436 Geometric analysis of variational quantum eigensolver

Zhen Qin.
Journal article | 2026 | Journal of Physics A: Mathematical and Theoretical | vol. 59 | no. 30 | pp. 305302.
Identifier and resource: [10.1088/1751-8121/ae8b60](https://doi.org/10.1088/1751-8121/ae8b60).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1751-8121%2Fae8b60); retrieved 2026-10-08.

#### Q0437 Quantum Tunneling in Adenine Deamination Using Variational Quantum Eigensolver

Don Roosan, Rubayat Khan, Saif Nirzhor, Brian Provenchar.
Conference paper | 2026 | Proceedings of the 19th International Joint Conference on Biomedical Engineering Systems and Technologies | pp. 591-599.
Identifier and resource: [10.5220/0014289200004070](https://doi.org/10.5220/0014289200004070).
Conference metadata: 17th International Conference on Bioinformatics Models, Methods and Algorithms.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5220%2F0014289200004070); retrieved 2026-10-08.

#### Q0438 Weighted approximate quantum natural gradient for variational quantum eigensolver

Chenyu Shi, Vedran Dunjko, Hao Wang.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 1 | pp. 015060.
Identifier and resource: [10.1088/2058-9565/ae3fc8](https://doi.org/10.1088/2058-9565/ae3fc8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae3fc8); retrieved 2026-10-08.

#### Q0439 Drug Discovery Using Variational Quantum EigenSolver

S. Surya Prakash, P. Banu Priya, Sudarshan Someneni, Udendhran, Arnab Banerjee.
Book chapter | 2025 | Lecture Notes in Networks and Systems | pp. 691-703.
Identifier and resource: [10.1007/978-981-96-3942-7_51](https://doi.org/10.1007/978-981-96-3942-7_51).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-96-3942-7_51); retrieved 2026-10-08.

#### Q0440 Enhancing Drug Design Using Variational Quantum Eigensolver

Rajalakshmi S, Reshmaa SS, Lalith Kannan R, Sree Harish SM, Naveen Kumar S.
Conference paper | 2025 | 2025 IEEE First International Conference on Innovations in Engineering and Next-Generation Technologies for Sustainability (ICINVENTS) | pp. 1-6.
Identifier and resource: [10.1109/icinvents64613.2025.11401986](https://doi.org/10.1109/icinvents64613.2025.11401986).
Conference metadata: 2025 IEEE First International Conference on Innovations in Engineering and Next-Generation Technologies for Sustainability (ICINVENTS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficinvents64613.2025.11401986); retrieved 2026-10-08.

#### Q0441 Photonic variational quantum eigensolver for NISQ-compatible quantum technology

Kang-Min Hu, Min Namkung, Hyang-Tag Lim.
Journal article | 2025 | Nano Convergence | vol. 12 | no. 1 | article 60.
Identifier and resource: [10.1186/s40580-025-00525-x](https://doi.org/10.1186/s40580-025-00525-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1186%2Fs40580-025-00525-x); retrieved 2026-10-08.

#### Q0442 Cascaded variational quantum eigensolver algorithm

Daniel Gunlycke, C. Stephen Hellberg, John P. T. Stenger.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 1 | article 013238.
Identifier and resource: [10.1103/physrevresearch.6.013238](https://doi.org/10.1103/physrevresearch.6.013238).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.013238); retrieved 2026-10-08.

#### Q0443 Hermitian-preserving ansatz and variational open quantum eigensolver

Zhong-Xia Shang.
Journal article | 2024 | Physical Review A | vol. 109 | no. 6 | article 062608.
Identifier and resource: [10.1103/physreva.109.062608](https://doi.org/10.1103/physreva.109.062608).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.062608); retrieved 2026-10-08.

#### Q0444 Photonic variational quantum eigensolver using entanglement measurements

Jinil Lee, Wooyeong Song, Donghwa Lee, Yosep Kim, Seung-Woo Lee, Hyang-Tag Lim, Hojoong Jung, Sang-Wook Han et al..
Journal article | 2024 | Quantum Science and Technology | vol. 9 | no. 4 | pp. 045028.
Identifier and resource: [10.1088/2058-9565/ad6d87](https://doi.org/10.1088/2058-9565/ad6d87).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad6d87); retrieved 2026-10-08.

#### Q0445 Variational Quantum Eigensolver Applications in Quantum Machine Learning

M Amshavalli, Shambhu Sharan Srivastava.
Book chapter | 2024 | Hybrid Algorithms for Quantum Computing and Artificial Intelligence | pp. 177-208.
Identifier and resource: [10.71443/9788197933646-07](https://doi.org/10.71443/9788197933646-07).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.71443%2F9788197933646-07); retrieved 2026-10-08.

#### Q0446 Variational Quantum Eigensolver Boosted by Adiabatic Connection

Mikuláš Matoušek, Katarzyna Pernal, Fabijan Pavošević, Libor Veis.
Journal article | 2024 | The Journal of Physical Chemistry A | vol. 128 | no. 3 | pp. 687-698.
Identifier and resource: [10.1021/acs.jpca.3c07590](https://doi.org/10.1021/acs.jpca.3c07590).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jpca.3c07590); retrieved 2026-10-08.

#### Q0447 Variational denoising for variational quantum eigensolver

Quoc Hoan Tran, Shinji Kikuchi, Hirotaka Oshima.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 2 | article 023181.
Identifier and resource: [10.1103/physrevresearch.6.023181](https://doi.org/10.1103/physrevresearch.6.023181).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.023181); retrieved 2026-10-08.

#### Q0448 Correlated Reference-Assisted Variational Quantum Eigensolver

Nhan Trong Le, Lan Nguyen Tran.
Journal article | 2023 | The Journal of Physical Chemistry A | vol. 127 | no. 24 | pp. 5222-5230.
Identifier and resource: [10.1021/acs.jpca.3c00993](https://doi.org/10.1021/acs.jpca.3c00993).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jpca.3c00993); retrieved 2026-10-08.

#### Q0449 Orbital expansion variational quantum eigensolver

Yusen Wu, Zigeng Huang, Jinzhao Sun, Xiao Yuan, Jingbo B Wang, Dingshun Lv.
Journal article | 2023 | Quantum Science and Technology | vol. 8 | no. 4 | pp. 045030.
Identifier and resource: [10.1088/2058-9565/acf9c7](https://doi.org/10.1088/2058-9565/acf9c7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Facf9c7); retrieved 2026-10-08.

#### Q0450 Symmetry enhanced variational quantum spin eigensolver

Chufan Lyu, Xusheng Xu, Man-Hong Yung, Abolfazl Bayat.
Journal article | 2023 | Quantum | vol. 7 | pp. 899 | article 899.
Identifier and resource: [10.22331/q-2023-01-19-899](https://doi.org/10.22331/q-2023-01-19-899).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-01-19-899); retrieved 2026-10-08.

### D09T02 Quantum approximate optimization

QAOA alternates cost evolution with a mixing operation to search for good solutions. Depth, constraints, parameter selection, and classical baseline quality determine the assessment.

Fine subcategories: QAOA; mixers; alternating operators; graph problems; approximation ratios.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0451 A Quantum Approximate Optimization Algorithm (QAOA) Approach to Portfolio Optimization

Yifei Huang.
Journal article | 2026 | Exploring Science Academic Conference Series | vol. 19 | pp. 628-635.
Identifier and resource: [10.70267/icfmb.202619628635](https://doi.org/10.70267/icfmb.202619628635).
Fine tags: QAOA.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.70267%2Ficfmb.202619628635); retrieved 2026-10-08.

#### Q0452 Enhancing Quantum Approximate Optimization Algorithm Through Manifold Optimization

Qingqing Yu, Yinhui Yu, Rong Jin.
Journal article | 2026 | Quantum Engineering | vol. 2026 | no. 1 | article 3418300.
Identifier and resource: [10.1155/que2/3418300](https://doi.org/10.1155/que2/3418300).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1155%2Fque2%2F3418300); retrieved 2026-10-08.

#### Q0453 Equivariant Quantum Approximate Optimization Algorithm

Boris Tsvelikhovskiy, Ilya Safro, Yuri Alexeev.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 1-13.
Identifier and resource: [10.1109/tqe.2026.3654930](https://doi.org/10.1109/tqe.2026.3654930).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3654930); retrieved 2026-10-08.

#### Q0454 Image thresholding using quantum approximate optimization algorithm and Grover’s algorithm

Joseph L. Pachuau, Nongmeikapam Brajabidhu Singh, Anish Kumar Saha.
Journal article | 2026 | The Journal of Supercomputing | vol. 82 | no. 9 | article 507.
Identifier and resource: [10.1007/s11227-026-08618-y](https://doi.org/10.1007/s11227-026-08618-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11227-026-08618-y); retrieved 2026-10-08.

#### Q0455 Iterative Interpolation Schedules for Quantum Approximate Optimization Algorithm

Anuj Apte, Shree Hari Sureshbabu, Ruslan Shaydulin, Sami Boulebnane, Zichang He, Dylan Herman, James Sud, Marco Pistoia.
Journal article | 2026 | ACM Transactions on Quantum Computing | vol. 7 | no. 4 | pp. 1-18.
Identifier and resource: [10.1145/3815778](https://doi.org/10.1145/3815778).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3815778); retrieved 2026-10-08.

#### Q0456 Quantum Approximate Optimization Algorithm: Applications, Limitations and Enhancement

P. Herrero-Gómez, M. Alemany-Manzanaro, D. Gil-Méndez, H. Mora-Mora.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 147-157.
Identifier and resource: [10.1007/978-3-032-22193-3_11](https://doi.org/10.1007/978-3-032-22193-3_11).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-22193-3_11); retrieved 2026-10-08.

#### Q0457 Universal resources for quantum approximate optimization algorithm and quantum annealing

Pablo Díez-Valle, Fernando J. Gómez-Ruiz, Diego Porras, Juan José García-Ripoll.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 1 | article 013211.
Identifier and resource: [10.1103/hxv2-sbr7](https://doi.org/10.1103/hxv2-sbr7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fhxv2-sbr7); retrieved 2026-10-08.

#### Q0458 Compressed Space Quantum Approximate Optimization Algorithm for Constrained Combinatorial Optimization

Tatsuhiko Shirai, Nozomu Togawa.
Journal article | 2025 | IEEE Transactions on Quantum Engineering | vol. 6 | pp. 1-14.
Identifier and resource: [10.1109/tqe.2025.3602404](https://doi.org/10.1109/tqe.2025.3602404).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2025.3602404); retrieved 2026-10-08.

#### Q0459 Exploring graph cuts in quantum approximate optimization algorithm

Nongmeikapam Brajabidhu Singh, Anish Kumar Saha.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 11 | pp. 115104.
Identifier and resource: [10.1088/1402-4896/ae1906](https://doi.org/10.1088/1402-4896/ae1906).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae1906); retrieved 2026-10-08.

#### Q0460 Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm

Valter Uotila, Julia Ripatti, Bo Zhao.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 01-12.
Identifier and resource: [10.1109/qce65121.2025.00244](https://doi.org/10.1109/qce65121.2025.00244).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00244); retrieved 2026-10-08.

#### Q0461 Multiscale quantum approximate optimization algorithm

Ping Zou.
Journal article | 2025 | Physical Review A | vol. 111 | no. 1 | article 012427.
Identifier and resource: [10.1103/physreva.111.012427](https://doi.org/10.1103/physreva.111.012427).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.012427); retrieved 2026-10-08.

#### Q0462 Quantum Approximate Optimization Algorithm on Different Qubit Systems

Seongmin Kim, In-Saeng Suh, Eduardo Antonio Coello Perez, Ryan Landfield, Michael Sandoval, Josh Cunningham, Thomas Beck, Heidi Nelson-Quillin et al..
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 542-543.
Identifier and resource: [10.1109/qce65121.2025.10436](https://doi.org/10.1109/qce65121.2025.10436).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10436); retrieved 2026-10-08.

#### Q0463 Warm-start adaptive-bias quantum approximate optimization algorithm

Yunlong Yu, Xiang-Bin Wang, Nic Shannon, Robert Joynt.
Journal article | 2025 | Physical Review A | vol. 112 | no. 1 | article 012422.
Identifier and resource: [10.1103/nt3w-j4mj](https://doi.org/10.1103/nt3w-j4mj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fnt3w-j4mj); retrieved 2026-10-08.

#### Q0464 Hamiltonian-oriented homotopy quantum approximate optimization algorithm

Akash Kundu, Ludmila Botelho, Adam Glos.
Journal article | 2024 | Physical Review A | vol. 109 | no. 2 | article 022611.
Identifier and resource: [10.1103/physreva.109.022611](https://doi.org/10.1103/physreva.109.022611).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.022611); retrieved 2026-10-08.

#### Q0465 Molecular docking via quantum approximate optimization algorithm

Qi-Ming Ding, Yi-Ming Huang, Xiao Yuan.
Journal article | 2024 | Physical Review Applied | vol. 21 | no. 3 | article 034036.
Identifier and resource: [10.1103/physrevapplied.21.034036](https://doi.org/10.1103/physrevapplied.21.034036).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.21.034036); retrieved 2026-10-08.

#### Q0466 Quantum Approximate Optimization Algorithm for Test Case Optimization

Xinyi Wang, Shaukat Ali, Tao Yue, Paolo Arcaini.
Journal article | 2024 | IEEE Transactions on Software Engineering | vol. 50 | no. 12 | pp. 3249-3264.
Identifier and resource: [10.1109/tse.2024.3479421](https://doi.org/10.1109/tse.2024.3479421).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftse.2024.3479421); retrieved 2026-10-08.

### D09T03 Ansatz design and expressibility

An ansatz defines the states reachable during optimization. Expressibility alone is not a guarantee of trainability or low resource cost.

Fine subcategories: Hardware efficient circuits; problem inspired circuits; symmetry preservation; entangling structure.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0467 Calibration of Variational Quantum Classifiers Under Depolarizing Noise: Expected Calibration Error, Ansatz Expressibility, and Post-Hoc Temperature Scaling

Souvik Ghosh, Amrita Kundu, Mithaguru, Vegi Fernando.
Conference paper | 2026 | 2026 International Conference on Intelligent and Sustainable AI Systems (ICOSAAS) | pp. 297-303.
Identifier and resource: [10.1109/icosaas68663.2026.11648877](https://doi.org/10.1109/icosaas68663.2026.11648877).
Conference metadata: 2026 International Conference on Intelligent and Sustainable AI Systems (ICOSAAS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficosaas68663.2026.11648877); retrieved 2026-10-08.

#### Q0468 Expressibility and Trainability Analysis of Hardware-Efficient Ansatz Variants in Variational Quantum Eigensolver with a Linear Mixing Model

Rasyid Ustman Ramadhan, Luthfiya Kurnia Permatahati, Teguh Budi Prayitno, Yanoar P. Sarwono.
Journal article | 2026 | The Journal of Physical Chemistry A | vol. 130 | no. 15 | pp. 3101-3112.
Identifier and resource: [10.1021/acs.jpca.5c08292](https://doi.org/10.1021/acs.jpca.5c08292).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jpca.5c08292); retrieved 2026-10-08.

#### Q0469 Genetic optimization of ansatz expressibility for enhanced variational-quantum-algorithm performance

Manish Mallapur, Ronit Raj, Ankur Raina.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032437.
Identifier and resource: [10.1103/812w-ytnb](https://doi.org/10.1103/812w-ytnb).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F812w-ytnb); retrieved 2026-10-08.

#### Q0470 Hamiltonian expressibility for ansatz selection in variational quantum algorithms

Filippo Brozzi, Gloria Turati, Maurizio Ferrari Dacrema, Filippo Caruso, Paolo Cremonesi.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 2 | article 76.
Identifier and resource: [10.1007/s42484-026-00407-3](https://doi.org/10.1007/s42484-026-00407-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00407-3); retrieved 2026-10-08.

#### Q0471 Radar Signal Classification with Quantum Machine Learning: Ansatz Depth Impact on Expressibility

Gabriel F. Martinez, Alberto Croci, Francesco Drago, Alessandro Niccolai, Marco Mussetta, Riccardo E. Zich.
Journal article | 2026 | Electronics | vol. 15 | no. 2 | pp. 370.
Identifier and resource: [10.3390/electronics15020370](https://doi.org/10.3390/electronics15020370).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Felectronics15020370); retrieved 2026-10-08.

#### Q0472 Learning the Expressibility of Quantum Circuit Ansatz Using Transformer

Fei Zhang, Jie Li, Zhimin He, Haozhen Situ.
Journal article | 2025 | Advanced Quantum Technologies | vol. 8 | no. 6 | article 2400366.
Identifier and resource: [10.1002/qute.202400366](https://doi.org/10.1002/qute.202400366).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202400366); retrieved 2026-10-08.

#### Q0473 The unified effect of data encoding, ansatz expressibility and entanglement on the trainability of HQNNs

Muhammad Kashif, Saif Al-Kuwari.
Journal article | 2023 | International Journal of Parallel, Emergent and Distributed Systems | vol. 38 | no. 5 | pp. 362-400.
Identifier and resource: [10.1080/17445760.2023.2231163](https://doi.org/10.1080/17445760.2023.2231163).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F17445760.2023.2231163); retrieved 2026-10-08.

#### Q0474 Connecting Ansatz Expressibility to Gradient Magnitudes and Barren Plateaus

Zoë Holmes, Kunal Sharma, M. Cerezo, Patrick J. Coles.
Journal article | 2022 | PRX Quantum | vol. 3 | no. 1 | article 010313.
Identifier and resource: [10.1103/prxquantum.3.010313](https://doi.org/10.1103/prxquantum.3.010313).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.3.010313); retrieved 2026-10-08.

### D09T04 Barren plateaus and trainability

Barren plateau analyses study exponentially small or concentrated gradients. The conclusion depends on circuit ensembles, cost locality, initialization, and noise.

Fine subcategories: Gradient concentration; depth dependence; local costs; initialization; noise induced plateaus.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0475 BRIDG-Q: Barren-Plateau-Resilient Initialisation with Data-Aware LLM-Generated Quantum Circuits

Ngoc Nhi Nguyen, Thai T. Vu, John Le, Hoa Khanh Dam, Dung Hoang Duong, Dinh Thai Hoang.
Book chapter | 2026 | IFIP Advances in Information and Communication Technology | pp. 434-448.
Identifier and resource: [10.1007/978-3-032-27993-4_30](https://doi.org/10.1007/978-3-032-27993-4_30).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-27993-4_30); retrieved 2026-10-08.

#### Q0476 Benchmarking Barren Plateau Mitigation Strategies in Quantum Neural Networks on Standard and Medical Image Datasets

Maqsudur Rahman, Rui Liu, Anup Majumder, Pintu Chandra Paul, Kangtong Mo, Amena Begum, Kashmi Sultana, Nahida Akter et al..
Journal article | 2026 | Journal of Imaging | vol. 12 | no. 7 | pp. 275.
Identifier and resource: [10.3390/jimaging12070275](https://doi.org/10.3390/jimaging12070275).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fjimaging12070275); retrieved 2026-10-08.

#### Q0477 Deep Variational Quantum Circuits with Barren-Plateau-Free Architectures

Kaining Zhang, Min-Hsiu Hsieh, Dacheng Tao.
Journal article | 2026 | Artificial Intelligence Science and Engineering | vol. 2 | no. 1 | pp. 66-84.
Identifier and resource: [10.23919/aise.2026.000005](https://doi.org/10.23919/aise.2026.000005).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Faise.2026.000005); retrieved 2026-10-08.

#### Q0478 Fourier Analysis of Parameterized Quantum Circuits and the Barren Plateau Problem

Shun Okumura, Masayuki Ohzeki.
Journal article | 2026 | Journal of the Physical Society of Japan | vol. 95 | no. 3 | article 033002.
Identifier and resource: [10.7566/jpsj.95.033002](https://doi.org/10.7566/jpsj.95.033002).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7566%2Fjpsj.95.033002); retrieved 2026-10-08.

#### Q0479 Illustration of Barren Plateaus in Quantum Computing

Gerhard Stenzel, Tobias Rohe, Michael Kölle, Leo Sünkel, Jonas Stein, Claudia Linnhoff-Popien.
Conference paper | 2026 | Proceedings of the 18th International Conference on Agents and Artificial Intelligence | pp. 731-742.
Identifier and resource: [10.5220/0014310300004052](https://doi.org/10.5220/0014310300004052).
Conference metadata: Workshop on Quantum Artificial Intelligence and Optimization.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5220%2F0014310300004052); retrieved 2026-10-08.

#### Q0480 Lie-geometric trainability of quantum dynamical systems: avoiding barren plateaus via low-dimensional Lie subalgebras

Haijian Shao, Yujie Wu, Xing Deng, Yingtao Jiang.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 25 | pp. 255107.
Identifier and resource: [10.1088/1402-4896/ae7d6d](https://doi.org/10.1088/1402-4896/ae7d6d).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae7d6d); retrieved 2026-10-08.

#### Q0481 Mitigating the barren plateau problem in linear optics

Anonymous.
Journal article | 2026 | Physical Review A.
Identifier and resource: [10.1103/xndq-ttdj](https://doi.org/10.1103/xndq-ttdj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fxndq-ttdj); retrieved 2026-10-08.

#### Q0482 Quantum Optimization for Reconfigurable Intelligent Surface Design: Trainability and Barren Plateau Analysis

Emanuel Colella, Luca Bastianelli, Valter Mariani Primiani, Franco Moglie, Zhen Peng, Gabriele Gradoni.
Journal article | 2026 | IEEE Open Journal of Antennas and Propagation | pp. 1-1.
Identifier and resource: [10.1109/ojap.2026.3705248](https://doi.org/10.1109/ojap.2026.3705248).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fojap.2026.3705248); retrieved 2026-10-08.

### D09T05 Quantum gradients and optimization

Gradient rules and optimization methods control the classical loop around a quantum circuit. Measurement complexity and gradient variance must accompany iteration counts.

Fine subcategories: Parameter shift rules; finite differences; stochastic gradients; quantum natural gradients.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0483 Efficient Optimization of Variational Quantum Algorithms via Gradient-Free Parameter Prediction

Satwik Kundu, Debarshi Kundu, Swaroop Ghosh.
Journal article | 2026 | IEEE Access | vol. 14 | pp. 42485-42499.
Identifier and resource: [10.1109/access.2026.3674830](https://doi.org/10.1109/access.2026.3674830).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Faccess.2026.3674830); retrieved 2026-10-08.

#### Q0484 Quantum Federated Gradient Aggregation Using the Parameter-Shift Rule

Jaehyun Chung, Chaemoon Im, Soohyun Park, Joongheon Kim, Wonjun Lee.
Journal article | 2026 | IEEE Internet of Things Journal | vol. 13 | no. 11 | pp. 25367-25379.
Identifier and resource: [10.1109/jiot.2026.3677003](https://doi.org/10.1109/jiot.2026.3677003).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjiot.2026.3677003); retrieved 2026-10-08.

#### Q0485 Quantum Optimization via Gradient-Based Hamiltonian Descent

Jiaqi Leng, Bin Shi.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 170-177.
Identifier and resource: [10.1007/978-981-95-7829-0_14](https://doi.org/10.1007/978-981-95-7829-0_14).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-7829-0_14); retrieved 2026-10-08.

#### Q0486 Gradient-Based Optimization for Linear Quantum Systems

Yunyan Lee, Ian R. Petersen, Daoyi Dong.
Conference paper | 2025 | 2025 IEEE 64th Conference on Decision and Control (CDC) | pp. 6679-6684.
Identifier and resource: [10.1109/cdc57313.2025.11312520](https://doi.org/10.1109/cdc57313.2025.11312520).
Conference metadata: 2025 IEEE 64th Conference on Decision and Control (CDC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcdc57313.2025.11312520); retrieved 2026-10-08.

#### Q0487 Natural gradient and parameter estimation for quantum Boltzmann machines

Dhrumil Patel, Mark M. Wilde.
Journal article | 2025 | Physical Review A | vol. 112 | no. 5 | article 052421.
Identifier and resource: [10.1103/j8nb-by4l](https://doi.org/10.1103/j8nb-by4l).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fj8nb-by4l); retrieved 2026-10-08.

#### Q0488 Photonic parameter-shift rule: Enabling gradient computation for photonic quantum computers

Axel Pappalardo, Pierre-Emmanuel Emeriau, Giovanni de Felice, Brian Ventura, Hugo Jaunin, Richie Yeung, Bob Coecke, Shane Mansfield.
Journal article | 2025 | Physical Review A | vol. 111 | no. 3 | article 032429.
Identifier and resource: [10.1103/physreva.111.032429](https://doi.org/10.1103/physreva.111.032429).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.032429); retrieved 2026-10-08.

#### Q0489 Efficient Parameter-Shift Rule Implementation for Computing Gradient on Quantum Simulators

Vu Tuan Hai, Le Vu Trung Duong, Pham Hoai Luan, Yasuhiko Nakashima.
Conference paper | 2024 | 2024 International Conference on Advanced Technologies for Communications (ATC) | pp. 449-454.
Identifier and resource: [10.1109/atc63255.2024.10908246](https://doi.org/10.1109/atc63255.2024.10908246).
Conference metadata: 2024 International Conference on Advanced Technologies for Communications (ATC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fatc63255.2024.10908246); retrieved 2026-10-08.

#### Q0490 General parameter-shift rules for quantum gradients

David Wierichs, Josh Izaac, Cody Wang, Cedric Yen-Yu Lin.
Journal article | 2022 | Quantum | vol. 6 | pp. 677 | article 677.
Identifier and resource: [10.22331/q-2022-03-30-677](https://doi.org/10.22331/q-2022-03-30-677).
Fine tags: Parameter shift rules.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2022-03-30-677); retrieved 2026-10-08.

### D09T06 Quantum imaginary time evolution

Imaginary time methods project toward low energy states through nonunitary evolution or approximations. Normalization and locality assumptions determine what is implementable.

Fine subcategories: QITE; variational imaginary time; imaginary time filtering; normalization; thermal preparation.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0491 Deterministic Quantum Trajectory via Imaginary Time Evolution

Shivan Mittal, Bin Yan.
Journal article | 2026 | Physical Review Letters | vol. 136 | no. 1 | article 010401.
Identifier and resource: [10.1103/fgkg-n2b9](https://doi.org/10.1103/fgkg-n2b9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ffgkg-n2b9); retrieved 2026-10-08.

#### Q0492 Double-Bracket Quantum Algorithms for Quantum Imaginary-Time Evolution

Marek Gluza, Jeongrak Son, Bi Hong Tiang, René Zander, Raphael Seidel, Yudai Suzuki, Zoë Holmes, Nelly H. Y. Ng.
Journal article | 2026 | Physical Review Letters | vol. 136 | no. 2 | article 020601.
Identifier and resource: [10.1103/rw81-k8vk](https://doi.org/10.1103/rw81-k8vk).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Frw81-k8vk); retrieved 2026-10-08.

#### Q0493 Equating quantum imaginary time evolution, Riemannian gradient flows, and stochastic implementations

Nathan A. McMahon, Mahum Pervez, Christian Arenz.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 2 | article 023024.
Identifier and resource: [10.1103/ht2m-1j91](https://doi.org/10.1103/ht2m-1j91).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fht2m-1j91); retrieved 2026-10-08.

#### Q0494 Operator-projected variational quantum imaginary time evolution

Aeishah Ameera Anuar, François Jamet, Fabio Gironella, Fedor Šimkovic IV, Riccardo Rossi.
Journal article | 2026 | Journal of Physics A: Mathematical and Theoretical | vol. 59 | no. 24 | pp. 245301.
Identifier and resource: [10.1088/1751-8121/ae767d](https://doi.org/10.1088/1751-8121/ae767d).
Fine tags: variational imaginary time.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1751-8121%2Fae767d); retrieved 2026-10-08.

#### Q0495 Optimizing QUBO on a quantum computer by mimicking imaginary time evolution

Yahui Chai, Alice Di Tucci.
Journal article | 2026 | New Journal of Physics | vol. 28 | no. 6 | pp. 064508.
Identifier and resource: [10.1088/1367-2630/ae6ded](https://doi.org/10.1088/1367-2630/ae6ded).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fae6ded); retrieved 2026-10-08.

#### Q0496 Physics-inspired transformer quantum states via latent imaginary-time evolution

Kimihiro Yamazaki, Itsushi Sakata, Takuya Konishi, Yoshinobu Kawahara.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033032.
Identifier and resource: [10.1103/bjxb-8tsk](https://doi.org/10.1103/bjxb-8tsk).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fbjxb-8tsk); retrieved 2026-10-08.

#### Q0497 Quantum imaginary-time evolution with polynomial resources in evolution time

Lei Zhang, Jizhe Lai, Xian Wu, Xin Wang.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 3 | pp. 035041.
Identifier and resource: [10.1088/2058-9565/ae7b7f](https://doi.org/10.1088/2058-9565/ae7b7f).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae7b7f); retrieved 2026-10-08.

#### Q0498 Quasiprobabilistic Imaginary-Time Evolution on Quantum Computers

Annie Ray, Esha Swaroop, Ningping Cao, Michael Vasmer, Anirban Chowdhury.
Journal article | 2026 | Quantum Information & Computation | vol. 26 | no. 1 | pp. 89-113.
Identifier and resource: [10.2478/qic-2026-0005](https://doi.org/10.2478/qic-2026-0005).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2478%2Fqic-2026-0005); retrieved 2026-10-08.

#### Q0499 Saturable quantum speed limits for imaginary-time evolution

Kohei Kobayashi.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032618.
Identifier and resource: [10.1103/bln8-8xzy](https://doi.org/10.1103/bln8-8xzy).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fbln8-8xzy); retrieved 2026-10-08.

#### Q0500 Understanding Quantum Imaginary Time Evolution and Its Variational Form

Andreu Anglés-Castillo, Luca Ion, Tanmoy Pandit, Rafael Gomez-Lurbe, Rodrigo Martínez, Miguel Angel Garcia-March.
Book chapter | 2026 | Lecture Notes in Networks and Systems | pp. 269-279.
Identifier and resource: [10.1007/978-3-032-05748-8_22](https://doi.org/10.1007/978-3-032-05748-8_22).
Fine tags: variational imaginary time.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-05748-8_22); retrieved 2026-10-08.

#### Q0501 Accelerating Large-Scale Linear Algebra Using Variational Quantum Imaginary Time Evolution

Willie Aboumrad, Daiwei Zhu, Claudio Girotto, François-Henry Rouet, Jezer Jojo, Robert Lucas, Jay Pathak, Ananth Kaushik et al..
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1965-1970.
Identifier and resource: [10.1109/qce65121.2025.00214](https://doi.org/10.1109/qce65121.2025.00214).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: variational imaginary time.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00214); retrieved 2026-10-08.

#### Q0502 Accelerating quantum imaginary-time evolution with random measurements

Ioannis Kolotouros, David Joseph, Anand Kumar Narayanan.
Journal article | 2025 | Physical Review A | vol. 111 | no. 1 | article 012424.
Identifier and resource: [10.1103/physreva.111.012424](https://doi.org/10.1103/physreva.111.012424).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.012424); retrieved 2026-10-08.

#### Q0503 Measurement-Based Variational Quantum Imaginary Time Evolution

Kübra Yeter-Aydeniz, Nora Bauer, George Siopsis.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 408-409.
Identifier and resource: [10.1109/qce65121.2025.10369](https://doi.org/10.1109/qce65121.2025.10369).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: variational imaginary time.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10369); retrieved 2026-10-08.

#### Q0504 Role of Riemannian Geometry in Double-Bracket Quantum Imaginary-Time Evolution

René Zander, Raphael Seidel, Li Xiaoyue, Marek Gluza.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 105-114.
Identifier and resource: [10.1007/978-3-032-03924-8_11](https://doi.org/10.1007/978-3-032-03924-8_11).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03924-8_11); retrieved 2026-10-08.

#### Q0505 Adiabatic quantum imaginary time evolution

Kasra Hejazi, Mario Motta, Garnet Kin-Lic Chan.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 3 | article 033084.
Identifier and resource: [10.1103/physrevresearch.6.033084](https://doi.org/10.1103/physrevresearch.6.033084).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.033084); retrieved 2026-10-08.

#### Q0506 Combinatorial optimization with quantum imaginary time evolution

Nora M. Bauer, Rizwanul Alam, George Siopsis, James Ostrowski.
Journal article | 2024 | Physical Review A | vol. 109 | no. 5 | article 052430.
Identifier and resource: [10.1103/physreva.109.052430](https://doi.org/10.1103/physreva.109.052430).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.052430); retrieved 2026-10-08.

## D10 Quantum machine learning

Quantum machine learning includes learning with quantum circuits and learning about quantum systems. Input encoding, sample complexity, classical comparisons, and trainability determine whether a method is useful.

Prerequisites: Machine learning, statistics, and quantum circuits.

Assessment focus: Input encoding, sample complexity, generalization, and classical comparison.

Primary catalog resources in this category: 88.

### D10T01 Quantum data encoding

Data encodings specify how classical or quantum inputs enter a circuit. State preparation cost and repeated access must be included in learning complexity.

Fine subcategories: Amplitude encoding; angle encoding; basis encoding; data reuploading; state preparation costs.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0507 Benchmarking Data Encoding Methods in Quantum Machine Learning

Orlane Zang, Grégoire Barrué, Tony Quertier.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 270-279.
Identifier and resource: [10.1007/978-3-032-13852-1_27](https://doi.org/10.1007/978-3-032-13852-1_27).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-13852-1_27); retrieved 2026-10-08.

#### Q0508 Encoding Numerical Data for Generative Quantum Machine Learning

Michael Krebsbach, Florentin Reiter, Thomas Wellens, Hagen-Henrik Kowalski, Ali Abedi.
Journal article | 2026 | Quantum Science and Technology.
Identifier and resource: [10.1088/2058-9565/aeaf7e](https://doi.org/10.1088/2058-9565/aeaf7e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faeaf7e); retrieved 2026-10-08.

#### Q0509 Fast quantum amplitude encoding of typical classical data

Vittorio Pagni, Sigurd Huber, Michael Epping, Michael Felderer.
Journal article | 2026 | EPJ Quantum Technology | vol. 13 | no. 1 | article 24.
Identifier and resource: [10.1140/epjqt/s40507-026-00473-3](https://doi.org/10.1140/epjqt/s40507-026-00473-3).
Fine tags: Amplitude encoding.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjqt%2Fs40507-026-00473-3); retrieved 2026-10-08.

#### Q0510 Feature Space Dimensional Reduction Based on Quantum Spin-Correlation Encoding

Chee Kian Yap.
Posted content | 2026 | MDPI AG.
Identifier and resource: [10.20944/preprints202601.0671.v1](https://doi.org/10.20944/preprints202601.0671.v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.20944%2Fpreprints202601.0671.v1); retrieved 2026-10-08.

#### Q0511 Quantum State Preparation for Classical Data Encoding

Miguel A. A. Lisboa, Victor H. F. Brasil, João V. H. Duarte, Leandro C. Souza.
Conference paper | 2026 | Anais do I Simpósio Brasileiro de Computação e Comunicação Quânticas (SBCCQ 2026) | pp. 119-130.
Identifier and resource: [10.5753/sbccq.2026.20984](https://doi.org/10.5753/sbccq.2026.20984).
Conference metadata: Simpósio Brasileiro de Computação e Comunicação Quânticas.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5753%2Fsbccq.2026.20984); retrieved 2026-10-08.

#### Q0512 Analisis Performa Variational Quantum Classifier (VQC) dengan ZZ Feature Map dan Angle Encoding Untuk Mengidentifikasi Serangan Jantung

Hilmia Rahma, Dahlan Abdullah, Desvina Yulisda.
Journal article | 2025 | Bulletin of Computer Science Research | vol. 5 | no. 5 | pp. 898-907.
Identifier and resource: [10.47065/bulletincsr.v5i5.712](https://doi.org/10.47065/bulletincsr.v5i5.712).
Fine tags: angle encoding.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.47065%2Fbulletincsr.v5i5.712); retrieved 2026-10-08.

#### Q0513 Improving Data Encoding for Enhanced AI Performance in Complex Datasets via Quantum Feature Space Mapping: Harnessing Quantum Algorithms

Gurpreet Singh Walia, Sathiya Priya S, KV Karthikeya, D. Suresh, P Sudheer, V. Syambabu.
Conference paper | 2025 | 2025 International Conference on Pervasive Computational Technologies (ICPCT) | pp. 985-990.
Identifier and resource: [10.1109/icpct64145.2025.10940638](https://doi.org/10.1109/icpct64145.2025.10940638).
Conference metadata: 2025 International Conference on Pervasive Computational Technologies (ICPCT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficpct64145.2025.10940638); retrieved 2026-10-08.

#### Q0514 A Parallel Quantum Feature Encoding Scheme for Effective Classical Data Classification in Quantum Convolutional Neural Networks

Raisa Mashtura, Jishnu Mahmud, Shaikh Anowarul Fattah, Mohammad Saquib.
Conference paper | 2023 | TENCON 2023 - 2023 IEEE Region 10 Conference (TENCON) | pp. 1-5.
Identifier and resource: [10.1109/tencon58879.2023.10322543](https://doi.org/10.1109/tencon58879.2023.10322543).
Conference metadata: TENCON 2023 - 2023 IEEE Region 10 Conference (TENCON).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftencon58879.2023.10322543); retrieved 2026-10-08.

### D10T02 Quantum kernels

Quantum kernels estimate similarities using quantum feature maps. Expressive features can still yield concentrated kernels or costly training measurements.

Fine subcategories: Fidelity kernels; projected kernels; kernel concentration; support vector machines; feature maps.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0515 Double Descent in Quantum Kernel Methods

Marie Kempkes, Aroosa Ijaz, Elies Gil-Fuster, Carlos Bravo-Prieto, Jakob Spiegelberg, Evert van Nieuwenburg, Vedran Dunjko.
Journal article | 2026 | PRX Quantum | vol. 7 | no. 1 | article 010312.
Identifier and resource: [10.1103/cn64-gs6b](https://doi.org/10.1103/cn64-gs6b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fcn64-gs6b); retrieved 2026-10-08.

#### Q0516 Leveraging Quantum Kernel Methods for Enhanced Intrusion Detection

Anuj Tiwari, Sameer G. Kulkarni.
Conference paper | 2026 | 2026 18th International Conference on COMmunication Systems and NETworks (COMSNETS) | pp. 567-572.
Identifier and resource: [10.1109/comsnets67989.2026.11418222](https://doi.org/10.1109/comsnets67989.2026.11418222).
Conference metadata: 2026 18th International Conference on COMmunication Systems and NETworks (COMSNETS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcomsnets67989.2026.11418222); retrieved 2026-10-08.

#### Q0517 Novel Algorithm for Adaptive Circuit Construction for Quantum Kernel Methods

Emanouil Atanassov, Aneta Karaivanova, Svetlozar Yordanov, Stanislav Spasov, Mariya Durchova, Alexandar Kirilov.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 379-387.
Identifier and resource: [10.1007/978-3-032-22221-3_42](https://doi.org/10.1007/978-3-032-22221-3_42).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-22221-3_42); retrieved 2026-10-08.

#### Q0518 Qmes: Quantum Meta-Learning for Encoding Selection in Quantum Kernel Methods

Duy Tung Dao, Quoc Chuong Nguyen, Tuan Hai Vu, Le Bin Ho, Nguyen Lan Tran.
Posted content | 2026 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.7434491](https://doi.org/10.2139/ssrn.7434491).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.7434491); retrieved 2026-10-08.

#### Q0519 Quantum Kernel Methods for Brain Aneurysm Risk Classification

Sangeeta Yadav, Harshit Yadav, Anusheel Munshi, Roshan M Dsouza.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 66-82.
Identifier and resource: [10.1007/978-3-032-17625-7_5](https://doi.org/10.1007/978-3-032-17625-7_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-17625-7_5); retrieved 2026-10-08.

#### Q0520 Quantum Kernel Methods for High Dimensional Data Classification

Maharaj Manohar, Prakash Shanmugam, Chella Pandi.
Journal article | 2026 | International Journal of Quantum Computing and Artificial Intelligence (IJQCAI) | vol. 1 | no. 2 | pp. 31-44.
Identifier and resource: [10.67714/3139-5201.vol.1.issue.2.3](https://doi.org/10.67714/3139-5201.vol.1.issue.2.3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.67714%2F3139-5201.vol.1.issue.2.3); retrieved 2026-10-08.

#### Q0521 Quantum Kernel Methods for Industrial Anomaly Detection

Takao Tomono.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 64-85.
Identifier and resource: [10.1007/978-981-95-7829-0_8](https://doi.org/10.1007/978-981-95-7829-0_8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-7829-0_8); retrieved 2026-10-08.

#### Q0522 Quantum Support Vector Machines and Quantum Kernel Methods

Li Xu, Jing Wang, Jiang Chen, Jiamin Xu, Ming Li, Weishan Zhang.
Journal article | 2026 | Software: Practice and Experience | vol. 56 | no. 6 | pp. 786-801.
Identifier and resource: [10.1002/spe.70070](https://doi.org/10.1002/spe.70070).
Fine tags: support vector machines.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fspe.70070); retrieved 2026-10-08.

#### Q0523 Quo Vadis, Quantum Machine Learning?: Quantum kernel methods meet Earth observation

Artur Miroszewski, Jakub Nalepa, Agata M. Wijata, Jakub Mielczarek, Bertrand Le Saux, Alessandro Sebastianelli.
Journal article | 2026 | IEEE Geoscience and Remote Sensing Magazine | vol. 14 | no. 1 | pp. 306-334.
Identifier and resource: [10.1109/mgrs.2025.3596291](https://doi.org/10.1109/mgrs.2025.3596291).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmgrs.2025.3596291); retrieved 2026-10-08.

#### Q0524 Spectral phase encoding for quantum kernel methods

Pablo Herrero Gómez, Antonio Jimeno Morenilla, David Muñoz-Hernández, Higinio Mora Mora.
Journal article | 2026 | EPJ Quantum Technology | vol. 13 | no. 1 | article 66.
Identifier and resource: [10.1140/epjqt/s40507-026-00509-8](https://doi.org/10.1140/epjqt/s40507-026-00509-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjqt%2Fs40507-026-00509-8); retrieved 2026-10-08.

#### Q0525 The Cross‐Kernel Margin: A Robustness Measure for Quantum Kernel Methods

S. Govender, I. Sinayskiy.
Journal article | 2026 | Advanced Quantum Technologies | vol. 9 | no. 9 | article e70459.
Identifier and resource: [10.1002/qute.70459](https://doi.org/10.1002/qute.70459).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.70459); retrieved 2026-10-08.

#### Q0526 Expressivity vs. Generalization in Quantum Kernel Methods

Markus Gross, Markus Lange, Bogusz Bujnowski, Hans-Martin Rieser.
Conference paper | 2025 | ESANN 2025 proceesdings | pp. 543-548.
Identifier and resource: [10.14428/esann/2025.es2025-152](https://doi.org/10.14428/esann/2025.es2025-152).
Conference metadata: ESANN 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.14428%2Fesann%2F2025.es2025-152); retrieved 2026-10-08.

#### Q0527 Quantum Kernel Methods

Yuxuan Du, Xinbiao Wang, Naixu Guo, Zhan Yu, Yang Qian, Kaining Zhang, Min-Hsiu Hsieh, Patrick Rebentrost et al..
Book chapter | 2025 | A Gentle Introduction to Quantum Machine Learning | pp. 69-110.
Identifier and resource: [10.1007/978-981-95-1284-3_3](https://doi.org/10.1007/978-981-95-1284-3_3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-1284-3_3); retrieved 2026-10-08.

#### Q0528 Quantum Support Vector Machines and Quantum Kernel Methods

Li Xu, Jing Wang, Chen Jiang, Jiamin Xu, Ming Li, Weishan Zhang.
Posted content | 2025 | Wiley.
Identifier and resource: [10.22541/au.175615204.43126822/v1](https://doi.org/10.22541/au.175615204.43126822/v1).
Fine tags: support vector machines.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22541%2Fau.175615204.43126822%2Fv1); retrieved 2026-10-08.

#### Q0529 Quantum adversarial learning for kernel methods

Giuseppe Montalbano, Leonardo Banchi.
Journal article | 2025 | Quantum Machine Intelligence | vol. 7 | no. 1 | article 15.
Identifier and resource: [10.1007/s42484-025-00238-8](https://doi.org/10.1007/s42484-025-00238-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-025-00238-8); retrieved 2026-10-08.

#### Q0530 Quantum kernel methods under scrutiny: a benchmarking study

Jan Schnabel, Marco Roth.
Journal article | 2025 | Quantum Machine Intelligence | vol. 7 | no. 1 | article 58.
Identifier and resource: [10.1007/s42484-025-00273-5](https://doi.org/10.1007/s42484-025-00273-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-025-00273-5); retrieved 2026-10-08.

### D10T03 Quantum neural networks and classifiers

Quantum neural networks use trainable quantum circuits as learning models. Their evaluation requires held out data, noise analysis, and comparable classical baselines.

Fine subcategories: Variational classifiers; quantum convolution; circuit architectures; supervised learning.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0531 Quantum Machine Learning

Andrea Delgado, Kathleen E Hamilton.
Book | 2025 | IOP Publishing.
Identifier and resource: [10.1088/978-0-7503-4952-9](https://doi.org/10.1088/978-0-7503-4952-9).
ISBN: 9780750349529; 9780750349505.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F978-0-7503-4952-9); retrieved 2026-10-08.

#### Q0532 Quantum machine learning

Jacob Biamonte, Peter Wittek, Nicola Pancotti, Patrick Rebentrost, Nathan Wiebe, Seth Lloyd.
Journal article | 2017 | Nature | vol. 549 | no. 7671 | pp. 195-202.
Identifier and resource: [10.1038/nature23474](https://doi.org/10.1038/nature23474).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fnature23474); retrieved 2026-10-08.

#### Q0533 Quantum Neural Network Classifier for Cancer Registry System Testing: A Feasibility Study

Xinyi Wang, Shaukat Ali, Paolo Arcaini, Narasimha Raghavan Veeraragavan, Jan F. Nygård.
Journal article | 2026 | ACM Transactions on Software Engineering and Methodology | vol. 35 | no. 5 | pp. 1-24.
Identifier and resource: [10.1145/3769302](https://doi.org/10.1145/3769302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3769302); retrieved 2026-10-08.

#### Q0534 Quantum Machine Learning Classifier and Neural Network Transfer Learning

Pauline Mosley, Avery Leider.
Book chapter | 2025 | Artificial Intelligence.
Identifier and resource: [10.5772/intechopen.115051](https://doi.org/10.5772/intechopen.115051).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5772%2Fintechopen.115051); retrieved 2026-10-08.

#### Q0535 Quantum neural network classifier with differential privacy

Guodong Li, Fangce Yu, Qingle Wang, Lin Liu, Ying Mao, Long Cheng.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 3 | pp. 035109.
Identifier and resource: [10.1088/1402-4896/adb228](https://doi.org/10.1088/1402-4896/adb228).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fadb228); retrieved 2026-10-08.

#### Q0536 Hybrid Quantum Machine Learning Classifier with Classical Neural Network Transfer Learning

Avery Leider, Gio Giorgio Abou Jaoude, Pauline Mosley.
Book chapter | 2023 | Lecture Notes in Networks and Systems | pp. 102-116.
Identifier and resource: [10.1007/978-3-031-28073-3_8](https://doi.org/10.1007/978-3-031-28073-3_8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-28073-3_8); retrieved 2026-10-08.

#### Q0537 Infected Plant Leaves Detection Using Multilayered Convolutional Neural Network and Quantum Classifier

Damandeep Kaur, Shamandeep Singh, Simarjeet Kaur, Gurpreet Singh, Rani Kumari.
Book chapter | 2023 | Advances in Bioinformatics and Biomedical Engineering | pp. 110-126.
Identifier and resource: [10.4018/979-8-3693-1479-1.ch007](https://doi.org/10.4018/979-8-3693-1479-1.ch007).
Fine tags: quantum convolution.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4018%2F979-8-3693-1479-1.ch007); retrieved 2026-10-08.

#### Q0538 On Hybrid Artificial Neural Networks and Variational Quantum Classifier for Network Intrusion Detection

Praveen Venkatachalam, David Q. Liu.
Conference paper | 2023 | 2023 International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC) | pp. 410-416.
Identifier and resource: [10.1109/cyberc58899.2023.00070](https://doi.org/10.1109/cyberc58899.2023.00070).
Conference metadata: 2023 International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcyberc58899.2023.00070); retrieved 2026-10-08.

#### Q0539 Quantum neural network autoencoder and classifier applied to an industrial case study

Stefano Mangini, Alessia Marruzzo, Marco Piantanida, Dario Gerace, Daniele Bajoni, Chiara Macchiavello.
Journal article | 2022 | Quantum Machine Intelligence | vol. 4 | no. 2 | article 13.
Identifier and resource: [10.1007/s42484-022-00070-4](https://doi.org/10.1007/s42484-022-00070-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-022-00070-4); retrieved 2026-10-08.

#### Q0540 Adversarial attacks and robustness for quantum machine learning | PennyLane Demos

Author metadata not supplied.
Tutorial | Undated | PennyLane.
Identifier and resource: [Official resource](https://pennylane.ai/demos/tutorial_adversarial_attacks_QML).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://pennylane.ai/demos/tutorial_adversarial_attacks_QML); retrieved 2026-10-08.

#### Q0541 Demos — PennyLane

Author metadata not supplied.
Tutorial | Undated | PennyLane.
Identifier and resource: [Official resource](https://pennylane.ai/demonstrations).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://pennylane.ai/demonstrations); retrieved 2026-10-08.

#### Q0542 GitHub - PennyLaneAI/pennylane: PennyLane is an open-source quantum software platform for quantum computing, quantum machine learning, and quantum chemistry. Create meaningful quantum algorithms, from inspiration to implementation. · GitHub

Author metadata not supplied.
Software repository | Undated | PennyLane.
Identifier and resource: [Official resource](https://github.com/PennyLaneAI/pennylane).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/PennyLaneAI/pennylane); retrieved 2026-10-08.

#### Q0543 GitHub - qiskit-community/qiskit-machine-learning: An open-source library built on Qiskit for quantum machine learning tasks at scale on quantum hardware and classical simulators · GitHub

Author metadata not supplied.
Software repository | Undated | Qiskit Machine Learning.
Identifier and resource: [Official resource](https://github.com/qiskit-community/qiskit-machine-learning).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/qiskit-community/qiskit-machine-learning); retrieved 2026-10-08.

#### Q0544 Introduction to Geometric Quantum Machine Learning | PennyLane Demos

Author metadata not supplied.
Tutorial | Undated | PennyLane.
Identifier and resource: [Official resource](https://pennylane.ai/demos/tutorial_geometric_qml).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://pennylane.ai/demos/tutorial_geometric_qml); retrieved 2026-10-08.

#### Q0545 PennyLane Documentation — PennyLane 0.45.1 documentation

Author metadata not supplied.
Documentation | Undated | PennyLane.
Identifier and resource: [Official resource](https://docs.pennylane.ai/en/stable/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://docs.pennylane.ai/en/stable/); retrieved 2026-10-08.

#### Q0546 Post Variational Quantum Neural Networks | PennyLane Demos

Author metadata not supplied.
Tutorial | Undated | PennyLane.
Identifier and resource: [Official resource](https://www.pennylane.ai/demos/tutorial_post-variational_quantum_neural_networks).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://www.pennylane.ai/demos/tutorial_post-variational_quantum_neural_networks); retrieved 2026-10-08.

### D10T04 Quantum generative models

Generative quantum models represent or sample data distributions. Training objectives, sample quality, likelihood access, and the data source define the task.

Fine subcategories: Born machines; quantum GANs; sampling models; generative benchmarks; likelihood estimation.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0547 Conditioning in generative quantum denoising diffusion models

Daniel Quinn, Lorenzo Buffoni, Stefano Gherardini, Gabriele De Chiara.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 3 | pp. 035047.
Identifier and resource: [10.1088/2058-9565/ae8881](https://doi.org/10.1088/2058-9565/ae8881).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae8881); retrieved 2026-10-08.

#### Q0548 Diabatic quantum annealing for training energy-based generative models

Gilhan Kim, Ju-Yeon Gyhm, Daniel K. Park.
Journal article | 2026 | Physical Review E | vol. 113 | no. 3 | article 035302.
Identifier and resource: [10.1103/2g6m-whm2](https://doi.org/10.1103/2g6m-whm2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F2g6m-whm2); retrieved 2026-10-08.

#### Q0549 Enhancing Breast Cancer Diagnosis with Quantum-Driven Generative Adversarial Models

V. Shankar Ganesh, A. Purushothaman, A.Abdul Hayum, K. Karuppusamy.
Journal article | 2026 | International Journal of Drug Delivery Technology | vol. 16 | no. 7.
Identifier and resource: [10.25258/ijddt.16.7.110](https://doi.org/10.25258/ijddt.16.7.110).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.25258%2Fijddt.16.7.110); retrieved 2026-10-08.

#### Q0550 Q-Tag: watermarking quantum circuit generative models

Yang Yang, Yuzhu Long, Han Fang, Zhaoyun Chen, Zhonghui Li, Weiming Zhang, Guoping Guo.
Journal article | 2026 | Science China Information Sciences | vol. 69 | no. 8 | article 180504.
Identifier and resource: [10.1007/s11432-025-5016-2](https://doi.org/10.1007/s11432-025-5016-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11432-025-5016-2); retrieved 2026-10-08.

#### Q0551 Quantum-classical generative models for drug design

Prateek Jain, Param Pathak, Krishna Bhatia, Shalini Devendrababu, Srinjoy Ganguly.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 1 | article 30.
Identifier and resource: [10.1007/s42484-026-00356-x](https://doi.org/10.1007/s42484-026-00356-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00356-x); retrieved 2026-10-08.

#### Q0552 Towards Stable and Diverse Generative Models with Dual Hybrid Quantum Generative Adversarial Network

S. Kushal Varma, Maski Yashasv, Lanka Dhanush, Kotari Harshith, Srinath Devale.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 388-399.
Identifier and resource: [10.1007/978-3-032-26352-0_32](https://doi.org/10.1007/978-3-032-26352-0_32).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-26352-0_32); retrieved 2026-10-08.

#### Q0553 A Review of Quantum-Based Diffusion Models in Generative AI

Glauco Lima, Ernestas Filatovas, Marco Marcozzi, Remigijus Paulavičius.
Journal article | 2025 | Vilnius University Open Series | pp. 109-120.
Identifier and resource: [10.15388/lmitt.2025.14](https://doi.org/10.15388/lmitt.2025.14).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15388%2Flmitt.2025.14); retrieved 2026-10-08.

#### Q0554 Adaptive Quantum Channels as Long-Memory Generative Models

Charlee Stefanski, Vanio Markov, David Novak, Vladimir Rastunkov.
Conference paper | 2025 | Proceedings of the 6th ACM International Conference on AI in Finance | pp. 492-500.
Identifier and resource: [10.1145/3768292.3770440](https://doi.org/10.1145/3768292.3770440).
Conference metadata: ICAIF '25: 6th ACM International Conference on AI in Finance.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3768292.3770440); retrieved 2026-10-08.

#### Q0555 Back Cover: Quantum‐Noise‐Driven Generative Diffusion Models (Adv. Quantum Technol. 12/2025)

Marco Parigi, Stefano Martina, Filippo Caruso.
Journal article | 2025 | Advanced Quantum Technologies | vol. 8 | no. 12 | article e70122.
Identifier and resource: [10.1002/qute.70122](https://doi.org/10.1002/qute.70122).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.70122); retrieved 2026-10-08.

#### Q0556 DisQu: Investigating the Impact of Disorder in Quantum Generative Models

Yannick Werner, Jasmin Frkatovic, Vitor Fortes Rey, Matthias Tschöpe, Sungho Suh, Paul Lukowicz, Nikolaos Palaiodimopoulos, Maximilian Kiefer-Emmanouilidis.
Conference paper | 2025 | 2025 International Joint Conference on Neural Networks (IJCNN) | pp. 1-8.
Identifier and resource: [10.1109/ijcnn64981.2025.11227841](https://doi.org/10.1109/ijcnn64981.2025.11227841).
Conference metadata: 2025 International Joint Conference on Neural Networks (IJCNN).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fijcnn64981.2025.11227841); retrieved 2026-10-08.

#### Q0557 Experimental demonstration of reconstructing quantum states with generative models

Xuegang Li, Wenjie Jiang, Ziyue Hua, Weiting Wang, Xiaoxuan Pan, Weizhou Cai, Zhide Lu, Jiaxiu Han et al..
Journal article | 2025 | Science Bulletin | vol. 70 | no. 10 | pp. 1572-1575.
Identifier and resource: [10.1016/j.scib.2025.03.007](https://doi.org/10.1016/j.scib.2025.03.007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.scib.2025.03.007); retrieved 2026-10-08.

#### Q0558 Exploring biological neuronal correlations with quantum generative models

Vinicius Hernandes, Eliska Greplova.
Journal article | 2025 | Cell Reports Physical Science | vol. 6 | no. 8 | pp. 102682 | article 102682.
Identifier and resource: [10.1016/j.xcrp.2025.102682](https://doi.org/10.1016/j.xcrp.2025.102682).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.xcrp.2025.102682); retrieved 2026-10-08.

#### Q0559 Monitoring and Evaluating Quantum Generative Models Using Spark and MLflow

Saman Siadati.
Journal article | 2025 | Proceedings of the AAAI Symposium Series | vol. 7 | no. 1 | pp. 398-403.
Identifier and resource: [10.1609/aaaiss.v7i1.36911](https://doi.org/10.1609/aaaiss.v7i1.36911).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1609%2Faaaiss.v7i1.36911); retrieved 2026-10-08.

#### Q0560 Quantum generative models

Andrea Delgado, Kathleen E Hamilton.
Book chapter | 2025 | Quantum Machine Learning | pp. 7-1-7-18.
Identifier and resource: [10.1088/978-0-7503-4952-9ch7](https://doi.org/10.1088/978-0-7503-4952-9ch7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F978-0-7503-4952-9ch7); retrieved 2026-10-08.

#### Q0561 Quantum-Enhanced Generative Models for Rare Event Prediction

M.Z. Haider, M.U. Ghouri, Tayyaba Noreen, M. Salman.
Conference paper | 2025 | 2025 Computing, Communications and IoT Applications (ComComAp) | pp. 103-110.
Identifier and resource: [10.1109/comcomap68359.2025.11353178](https://doi.org/10.1109/comcomap68359.2025.11353178).
Conference metadata: 2025 Computing, Communications and IoT Applications (ComComAp).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcomcomap68359.2025.11353178); retrieved 2026-10-08.

#### Q0562 A Characterization of Quantum Generative Models

Carlos A. Riofrio, Oliver Mitevski, Caitlin Jones, Florian Krellner, Aleksandar Vuckovic, Joseph Doetsch, Johannes Klepsch, Thomas Ehmer et al..
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 2 | pp. 1-34.
Identifier and resource: [10.1145/3655027](https://doi.org/10.1145/3655027).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3655027); retrieved 2026-10-08.

### D10T05 Quantum reinforcement learning

Quantum reinforcement learning studies quantum resources in sequential decision tasks. Coherent access to an environment is a substantial assumption and is not always physically available.

Fine subcategories: Agents; policies; value functions; environment access; exploration; speedup assumptions.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0563 Noise-resilient quantum reinforcement learning

Jing-Ci Yue, Jun-Hong An.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 4 | article 044060.
Identifier and resource: [10.1103/8gfc-2nsc](https://doi.org/10.1103/8gfc-2nsc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8gfc-2nsc); retrieved 2026-10-08.

#### Q0564 Quantum reinforcement learning

Samuel Yen-Chi Chen.
Book chapter | 2026 | Quantum Computational AI | pp. 3-23.
Identifier and resource: [10.1016/b978-0-44-330259-6.00009-8](https://doi.org/10.1016/b978-0-44-330259-6.00009-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-44-330259-6.00009-8); retrieved 2026-10-08.

#### Q0565 Quantum reinforcement learning in dynamic environments

Oliver Sefrin, Manuel Radons, Lars Simon, Sabine Wölk.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 1 | article 58.
Identifier and resource: [10.1007/s42484-026-00383-8](https://doi.org/10.1007/s42484-026-00383-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00383-8); retrieved 2026-10-08.

#### Q0566 Variational Quantum Reinforcement Learning for Quantum Control

Haixu Yu, Lei Ye, Peng Wang.
Conference paper | 2026 | 2026 6th IEEE International Conference on Cybernetics (CYBCONF) | pp. 161-166.
Identifier and resource: [10.1109/cybconf69298.2026.11670283](https://doi.org/10.1109/cybconf69298.2026.11670283).
Conference metadata: 2026 6th IEEE International Conference on Cybernetics (CYBCONF).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcybconf69298.2026.11670283); retrieved 2026-10-08.

#### Q0567 Benchmarking Quantum Reinforcement Learning

Georg Kruse, Rodrigo Coelho, Andreas Rosskopf, Robert Wille, Jeanette-Miriam Lorenz.
Conference paper | 2025 | Proceedings of the 17th International Conference on Agents and Artificial Intelligence | pp. 773-782.
Identifier and resource: [10.5220/0013393200003890](https://doi.org/10.5220/0013393200003890).
Conference metadata: Workshop on Quantum Artificial Intelligence and Optimization 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5220%2F0013393200003890); retrieved 2026-10-08.

#### Q0568 Quantum Circuit Structure Optimization for Quantum Reinforcement Learning

Seok Bin Son, Joongheon Kim.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 247-251.
Identifier and resource: [10.1109/qce65121.2025.10327](https://doi.org/10.1109/qce65121.2025.10327).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10327); retrieved 2026-10-08.

#### Q0569 Quantum Reinforcement Learning with Adaptive Variational Quantum Circuits

Sarvesh Bendre, Samiksha Apake, Ashish Mishra, Atharva Bali, Anikita Bhagade.
Posted content | 2025 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.5220513](https://doi.org/10.2139/ssrn.5220513).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.5220513); retrieved 2026-10-08.

#### Q0570 Quantum noise modeling through reinforcement learning

Simone Bordoni, Andrea Papaluca, Piergiorgio Buttarini, Alejandro Sopena, Stefano Giagu, Stefano Carrazza.
Journal article | 2025 | Quantum Science and Technology | vol. 11 | no. 1 | pp. 015005.
Identifier and resource: [10.1088/2058-9565/ae1e98](https://doi.org/10.1088/2058-9565/ae1e98).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae1e98); retrieved 2026-10-08.

#### Q0571 Quantum-Inspired Reinforcement Learning for Quantum Control

Haixu Yu, Xudong Zhao, Chunlin Chen.
Journal article | 2025 | IEEE Transactions on Control Systems Technology | vol. 33 | no. 1 | pp. 61-76.
Identifier and resource: [10.1109/tcst.2024.3437142](https://doi.org/10.1109/tcst.2024.3437142).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcst.2024.3437142); retrieved 2026-10-08.

#### Q0572 Model-Based Offline Quantum Reinforcement Learning

Simon Eisenmann, Daniel Hein, Steffen Udluft, Thomas A. Runkler.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1490-1496.
Identifier and resource: [10.1109/qce60285.2024.00175](https://doi.org/10.1109/qce60285.2024.00175).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.00175); retrieved 2026-10-08.

#### Q0573 Parametrized Quantum Circuits for Reinforcement Learning

K.T. Mpofu, P. Mthunzi-Kufa.
Conference paper | 2024 | 2024 4th International Multidisciplinary Information Technology and Engineering Conference (IMITEC) | pp. 240-251.
Identifier and resource: [10.1109/imitec60221.2024.10850927](https://doi.org/10.1109/imitec60221.2024.10850927).
Conference metadata: 2024 4th International Multidisciplinary Information Technology and Engineering Conference (IMITEC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fimitec60221.2024.10850927); retrieved 2026-10-08.

#### Q0574 QTRL: Toward Practical Quantum Reinforcement Learning via Quantum-Train

Chen-Yu Liu, Chu-Hsuan Abraham Lin, Chao-Han Huck Yang, Kuan-Cheng Chen, Min-Hsiu Hsieh.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 317-322.
Identifier and resource: [10.1109/qce60285.2024.10299](https://doi.org/10.1109/qce60285.2024.10299).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.10299); retrieved 2026-10-08.

#### Q0575 Quantum Reinforcement Learning for Cognitive SAR

Jan Meyer, Kay Glatting, Sigurd Huber, Gerhard Krieger.
Conference paper | 2024 | IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium | pp. 794-798.
Identifier and resource: [10.1109/igarss53475.2024.10642330](https://doi.org/10.1109/igarss53475.2024.10642330).
Conference metadata: IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Figarss53475.2024.10642330); retrieved 2026-10-08.

#### Q0576 Quantum Reinforcement Learning: An Overview

Gyu Seon Kim, Soohyun Park, Joongheon Kim.
Conference paper | 2024 | 2024 15th International Conference on Information and Communication Technology Convergence (ICTC) | pp. 1145-1150.
Identifier and resource: [10.1109/ictc62082.2024.10826656](https://doi.org/10.1109/ictc62082.2024.10826656).
Conference metadata: 2024 15th International Conference on Information and Communication Technology Convergence (ICTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fictc62082.2024.10826656); retrieved 2026-10-08.

#### Q0577 Quantum Task Impact Learning (QTIL)Algorithm on Quantum Reinforcement Learning

R. Palanivel, P. Muthulakshmi.
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-4766272/v1](https://doi.org/10.21203/rs.3.rs-4766272/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-4766272%2Fv1); retrieved 2026-10-08.

#### Q0578 Quantum reinforcement learning

Niels M. P. Neumann, Paolo B. U. L. de Heer, Frank Phillipson.
Journal article | 2023 | Quantum Information Processing | vol. 22 | no. 2 | article 125.
Identifier and resource: [10.1007/s11128-023-03867-9](https://doi.org/10.1007/s11128-023-03867-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-023-03867-9); retrieved 2026-10-08.

### D10T06 Quantum learning theory

Quantum learning theory analyzes sample complexity and generalization under explicit learning models. Results differ for classical data, quantum examples, and unknown quantum states.

Fine subcategories: PAC models; sample complexity; generalization; learnability; quantum examples.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0579 Learning complexity gradually in quantum machine learning models

Erik Recio-Armengol, Franz J. Schreiber, Jens Eisert, Carlos Bravo-Prieto.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033006.
Identifier and resource: [10.1103/wnlr-q9xd](https://doi.org/10.1103/wnlr-q9xd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fwnlr-q9xd); retrieved 2026-10-08.

#### Q0580 Run-length certificates in quantum learning: Sample complexity and noise thresholds

Jeongho Bang.
Journal article | 2026 | Physical Review A | vol. 113 | no. 6 | article 062601.
Identifier and resource: [10.1103/cn9t-dynd](https://doi.org/10.1103/cn9t-dynd).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fcn9t-dynd); retrieved 2026-10-08.

#### Q0581 Universal Sample Complexity Bounds in Quantum Learning Theory via Fisher Information Matrix

Hyukgun Kwon, Seok Hyung Lie, Liang Jiang.
Journal article | 2026 | PRX Quantum | vol. 7 | no. 3 | article 033063.
Identifier and resource: [10.1103/8k5v-ddtw](https://doi.org/10.1103/8k5v-ddtw).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8k5v-ddtw); retrieved 2026-10-08.

#### Q0582 A quadratic sample complexity reduction for agnostic learning via quantum algorithms

Daniel Z. Zanger.
Journal article | 2025 | International Journal of Quantum Information | vol. 23 | no. 06 | article 2550023.
Identifier and resource: [10.1142/s0219749925500236](https://doi.org/10.1142/s0219749925500236).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0219749925500236); retrieved 2026-10-08.

#### Q0583 On the sample complexity of quantum Boltzmann machine learning

Luuk Coopmans, Marcello Benedetti.
Journal article | 2024 | Communications Physics | vol. 7 | no. 1 | article 274.
Identifier and resource: [10.1038/s42005-024-01763-x](https://doi.org/10.1038/s42005-024-01763-x).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42005-024-01763-x); retrieved 2026-10-08.

#### Q0584 Sample complexity of learning parametric quantum circuits

Haoyuan Cai, Qi Ye, Dong-Ling Deng.
Journal article | 2022 | Quantum Science and Technology | vol. 7 | no. 2 | pp. 025014.
Identifier and resource: [10.1088/2058-9565/ac4f30](https://doi.org/10.1088/2058-9565/ac4f30).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fac4f30); retrieved 2026-10-08.

#### Q0585 Tangible reduction in learning sample complexity with large classical samples and small quantum system

Wooyeong Song, Marcin Wieśniak, Nana Liu, Marcin Pawłowski, Jinhyoung Lee, Jaewan Kim, Jeongho Bang.
Journal article | 2021 | Quantum Information Processing | vol. 20 | no. 8 | article 275.
Identifier and resource: [10.1007/s11128-021-03217-7](https://doi.org/10.1007/s11128-021-03217-7).
Fine tags: sample complexity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-021-03217-7); retrieved 2026-10-08.

#### Q0586 Generalization in QML from few training data | PennyLane Demos

Author metadata not supplied.
Tutorial | Undated | PennyLane.
Identifier and resource: [Official resource](https://pennylane.ai/demos/tutorial_learning_few_data).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://pennylane.ai/demos/tutorial_learning_few_data); retrieved 2026-10-08.

### D10T07 Machine learning for quantum systems

Machine learning can assist calibration, control, characterization, and decoding of quantum hardware. This direction can be useful without claiming a speedup from a quantum learning model.

Fine subcategories: Control optimization; calibration models; learned decoders; state classification; scientific discovery.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0587 Adaptive Quantum Error Mitigation Using Machine Learning in Noisy Intermediate-Scale Quantum Systems

Jefin Rojar J, Haribaskar R, Nithya Jayakumar, Ramya Jayakumar.
Conference paper | 2026 | 2026 9th International Conference on Computational Intelligence in Data Science (ICCIDS) | pp. 1-6.
Identifier and resource: [10.1109/iccids69108.2026.11407599](https://doi.org/10.1109/iccids69108.2026.11407599).
Conference metadata: 2026 9th International Conference on Computational Intelligence in Data Science (ICCIDS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcids69108.2026.11407599); retrieved 2026-10-08.

#### Q0588 Error-Corrected Quantum Machine Learning in Financial Forecasting

Mustafa Nazar, Hussein Aljan Hasan, Kahtan Mohammed Adnan, Mahmood Jawad Abu-Alshaeer, Dmytro Hnatchenko.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 458-482.
Identifier and resource: [10.1007/978-3-032-39708-9_23](https://doi.org/10.1007/978-3-032-39708-9_23).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-39708-9_23); retrieved 2026-10-08.

#### Q0589 Quantum Error Correction and Detection for Quantum Machine Learning

Eromanga Adermann, Haiyue Kang, Martin Sevior, Muhammad Usman.
Book chapter | 2026 | Quantum Science and Technology | pp. 413-436.
Identifier and resource: [10.1007/978-3-032-11153-1_17](https://doi.org/10.1007/978-3-032-11153-1_17).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-11153-1_17); retrieved 2026-10-08.

#### Q0590 Qyn: FPGA-Based Quantum Error Correction with Integrated Quantum Machine Learning

Claritta AlSaneh, Claudia Mattar, Soraia Oueida.
Conference paper | 2026 | 2026 7th International Conference on Bio-engineering for Smart Technologies (BioSMART) | pp. 1-7.
Identifier and resource: [10.1109/biosmart71257.2026.11598218](https://doi.org/10.1109/biosmart71257.2026.11598218).
Conference metadata: 2026 7th International Conference on Bio-engineering for Smart Technologies (BioSMART).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fbiosmart71257.2026.11598218); retrieved 2026-10-08.

#### Q0591 Variational quantum machine learning with quantum error detection

Eromanga Adermann, Hajime Suzuki, Muhammad Usman.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 1 | article 1.
Identifier and resource: [10.1007/s42484-026-00347-y](https://doi.org/10.1007/s42484-026-00347-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00347-y); retrieved 2026-10-08.

#### Q0592 Efficiently decoding quantum errors with machine learning

Xiu-Hao Deng, Yuan Xu.
Journal article | 2025 | Nature Computational Science | vol. 5 | no. 12 | pp. 1100-1101.
Identifier and resource: [10.1038/s43588-025-00907-5](https://doi.org/10.1038/s43588-025-00907-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs43588-025-00907-5); retrieved 2026-10-08.

#### Q0593 Machine learning approach toward quantum error mitigation for accurate molecular energetics

Srushti Patil, Dibyendu Mondal, Rahul Maitra.
Journal article | 2025 | The Journal of Chemical Physics | vol. 163 | no. 2 | article 024129.
Identifier and resource: [10.1063/5.0274910](https://doi.org/10.1063/5.0274910).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0274910); retrieved 2026-10-08.

#### Q0594 Machine-Learning based Decoding of Surface Code Syndromes in Quantum Error Correction

Debasmita Bhoumik, Pinaki Sen, Ritajit Majumdar, Susmita Sur-Kolay, Latesh Kumar KJ, Sundaraja Sitharama Iyengar.
Journal article | 2022 | Journal of Engineering Research and Sciences | vol. 1 | no. 6 | pp. 21-35.
Identifier and resource: [10.55708/js0106004](https://doi.org/10.55708/js0106004).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55708%2Fjs0106004); retrieved 2026-10-08.

## D11 Optimization and operations research

Quantum optimization includes annealing, variational methods, and algorithms with provable guarantees. Application results should report feasible solutions and comparisons to strong classical solvers.

Prerequisites: Optimization, constraint modeling, and algorithm analysis.

Assessment focus: Feasibility, approximation quality, embedding overhead, and solver baselines.

Primary catalog resources in this category: 55.

### D11T01 Combinatorial optimization

Combinatorial methods encode discrete decisions and constraints into quantum workflows. Feasibility, approximation quality, and problem size must be reported.

Fine subcategories: MaxCut; satisfiability; graph coloring; constraint satisfaction; approximation guarantees.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q0595 Benchmarking variational quantum algorithms for combinatorial optimization in practice

Tim Schwägerl, Yahui Chai, Tobias Hartung, Karl Jansen, Stefan Kühn.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 1 | article 26.
Identifier and resource: [10.1007/s42484-026-00355-y](https://doi.org/10.1007/s42484-026-00355-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00355-y); retrieved 2026-10-08.

#### Q0596 Enhanced multiscale quantum approximate optimization algorithm in multibody combinatorial optimization problems

Lei-Lei 蕾蕾 Chen 陈, Ping 平 Zou 邹, Ya-Fei 亚飞 Yu 於.
Journal article | 2026 | Chinese Physics B | vol. 35 | no. 7 | pp. 070305.
Identifier and resource: [10.1088/1674-1056/ae29f7](https://doi.org/10.1088/1674-1056/ae29f7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fae29f7); retrieved 2026-10-08.

#### Q0597 Quantum-Assisted Hybrid Optimization for Graph-Based Combinatorial Optimization

Srinivasarao Thota, N. Shilpa, Nasr Al Din Ide.
Journal article | 2026 | IEEE Access | vol. 14 | pp. 142245-142261.
Identifier and resource: [10.1109/access.2026.3733232](https://doi.org/10.1109/access.2026.3733232).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Faccess.2026.3733232); retrieved 2026-10-08.

#### Q0598 Quantum-Inspired Butterfly Optimization Algorithm for Combinatorial Optimization on Binary Problems

Freddy Alejandro Chaurra Gutierrez, Claudia Feregrino-Uribe, Guohua Sun.
Posted content | 2026 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.6968611](https://doi.org/10.2139/ssrn.6968611).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.6968611); retrieved 2026-10-08.

#### Q0599 Qubit-efficient quantum combinatorial-optimization solver

Bhuvanesh Sundar, Maxime Dupont.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 3 | article 034071.
Identifier and resource: [10.1103/s5jv-jh24](https://doi.org/10.1103/s5jv-jh24).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fs5jv-jh24); retrieved 2026-10-08.

#### Q0600 Qubit‐Efficient Quantum Local Search for Combinatorial Optimization

Mikhail Podobrii, Viacheslav Kuzmin, Vladimir Voloshinov, Margarita Veshchezerova, Michael R. Perelshtein.
Journal article | 2026 | Advanced Quantum Technologies | vol. 9 | no. 3 | article e00438.
Identifier and resource: [10.1002/qute.202500438](https://doi.org/10.1002/qute.202500438).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202500438); retrieved 2026-10-08.

#### Q0601 Toward Quantum Combinatorial Optimization

Yunpyo Hong, Jaejoon Gill, Daeyeun Kim, Seungcheol Oh, Byung-Soo Kim, Joongheon Kim.
Journal article | 2026 | IEEE Nanotechnology Magazine | pp. 1-11.
Identifier and resource: [10.1109/mnano.2026.3728349](https://doi.org/10.1109/mnano.2026.3728349).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmnano.2026.3728349); retrieved 2026-10-08.

#### Q0602 Variational quantum algorithm for constrained combinatorial optimization problems

Hui-Min Li, Yuan-Liang Han, Zhi-Xi Wang, Shao-Ming Fei.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032406.
Identifier and resource: [10.1103/ykxd-h19w](https://doi.org/10.1103/ykxd-h19w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fykxd-h19w); retrieved 2026-10-08.

#### Q0603 Benchmarking Quantum Computing for Combinatorial Optimization

Nathan Kittichaikoonkij, Nutthapat Pongtanyavichai, Poopha Suwananek, Prabhas Chongstitvatana, Kamonluk Suksen.
Conference paper | 2025 | 2025 22nd International Conference on Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology (ECTI-CON) | pp. 1-6.
Identifier and resource: [10.1109/ecti-con64996.2025.11100821](https://doi.org/10.1109/ecti-con64996.2025.11100821).
Conference metadata: 2025 22nd International Conference on Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology (ECTI-CON).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fecti-con64996.2025.11100821); retrieved 2026-10-08.

#### Q0604 Combinatorial optimization with quantum computers

Francisco Chicano, Gabiel Luque, Zakaria Abdelmoiz Dahi, Rodrigo Gil-Merino.
Journal article | 2025 | Engineering Optimization | vol. 57 | no. 1 | pp. 208-233.
Identifier and resource: [10.1080/0305215x.2024.2435538](https://doi.org/10.1080/0305215x.2024.2435538).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F0305215x.2024.2435538); retrieved 2026-10-08.

#### Q0605 Quantum Optimization Realized: Quantum Annealing for Combinatorial Spatial Problems in Practice

Amr Magdy.
Conference paper | 2025 | Proceedings of the 1st ACM SIGSPATIAL International Workshop on Quantum Computing for Spatial Data Systems and Applications | pp. 11-14.
Identifier and resource: [10.1145/3764923.3777407](https://doi.org/10.1145/3764923.3777407).
Conference metadata: SIGSPATIAL '25: The 33rd ACM International Conference on Advances in Geographic Information Systems.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3764923.3777407); retrieved 2026-10-08.

#### Q0606 Quantum Optimization for Enhanced Combinatorial Algorithms

Pradeep Kumar Pandey, Ruchi Chaturvedi, Suraj Bhan Dangi.
Journal article | 2025 | The Nucleus | vol. 62 | no. 1 | pp. 54-58.
Identifier and resource: [10.71330/thenucleus.2025.1453](https://doi.org/10.71330/thenucleus.2025.1453).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.71330%2Fthenucleus.2025.1453); retrieved 2026-10-08.

#### Q0607 Quantum annealing for combinatorial optimization: a benchmarking study

Seongmin Kim, Sang-Woo Ahn, In-Saeng Suh, Alexander W. Dowling, Eungkyu Lee, Tengfei Luo.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 77.
Identifier and resource: [10.1038/s41534-025-01020-1](https://doi.org/10.1038/s41534-025-01020-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01020-1); retrieved 2026-10-08.

#### Q0608 Quantum-Guided Cluster Algorithms for Combinatorial Optimization

Peter J. Eder, Aron Kerschbaumer, Jernej Rudi Finžgar, Raimel A. Medina, Martin J. A. Schuetz, Helmut G. Katzgraber, Sarah Braun, Christian B. Mendl.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 219-229.
Identifier and resource: [10.1109/qce65121.2025.00033](https://doi.org/10.1109/qce65121.2025.00033).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00033); retrieved 2026-10-08.

#### Q0609 Recursive Quantum Relaxation for Combinatorial Optimization Problems

Ruho Kondo, Yuki Sato, Rudy Raymond, Naoki Yamamoto.
Journal article | 2025 | Quantum | vol. 9 | pp. 1594 | article 1594.
Identifier and resource: [10.22331/q-2025-01-15-1594](https://doi.org/10.22331/q-2025-01-15-1594).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-01-15-1594); retrieved 2026-10-08.

### D11T02 Quantum semidefinite programming

Quantum SDP solvers use structured access to matrices and constraints. Their advantage depends on sparsity, rank, input models, and the required output.

Fine subcategories: Matrix access; feasibility; trace constraints; solver accuracy; oracle costs.

Primary resources: 11. Additional related assignments can be found in the interactive HTML.

#### Q0610 Quantum Alternating Direction Method of Multipliers for Semidefinite Programming

Hantao Nie, Dong An, Zaiwen Wen.
Journal article | 2026 | Quantum | vol. 10 | pp. 2154 | article 2154.
Identifier and resource: [10.22331/q-2026-07-08-2154](https://doi.org/10.22331/q-2026-07-08-2154).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-07-08-2154); retrieved 2026-10-08.

#### Q0611 Semidefinite programming for quantum channel learning

Mikhail Gennadievich Belov, Victor Victorovich Dubov, Vadim Konstantinovich Ivanov, Alexander Yurievich Maslov, Olga Vladimirovna Proshina, Vladislav Gennadievich Malyshkin.
Journal article | 2026 | Physical Review E | vol. 114 | no. 3 | article 035302.
Identifier and resource: [10.1103/kdl5-smrh](https://doi.org/10.1103/kdl5-smrh).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fkdl5-smrh); retrieved 2026-10-08.

#### Q0612 Slack-variable approach for variational quantum semidefinite programming

Jingxuan Chen, Hanna Westerheim, Zoë Holmes, Ivy Luo, Theshani Nuradha, Dhrumil Patel, Soorya Rethinasamy, Kathie Wang et al..
Journal article | 2025 | Physical Review A | vol. 112 | no. 2 | article 022607.
Identifier and resource: [10.1103/lwxq-4myj](https://doi.org/10.1103/lwxq-4myj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Flwxq-4myj); retrieved 2026-10-08.

#### Q0613 Semidefinite programming in quantum information science

Stefano Scali.
Journal article | 2024 | Contemporary Physics | vol. 65 | no. 3 | pp. 202-203.
Identifier and resource: [10.1080/00107514.2024.2415998](https://doi.org/10.1080/00107514.2024.2415998).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F00107514.2024.2415998); retrieved 2026-10-08.

#### Q0614 Semidefinite programming relaxations for quantum correlations

Armin Tavakoli, Alejandro Pozas-Kerstjens, Peter Brown, Mateus Araújo.
Journal article | 2024 | Reviews of Modern Physics | vol. 96 | no. 4 | article 045006.
Identifier and resource: [10.1103/revmodphys.96.045006](https://doi.org/10.1103/revmodphys.96.045006).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Frevmodphys.96.045006); retrieved 2026-10-08.

#### Q0615 Variational Quantum Algorithms for Semidefinite Programming

Dhrumil Patel, Patrick J. Coles, Mark M. Wilde.
Journal article | 2024 | Quantum | vol. 8 | pp. 1374 | article 1374.
Identifier and resource: [10.22331/q-2024-06-17-1374](https://doi.org/10.22331/q-2024-06-17-1374).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-06-17-1374); retrieved 2026-10-08.

#### Q0616 Quantum key distribution rates from semidefinite programming

Mateus Araújo, Marcus Huber, Miguel Navascués, Matej Pivoluska, Armin Tavakoli.
Journal article | 2023 | Quantum | vol. 7 | pp. 1019 | article 1019.
Identifier and resource: [10.22331/q-2023-05-24-1019](https://doi.org/10.22331/q-2023-05-24-1019).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-05-24-1019); retrieved 2026-10-08.

#### Q0617 Self-consistent quantum measurement tomography based on semidefinite programming

Marco Cattaneo, Matteo A. C. Rossi, Keijo Korhonen, Elsi-Mari Borrelli, Guillermo García-Pérez, Zoltán Zimborás, Daniel Cavalcanti.
Journal article | 2023 | Physical Review Research | vol. 5 | no. 3 | article 033154.
Identifier and resource: [10.1103/physrevresearch.5.033154](https://doi.org/10.1103/physrevresearch.5.033154).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.5.033154); retrieved 2026-10-08.

#### Q0618 Semidefinite Programming in Quantum Information Science

Paul Skrzypczyk, Daniel Cavalcanti.
Book | 2023 | IOP Publishing.
Identifier and resource: [10.1088/978-0-7503-3343-6](https://doi.org/10.1088/978-0-7503-3343-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F978-0-7503-3343-6); retrieved 2026-10-08.

#### Q0619 Semidefinite programming algorithm for the quantum mechanical bootstrap

David Berenstein, George Hulsey.
Journal article | 2023 | Physical Review E | vol. 107 | no. 5 | article L053301.
Identifier and resource: [10.1103/physreve.107.l053301](https://doi.org/10.1103/physreve.107.l053301).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreve.107.l053301); retrieved 2026-10-08.

#### Q0620 Noisy intermediate-scale quantum algorithm for semidefinite programming

Kishor Bharti, Tobias Haug, Vlatko Vedral, Leong-Chuan Kwek.
Journal article | 2022 | Physical Review A | vol. 105 | no. 5 | article 052445.
Identifier and resource: [10.1103/physreva.105.052445](https://doi.org/10.1103/physreva.105.052445).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.105.052445); retrieved 2026-10-08.

### D11T03 Quantum scheduling and routing

Routing and scheduling applications combine difficult constraints with discrete optimization. Penalties and embedding can create substantial overhead or infeasible solutions.

Fine subcategories: Vehicle routing; job shop scheduling; logistics; constraints; feasibility repair.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0621 Hybrid Classical–Quantum Optimization of Wireless Routing Using QAOA and Quantum Walks

Author metadata not supplied.
Journal article | 2026 | International Journal of Intelligent Systems and Applications in Engineering.
Identifier and resource: [10.17762/ijisae.v14i1s.8149](https://doi.org/10.17762/ijisae.v14i1s.8149).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.17762%2Fijisae.v14i1s.8149); retrieved 2026-10-08.

#### Q0622 Purification Strategy Optimization for Entanglement Routing in Quantum Networks

Javier Vecino Peñas, Ana Fernández-Vilas, Rebeca P. Díaz-Redondo, Sergio Gándara Gándara, Manuel Fernández-Veiga.
Conference paper | 2026 | 2026 International Conference on Quantum Control, Computing and Learning (qCCL) | pp. 1-8.
Identifier and resource: [10.1109/qccl70331.2026.11668568](https://doi.org/10.1109/qccl70331.2026.11668568).
Conference metadata: 2026 International Conference on Quantum Control, Computing and Learning (qCCL).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqccl70331.2026.11668568); retrieved 2026-10-08.

#### Q0623 Quantum-Inspired Optimization for Robust MANET Routing Protocols

K Subhashini, Kamini Sharma, Aashima Bansal, Jatinder Kaur, Ankit Chamoli, Vipin Kumar Chaudhary.
Conference paper | 2026 | 2026 Second International Conference on Emerging Computational Intelligence (ICECI) | pp. 1-6.
Identifier and resource: [10.1109/iceci69159.2026.11519468](https://doi.org/10.1109/iceci69159.2026.11519468).
Conference metadata: 2026 Second International Conference on Emerging Computational Intelligence (ICECI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficeci69159.2026.11519468); retrieved 2026-10-08.

#### Q0624 Cyber Risk-Aware Quantum-inspired Optimization of Home Healthcare Routing and Scheduling with Electric Autonomous Vehicles

Hooman Razavi, Shadan Ghaffary, Mostafa Hajiaghaei-Keshteli, Amirhossein Mostofi.
Conference paper | 2025 | 2025 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM) | pp. 1247-1254.
Identifier and resource: [10.1109/ieem63636.2025.11357715](https://doi.org/10.1109/ieem63636.2025.11357715).
Conference metadata: 2025 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM).
Fine tags: Vehicle routing.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fieem63636.2025.11357715); retrieved 2026-10-08.

#### Q0625 Quantum optimization in autonomous underwater vehicle routing navigation

Author metadata not supplied.
Journal article | 2025 | Journal of Transportation Science and Technology | vol. 14 | no. 2.
Identifier and resource: [10.55228/jtst.14(2).76-83](https://doi.org/10.55228/jtst.14(2).76-83).
Fine tags: Vehicle routing.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55228%2Fjtst.14%282%29.76-83); retrieved 2026-10-08.

#### Q0626 Routing and scheduling optimization for urban air mobility fleet management using quantum annealing

Renichiro Haba, Takuya Mano, Ryosuke Ueda, Genichiro Ebe, Kohei Takeda, Masayoshi Terabe, Masayuki Ohzeki.
Journal article | 2025 | Scientific Reports | vol. 15 | no. 1 | article 4326.
Identifier and resource: [10.1038/s41598-025-86843-w](https://doi.org/10.1038/s41598-025-86843-w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-025-86843-w); retrieved 2026-10-08.

#### Q0627 An optimization method for maintenance routing and scheduling in offshore wind farms based on chaotic quantum Harris hawks optimization

Ming-Wei Li, Yi-Zhang Lei, Zhong-Yi Yang, Hsin-Pou Huang, Wei-Chiang Hong.
Journal article | 2024 | Ocean Engineering | vol. 308 | pp. 118306 | article 118306.
Identifier and resource: [10.1016/j.oceaneng.2024.118306](https://doi.org/10.1016/j.oceaneng.2024.118306).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.oceaneng.2024.118306); retrieved 2026-10-08.

#### Q0628 Encoding trade-offs and design toolkits in quantum algorithms for discrete optimization: coloring, routing, scheduling, and other problems

Nicolas PD Sawaya, Albert T Schmitz, Stuart Hadfield.
Journal article | 2023 | Quantum | vol. 7 | pp. 1111 | article 1111.
Identifier and resource: [10.22331/q-2023-09-14-1111](https://doi.org/10.22331/q-2023-09-14-1111).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-09-14-1111); retrieved 2026-10-08.

### D11T04 Quantum portfolio and financial estimation

Financial algorithms include estimation, pricing, and portfolio models. Model calibration, input access, error tolerances, and real computational costs determine relevance.

Fine subcategories: Portfolio optimization; option pricing; risk estimation; Monte Carlo; data costs.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0629 Quantum advantage for multi-option portfolio pricing and valuation adjustments

Jeong Yu Han, Bin Cheng, Dinh-Long Vu, Patrick Rebentrost.
Journal article | 2026 | Quantitative Finance | vol. 26 | no. 3 | pp. 467-489.
Identifier and resource: [10.1080/14697688.2026.2614573](https://doi.org/10.1080/14697688.2026.2614573).
Fine tags: option pricing.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F14697688.2026.2614573); retrieved 2026-10-08.

#### Q0630 Quantum computing for loan portfolio pricing optimization

Yanbo J. Wang, Xuan Yang, Chao Ju, Zhihang Liu, Jiawei Lu, Yue Zhang, Yiduo Wang, Xinkai Gao et al..
Journal article | 2026 | Frontiers in Physics | vol. 14 | article 1744791.
Identifier and resource: [10.3389/fphy.2026.1744791](https://doi.org/10.3389/fphy.2026.1744791).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffphy.2026.1744791); retrieved 2026-10-08.

#### Q0631 Quantum-Inspired Quantitative Finance for Portfolio Optimization, Derivatives Pricing and Large-Scale Risk Management

Murali Krishna Pasupuleti.
Reference book | 2026 | National Education Services.
Identifier and resource: [10.62311/nesx/rb-66ag-978-81-68314-34-4](https://doi.org/10.62311/nesx/rb-66ag-978-81-68314-34-4).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62311%2Fnesx%2Frb-66ag-978-81-68314-34-4); retrieved 2026-10-08.

#### Q0632 Bridging Quantum Algorithms and Classical Finance: Portfolio Optimization Using QAOA and QUBO Framework

Arnav Aggarwal, Pranav Shrivastava, Rajneesh Kler, Prerna Agarwal.
Conference paper | 2025 | 2025 1st IEEE Uttar Pradesh Section Women in Engineering International Conference on Electrical Electronics and Computer Engineering (UPWIECON) | pp. 682-687.
Identifier and resource: [10.1109/upwiecon67212.2025.11390104](https://doi.org/10.1109/upwiecon67212.2025.11390104).
Conference metadata: 2025 1st IEEE Uttar Pradesh Section Women in Engineering International Conference on Electrical Electronics and Computer Engineering (UPWIECON).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fupwiecon67212.2025.11390104); retrieved 2026-10-08.

#### Q0633 Comprehensive Review of Quantum Computing Applications in Finance: Derivative Pricing, Risk Management, and Portfolio Optimization

Cem Fotocan.
Journal article | 2025 | Next Generation Journal for The Young Researchers | vol. 9 | no. 1 | pp. 65-67.
Identifier and resource: [10.62802/dnf08z38](https://doi.org/10.62802/dnf08z38).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62802%2Fdnf08z38); retrieved 2026-10-08.

#### Q0634 From portfolio optimization to quantum blockchain and security: a systematic review of quantum computing in finance

Abha Satyavan Naik, Esra Yeniaras, Gerhard Hellstern, Grishma Prasad, Sanjay Kumar Lalta Prasad Vishwakarma.
Journal article | 2025 | Financial Innovation | vol. 11 | no. 1 | article 88.
Identifier and resource: [10.1186/s40854-025-00751-6](https://doi.org/10.1186/s40854-025-00751-6).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1186%2Fs40854-025-00751-6); retrieved 2026-10-08.

#### Q0635 Quantum Algorithms for Portfolio Optimization in Finance

Efe Büke.
Journal article | 2025 | Next Generation Journal for The Young Researchers | vol. 9 | no. 1 | pp. 57-59.
Identifier and resource: [10.62802/krgj1w70](https://doi.org/10.62802/krgj1w70).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62802%2Fkrgj1w70); retrieved 2026-10-08.

#### Q0636 Quantum Computing and Portfolio Optimization in Finance Services

Alex Khang, Kali Charan Rath, Karteek Madapana, Jagannadha Rao, Lakshmi Prasad Panda, Subhasish Das.
Book chapter | 2025 | Shaping Cutting-Edge Technologies and Applications for Digital Banking and Financial Services | pp. 27-45.
Identifier and resource: [10.4324/9781003501947-2](https://doi.org/10.4324/9781003501947-2).
Fine tags: Portfolio optimization.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4324%2F9781003501947-2); retrieved 2026-10-08.

### D11T05 Quantum optimization benchmarks

Optimization benchmarking compares solution quality, runtime, and scaling against strong classical solvers. A quantum label or a favorable small instance is insufficient evidence of advantage.

Fine subcategories: Classical baselines; scaling; solution quality; wall time; statistical uncertainty.

Primary resources: 13. Additional related assignments can be found in the interactive HTML.

#### Q0637 A Quantum Enhanced Portfolio Optimization Pipeline: An Extensive Backtesting and Benchmarking Approach

Amar G. Nadh, Dushyant K. Sharma, Raghavan Solium.
Conference paper | 2026 | 2026 International Conference on Trends in Quantum Computing and Emerging Business Technologies (TQCEBT) | pp. 1-5.
Identifier and resource: [10.1109/tqcebt67648.2026.11681042](https://doi.org/10.1109/tqcebt67648.2026.11681042).
Conference metadata: 2026 International Conference on Trends in Quantum Computing and Emerging Business Technologies (TQCEBT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqcebt67648.2026.11681042); retrieved 2026-10-08.

#### Q0638 Benchmarking Blockchain, Federated Learning, and Quantum Evolutionary Algorithm for Combinatorial Optimization

Hamza Baniata, Attila Kertesz.
Journal article | 2026 | Blockchain: Research and Applications | pp. 100446 | article 100446.
Identifier and resource: [10.1016/j.bcra.2026.100446](https://doi.org/10.1016/j.bcra.2026.100446).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.bcra.2026.100446); retrieved 2026-10-08.

#### Q0639 Benchmarking Classical and Quantum Optimization Approaches for Rider-Order Assignment

Tharrmashastha SAPV, Surya Prakash Palanivel, Jasjyot Singh Gulati, M Maruthu Pandi.
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 930-936.
Identifier and resource: [10.1109/qcnc69040.2026.00153](https://doi.org/10.1109/qcnc69040.2026.00153).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00153); retrieved 2026-10-08.

#### Q0640 Benchmarking Quantum Optimization Algorithms for the 0–1 Knapsack Problem Using Qiskit

Kampa Lavanya, T. Surekha, J. David Sukeerthi Kumar, K. S. R. K. Sarma, Yaramachu Srikanth.
Book chapter | 2026 | Lecture Notes in Networks and Systems | pp. 532-540.
Identifier and resource: [10.1007/978-3-032-30960-0_42](https://doi.org/10.1007/978-3-032-30960-0_42).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-30960-0_42); retrieved 2026-10-08.

#### Q0641 Benchmarking Quantum Solvers in Noisy Digital Simulations for Financial Portfolio Optimization

Ruizhe Shen, Zichang Hao, Ching Hua Lee.
Journal article | 2026 | Entropy | vol. 28 | no. 8 | pp. 916.
Identifier and resource: [10.3390/e28080916](https://doi.org/10.3390/e28080916).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe28080916); retrieved 2026-10-08.

#### Q0642 Benchmarking optimization algorithms for automated calibration of quantum devices

Kevin Pack, Shai Machnes, Frank K Wilhelm.
Journal article | 2026 | New Journal of Physics | vol. 28 | no. 5 | pp. 054510.
Identifier and resource: [10.1088/1367-2630/ae6c54](https://doi.org/10.1088/1367-2630/ae6c54).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fae6c54); retrieved 2026-10-08.

#### Q0643 Benchmarking quantum heuristics: Nonvariational quantum-walk-based optimization algorithm for the weighted MaxCut problem

Tavis Bennett, Aidan Smith, Edric Matwiejew, Jingbo B. Wang.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032603.
Identifier and resource: [10.1103/sdlc-wl67](https://doi.org/10.1103/sdlc-wl67).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fsdlc-wl67); retrieved 2026-10-08.

#### Q0644 Parameter Analysis and Optimization of Layer Fidelity for Quantum Processor Benchmarking at Scale

Maria Jose Lozano Palacio, Hasan Nayfeh, Matthew Ware, David C. McKay.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 1-10.
Identifier and resource: [10.1109/tqe.2026.3668098](https://doi.org/10.1109/tqe.2026.3668098).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3668098); retrieved 2026-10-08.

#### Q0645 QOPTec: a modular platform for benchmarking quantum algorithms through combinatorial optimization problems

Pablo Miranda-Rodríguez, Eneko Osaba.
Journal article | 2026 | SoftwareX | vol. 33 | pp. 102507 | article 102507.
Identifier and resource: [10.1016/j.softx.2026.102507](https://doi.org/10.1016/j.softx.2026.102507).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.softx.2026.102507); retrieved 2026-10-08.

#### Q0646 Quantum Algorithms for Financial Optimization: Benchmarking QAOA, VQE, and Classical Portfolio Techniques

Subodh Nath Pushpak, Sarika Jain, Siddharth Kalra.
Conference paper | 2026 | 2026 5th International Conference on Innovative Practices in Technology and Management (ICIPTM) | pp. 1-5.
Identifier and resource: [10.1109/iciptm69057.2026.11465578](https://doi.org/10.1109/iciptm69057.2026.11465578).
Conference metadata: 2026 5th International Conference on Innovative Practices in Technology and Management (ICIPTM).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficiptm69057.2026.11465578); retrieved 2026-10-08.

#### Q0647 The Quantum Optimization Benchmarking Library

Thorsten Koch, David E. Bernal Neira, Ying Chen, Giorgio Cortiana, Daniel J. Egger, Raoul Heese, Narendra N. Hegade, Alejandro Gomez Cadavid et al..
Journal article | 2026 | Nature Computational Science | vol. 6 | no. 6 | pp. 653-671.
Identifier and resource: [10.1038/s43588-026-00991-1](https://doi.org/10.1038/s43588-026-00991-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs43588-026-00991-1); retrieved 2026-10-08.

#### Q0648 Benchmarking Adaptive Genetic Pulse-Level Optimization on Standard Quantum Algorithms

William Aguilar-Calvo, Santiago Núñez-Corrales.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 260-263.
Identifier and resource: [10.1109/qce65121.2025.10330](https://doi.org/10.1109/qce65121.2025.10330).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10330); retrieved 2026-10-08.

#### Q0649 Benchmarking quantum optimization for the maximum-cut problem on a superconducting quantum computer

Maxime Dupont, Bhuvanesh Sundar, Bram Evert, David E. Bernal Neira, Zedong Peng, Stephen Jeffrey, Mark J. Hodson.
Journal article | 2025 | Physical Review Applied | vol. 23 | no. 1 | article 014045.
Identifier and resource: [10.1103/physrevapplied.23.014045](https://doi.org/10.1103/physrevapplied.23.014045).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.23.014045); retrieved 2026-10-08.

## D12 Superconducting qubit hardware

Superconducting circuits combine microwave control, cryogenics, fabrication, and readout. Device coherence and gate fidelity must be distinguished from logical error performance.

Prerequisites: Microwave circuits, cryogenics, and solid state physics.

Assessment focus: Coherence, leakage, crosstalk, fabrication variation, and system wiring.

Primary catalog resources in this category: 59.

### D12T01 Transmon and circuit QED

Transmons reduce charge sensitivity through circuit design and couple to microwave resonators. Coherence, anharmonicity, coupling, and control tradeoffs shape performance.

Fine subcategories: Josephson junctions; anharmonicity; dispersive coupling; charge noise; resonators.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0650 Circuit quantum electrodynamics

Alexandre Blais, Arne L. Grimsmo, S. M. Girvin, Andreas Wallraff.
Journal article | 2021 | Reviews of Modern Physics | vol. 93 | no. 2 | article 025005.
Identifier and resource: [10.1103/revmodphys.93.025005](https://doi.org/10.1103/revmodphys.93.025005).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FRevModPhys.93.025005); retrieved 2026-10-08.

#### Q0651 From Macroscopic Quantum Tunneling to Circuit QED: Coherence and Dissipation in 3D Transmon Qubits

Gustavo Moreto, Diego Molina, Saulo Gabriel Alberton, Denys Derlian Carvalho Brito, Ednilson dos Santos Lopes da Cunha, Arthur Rebello, Daniel GONÇALVES BENVENUTTI, Agatha Sandes Dutra et al..
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-9657238/v1](https://doi.org/10.21203/rs.3.rs-9657238/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-9657238%2Fv1); retrieved 2026-10-08.

#### Q0652 Electromagnetically induced acoustic transparency using a superconducting transmon circuit

Abdul Wahab, Muqaddar Abbas, Xiaosen Yang, Yuanping Chen.
Journal article | 2024 | The European Physical Journal Plus | vol. 139 | no. 4 | article 318.
Identifier and resource: [10.1140/epjp/s13360-024-05069-3](https://doi.org/10.1140/epjp/s13360-024-05069-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjp%2Fs13360-024-05069-3); retrieved 2026-10-08.

#### Q0653 Electromagnetically induced acoustic transparency amplifier using a superconducting transmon circuit

Syeda Aliya Batool, Rahmatullah, Sajid Qamar.
Journal article | 2023 | Physica Scripta | vol. 98 | no. 2 | pp. 025105.
Identifier and resource: [10.1088/1402-4896/acb32f](https://doi.org/10.1088/1402-4896/acb32f).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Facb32f); retrieved 2026-10-08.

#### Q0654 Design and Performance Analysis of Hexagonal Transmon Qubit in a Superconducting Circuit

Seong Hyeon Park, Jeseok Bang, Soobin An, Seungyong Hahn.
Journal article | 2021 | IEEE Transactions on Applied Superconductivity | vol. 31 | no. 5 | pp. 1-5.
Identifier and resource: [10.1109/tasc.2021.3070469](https://doi.org/10.1109/tasc.2021.3070469).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftasc.2021.3070469); retrieved 2026-10-08.

#### Q0655 N Two-Transmon-Qubit Quantum Logic Gates Realized in a Circuit QED System

T., A., M. Said, Chouikh, Benna.
Journal article | 2019 | Applied Mathematics & Information Sciences | vol. 13 | no. 5 | pp. 839-846.
Identifier and resource: [10.18576/amis/130518](https://doi.org/10.18576/amis/130518).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.18576%2Famis%2F130518); retrieved 2026-10-08.

#### Q0656 Transferring arbitrary d-dimensional quantum states of a superconducting transmon qudit in circuit QED

Tong Liu, Qi-Ping Su, Jin-Hu Yang, Yu Zhang, Shao-Jie Xiong, Jin-Ming Liu, Chui-Ping Yang.
Journal article | 2017 | Scientific Reports | vol. 7 | no. 1 | article 7039.
Identifier and resource: [10.1038/s41598-017-07225-5](https://doi.org/10.1038/s41598-017-07225-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-017-07225-5); retrieved 2026-10-08.

### D12T02 Flux and fluxonium qubits

Flux based circuits use magnetic flux and specialized inductive elements to define qubit transitions. Sweet spots and device parameters affect both noise and control.

Fine subcategories: Flux bias; superinductors; sweet spots; tunneling; circuit design.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0657 Exploration of Quantum Control Landscapes for Single-qubit Gate Generation in Few-Level Fluxonium Approximations

I. M. Korolev, A. N. Pechen.
Journal article | 2026 | Lobachevskii Journal of Mathematics | vol. 47 | no. 6 | pp. 2541-2549.
Identifier and resource: [10.1134/s1995080226619612](https://doi.org/10.1134/s1995080226619612).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1995080226619612); retrieved 2026-10-08.

#### Q0658 Fluxonium as a Control Qubit for Bosonic Quantum Information

Ke Nie, J. Nofear Bradford, Supriya Mandal, Aayam Bista, Wolfgang Pfaff, Angela Kou.
Journal article | 2026 | PRX Quantum | vol. 7 | no. 1 | article 010357.
Identifier and resource: [10.1103/dgwk-w3jj](https://doi.org/10.1103/dgwk-w3jj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fdgwk-w3jj); retrieved 2026-10-08.

#### Q0659 Fluxonium qubit-based hybrid electromechanical system

Roson Nongthombam, Anshika Ranjan, Amarendra K. Sarma, Vibhor Singh.
Journal article | 2026 | Physical Review A | vol. 113 | no. 6 | article 063707.
Identifier and resource: [10.1103/mhnl-b2wp](https://doi.org/10.1103/mhnl-b2wp).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fmhnl-b2wp); retrieved 2026-10-08.

#### Q0660 Measurement-induced state transitions across the fluxonium qubit landscape

Anonymous.
Journal article | 2026 | Physical Review Applied.
Identifier and resource: [10.1103/n2qr-9p7z](https://doi.org/10.1103/n2qr-9p7z).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fn2qr-9p7z); retrieved 2026-10-08.

#### Q0661 Optimization of high-fidelity single-qubit gates for fluxonium qubits using single-flux quantum control

Maxime Lapointe-Major, Boyan Torosov, Bohdan Kulchytskyy, Pooya Ronagh.
Journal article | 2026 | Physical Review Applied | vol. 26 | no. 1 | article 014048.
Identifier and resource: [10.1103/dz26-n1jc](https://doi.org/10.1103/dz26-n1jc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fdz26-n1jc); retrieved 2026-10-08.

#### Q0662 Readout-induced leakage of the fluxonium qubit

Aayam Bista, Matthew Thibodeau, Ke Nie, Kaicheung Chow, Bryan K. Clark, Angela Kou.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 3 | article 034058.
Identifier and resource: [10.1103/wjdb-4814](https://doi.org/10.1103/wjdb-4814).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fwjdb-4814); retrieved 2026-10-08.

#### Q0663 Scalable fluxonium-qubit architecture with tunable interactions between noncomputational levels

Peng Zhao, Guming Zhao, Shaowei Li, Chen Zha, Ming Gong.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 4 | article 044072.
Identifier and resource: [10.1103/mfjl-5rk6](https://doi.org/10.1103/mfjl-5rk6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fmfjl-5rk6); retrieved 2026-10-08.

#### Q0664 Cross-resonance control of an oscillator with an auxiliary fluxonium qubit

Guo Zheng, Simon Lieu, Emma L. Rosenfeld, Kyungjoo Noh, Connor T. Hann.
Journal article | 2025 | Physical Review Applied | vol. 23 | no. 2 | article 024067.
Identifier and resource: [10.1103/physrevapplied.23.024067](https://doi.org/10.1103/physrevapplied.23.024067).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.23.024067); retrieved 2026-10-08.

#### Q0665 Flux-trapping fluxonium qubit

Kotaro Hida, Kohei Matsuura, Shu Watanabe, Yasunobu Nakamura.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 6 | article 064069.
Identifier and resource: [10.1103/b99c-y22b](https://doi.org/10.1103/b99c-y22b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fb99c-y22b); retrieved 2026-10-08.

#### Q0666 Niobium-buffered tantalum for a superconducting fluxonium qubit

Zi shuo Li, Ting ting Guo, Wen qu Xu, Li li Shi, Kai xuan Zhang, Quan Zuo, Tian shi Zhou, Guo zhu Sun et al..
Journal article | 2025 | Materials Research Express | vol. 12 | no. 2 | pp. 026001.
Identifier and resource: [10.1088/2053-1591/adb091](https://doi.org/10.1088/2053-1591/adb091).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2053-1591%2Fadb091); retrieved 2026-10-08.

#### Q0667 Numerical Analysis of Quantum Control Landscapes for Single-Qubit Gate Generation in Three-Level Fluxonium Systems

I. M. Korolev, A. N. Pechen.
Journal article | 2025 | Lobachevskii Journal of Mathematics | vol. 46 | no. 6 | pp. 2581-2590.
Identifier and resource: [10.1134/s1995080225607830](https://doi.org/10.1134/s1995080225607830).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1995080225607830); retrieved 2026-10-08.

#### Q0668 Subharmonic Control of a Fluxonium Qubit via a Purcell-Protected Flux Line

J. Schirk, F. Wallner, L. Huang, I. Tsitsilin, N. Bruckmoser, L. Koch, D. Bunch, N.J. Glaser et al..
Journal article | 2025 | PRX Quantum | vol. 6 | no. 3 | article 030315.
Identifier and resource: [10.1103/yx15-jyl7](https://doi.org/10.1103/yx15-jyl7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fyx15-jyl7); retrieved 2026-10-08.

#### Q0669 Flux-pulse-assisted readout of a fluxonium qubit

Taryn V. Stefanski, Christian Kraglund Andersen.
Journal article | 2024 | Physical Review Applied | vol. 22 | no. 1 | article 014079.
Identifier and resource: [10.1103/physrevapplied.22.014079](https://doi.org/10.1103/physrevapplied.22.014079).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.22.014079); retrieved 2026-10-08.

#### Q0670 Fluxonium-based superconducting qubit magnetometer: Optimization of phase estimation algorithms

Vladimir Slepnev, Azat Gubaydullin, Valerii Vinokur.
Journal article | 2024 | Physical Review B | vol. 110 | no. 21 | article 214423.
Identifier and resource: [10.1103/physrevb.110.214423](https://doi.org/10.1103/physrevb.110.214423).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.110.214423); retrieved 2026-10-08.

#### Q0671 Integer Fluxonium Qubit

Raymond A. Mencia, Wei-Ju Lin, Hyunheung Cho, Maxim G. Vavilov, Vladimir E. Manucharyan.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 4 | article 040318.
Identifier and resource: [10.1103/prxquantum.5.040318](https://doi.org/10.1103/prxquantum.5.040318).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.040318); retrieved 2026-10-08.

#### Q0672 Using Bifluxon Tunneling to Protect the Fluxonium Qubit

Waël Ardati, Sébastien Léger, Shelender Kumar, Vishnu Narayanan Suresh, Dorian Nicolas, Cyril Mori, Francesca D’Esposito, Tereza Vakhtel et al..
Journal article | 2024 | Physical Review X | vol. 14 | no. 4 | article 041014.
Identifier and resource: [10.1103/physrevx.14.041014](https://doi.org/10.1103/physrevx.14.041014).
Fine tags: tunneling.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.14.041014); retrieved 2026-10-08.

### D12T03 Superconducting gates and couplers

Couplers and entangling gates control interactions between superconducting qubits. Gate error, residual coupling, leakage, and spectator effects require joint calibration.

Fine subcategories: Cross resonance; controlled phase; parametric gates; tunable coupling; leakage.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q0673 Crosstalk-robust superconducting two-qubit geometric gates using tunable couplers

Bo-Xun Deng, Jia-Qi Hu, Cheng-Yun Ding, Zheng-Yuan Xue, Tao Chen.
Journal article | 2026 | Frontiers of Physics | vol. 21 | no. 10 | pp. 103205.
Identifier and resource: [10.15302/frontphys.2026.103205](https://doi.org/10.15302/frontphys.2026.103205).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15302%2Ffrontphys.2026.103205); retrieved 2026-10-08.

#### Q0674 Inherent flux crosstalk and coupler-driven single-qubit gates in superconducting circuits

Anonymous.
Journal article | 2026 | Physical Review Applied.
Identifier and resource: [10.1103/q2j3-mftf](https://doi.org/10.1103/q2j3-mftf).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fq2j3-mftf); retrieved 2026-10-08.

#### Q0675 Direct Implementation of High-Fidelity Three-Qubit Gates for Superconducting Processor with Tunable Couplers

Hao-Tian Liu, Bing-Jie Chen, Jia-Chi Zhang, Yong-Xi Xiao, Tian-Ming Li, Kaixuan Huang, Ziting Wang, Hao Li et al..
Journal article | 2025 | Physical Review Letters | vol. 135 | no. 5 | article 050602.
Identifier and resource: [10.1103/lvb9-pfr3](https://doi.org/10.1103/lvb9-pfr3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Flvb9-pfr3); retrieved 2026-10-08.

#### Q0676 High-precision pulse calibration of tunable couplers for high-fidelity two-qubit gates in superconducting quantum processors

Tian-Ming Li, Jia-Chi Zhang, Bing-Jie Chen, Kaixuan Huang, Hao-Tian Liu, Yong-Xi Xiao, Cheng-Lin Deng, Gui-Han Liang et al..
Journal article | 2025 | Physical Review Applied | vol. 23 | no. 2 | article 024059.
Identifier and resource: [10.1103/physrevapplied.23.024059](https://doi.org/10.1103/physrevapplied.23.024059).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.23.024059); retrieved 2026-10-08.

#### Q0677 Simulation Framework and Optimization of Superconducting Transmon-Tunable Coupler-Transmon System for Qudit Gates

Ferris Prima Nugraha, Yuhan Huang, Jiacheng Liu, Qiming Shao.
Conference paper | 2025 | 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD) | pp. 1-8.
Identifier and resource: [10.1109/iccad66269.2025.11240859](https://doi.org/10.1109/iccad66269.2025.11240859).
Conference metadata: 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcad66269.2025.11240859); retrieved 2026-10-08.

#### Q0678 Three-mode tunable coupler for superconducting two-qubit gates

Elena Yu. Egorova, Alena S. Kazmina, Ilya A. Simakov, Ilya N. Moskalenko, Nikolay N. Abramov, Daria A. Kalacheva, Viktor B. Lubsanov, Alexey N. Bolgar et al..
Journal article | 2025 | Physical Review Applied | vol. 23 | no. 6 | article 064056.
Identifier and resource: [10.1103/2h4m-mg2p](https://doi.org/10.1103/2h4m-mg2p).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F2h4m-mg2p); retrieved 2026-10-08.

#### Q0679 Controlled-Controlled-Phase Gates for Superconducting Qubits Mediated by a Shared Tunable Coupler

Niklas J. Glaser, Federico Roy, Stefan Filipp.
Journal article | 2023 | Physical Review Applied | vol. 19 | no. 4 | article 044001.
Identifier and resource: [10.1103/physrevapplied.19.044001](https://doi.org/10.1103/physrevapplied.19.044001).
Fine tags: controlled phase.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.19.044001); retrieved 2026-10-08.

#### Q0680 Realization of High-Fidelity Controlled-Phase Gates in Extensible Superconducting Qubits Design with a Tunable Coupler

Yangsen Ye, Sirui Cao, Yulin Wu, Xiawei Chen, Qingling Zhu, Shaowei Li, Fusheng Chen, Ming Gong et al..
Journal article | 2021 | Chinese Physics Letters | vol. 38 | no. 10 | pp. 100301.
Identifier and resource: [10.1088/0256-307x/38/10/100301](https://doi.org/10.1088/0256-307x/38/10/100301).
Fine tags: controlled phase.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F0256-307x%2F38%2F10%2F100301); retrieved 2026-10-08.

#### Q0681 Realization of adiabatic and diabatic CZ gates in superconducting qubits coupled with a tunable coupler*

Huikai Xu, Weiyang Liu, Zhiyuan Li, Jiaxiu Han, Jingning Zhang, Kehuan Linghu, Yongchao Li, Mo Chen et al..
Journal article | 2021 | Chinese Physics B | vol. 30 | no. 4 | pp. 044212.
Identifier and resource: [10.1088/1674-1056/abf03a](https://doi.org/10.1088/1674-1056/abf03a).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fabf03a); retrieved 2026-10-08.

### D12T04 Superconducting readout

Dispersive readout infers a qubit state from a coupled resonator response. Measurement speed, fidelity, backaction, and multiplexing compete.

Fine subcategories: Dispersive measurement; Purcell filters; parametric amplifiers; multiplexing; assignment errors.

Primary resources: 14. Additional related assignments can be found in the interactive HTML.

#### Q0682 A Survey of Microwave-Implemented Superconducting Qubit Control and Readout Circuits

Naheel Raza Rizvi, Meraj Ahmad, Arslan Shafique, Hadi Heidari, Martin Weides, Muhammad Ali Imran, Atif Raza Jafri.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 1-52.
Identifier and resource: [10.1109/tqe.2026.3659400](https://doi.org/10.1109/tqe.2026.3659400).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3659400); retrieved 2026-10-08.

#### Q0683 Millimeter wave readout of a superconducting qubit

Anonymous.
Journal article | 2026 | Physical Review Letters.
Identifier and resource: [10.1103/c84y-ggqs](https://doi.org/10.1103/c84y-ggqs).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fc84y-ggqs); retrieved 2026-10-08.

#### Q0684 Pound-Drever-Hall Method for Superconducting-Qubit Readout

Ibukunoluwa Adisa, Won Chan Lee, Kevin C. Cox, Alicia J. Kollár.
Journal article | 2026 | Physical Review Letters | vol. 136 | no. 23 | article 233601.
Identifier and resource: [10.1103/ng1d-6gb8](https://doi.org/10.1103/ng1d-6gb8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fng1d-6gb8); retrieved 2026-10-08.

#### Q0685 Superconducting-qubit readout using next-generation reservoir computing

Robert Kent, Benjamin Lienhard, Gregory Lafyatis, Daniel J. Gauthier.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 4 | article 044009.
Identifier and resource: [10.1103/bnwn-d2p4](https://doi.org/10.1103/bnwn-d2p4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fbnwn-d2p4); retrieved 2026-10-08.

#### Q0686 A Survey of Microwave-Implemented Superconducting Qubit Control and Readout Circuits

Naheel Raza Rizvi, Meraj Ahmad, Arslan Shafique, Hadi Heidari, Martin Weides, Muhammad Ali Imran, Atif Raza Jafri.
Posted content | 2025 | Institute of Electrical and Electronics Engineers (IEEE).
Identifier and resource: [10.36227/techrxiv.175624606.62662608/v1](https://doi.org/10.36227/techrxiv.175624606.62662608/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.36227%2Ftechrxiv.175624606.62662608%2Fv1); retrieved 2026-10-08.

#### Q0687 All-optical superconducting qubit readout

Georg Arnold, Thomas Werner, Rishabh Sahu, Lucky N. Kapoor, Liu Qiu, Johannes M. Fink.
Journal article | 2025 | Nature Physics | vol. 21 | no. 3 | pp. 393-400.
Identifier and resource: [10.1038/s41567-024-02741-4](https://doi.org/10.1038/s41567-024-02741-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-024-02741-4); retrieved 2026-10-08.

#### Q0688 Balanced Cross-Kerr Coupling for Superconducting Qubit Readout

Alex A. Chapple, Othmane Benhayoune-Khadraoui, Simon Richer, Alexandre Blais.
Journal article | 2025 | Physical Review Letters | vol. 135 | no. 25 | article 256002.
Identifier and resource: [10.1103/r4v5-wyyt](https://doi.org/10.1103/r4v5-wyyt).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fr4v5-wyyt); retrieved 2026-10-08.

#### Q0689 Benchmarking the Readout of a Superconducting Qubit for Repeated Measurements

S. Hazra, W. Dai, T. Connolly, P. D. Kurilovich, Z. Wang, L. Frunzio, M. H. Devoret.
Journal article | 2025 | Physical Review Letters | vol. 134 | no. 10 | article 100601.
Identifier and resource: [10.1103/physrevlett.134.100601](https://doi.org/10.1103/physrevlett.134.100601).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.134.100601); retrieved 2026-10-08.

#### Q0690 Efficient and Scalable Architectures for Multi-level Superconducting Qubit Readout

Chaithanya Naik Mude, Satvik Maurya, Benjamin Lienhard, Swamit Tannu.
Conference paper | 2025 | 2025 62nd ACM/IEEE Design Automation Conference (DAC) | pp. 1-7.
Identifier and resource: [10.1109/dac63849.2025.11133314](https://doi.org/10.1109/dac63849.2025.11133314).
Conference metadata: 2025 62nd ACM/IEEE Design Automation Conference (DAC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fdac63849.2025.11133314); retrieved 2026-10-08.

#### Q0691 Josephson Junction-Based Compact Notch Purcell Filters for Superconducting Qubit Readout

Simona Zaccaria, Antonio Gnudi.
Journal article | 2025 | IEEE Transactions on Applied Superconductivity | vol. 35 | no. 8 | pp. 1-7.
Identifier and resource: [10.1109/tasc.2025.3610252](https://doi.org/10.1109/tasc.2025.3610252).
Fine tags: Purcell filters.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftasc.2025.3610252); retrieved 2026-10-08.

#### Q0692 Multiphysics Numerical Methods for Designing Multiplexed Superconducting Qubit Readout Chains

Samuel T. Elkin, Michael Haider, Thomas E. Roth.
Conference paper | 2025 | 2025 International Applied Computational Electromagnetics Society Symposium (ACES) | pp. 1-2.
Identifier and resource: [10.23919/aces66556.2025.11052488](https://doi.org/10.23919/aces66556.2025.11052488).
Conference metadata: 2025 International Applied Computational Electromagnetics Society Symposium (ACES).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Faces66556.2025.11052488); retrieved 2026-10-08.

#### Q0693 Optical readout of a superconducting qubit using a piezo-optomechanical transducer

T. C. van Thiel, M. J. Weaver, F. Berto, P. Duivestein, M. Lemang, K. L. Schuurman, M. Žemlička, F. Hijazi et al..
Journal article | 2025 | Nature Physics | vol. 21 | no. 3 | pp. 401-405.
Identifier and resource: [10.1038/s41567-024-02742-3](https://doi.org/10.1038/s41567-024-02742-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-024-02742-3); retrieved 2026-10-08.

#### Q0694 Superconducting Parametric Amplifiers: Resonator Design and Role in Qubit Readout

Babak Mohammadian.
Book chapter | 2025 | Perspectives on Quantum Technologies - Modeling, Simulation, and Implementation.
Identifier and resource: [10.5772/intechopen.1013108](https://doi.org/10.5772/intechopen.1013108).
Fine tags: parametric amplifiers.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5772%2Fintechopen.1013108); retrieved 2026-10-08.

#### Q0695 Superconducting Qubit: Readout and Initialization

Hiu Yung Wong.
Book chapter | 2025 | Quantum Computing Architecture and Hardware for Engineers | pp. 309-324.
Identifier and resource: [10.1007/978-3-031-78219-0_22](https://doi.org/10.1007/978-3-031-78219-0_22).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-78219-0_22); retrieved 2026-10-08.

### D12T05 Cryogenic circuits and packaging

Cryogenic packaging delivers signals while removing heat and controlling electromagnetic environments. System scaling includes wiring, thermal budgets, and electronics placement.

Fine subcategories: Dilution refrigeration; microwave wiring; interposers; thermal budgets; cryogenic electronics.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0696 Cryogenic microwave frequency combs based on quantum paraelectric superconducting resonators

Prasad Muragesh, Harikrishnan Sundaresan, Madhu Thalakulam.
Journal article | 2026 | Applied Physics Letters | vol. 129 | no. 7 | article 072601.
Identifier and resource: [10.1063/5.0349286](https://doi.org/10.1063/5.0349286).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0349286); retrieved 2026-10-08.

#### Q0697 2.5D Cryogenic Packaging for Advanced Quantum Processors

Norhanani Binte Jaafar, Li Hongyu, Ya-Ching Tseng, Yong Chyn Ng, Daniel Lau.
Conference paper | 2025 | 2025 IEEE 27th Electronics Packaging Technology Conference (EPTC) | pp. 1-6.
Identifier and resource: [10.1109/eptc67330.2025.11392196](https://doi.org/10.1109/eptc67330.2025.11392196).
Conference metadata: 2025 IEEE 27th Electronics Packaging Technology Conference (EPTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Feptc67330.2025.11392196); retrieved 2026-10-08.

#### Q0698 Cryogenic microwave link for quantum local area networks

W. K. Yam, M. Renger, S. Gandorfer, F. Fesquet, M. Handschuh, K. E. Honasoge, F. Kronowetter, Y. Nojiri et al..
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 87.
Identifier and resource: [10.1038/s41534-025-01046-5](https://doi.org/10.1038/s41534-025-01046-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01046-5); retrieved 2026-10-08.

#### Q0699 A cryogenic on-chip microwave pulse generator for large-scale superconducting quantum computing

Zenghui Bao, Yan Li, Zhiling Wang, Jiahui Wang, Jize Yang, Haonan Xiong, Yipu Song, Yukai Wu et al..
Journal article | 2024 | Nature Communications | vol. 15 | no. 1 | article 5958.
Identifier and resource: [10.1038/s41467-024-50333-w](https://doi.org/10.1038/s41467-024-50333-w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-024-50333-w); retrieved 2026-10-08.

#### Q0700 Cryogenic DC and Microwave Characterization and Modeling of 40-nm CMOS for Quantum Computing Applications

Mahesh Kumar Chaubey, Yeke Liu, Po-Chang Wu, Hann-Huei Tsai, Shawn S.H. Hsu.
Conference paper | 2024 | 2024 IEEE Asia-Pacific Microwave Conference (APMC) | pp. 1311-1313.
Identifier and resource: [10.1109/apmc60911.2024.10867529](https://doi.org/10.1109/apmc60911.2024.10867529).
Conference metadata: 2024 Asia-Pacific Microwave Conference (APMC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fapmc60911.2024.10867529); retrieved 2026-10-08.

#### Q0701 Cryogenic bridging via propagating microwave quantum teleportation

Vahid Salari, Nasser Gohari Kamel, Farhad Rasekh, Roohollah Ghobadi, Jordan Smith, Daniel Oblak.
Journal article | 2024 | AVS Quantum Science | vol. 6 | no. 4 | article 042001.
Identifier and resource: [10.1116/5.0208451](https://doi.org/10.1116/5.0208451).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1116%2F5.0208451); retrieved 2026-10-08.

#### Q0702 Cryogenic packaging for scalable hybrid quantum PICs

Robert Bernson, Alexander Witte, Genevieve Clark, Kamil Gradkowski, Matthew Saha, Andrew Leenheer, Kevin Chen, Gerald Gilbert et al..
Conference paper | 2024 | Frontiers in Optics + Laser Science 2024 (FiO, LS) | pp. FTh1D.2.
Identifier and resource: [10.1364/fio.2024.fth1d.2](https://doi.org/10.1364/fio.2024.fth1d.2).
Conference metadata: Frontiers in Optics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ffio.2024.fth1d.2); retrieved 2026-10-08.

#### Q0703 High performance cryogenic packaging for microwave applications of high temperature superconductors

R.B. Greed, R.F. Jeffries, D.C. Voyce, A.J. Barkway, R.G. Humphreys, S.W. Goodyear.
Journal article | 2001 | IEEE Transactions on Appiled Superconductivity | vol. 11 | no. 1 | pp. 493-496.
Identifier and resource: [10.1109/77.919390](https://doi.org/10.1109/77.919390).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2F77.919390); retrieved 2026-10-08.

### D12T06 Superconducting fabrication and loss

Fabrication and materials affect loss, disorder, yield, and device uniformity. A scalable process must control interfaces as well as individual junction properties.

Fine subcategories: Surface loss; materials interfaces; junction yield; quasiparticles; process control.

Primary resources: 5. Additional related assignments can be found in the interactive HTML.

#### Q0704 Design, Fabrication and Characterization of a Superconducting Transmon Qubit Fabricated in Brazil

Diego Molina, Gustavo Moreto, Denys Derlian, Saulo Alberton, Ednilson Cunha, Francisco Rouxinol.
Conference paper | 2026 | 2026 40th Symposium on Microelectronics Technology and Devices (SBMicro) | pp. 1-4.
Identifier and resource: [10.1109/sbmicro70495.2026.11684417](https://doi.org/10.1109/sbmicro70495.2026.11684417).
Conference metadata: 2026 40th Symposium on Microelectronics Technology and Devices (SBMicro).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fsbmicro70495.2026.11684417); retrieved 2026-10-08.

#### Q0705 Scaffold-assisted window junctions for superconducting qubit fabrication

Chung-Ting Ke, Jun-Yi Tsai, Yen-Chun Chen, Zhen-Wei Xu, Elam Blackwell, Matthew A. Snyder, Spencer Weeden, Peng-Sheng Chen et al..
Journal article | 2026 | npj Quantum Information | vol. 12 | no. 1 | article 98.
Identifier and resource: [10.1038/s41534-026-01249-4](https://doi.org/10.1038/s41534-026-01249-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-026-01249-4); retrieved 2026-10-08.

#### Q0706 Materials Science Problems in the Fabrication of Superconducting Qubit Devices

Mingzhao Liu.
Conference paper | 2023 | 2023 IEEE Nanotechnology Materials and Devices Conference (NMDC) | pp. 832-832.
Identifier and resource: [10.1109/nmdc57951.2023.10343535](https://doi.org/10.1109/nmdc57951.2023.10343535).
Conference metadata: 2023 IEEE Nanotechnology Materials and Devices Conference (NMDC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fnmdc57951.2023.10343535); retrieved 2026-10-08.

#### Q0707 Fabrication of Low AC Loss Cu0.5Mn-Based NbTi Superconducting Strands

Qiang Guo, Ruilong Wang, Kailin Zhang, Yanmin Zhu, Jianfeng Li, Xianghong Liu, Yong Feng.
Journal article | 2021 | IEEE Transactions on Applied Superconductivity | vol. 31 | no. 8 | pp. 1-4.
Identifier and resource: [10.1109/tasc.2021.3107813](https://doi.org/10.1109/tasc.2021.3107813).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftasc.2021.3107813); retrieved 2026-10-08.

#### Q0708 Robust surface code topology against sparse fabrication defects in a superconducting-qubit array

Yong-Chao Tang, Guo-Xing Miao.
Journal article | 2016 | Physical Review A | vol. 93 | no. 3 | article 032322.
Identifier and resource: [10.1103/physreva.93.032322](https://doi.org/10.1103/physreva.93.032322).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.93.032322); retrieved 2026-10-08.

## D13 Trapped ion quantum computing

Ion processors use internal states coupled through collective motion. Scaling requires high quality gates, optical control, shuttling, and modular interconnects.

Prerequisites: Atomic physics, optics, and motional dynamics.

Assessment focus: Gate fidelity, mode management, optical stability, and transport cost.

Primary catalog resources in this category: 44.

### D13T01 Ion traps and architectures

Ion trap architectures confine and address charged atoms used as qubits. Trap geometry, motional modes, and modular organization affect scaling.

Fine subcategories: Paul traps; Penning traps; surface traps; ion chains; modular architectures.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q0709 Programmable quantum simulations of spin systems with trapped ions

C. Monroe, W. C. Campbell, L.-M. Duan, Z.-X. Gong, A. V. Gorshkov, P. W. Hess, R. Islam, K. Kim et al..
Journal article | 2021 | Reviews of Modern Physics | vol. 93 | no. 2 | article 025001.
Identifier and resource: [10.1103/revmodphys.93.025001](https://doi.org/10.1103/revmodphys.93.025001).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FRevModPhys.93.025001); retrieved 2026-10-08.

#### Q0710 Quantum computing architecture with trapped ion crystals and fast Rydberg gates

Han Bao, Jonas Vogel, Ulrich Poschinger, Ferdinand Schmidt-Kaler.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 2 | article 023035.
Identifier and resource: [10.1103/physrevresearch.7.023035](https://doi.org/10.1103/physrevresearch.7.023035).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.7.023035); retrieved 2026-10-08.

#### Q0711 Visible Photonic Component Development for Trapped-Ion Quantum Computing

Elliot Lehman, Molly Krogstad, Molly P. Andersen, Sara Campbell, Kirk Cook, Bryan DeBono, Christopher Ertsgaard, Azure Hansen et al..
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 518-519.
Identifier and resource: [10.1109/qce65121.2025.10424](https://doi.org/10.1109/qce65121.2025.10424).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10424); retrieved 2026-10-08.

#### Q0712 Scalable Architecture for Trapped-Ion Quantum Computing Using rf Traps and Dynamic Optical Potentials

David Schwerdt, Lee Peleg, Yotam Shapira, Nadav Priel, Yanay Florshaim, Avram Gross, Ayelet Zalic, Gadi Afek et al..
Journal article | 2024 | Physical Review X | vol. 14 | no. 4 | article 041017.
Identifier and resource: [10.1103/physrevx.14.041017](https://doi.org/10.1103/physrevx.14.041017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.14.041017); retrieved 2026-10-08.

#### Q0713 Multispecies Segmented Trapped Ion Architecture for Scalable Quantum Computing

M. Popov, N. Sterligov, O. Lakhmanskaya, K. Lakhmanskiy.
Conference paper | 2022 | Quantum 2.0 Conference and Exhibition | pp. QW3A.7.
Identifier and resource: [10.1364/quantum.2022.qw3a.7](https://doi.org/10.1364/quantum.2022.qw3a.7).
Conference metadata: Quantum 2.0.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fquantum.2022.qw3a.7); retrieved 2026-10-08.

#### Q0714 TILT: Achieving Higher Fidelity on a Trapped-Ion Linear-Tape Quantum Computing Architecture

Xin-Chuan Wu, Dripto M. Debroy, Yongshan Ding, Jonathan M. Baker, Yuri Alexeev, Kenneth R. Brown, Frederic T. Chong.
Conference paper | 2021 | 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA) | pp. 153-166.
Identifier and resource: [10.1109/hpca51647.2021.00023](https://doi.org/10.1109/hpca51647.2021.00023).
Conference metadata: 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fhpca51647.2021.00023); retrieved 2026-10-08.

#### Q0715 A Two-Dimensional Architecture for Fast Large-Scale Trapped-Ion Quantum Computing

Y.-K. Wu, L.-M. Duan.
Journal article | 2020 | Chinese Physics Letters | vol. 37 | no. 7 | pp. 070302.
Identifier and resource: [10.1088/0256-307x/37/7/070302](https://doi.org/10.1088/0256-307x/37/7/070302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F0256-307x%2F37%2F7%2F070302); retrieved 2026-10-08.

#### Q0716 Trapped Ion Architecture for Multi‐Dimensional Quantum Simulations

Ulrich Warring, Frederick Hakelberg, Philip Kiefer, Matthias Wittemer, Tobias Schaetz.
Journal article | 2020 | Advanced Quantum Technologies | vol. 3 | no. 11 | article 1900137.
Identifier and resource: [10.1002/qute.201900137](https://doi.org/10.1002/qute.201900137).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.201900137); retrieved 2026-10-08.

#### Q0717 Integrated optics architecture for trapped-ion quantum information processing

D. Kielpinski, C. Volin, E. W. Streed, F. Lenzini, M. Lobino.
Journal article | 2015 | Quantum Information Processing | vol. 15 | no. 12 | pp. 5315-5338.
Identifier and resource: [10.1007/s11128-015-1162-2](https://doi.org/10.1007/s11128-015-1162-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-015-1162-2); retrieved 2026-10-08.

### D13T02 Ion entangling gates

Entangling ion gates typically use shared motion or geometric phases. Mode crowding, heating, optical noise, and pulse design determine achievable fidelity.

Fine subcategories: Molmer Sorensen gates; geometric phase gates; motional modes; pulse shaping.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q0718 Analysis of the action of conventional trapped-ion entangling gates in qudit space

Pavel A. Kamenskikh, Nikita V. Semenin, Ilia V. Zalivako, Vasiliy N. Smirnov, Ilya A. Semerikov, Ksenia Yu. Khabarova, Nikolay N. Kolachevsky.
Journal article | 2026 | Physical Review A | vol. 114 | no. 1 | article 012458.
Identifier and resource: [10.1103/sxrf-1h7v](https://doi.org/10.1103/sxrf-1h7v).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fsxrf-1h7v); retrieved 2026-10-08.

#### Q0719 Computational optimization of two-qubit entangling gates in trapped-ion systems under system frequency drift

Woojun Lee, Chaewon Kim, Taeyoung Choi, Taehyun Kim.
Journal article | 2026 | Current Applied Physics | vol. 83 | pp. 28-37.
Identifier and resource: [10.1016/j.cap.2025.11.009](https://doi.org/10.1016/j.cap.2025.11.009).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.cap.2025.11.009); retrieved 2026-10-08.

#### Q0720 Efficient optical configurations for trapped-ion entangling gates

Aditya Milind Kolhatkar, Karan K. Mehta.
Journal article | 2026 | Physical Review A | vol. 113 | no. 4 | article 042424.
Identifier and resource: [10.1103/ly5s-tjk2](https://doi.org/10.1103/ly5s-tjk2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fly5s-tjk2); retrieved 2026-10-08.

#### Q0721 Radial fast entangling gates under micromotion in trapped-ion quantum computers

Phoebe Grosser, Monica Gutierrez Galan, Isabelle Savill-Brown, Alexander K. Ratcliffe, Haonan Liu, Varun D. Vaidya, Simon A. Haine, C. Ricardo Viteri et al..
Journal article | 2026 | Physical Review A | vol. 114 | no. 2 | article 022617.
Identifier and resource: [10.1103/zg69-17xc](https://doi.org/10.1103/zg69-17xc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fzg69-17xc); retrieved 2026-10-08.

#### Q0722 Amplitude-noise-resilient entangling gates for trapped ions

Nguyen H. Le, Modesto Orozco-Ruiz, Sahra A. Kulmiya, James G. Urquhart, Samuel J. Hile, Winfried K. Hensinger, Florian Mintert.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 5 | article 054060.
Identifier and resource: [10.1103/yrj7-tvw8](https://doi.org/10.1103/yrj7-tvw8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fyrj7-tvw8); retrieved 2026-10-08.

#### Q0723 Fast, Robust, and Laser-Free Universal Entangling Gates for Trapped-Ion Quantum Computing

Markus Nünnerich, Daniel Cohen, Patrick Barthel, Patrick H. Huber, Dorna Niroomand, Alex Retzker, Christof Wunderlich.
Journal article | 2025 | Physical Review X | vol. 15 | no. 2 | article 021079.
Identifier and resource: [10.1103/physrevx.15.021079](https://doi.org/10.1103/physrevx.15.021079).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.15.021079); retrieved 2026-10-08.

#### Q0724 Performance analysis for crosstalk errors between parallel entangling gates in trapped-ion quantum error correction

Fangxuan Liu, Gaoxiang Tang, Luming Duan, Yukai Wu.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 1 | article 014032.
Identifier and resource: [10.1103/c7w3-pxls](https://doi.org/10.1103/c7w3-pxls).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fc7w3-pxls); retrieved 2026-10-08.

#### Q0725 Power-optimized amplitude modulation for robust trapped-ion entangling gates: A study of gate-timing errors

Luke Ellert-Beck, Wenchao Ge.
Journal article | 2025 | Physical Review A | vol. 111 | no. 6 | article 062422.
Identifier and resource: [10.1103/physreva.111.062422](https://doi.org/10.1103/physreva.111.062422).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.062422); retrieved 2026-10-08.

#### Q0726 Transverse Polarization Gradient Entangling Gates for Trapped-Ion Quantum Computation

Jin-Ming Cui, Yan Chen, Yi-Fan Zhou, Quan Long, En-Teng An, Ran He, Yun-Feng Huang, Chuan-Feng Li et al..
Journal article | 2025 | Physical Review Letters | vol. 135 | no. 26 | article 260604.
Identifier and resource: [10.1103/w5l6-wmrl](https://doi.org/10.1103/w5l6-wmrl).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fw5l6-wmrl); retrieved 2026-10-08.

#### Q0727 Laser-free trapped ion entangling gates with AESE: adiabatic elimination of spin-motion entanglement

R Tyler Sutherland, Michael Foss-Feig.
Journal article | 2024 | New Journal of Physics | vol. 26 | no. 1 | pp. 013013.
Identifier and resource: [10.1088/1367-2630/ad19f9](https://doi.org/10.1088/1367-2630/ad19f9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fad19f9); retrieved 2026-10-08.

#### Q0728 Entangling gates for trapped-ion quantum computation and quantum simulation

Zhengyang Cai, Chun -Yang Luan, Lingfeng Ou, Hengchao Tu, Zihan Yin, Jing -Ning Zhang, Kihwan Kim.
Journal article | 2023 | Journal of the Korean Physical Society | vol. 82 | no. 9 | pp. 882-900.
Identifier and resource: [10.1007/s40042-023-00772-3](https://doi.org/10.1007/s40042-023-00772-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs40042-023-00772-3); retrieved 2026-10-08.

#### Q0729 Error mitigation on global entangling gates with trapped ions*

Zhengyang Cai, Pengfei Wang, Wentao Chen, Jialiang Zhang, Jing-Ning Zhang, Kihwan Kim.
Posted content | 2023 | Morressier.
Identifier and resource: [10.26226/m.646635e94d8a9d0012931f3e](https://doi.org/10.26226/m.646635e94d8a9d0012931f3e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.26226%2Fm.646635e94d8a9d0012931f3e); retrieved 2026-10-08.

#### Q0730 Pairwise‐Parallel Entangling Gates on Orthogonal Modes in a Trapped‐Ion Chain

Yingyue Zhu, Alaina M. Green, Nhung H. Nguyen, C. Huerta Alderete, Elijah Mossman, Norbert M. Linke.
Journal article | 2023 | Advanced Quantum Technologies | vol. 6 | no. 11 | article 2300056.
Identifier and resource: [10.1002/qute.202300056](https://doi.org/10.1002/qute.202300056).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202300056); retrieved 2026-10-08.

#### Q0731 Fast multi-qubit global-entangling gates without individual addressing of trapped ions

Kaizhao Wang, Jing-Fan Yu, Pengfei Wang, Chunyang Luan, Jing-Ning Zhang, Kihwan Kim.
Journal article | 2022 | Quantum Science and Technology | vol. 7 | no. 4 | pp. 044005.
Identifier and resource: [10.1088/2058-9565/ac84a3](https://doi.org/10.1088/2058-9565/ac84a3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fac84a3); retrieved 2026-10-08.

#### Q0732 Trapped-Ion Quantum Computer with Robust Entangling Gates and Quantum Coherent Feedback

Tom Manovitz, Yotam Shapira, Lior Gazit, Nitzan Akerman, Roee Ozeri.
Journal article | 2022 | PRX Quantum | vol. 3 | no. 1 | article 010347.
Identifier and resource: [10.1103/prxquantum.3.010347](https://doi.org/10.1103/prxquantum.3.010347).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.3.010347); retrieved 2026-10-08.

### D13T03 Ion transport and QCCD

QCCD architectures move ions between operation regions. Transport must preserve quantum information and manage motional excitation and cooling.

Fine subcategories: Junction transport; sympathetic cooling; motional excitation; trap scheduling.

Primary resources: 5. Additional related assignments can be found in the interactive HTML.

#### Q0733 Reinforcement learning for ion shuttling on trapped-ion quantum computers

Maximilian Schier, Lea Richtmann, Christian Staufenbiel, Tobias Schmale, Daniel Borcherding, Michèle Heurs, Bodo Rosenhahn.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033360.
Identifier and resource: [10.1103/b7ck-8wh4](https://doi.org/10.1103/b7ck-8wh4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fb7ck-8wh4); retrieved 2026-10-08.

#### Q0734 Robust Shuttling Compilation for Trapped-Ion Quantum Computers

Daniel Schoenberger, Robert Wille.
Conference paper | 2026 | 2026 IEEE International Conference on Quantum Software (QSW) | pp. 240-246.
Identifier and resource: [10.1109/qsw72780.2026.00036](https://doi.org/10.1109/qsw72780.2026.00036).
Conference metadata: 2026 IEEE International Conference on Quantum Software (QSW).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqsw72780.2026.00036); retrieved 2026-10-08.

#### Q0735 Shuttling for Scalable Trapped-Ion Quantum Computers

Daniel Schoenberger, Stefan Hillmich, Matthias Brandl, Robert Wille.
Journal article | 2025 | IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | vol. 44 | no. 6 | pp. 2144-2155.
Identifier and resource: [10.1109/tcad.2024.3513262](https://doi.org/10.1109/tcad.2024.3513262).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcad.2024.3513262); retrieved 2026-10-08.

#### Q0736 CHARGE SHUTTLING: CELL BALANCING FOR PARALLEL LI-ION PACKS

Manish Ramaswamy.
Journal article | 2024 | International Education and Research Journal | vol. 10 | no. 1.
Identifier and resource: [10.21276/ierj24376418103884](https://doi.org/10.21276/ierj24376418103884).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21276%2Fierj24376418103884); retrieved 2026-10-08.

#### Q0737 Shuttling-based trapped-ion quantum information processing

V. Kaushal, B. Lekitsch, A. Stahl, J. Hilder, D. Pijn, C. Schmiegelow, A. Bermudez, M. Müller et al..
Journal article | 2020 | AVS Quantum Science | vol. 2 | no. 1 | article 014101.
Identifier and resource: [10.1116/1.5126186](https://doi.org/10.1116/1.5126186).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1116%2F1.5126186); retrieved 2026-10-08.

### D13T04 Ion optical control and readout

Laser control and fluorescence readout link ion states to optical hardware. Addressing errors, stability, collection efficiency, and crosstalk matter.

Fine subcategories: Laser addressing; fluorescence; optical stability; crosstalk; state preparation.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0738 Monolithic ion trap integration of superconducting nanowire single-photon detectors and photonics for trapped-ion qubit state readout

Benedikt Hampel, Daniel H. Slichter, Dietrich Leibfried, Colin D. Bruzewicz, John Chiaverini, Ashton Hattori, Dave Kharas, Thomas Mahony et al..
Conference paper | 2026 | Quantum Computing, Communication, and Simulation VI | pp. 63.
Identifier and resource: [10.1117/12.3080210](https://doi.org/10.1117/12.3080210).
Conference metadata: Quantum Computing, Communication, and Simulation VI.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3080210); retrieved 2026-10-08.

#### Q0739 Towards site-resolved readout of ions using multimode fibre for scalable trapped ion quantum computing

Thomas Hinde, Emre Pasaogullari, Lorenzo Versini, Catherine E. J. Challoner, Tim F. Wohlers-Reichel, Arjun D. Rao, Mika A. Zalewski, Peter Drmota et al..
Conference paper | 2026 | Quantum Technologies 2026 | pp. 34.
Identifier and resource: [10.1117/12.3107916](https://doi.org/10.1117/12.3107916).
Conference metadata: Quantum Technologies 2026.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3107916); retrieved 2026-10-08.

#### Q0740 Control and readout of a 13-level trapped ion qudit

Pei Jiang Low, Brendan White, Crystal Senko.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 85.
Identifier and resource: [10.1038/s41534-025-01031-y](https://doi.org/10.1038/s41534-025-01031-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01031-y); retrieved 2026-10-08.

#### Q0741 Trap-integrated superconducting nanowire single-photon detectors for trapped-ion qubit state readout

Benedikt Hampel, Daniel H. Slichter, Dietrich G. Leibfried, Richard P. Mirin, Sae Woo Nam, Varun B. Verma.
Conference paper | 2024 | Advanced Photon Counting Techniques XVIII | pp. 8.
Identifier and resource: [10.1117/12.3014455](https://doi.org/10.1117/12.3014455).
Conference metadata: Advanced Photon Counting Techniques XVIII.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3014455); retrieved 2026-10-08.

#### Q0742 Fault-Tolerant Parity Readout on a Shuttling-Based Trapped-Ion Quantum Computer

J. Hilder, D. Pijn, O. Onishchenko, A. Stahl, M. Orth, B. Lekitsch, A. Rodriguez-Blanco, M. Müller et al..
Journal article | 2022 | Physical Review X | vol. 12 | no. 1 | article 011032.
Identifier and resource: [10.1103/physrevx.12.011032](https://doi.org/10.1103/physrevx.12.011032).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.12.011032); retrieved 2026-10-08.

#### Q0743 High-Fidelity Indirect Readout of Trapped-Ion Hyperfine Qubits

Stephen D. Erickson, Jenny J. Wu, Pan-Yu Hou, Daniel C. Cole, Shawn Geller, Alex Kwiatkowski, Scott Glancy, Emanuel Knill et al..
Journal article | 2022 | Physical Review Letters | vol. 128 | no. 16 | article 160503.
Identifier and resource: [10.1103/physrevlett.128.160503](https://doi.org/10.1103/physrevlett.128.160503).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.128.160503); retrieved 2026-10-08.

#### Q0744 State Readout of a Trapped Ion Qubit Using a Trap-Integrated Superconducting Photon Detector

S. L. Todaro, V. B. Verma, K. C. McCormick, D. T. C. Allcock, R. P. Mirin, D. J. Wineland, S. W. Nam, A. C. Wilson et al..
Journal article | 2021 | Physical Review Letters | vol. 126 | no. 1 | article 010501.
Identifier and resource: [10.1103/physrevlett.126.010501](https://doi.org/10.1103/physrevlett.126.010501).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.126.010501); retrieved 2026-10-08.

#### Q0745 Fast High-Fidelity Readout of a Single Trapped-Ion Qubit via Machine-Learning Methods

Zi-Han Ding, Jin-Ming Cui, Yun-Feng Huang, Chuan-Feng Li, Tao Tu, Guang-Can Guo.
Journal article | 2019 | Physical Review Applied | vol. 12 | no. 1 | article 014038.
Identifier and resource: [10.1103/physrevapplied.12.014038](https://doi.org/10.1103/physrevapplied.12.014038).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.12.014038); retrieved 2026-10-08.

### D13T05 Photonic links between ions

Photonic links generate entanglement between distant ion modules. Heralding rates, photon collection, indistinguishability, and memory lifetime constrain execution.

Fine subcategories: Remote entanglement; collection optics; heralding; frequency conversion; modular links.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0746 Individual trapped-ion addressing with adjoint-optimized multimode photonic circuits

Melika Momenzadeh, Ke Sun, Qiming Wu, Bingran You, Yu-Lung Tang, Hartmut Häffner, Maxim R. Shcherbakov.
Journal article | 2026 | npj Nanophotonics | vol. 3 | no. 1 | article 3.
Identifier and resource: [10.1038/s44310-025-00102-4](https://doi.org/10.1038/s44310-025-00102-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs44310-025-00102-4); retrieved 2026-10-08.

#### Q0747 Integrated photonic structures for photon-mediated entanglement of trapped ions

F. W. Knollmann, E. Clements, P. T. Callahan, M. Gehl, J. D. Hunker, T. Mahony, R. McConnell, R. Swint et al..
Journal article | 2024 | Optica Quantum | vol. 2 | no. 4 | pp. 230.
Identifier and resource: [10.1364/opticaq.522128](https://doi.org/10.1364/opticaq.522128).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fopticaq.522128); retrieved 2026-10-08.

#### Q0748 Utilizing integrated photonic technology for trapped-ion quantum computing

May Eun Yeon Kim.
Conference paper | 2024 | Quantum Computing, Communication, and Simulation IV | pp. 73.
Identifier and resource: [10.1117/12.3012126](https://doi.org/10.1117/12.3012126).
Conference metadata: Quantum Computing, Communication, and Simulation IV.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3012126); retrieved 2026-10-08.

#### Q0749 High-fidelity trapped-ion qubit operations with scalable photonic modulators

C. W. Hogle, D. Dominguez, M. Dong, A. Leenheer, H. J. McGuinness, B. P. Ruzic, M. Eichenfield, D. Stick.
Journal article | 2023 | npj Quantum Information | vol. 9 | no. 1 | article 74.
Identifier and resource: [10.1038/s41534-023-00737-1](https://doi.org/10.1038/s41534-023-00737-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-023-00737-1); retrieved 2026-10-08.

#### Q0750 High-fidelity trapped-ion qubit operations with scalable photonic modulators

Craig Hogle, Daniel Dominguez, Mark Dong, Andrew Leenheer, Hayden McGuinness, Brandon Ruzic, Matt Eichenfield, Daniel Stick.
Conference paper | 2023 | 54th Annual Meeting of the APS Division of Atomic, Molecular and Optical Physics (DAMOP) - Spokane, Washington, United States of America - June - 2023.
Identifier and resource: [10.2172/2431086](https://doi.org/10.2172/2431086).
Conference metadata: 54th Annual Meeting of the APS Division of Atomic, Molecular and Optical Physics (DAMOP) - Spokane, Washington, United States of America - June - 2023.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2431086); retrieved 2026-10-08.

#### Q0751 Routing single photons from a trapped ion with photonic integrated circuits

Uday Saha, James D. Siverns, John Hannegan, Mihika Prabhu, Eric Bersin, Saumil Bandyopadhyay, Jacques Carolan, Qudsia Quraishi et al..
Conference paper | 2022 | Conference on Lasers and Electro-Optics | pp. FTh5O.1.
Identifier and resource: [10.1364/cleo_qels.2022.fth5o.1](https://doi.org/10.1364/cleo_qels.2022.fth5o.1).
Conference metadata: CLEO: QELS_Fundamental Science.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_qels.2022.fth5o.1); retrieved 2026-10-08.

#### Q0752 CMOS Photonic Circuits for Trapped Ion Quantum Computing and Molecular Sensing

Rajeev J. Ram.
Conference paper | 2018 | Conference on Lasers and Electro-Optics | pp. STu3A.5.
Identifier and resource: [10.1364/cleo_si.2018.stu3a.5](https://doi.org/10.1364/cleo_si.2018.stu3a.5).
Conference metadata: CLEO: Science and Innovations.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_si.2018.stu3a.5); retrieved 2026-10-08.

## D14 Neutral atom and Rydberg processors

Neutral atom arrays offer reconfigurable geometries and interactions controlled by optical fields. Coherent gates, atom loss, rearrangement, and measurement determine computational reliability.

Prerequisites: Atomic physics, optical trapping, and interacting spin models.

Assessment focus: Atom loading, loss, gate error, geometry, and measurement backaction.

Primary catalog resources in this category: 38.

### D14T01 Optical tweezer arrays

Optical tweezers create reconfigurable arrays of individual atoms. Loading and rearrangement establish the geometry used by later simulation or gate operations.

Fine subcategories: Loading; rearrangement; trapping; addressing; geometry control.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0753 Hybrid Atom Tweezer Array of Nuclear Spin and Optical Clock Qubits

Yuma Nakamura.
Book chapter | 2026 | Springer Theses | pp. 95-119.
Identifier and resource: [10.1007/978-981-95-2836-3_6](https://doi.org/10.1007/978-981-95-2836-3_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-2836-3_6); retrieved 2026-10-08.

#### Q0754 Scalable Neutral-Atom Tweezer Arrays Based on TiO2 Holographic Metasurfaces

Zezheng Zhu, Yuan Xu, Aaron Holman, Jiahao Wu, Ximo Sun, Mingxuan Wang, Bojeong Seo, Sebastian Will et al..
Conference paper | 2026 | CLEO 2026 | pp. SM1K.2.
Identifier and resource: [10.1364/cleo_si.2026.sm1k.2](https://doi.org/10.1364/cleo_si.2026.sm1k.2).
Conference metadata: CLEO: Science and Innovations.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_si.2026.sm1k.2); retrieved 2026-10-08.

#### Q0755 Narrowline cooling of dysprosium atoms in an optical tweezer array

Giulio Biagioni, Britton Hofer, Nathan Bonvalet, Damien Bloch, Antoine Browaeys, Igor Ferrier-Barbut.
Journal article | 2025 | Physical Review A | vol. 112 | no. 1 | article 013316.
Identifier and resource: [10.1103/k4vn-y7mb](https://doi.org/10.1103/k4vn-y7mb).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fk4vn-y7mb); retrieved 2026-10-08.

#### Q0756 An optical tweezer array of ultracold polyatomic molecules

Nathaniel B. Vilas, Paige Robichaud, Christian Hallas, Grace K. Li, Loïc Anderegg, John M. Doyle.
Journal article | 2024 | Nature | vol. 628 | no. 8007 | pp. 282-286.
Identifier and resource: [10.1038/s41586-024-07199-1](https://doi.org/10.1038/s41586-024-07199-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-024-07199-1); retrieved 2026-10-08.

#### Q0757 Apparatus for producing single strontium atoms in an optical tweezer array

Kai 凯 Wen 文, Huijin 辉锦 Chen 陈, Xu 煦 Yan 颜, Zejian 泽剑 Ren 任, Chengdong 成东 He 何, Elnur Hajiyev, Preston Tsz 梓峰 Fung Wong 黄, Gyu-Boong Jo.
Journal article | 2024 | Chinese Physics B | vol. 33 | no. 12 | pp. 120703.
Identifier and resource: [10.1088/1674-1056/ad84d0](https://doi.org/10.1088/1674-1056/ad84d0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fad84d0); retrieved 2026-10-08.

#### Q0758 Erbium Atoms in an Optical Tweezer Array

David Ehrenstein.
Journal article | 2024 | Physics | vol. 17 | article s151.
Identifier and resource: [10.1103/physics.17.s151](https://doi.org/10.1103/physics.17.s151).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysics.17.s151); retrieved 2026-10-08.

#### Q0759 Hybrid Atom Tweezer Array of Nuclear Spin and Optical Clock Qubits

Yuma Nakamura, Toshi Kusano, Rei Yokoyama, Keito Saito, Koichiro Higashi, Naoya Ozawa, Tetsushi Takano, Yosuke Takasu et al..
Journal article | 2024 | Physical Review X | vol. 14 | no. 4 | article 041062.
Identifier and resource: [10.1103/physrevx.14.041062](https://doi.org/10.1103/physrevx.14.041062).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.14.041062); retrieved 2026-10-08.

#### Q0760 Optical setup for a two-dimensional tweezer array with independently adjustable columns for neutral atom quantum computing

Martin Adams, Martin Traub, Hans-Dieter Hoffmann, Florian Meinert, Philipp Ilzhöfer, Thomas Westphalen, Kersten Ludwig, Jiachen Zhao et al..
Conference paper | 2024 | Quantum Computing, Communication, and Simulation IV | pp. 45.
Identifier and resource: [10.1117/12.2692620](https://doi.org/10.1117/12.2692620).
Conference metadata: Quantum Computing, Communication, and Simulation IV.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2692620); retrieved 2026-10-08.

### D14T02 Rydberg blockade gates

Rydberg excitation enables strong interactions and blockade gates. Decay, motion, pulse control, and blockade imperfections determine gate error.

Fine subcategories: Blockade interactions; excitation errors; entangling gates; pulse design; decay.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0761 Floquet quantum gates with ion-enhanced Rydberg blockade

Anonymous.
Journal article | 2026 | Physical Review A.
Identifier and resource: [10.1103/247k-6zy1](https://doi.org/10.1103/247k-6zy1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F247k-6zy1); retrieved 2026-10-08.

#### Q0762 Multitarget Rydberg gates via spatial blockade engineering

Samuel Stein, Chenxu Liu, Shuwen Kan, Eleanor Crane, Yufei Ding, Ying Mao, Alexander Schuckert, Ang Li.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 1 | article 013254.
Identifier and resource: [10.1103/k72m-9tn8](https://doi.org/10.1103/k72m-9tn8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fk72m-9tn8); retrieved 2026-10-08.

#### Q0763 Design of fast Rydberg blockade SWAP gates with synthetic modulated driving

Xin Wang, Tianze Sheng, Yuan Sun.
Journal article | 2025 | Photonics Research | vol. 13 | no. 4 | pp. 1074.
Identifier and resource: [10.1364/prj.550203](https://doi.org/10.1364/prj.550203).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fprj.550203); retrieved 2026-10-08.

#### Q0764 Geometric gates in atomic arrays without Rydberg blockade

Yue Ming, Zhao-Xin Fu, Yan-Xiong Du.
Journal article | 2025 | Physical Review A | vol. 112 | no. 4 | article 042609.
Identifier and resource: [10.1103/tmr4-gtnl](https://doi.org/10.1103/tmr4-gtnl).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ftmr4-gtnl); retrieved 2026-10-08.

#### Q0765 Optimization of Entangling Logic Gates Based on the Rydberg Blockade Effect

L. V. Gerasimov, D. V. Kupriyanov, S. S. Straupe.
Journal article | 2023 | Journal of Experimental and Theoretical Physics | vol. 137 | no. 2 | pp. 157-162.
Identifier and resource: [10.1134/s1063776123080113](https://doi.org/10.1134/s1063776123080113).
Fine tags: entangling gates.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1063776123080113); retrieved 2026-10-08.

#### Q0766 Rabi- and Blockade-Error-Resilient All-Geometric Rydberg Quantum Gates

S.-L. Su, Li-Na Sun, B.-J. Liu, L.-L. Yan, M.-H. Yung, W. Li, M. Feng.
Journal article | 2023 | Physical Review Applied | vol. 19 | no. 4 | article 044007.
Identifier and resource: [10.1103/physrevapplied.19.044007](https://doi.org/10.1103/physrevapplied.19.044007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.19.044007); retrieved 2026-10-08.

#### Q0767 Two-Qubit Geometric Gates Based on Ground-State Blockade of Rydberg Atoms

Ji-Ze Xu, Li-Na Sun, J.-F. Wei, Y.-L. Du, Ronghui Luo, Lei-Lei Yan, M. Feng, Shi-Lei Su.
Journal article | 2022 | Chinese Physics Letters | vol. 39 | no. 9 | pp. 090301.
Identifier and resource: [10.1088/0256-307x/39/9/090301](https://doi.org/10.1088/0256-307x/39/9/090301).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F0256-307x%2F39%2F9%2F090301); retrieved 2026-10-08.

#### Q0768 Unselective ground-state blockade of Rydberg atoms for implementing quantum gates

Jin-Lei Wu, Yan Wang, Jin-Xuan Han, Shi-Lei Su, Yan Xia, Yongyuan Jiang, Jie Song.
Journal article | 2021 | Frontiers of Physics | vol. 17 | no. 2 | article 22501.
Identifier and resource: [10.1007/s11467-021-1104-7](https://doi.org/10.1007/s11467-021-1104-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11467-021-1104-7); retrieved 2026-10-08.

### D14T03 Neutral atom analog simulation

Neutral atom simulators realize programmable interacting spin systems. Interpretation depends on the realized Hamiltonian and measured observable rather than array size alone.

Fine subcategories: Rydberg Hamiltonians; spin systems; many body dynamics; programmable geometry.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0769 Analog quantum feature selection with neutral-atom quantum processors

José J. Orquín-Marqués, Carlos Flores-Garrigós, Alejandro Gomez Cadavid, Anton Simen, Enrique Solano, Narendra N. Hegade, José D. Martín-Guerrero, Yolanda Vives-Gilabert.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 2 | article 108.
Identifier and resource: [10.1007/s42484-026-00456-8](https://doi.org/10.1007/s42484-026-00456-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00456-8); retrieved 2026-10-08.

#### Q0770 Neutral atom quantum computing

J. D. Pritchard.
Journal article | 2026 | Contemporary Physics | pp. 1-19.
Identifier and resource: [10.1080/00107514.2026.2675142](https://doi.org/10.1080/00107514.2026.2675142).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1080%2F00107514.2026.2675142); retrieved 2026-10-08.

#### Q0771 Qubit ‘recycling’ gives neutral-atom quantum computing a boost

Anna Demming.
Journal article | 2026 | Physics World | vol. 39 | no. 2 | pp. 10ii-10ii.
Identifier and resource: [10.1088/2058-7058/39/02/10](https://doi.org/10.1088/2058-7058/39/02/10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-7058%2F39%2F02%2F10); retrieved 2026-10-08.

#### Q0772 Quantum Simulation Using Ultracold Neutral Atoms

Jongchul MUN, Jeewoo PARK, Yong-il SHIN, Jae-yoon CHOI.
Journal article | 2025 | Physics and High Technology | vol. 34 | no. 6 | pp. 10-18.
Identifier and resource: [10.3938/phit.34.017](https://doi.org/10.3938/phit.34.017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3938%2Fphit.34.017); retrieved 2026-10-08.

#### Q0773 Variational Simulation of the Lipkin-Meshkov-Glick Model on a Neutral Atom Quantum Computer

R. Chinnarasu, C. Poole, L. Phuttitarn, A. Noori, T. M. Graham, S. N. Coppersmith, A. B. Balantekin, M. Saffman.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 2 | article 020350.
Identifier and resource: [10.1103/prxquantum.6.020350](https://doi.org/10.1103/prxquantum.6.020350).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.6.020350); retrieved 2026-10-08.

#### Q0774 Realistic Neutral Atom Image Simulation

Jonas Winklmann, Dimitrios Tsevas, Martin Schulz.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1349-1359.
Identifier and resource: [10.1109/qce57702.2023.00153](https://doi.org/10.1109/qce57702.2023.00153).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00153); retrieved 2026-10-08.

#### Q0775 Quantum computation and simulation with programmable neutral atom arrays

Alex Keesling.
Conference paper | 2022 | Quantum Computing, Communication, and Simulation II | pp. 13.
Identifier and resource: [10.1117/12.2613790](https://doi.org/10.1117/12.2613790).
Conference metadata: Quantum Computing, Communication, and Simulation II.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2613790); retrieved 2026-10-08.

#### Q0776 Computer simulation of neutral atom traps

A. Antillón, A. Góngora-T., T. H. Seligman.
Journal article | 1992 | Zeitschrift für Physik D Atoms, Molecules and Clusters | vol. 24 | no. 4 | pp. 347-350.
Identifier and resource: [10.1007/bf01426683](https://doi.org/10.1007/bf01426683).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbf01426683); retrieved 2026-10-08.

### D14T04 Neutral atom error correction

Neutral atom error correction combines logical encodings with atom transport and syndrome measurement. Atom loss and measurement backaction require platform aware analysis.

Fine subcategories: Logical arrays; atom loss; syndrome extraction; transport; transversal gates.

Primary resources: 6. Additional related assignments can be found in the interactive HTML.

#### Q0777 Building Error-Corrected Quantum Computers With Neutral-Atom Qubits

Krish Kotru.
Conference paper | 2025 | CLEO 2025 | pp. AA107_1.
Identifier and resource: [10.1364/cleo_at.2025.aa107_1](https://doi.org/10.1364/cleo_at.2025.aa107_1).
Conference metadata: CLEO: Applications and Technology.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_at.2025.aa107_1); retrieved 2026-10-08.

#### Q0778 Coniq: Enabling Concatenated Quantum Error Correction on Neutral Atom Arrays

Pengyu Liu, Mingkuan Xu, Hengyun Zhou, Hanrui Wang, Umut A. Acar, Yunong Shi.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 615-626.
Identifier and resource: [10.1109/qce65121.2025.00073](https://doi.org/10.1109/qce65121.2025.00073).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00073); retrieved 2026-10-08.

#### Q0779 State-selective electromagnetically induced transparency for quantum error correction in neutral atom quantum computers

Felipe Giraldo, Aishwarya Kumar, Tsung-Yao Wu, Peng Du, David S. Weiss.
Journal article | 2022 | Physical Review A | vol. 106 | no. 3 | article 032425.
Identifier and resource: [10.1103/physreva.106.032425](https://doi.org/10.1103/physreva.106.032425).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.106.032425); retrieved 2026-10-08.

#### Q0780 Quantum Error Correction with a Globally-Coupled Array of Neutral Atom Qubits

Mark Saffman.
Report | 2013 | Defense Technical Information Center.
Identifier and resource: [10.21236/ada579666](https://doi.org/10.21236/ada579666).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21236%2Fada579666); retrieved 2026-10-08.

#### Q0781 Neutral Atom Quantum Computing

Carl J. Williams.
Conference paper | 2004 | Frontiers in Optics 2004/Laser Science XXII/Diffractive Optics and Micro-Optics/Optical Fabrication and Testing | pp. FMI4.
Identifier and resource: [10.1364/fio.2004.fmi4](https://doi.org/10.1364/fio.2004.fmi4).
Conference metadata: Frontiers in Optics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ffio.2004.fmi4); retrieved 2026-10-08.

#### Q0782 Neutral Atom Quantum Register

D. Schrader, I. Dotsenko, M. Khudaverdyan, Y. Miroshnychenko, A. Rauschenbeutel, D. Meschede.
Journal article | 2004 | Physical Review Letters | vol. 93 | no. 15 | article 150501.
Identifier and resource: [10.1103/physrevlett.93.150501](https://doi.org/10.1103/physrevlett.93.150501).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.93.150501); retrieved 2026-10-08.

### D14T05 Alkaline earth atomic qubits

Alkaline earth and related atoms offer nuclear spin and optical transition resources. Storage, control, readout, and metastable state lifetimes must be considered together.

Fine subcategories: Nuclear spins; optical clocks; metastable states; qubit storage; control transitions.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0783 Quantum metrology with alkaline-earth atoms

Nelson Darkwah Oppong.
Conference paper | 2026 | Quantum Sensing, Imaging, and Precision Metrology IV | pp. 158.
Identifier and resource: [10.1117/12.3089700](https://doi.org/10.1117/12.3089700).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology IV.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3089700); retrieved 2026-10-08.

#### Q0784 Coherent Control Over the High-Dimensional Space of the Nuclear Spin of Alkaline-Earth Atoms

H. Ahmed, A. Litvinov, P. Guesdon, E. Maréchal, J.H. Huckans, B. Pasquiou, B. Laburthe-Tolra, M. Robert-de-Saint-Vincent.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 2 | article 020352.
Identifier and resource: [10.1103/prxquantum.6.020352](https://doi.org/10.1103/prxquantum.6.020352).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.6.020352); retrieved 2026-10-08.

#### Q0785 Quantum metrology with alkaline-earth atom arrays

Nelson Darkwah Oppong.
Conference paper | 2025 | Quantum Sensing, Imaging, and Precision Metrology III | pp. 85.
Identifier and resource: [10.1117/12.3053683](https://doi.org/10.1117/12.3053683).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology III.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3053683); retrieved 2026-10-08.

#### Q0786 Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays

Yue Wu, Shimon Kolkowitz, Shruti Puri, Jeff D. Thompson.
Journal article | 2022 | Nature Communications | vol. 13 | no. 1 | article 4657.
Identifier and resource: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-022-32094-6); retrieved 2026-10-08.

#### Q0787 Spin-orbit effects in the heavy alkaline-earth atoms

Chris H. Greene, Mireille Aymar.
Book chapter | 2019 | Molecular Applications of Quantum Defect Theory | pp. 421-438.
Identifier and resource: [10.1201/9780203746608-25](https://doi.org/10.1201/9780203746608-25).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9780203746608-25); retrieved 2026-10-08.

#### Q0788 State-dependent lattices for quantum computing with alkaline-earth-metal atoms

A. J. Daley, J. Ye, P. Zoller.
Journal article | 2011 | The European Physical Journal D | vol. 65 | no. 1-2 | pp. 207-217.
Identifier and resource: [10.1140/epjd/e2011-20095-2](https://doi.org/10.1140/epjd/e2011-20095-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjd%2Fe2011-20095-2); retrieved 2026-10-08.

#### Q0789 Quantum Computing with Alkaline-Earth-Metal Atoms

Andrew J. Daley, Martin M. Boyd, Jun Ye, Peter Zoller.
Journal article | 2008 | Physical Review Letters | vol. 101 | no. 17 | article 170504.
Identifier and resource: [10.1103/physrevlett.101.170504](https://doi.org/10.1103/physrevlett.101.170504).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.101.170504); retrieved 2026-10-08.

#### Q0790 Spin-orbit effects in the heavy alkaline-earth atoms

Chris H. Greene, Mireille Aymar.
Journal article | 1991 | Physical Review A | vol. 44 | no. 3 | pp. 1773-1790.
Identifier and resource: [10.1103/physreva.44.1773](https://doi.org/10.1103/physreva.44.1773).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.44.1773); retrieved 2026-10-08.

## D15 Spin qubits and semiconductor platforms

Spin qubits connect quantum control to semiconductor materials and nanofabrication. Scaling involves disorder, charge noise, wiring, exchange coupling, and readout.

Prerequisites: Semiconductor physics, spin dynamics, and nanofabrication.

Assessment focus: Disorder, charge noise, valley structure, readout, and array wiring.

Primary catalog resources in this category: 48.

### D15T01 Silicon spin qubits

Silicon spin qubits combine quantum dot confinement with magnetic or electrical control. Valley structure, isotopic purity, and disorder are key device variables.

Fine subcategories: Quantum dots; valley splitting; spin orbit coupling; enriched silicon; gate fidelity.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q0791 A Cryogenic 2-3 GHz LC-VCO for Silicon Spin Qubit Readout

Jiaxuan Wang, Huazi Huang, Lijun Xiao, Hua Chen.
Conference paper | 2026 | 2026 International Conference on Microwave and Millimeter Wave Technology (ICMMT) | pp. 1-3.
Identifier and resource: [10.1109/icmmt69626.2026.11678947](https://doi.org/10.1109/icmmt69626.2026.11678947).
Conference metadata: 2026 International Conference on Microwave and Millimeter Wave Technology (ICMMT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficmmt69626.2026.11678947); retrieved 2026-10-08.

#### Q0792 Control and Readout of a Spin Qubit Register in Silicon Photonics

Hanbin Song, Xueyue Zhang, Lukasz Komza, Niccolo Fiaschi, Magnus L. Madsen, Zi-Huai Zhang, Alp Sipahigil.
Conference paper | 2026 | CLEO 2026 | pp. SM2F.2.
Identifier and resource: [10.1364/cleo_si.2026.sm2f.2](https://doi.org/10.1364/cleo_si.2026.sm2f.2).
Conference metadata: CLEO: Science and Innovations.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_si.2026.sm2f.2); retrieved 2026-10-08.

#### Q0793 Improved readout accuracy of a silicon spin qubit via log-likelihood ratio

R. Mizokuchi, R. Wada, R. Matsuoka, S. Ota, I. Yanagi, T. Mine, R. Tsuchiya, D. Hisamoto et al..
Journal article | 2026 | Japanese Journal of Applied Physics | vol. 65 | no. 2 | pp. 02SP03.
Identifier and resource: [10.35848/1347-4065/ae2d60](https://doi.org/10.35848/1347-4065/ae2d60).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.35848%2F1347-4065%2Fae2d60); retrieved 2026-10-08.

#### Q0794 Predicting charge stability in donor spin-qubit arrays in silicon

Songqi Jia, Pericles Philippopoulos, Félix Beaudoin, Hong Guo.
Journal article | 2026 | Physical Review Applied | vol. 26 | no. 2 | article 024013.
Identifier and resource: [10.1103/vrkm-4x3p](https://doi.org/10.1103/vrkm-4x3p).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fvrkm-4x3p); retrieved 2026-10-08.

#### Q0795 Robust composite two-qubit gates for silicon-based spin qubits

Yang-Yang Yu, Guang-Hui Zhang, Yan-Jie He, Jun Wu, Xue-Ke Song, Dong Wang.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 2 | article 024076.
Identifier and resource: [10.1103/t8xj-6c5m](https://doi.org/10.1103/t8xj-6c5m).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ft8xj-6c5m); retrieved 2026-10-08.

#### Q0796 Running a Six-Qubit Quantum Circuit on a Silicon Spin-Qubit Array

I. Fernández de Fuentes, E. Raymenants, B. Undseth, O. Pietx-Casas, S. Philips, M. Mądzik, S.L. de Snoo, S.V. Amitonov et al..
Journal article | 2026 | PRX Quantum | vol. 7 | no. 1 | article 010308.
Identifier and resource: [10.1103/f285-l2v5](https://doi.org/10.1103/f285-l2v5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ff285-l2v5); retrieved 2026-10-08.

#### Q0797 Two-qubit logic and teleportation with mobile spin qubits in silicon

Y. Matsumoto, M. De Smet, L. Tryputen, S. L. de Snoo, S. V. Amitonov, A. Sammak, M. Rimbach-Russ, G. Scappucci et al..
Journal article | 2026 | Nature | vol. 653 | no. 8114 | pp. 391-397.
Identifier and resource: [10.1038/s41586-026-10423-9](https://doi.org/10.1038/s41586-026-10423-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-026-10423-9); retrieved 2026-10-08.

#### Q0798 300mm All Silicon Gate-Stack for Si/SiGe Spin Qubit

Clément Godfrin, Arne Loenders, Yosuke Shimura, Roger Loo, Bart Raes, Gulzat Juliel, Sugandha Sharma, Stefan Kubicek et al..
Conference paper | 2025 | Extended Abstracts of the 2025 International Conference on Solid State Devices and Materials.
Identifier and resource: [10.7567/ssdm.2025.e-5-01](https://doi.org/10.7567/ssdm.2025.e-5-01).
Conference metadata: 2025 International Conference on Solid State Devices and Materials.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7567%2Fssdm.2025.e-5-01); retrieved 2026-10-08.

#### Q0799 An Efficient Routing Optimization Framework for Silicon-Based Spin-Qubit Devices

Ching-Yao Huang, Wai-Kei Mak.
Conference paper | 2025 | 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD) | pp. 1-9.
Identifier and resource: [10.1109/iccad66269.2025.11240960](https://doi.org/10.1109/iccad66269.2025.11240960).
Conference metadata: 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcad66269.2025.11240960); retrieved 2026-10-08.

#### Q0800 Entanglement of a nuclear spin qubit register in silicon photonics

Hanbin Song, Xueyue Zhang, Lukasz Komza, Niccolo Fiaschi, Yihuang Xiong, Yiyang Zhi, Scott Dhuey, Adam Schwartzberg et al..
Journal article | 2025 | Nature Nanotechnology | vol. 21 | no. 1 | pp. 53-57.
Identifier and resource: [10.1038/s41565-025-02066-0](https://doi.org/10.1038/s41565-025-02066-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41565-025-02066-0); retrieved 2026-10-08.

#### Q0801 Improved Readout Accuracy of a Silicon Spin Qubit via Maximum Likelihood Estimation

Raisei Mizokuchi, Riku Wada, Ryutaro Matsuoka, Shunsuke Ota, Itaru Yanagi, Toshiyuki Mine, Ryuta Tsuchiya, Digh Hisamoto et al..
Conference paper | 2025 | Extended Abstracts of the 2025 International Conference on Solid State Devices and Materials.
Identifier and resource: [10.7567/ssdm.2025.e-6-04](https://doi.org/10.7567/ssdm.2025.e-6-04).
Conference metadata: 2025 International Conference on Solid State Devices and Materials.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7567%2Fssdm.2025.e-6-04); retrieved 2026-10-08.

#### Q0802 Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity

Paul Steinacker, Nard Dumoulin Stuyck, Wee Han Lim, Tuomo Tanttu, MengKe Feng, Santiago Serrano, Andreas Nickl, Marco Candido et al..
Journal article | 2025 | Nature | vol. 646 | no. 8083 | pp. 81-87.
Identifier and resource: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-025-09531-9); retrieved 2026-10-08.

#### Q0803 Modeling correlated-noise in silicon spin qubit device

Guoting Cheng, Jing Guo.
Journal article | 2025 | APL Quantum | vol. 2 | no. 1 | article 016101.
Identifier and resource: [10.1063/5.0216833](https://doi.org/10.1063/5.0216833).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0216833); retrieved 2026-10-08.

#### Q0804 A singlet-triplet hole-spin qubit in MOS silicon

S. D. Liles, D. J. Halverson, Z. Wang, A. Shamim, R. S. Eggli, I. K. Jin, J. Hillier, K. Kumar et al..
Journal article | 2024 | Nature Communications | vol. 15 | no. 1 | article 7690.
Identifier and resource: [10.1038/s41467-024-51902-9](https://doi.org/10.1038/s41467-024-51902-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-024-51902-9); retrieved 2026-10-08.

#### Q0805 A singlet-triplet hole-spin qubit in MOS silicon

Scott Liles, Daniel Halverson, Zhanning Wang, Aaquib Shamim, Rafael Eggli, Ik Kyeong Jin, Joe Hillier, Krittika Kumar et al..
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-3603337/v1](https://doi.org/10.21203/rs.3.rs-3603337/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-3603337%2Fv1); retrieved 2026-10-08.

#### Q0806 Tin as a nuclear spin qubit in silicon

Wayne Witzel.
Conference paper | 2024 | APS March Meeting 2024 - Minneapolis, Minnesota, United States of America - March - 2024.
Identifier and resource: [10.2172/2540383](https://doi.org/10.2172/2540383).
Conference metadata: APS March Meeting 2024 - Minneapolis, Minnesota, United States of America - March - 2024.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2540383); retrieved 2026-10-08.

### D15T02 Germanium hole qubits

Germanium hole systems provide strong electric control through spin orbit coupling. Strain, confinement, charge noise, and interactions determine operation quality.

Fine subcategories: Heavy holes; strong spin orbit coupling; planar dots; strain; electric control.

Primary resources: 10. Additional related assignments can be found in the interactive HTML.

#### Q0807 Comparative assessment of germanium-based spin-qubit modalities: donor, acceptor, gate-defined hole, and gate-defined electron platforms

D-M Mei, K-M Dong, S A Panamaldeniya, A Prem, S Chhetri, N Budhathoki, S Bhattarai.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 4 | pp. 043001.
Identifier and resource: [10.1088/2058-9565/ae9cda](https://doi.org/10.1088/2058-9565/ae9cda).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae9cda); retrieved 2026-10-08.

#### Q0808 Optimising germanium hole spin qubits with a room-temperature magnet

Cécile X. Yu, Barnaby van Straaten, Alexander S. Ivlev, Valentin John, Damien R. Crielaard, Stefan D. Oosterhout, Lucas E. A. Stehouwer, Francesco Borsoi et al..
Journal article | 2026 | Communications Physics | vol. 9 | no. 1 | article 272.
Identifier and resource: [10.1038/s42005-026-02634-3](https://doi.org/10.1038/s42005-026-02634-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42005-026-02634-3); retrieved 2026-10-08.

#### Q0809 Variability of hole-spin qubits in planar germanium

Biel Martinez, Yann-Michel Niquet.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 1 | article 014018.
Identifier and resource: [10.1103/mtky-93p1](https://doi.org/10.1103/mtky-93p1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fmtky-93p1); retrieved 2026-10-08.

#### Q0810 Hole spin qubits in unstrained Germanium layers

Lorenzo Mauro, Mauricio J. Rodríguez, Esteban A. Rodríguez-Mena, Yann-Michel Niquet.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 167.
Identifier and resource: [10.1038/s41534-025-01108-8](https://doi.org/10.1038/s41534-025-01108-8).
Fine tags: strain.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01108-8); retrieved 2026-10-08.

#### Q0811 Low-noise hole spin qubits in germanium

Danielle Holmes.
Journal article | 2025 | Nature Materials | vol. 24 | no. 12 | pp. 1869-1870.
Identifier and resource: [10.1038/s41563-025-02307-6](https://doi.org/10.1038/s41563-025-02307-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41563-025-02307-6); retrieved 2026-10-08.

#### Q0812 Sweet-spot operation of a germanium hole spin qubit with highly anisotropic noise sensitivity

N. W. Hendrickx, L. Massai, M. Mergenthaler, F. J. Schupp, S. Paredes, S. W. Bedell, G. Salis, A. Fuhrer.
Journal article | 2024 | Nature Materials | vol. 23 | no. 7 | pp. 920-927.
Identifier and resource: [10.1038/s41563-024-01857-5](https://doi.org/10.1038/s41563-024-01857-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41563-024-01857-5); retrieved 2026-10-08.

#### Q0813 Ultrafast and Electrically Tunable Rabi Frequency in a Germanium Hut Wire Hole Spin Qubit

He Liu, Ke Wang, Fei Gao, Jin Leng, Yang Liu, Yu-Chen Zhou, Gang Cao, Ting Wang et al..
Journal article | 2023 | Nano Letters | vol. 23 | no. 9 | pp. 3810-3817.
Identifier and resource: [10.1021/acs.nanolett.3c00213](https://doi.org/10.1021/acs.nanolett.3c00213).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.nanolett.3c00213); retrieved 2026-10-08.

#### Q0814 DFT Analysis of Hole Qubits Spin State in Germanium Thin Layer

Andrey Chibisov, Maxim Aleshin, Mary Chibisova.
Journal article | 2022 | Nanomaterials | vol. 12 | no. 13 | pp. 2244.
Identifier and resource: [10.3390/nano12132244](https://doi.org/10.3390/nano12132244).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fnano12132244); retrieved 2026-10-08.

#### Q0815 Emergent linear Rashba spin-orbit coupling offers fast manipulation of hole-spin qubits in germanium

Yang Liu, Jia-Xin Xiong, Zhi Wang, Wen-Long Ma, Shan Guan, Jun-Wei Luo, Shu-Shen Li.
Journal article | 2022 | Physical Review B | vol. 105 | no. 7 | article 075313.
Identifier and resource: [10.1103/physrevb.105.075313](https://doi.org/10.1103/physrevb.105.075313).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.105.075313); retrieved 2026-10-08.

#### Q0816 Ultrafast coherent control of a hole spin qubit in a germanium quantum dot

Ke Wang, Gang Xu, Fei Gao, He Liu, Rong-Long Ma, Xin Zhang, Zhanning Wang, Gang Cao et al..
Journal article | 2022 | Nature Communications | vol. 13 | no. 1 | article 206.
Identifier and resource: [10.1038/s41467-021-27880-7](https://doi.org/10.1038/s41467-021-27880-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-021-27880-7); retrieved 2026-10-08.

### D15T03 Donor qubits

Donor processors use localized electron and nuclear spins in semiconductors. Placement, hyperfine control, and readout interfaces affect scalability.

Fine subcategories: Phosphorus donors; nuclear spins; hyperfine coupling; atom placement; donor readout.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0817 Atomistic first-principles modeling of single donor spin-qubit

Songqi Jia, Félix Beaudoin, Pericles Philippopoulos, Hong Guo.
Journal article | 2024 | Applied Physics Letters | vol. 125 | no. 18 | article 184001.
Identifier and resource: [10.1063/5.0221229](https://doi.org/10.1063/5.0221229).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0221229); retrieved 2026-10-08.

#### Q0818 Precision tomography of a three-qubit donor quantum processor in silicon

Mateusz T. Mądzik, Serwan Asaad, Akram Youssry, Benjamin Joecker, Kenneth M. Rudinger, Erik Nielsen, Kevin C. Young, Timothy J. Proctor et al..
Journal article | 2022 | Nature | vol. 601 | no. 7893 | pp. 348-353.
Identifier and resource: [10.1038/s41586-021-04292-7](https://doi.org/10.1038/s41586-021-04292-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-021-04292-7); retrieved 2026-10-08.

#### Q0819 Coherent control of a donor-molecule electron spin qubit in silicon

Lukas Fricke, Samuel J. Hile, Ludwik Kranz, Yousun Chung, Yu He, Prasanna Pakkiam, Matthew G. House, Joris G. Keizer et al..
Journal article | 2021 | Nature Communications | vol. 12 | no. 1 | article 3323.
Identifier and resource: [10.1038/s41467-021-23662-3](https://doi.org/10.1038/s41467-021-23662-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-021-23662-3); retrieved 2026-10-08.

#### Q0820 A two-qubit gate between phosphorus donor electrons in silicon

Y. He, S. K. Gorman, D. Keith, L. Kranz, J. G. Keizer, M. Y. Simmons.
Journal article | 2019 | Nature | vol. 571 | no. 7765 | pp. 371-375.
Identifier and resource: [10.1038/s41586-019-1381-2](https://doi.org/10.1038/s41586-019-1381-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-019-1381-2); retrieved 2026-10-08.

#### Q0821 Characterization of a Scalable Donor-Based Singlet–Triplet Qubit Architecture in Silicon

Prasanna Pakkiam, Matthew G. House, Matthias Koch, Michelle Y. Simmons.
Journal article | 2018 | Nano Letters | vol. 18 | no. 7 | pp. 4081-4085.
Identifier and resource: [10.1021/acs.nanolett.8b00006](https://doi.org/10.1021/acs.nanolett.8b00006).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.nanolett.8b00006); retrieved 2026-10-08.

#### Q0822 Optical control of donor spin qubits in silicon

M. J. Gullans, J. M. Taylor.
Journal article | 2015 | Physical Review B | vol. 92 | no. 19 | article 195411.
Identifier and resource: [10.1103/physrevb.92.195411](https://doi.org/10.1103/physrevb.92.195411).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.92.195411); retrieved 2026-10-08.

#### Q0823 Spin delocalization in phosphorus donor pairs in silicon

J. H. Pifer.
Journal article | 1985 | Physical Review B | vol. 32 | no. 11 | pp. 7091-7097.
Identifier and resource: [10.1103/physrevb.32.7091](https://doi.org/10.1103/physrevb.32.7091).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.32.7091); retrieved 2026-10-08.

### D15T04 Spin readout and exchange gates

Exchange operations couple nearby spins, while spin to charge conversion enables readout. Control uniformity and charge noise connect gate and measurement performance.

Fine subcategories: Pauli blockade; charge sensing; exchange coupling; resonator readout; spin to charge conversion.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0824 Electron readout contrast enhancement in the parallel nuclear regime of an exchange-coupled donor spin qubit system

Holly G. Stemp, Mark R. van Blankenstein, Benjamin Wilhelm, Serwan Asaad, Mateusz T. Mądzik, Arne Laucht, Fay E. Hudson, Andrew S. Dzurak et al..
Journal article | 2026 | Physical Review B | vol. 113 | no. 24 | article 245409.
Identifier and resource: [10.1103/1jc4-v2zt](https://doi.org/10.1103/1jc4-v2zt).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F1jc4-v2zt); retrieved 2026-10-08.

#### Q0825 Exchange-only qubit stabilized by a single-spin qubit

Irina Heinz, Mira Sharma, Joris Kattemölle.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-10700701/v1](https://doi.org/10.21203/rs.3.rs-10700701/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-10700701%2Fv1); retrieved 2026-10-08.

#### Q0826 Singlet-only always-on gapless exchange spin qubits: Charge noise effects and two-qubit gates

Anonymous.
Journal article | 2026 | Physical Review B.
Identifier and resource: [10.1103/8bzz-rw2j](https://doi.org/10.1103/8bzz-rw2j).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8bzz-rw2j); retrieved 2026-10-08.

#### Q0827 Integrated silicon qubit platform with single-spin addressability, exchange control and single-shot singlet-triplet readout

M. A. Fogarty, K. W. Chan, B. Hensen, W. Huang, T. Tanttu, C. H. Yang, A. Laucht, M. Veldhorst et al..
Journal article | 2018 | Nature Communications | vol. 9 | no. 1 | article 4370.
Identifier and resource: [10.1038/s41467-018-06039-x](https://doi.org/10.1038/s41467-018-06039-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-018-06039-x); retrieved 2026-10-08.

#### Q0828 Quadrupolar Exchange-Only Spin Qubit

Maximilian Russ, J. R. Petta, Guido Burkard.
Journal article | 2018 | Physical Review Letters | vol. 121 | no. 17 | article 177701.
Identifier and resource: [10.1103/physrevlett.121.177701](https://doi.org/10.1103/physrevlett.121.177701).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.121.177701); retrieved 2026-10-08.

#### Q0829 Exchange-only singlet-only spin qubit

Arnau Sala, Jeroen Danon.
Journal article | 2017 | Physical Review B | vol. 95 | no. 24 | article 241303.
Identifier and resource: [10.1103/physrevb.95.241303](https://doi.org/10.1103/physrevb.95.241303).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.95.241303); retrieved 2026-10-08.

#### Q0830 Anisotropic Spin Exchange in Pulsed Quantum Gates

N. E. Bonesteel, D. Stepanenko, D. P. DiVincenzo.
Journal article | 2001 | Physical Review Letters | vol. 87 | no. 20 | article 207901.
Identifier and resource: [10.1103/physrevlett.87.207901](https://doi.org/10.1103/physrevlett.87.207901).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.87.207901); retrieved 2026-10-08.

### D15T05 Spin shuttling and scalable arrays

Shuttling and array control seek to connect spin qubits beyond immediate neighbors. Transport coherence and wiring complexity become system level constraints.

Fine subcategories: Electron transport; crossbar control; long range coupling; arrays; cryogenic interfaces.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0831 Interplay of Zeeman splitting and tunnel coupling in coherent spin-qubit shuttling

Ssu-Chih Lin, Paul Steinacker, MengKe Feng, Ajit Dash, Santiago Serrano, Wee Han Lim, Kohei M. Itoh, Fay E. Hudson et al..
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 3 | article 034016.
Identifier and resource: [10.1103/3d1t-pr7m](https://doi.org/10.1103/3d1t-pr7m).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F3d1t-pr7m); retrieved 2026-10-08.

#### Q0832 Numerical simulation of charged-defect-induced decoherence in conveyor-mode spin qubit shuttling in Si/SiGe

Nils Ciroth, Arnau Sala, Ran Xue, Lasse Ermoneit, Thomas Koprucki, Markus Kantner, Lars R. Schreiber.
Journal article | 2026 | Physical Review B | vol. 114 | no. 10 | article 105305.
Identifier and resource: [10.1103/styv-ypg9](https://doi.org/10.1103/styv-ypg9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fstyv-ypg9); retrieved 2026-10-08.

#### Q0833 Performance of the spin qubit shuttling architecture for a surface code implementation

Berat Yenilen, Arnau Sala, Hendrik Bluhm, Markus Müller, Manuel Rispler.
Journal article | 2026 | Quantum | vol. 10 | pp. 2219 | article 2219.
Identifier and resource: [10.22331/q-2026-09-30-2219](https://doi.org/10.22331/q-2026-09-30-2219).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-09-30-2219); retrieved 2026-10-08.

#### Q0834 Spin Qubit Leapfrogging: Dynamics of shuttling electrons on top of another

Anonymous.
Journal article | 2026 | Physical Review Research.
Identifier and resource: [10.1103/l1vq-9zhr](https://doi.org/10.1103/l1vq-9zhr).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fl1vq-9zhr); retrieved 2026-10-08.

#### Q0835 Synthesizing an optimal spin-qubit shuttling-bus architecture for the surface code

Pau Escofet, Eduard Alarcón, Sergi Abadal, Andrii Semenov, Niall Murphy, Elena Blokhina, Carmen G. Almudéver.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032404.
Identifier and resource: [10.1103/4p4q-fm3y](https://doi.org/10.1103/4p4q-fm3y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F4p4q-fm3y); retrieved 2026-10-08.

#### Q0836 Dephasing and error dynamics affecting a singlet-triplet qubit during coherent spin shuttling

Natalie D. Foster, Jacob D. Henshaw, Martin Rudolph, Dwight R. Luhman, Ryan M. Jock.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 63.
Identifier and resource: [10.1038/s41534-025-00996-0](https://doi.org/10.1038/s41534-025-00996-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-00996-0); retrieved 2026-10-08.

#### Q0837 High-fidelity single-electron shuttling in industrially fabricated spin qubit devices

P. Muster, W. Langheinrich, T. Huckemann, S. Pregl, V. Brackmann, M. Friedrich, F. Reichmann, N. D. Komerički et al..
Conference paper | 2025 | 2025 IEEE International Electron Devices Meeting (IEDM) | pp. 1-4.
Identifier and resource: [10.1109/iedm50572.2025.11353490](https://doi.org/10.1109/iedm50572.2025.11353490).
Conference metadata: 2025 IEEE International Electron Devices Meeting (IEDM).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fiedm50572.2025.11353490); retrieved 2026-10-08.

#### Q0838 Large spin-shuttling oscillations enabling high-fidelity single-qubit gates

Akshay Menon Pazhedath, Alessandro David, Max Oberländer, Matthias M. Müller, Tommaso Calarco, Hendrik Bluhm, Felix Motzoi.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 3 | article 034029.
Identifier and resource: [10.1103/4lky-413f](https://doi.org/10.1103/4lky-413f).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F4lky-413f); retrieved 2026-10-08.

## D16 Photonic quantum computing

Photonic approaches encode information in optical modes and use interference, measurements, and sometimes nonlinear interactions. Loss and resource generation are central engineering constraints.

Prerequisites: Quantum optics, interference, and photodetection.

Assessment focus: Loss, indistinguishability, source rate, detector efficiency, and resource overhead.

Primary catalog resources in this category: 57.

### D16T01 Linear optical computation

Linear optics uses interference, measurement, and ancillary photons for computation. Probabilistic operations require resource accounting and feed forward.

Fine subcategories: KLM; interferometers; photon counting; postselection; feed forward.

Primary resources: 10. Additional related assignments can be found in the interactive HTML.

#### Q0839 A dataflow programming framework for linear optical distributed quantum computing

Giovanni de Felice, Boldizsár Poór, Cole Comfort, Lia Yeh, Mateusz Kupper, William Cashman, Bob Coecke.
Journal article | 2026 | Quantum | vol. 10 | pp. 1972 | article 1972.
Identifier and resource: [10.22331/q-2026-01-19-1972](https://doi.org/10.22331/q-2026-01-19-1972).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-01-19-1972); retrieved 2026-10-08.

#### Q0840 Fusion for high-dimensional linear-optical quantum computing with improved success probability

Gözde Üstün, Eleanor G. Rieffel, Simon J. Devitt, Jason Saied.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 4 | article 044024.
Identifier and resource: [10.1103/l7bg-hc8c](https://doi.org/10.1103/l7bg-hc8c).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fl7bg-hc8c); retrieved 2026-10-08.

#### Q0841 Linear optical quantum computing with a hybrid squeezed-cat code

Shohei Kiryu, Kosuke Fukui, Atsushi Okamoto, Akihisa Tomita.
Journal article | 2025 | Physical Review A | vol. 112 | no. 4 | article 042615.
Identifier and resource: [10.1103/jxbx-75m9](https://doi.org/10.1103/jxbx-75m9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fjxbx-75m9); retrieved 2026-10-08.

#### Q0842 4-Bit Linear Optical Quantum Computing with Liquid Crystal Devices

Satoshi Yokotsuka, Hiroyuki Okada.
Posted content | 2024 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.4792710](https://doi.org/10.2139/ssrn.4792710).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.4792710); retrieved 2026-10-08.

#### Q0843 Four-bit input linear optical quantum computing with liquid crystal devices

Satoshi Yokotsuka, Hiroyuki Okada.
Journal article | 2024 | APL Quantum | vol. 1 | no. 4 | article 046105.
Identifier and resource: [10.1063/5.0224043](https://doi.org/10.1063/5.0224043).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0224043); retrieved 2026-10-08.

#### Q0844 Quantum photonic integrated circuits simulation tool for linear optical quantum computing gates

Argiris Ntanos, Giannis Giannoulis, Aris Stathis, Dimitris Zavitsanos, Hercules Avramopoulos.
Conference paper | 2024 | Quantum Technologies 2024 | pp. 50.
Identifier and resource: [10.1117/12.3022597](https://doi.org/10.1117/12.3022597).
Conference metadata: Quantum Technologies 2024.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3022597); retrieved 2026-10-08.

#### Q0845 Linear optical quantum computation

Varna University of Management, Andreas Cristoforides, Aaaron Miller.
Report | 2020 | Web of Open Science.
Identifier and resource: [10.37686/qrl.v1i2.58](https://doi.org/10.37686/qrl.v1i2.58).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.37686%2Fqrl.v1i2.58); retrieved 2026-10-08.

#### Q0846 Scalable controlled-not gate for linear optical quantum computing using microring resonators

Ryan E. Scott, Paul M. Alsing, A. Matthew Smith, Michael L. Fanto, Christopher C. Tison, James Schneeloch, Edwin E. Hach.
Journal article | 2019 | Physical Review A | vol. 100 | no. 2 | article 022322.
Identifier and resource: [10.1103/physreva.100.022322](https://doi.org/10.1103/physreva.100.022322).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.100.022322); retrieved 2026-10-08.

#### Q0847 Resource Costs for Fault-Tolerant Linear Optical Quantum Computing

Ying Li, Peter C. Humphreys, Gabriel J. Mendoza, Simon C. Benjamin.
Journal article | 2015 | Physical Review X | vol. 5 | no. 4 | article 041007.
Identifier and resource: [10.1103/physrevx.5.041007](https://doi.org/10.1103/physrevx.5.041007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.5.041007); retrieved 2026-10-08.

#### Q0848 Redirecting to main branch docs

Author metadata not supplied.
Documentation | Undated | Quandela Perceval.
Identifier and resource: [Official resource](https://perceval.quandela.net/docs/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://perceval.quandela.net/docs/); retrieved 2026-10-08.

### D16T02 Boson sampling

Boson sampling samples distributions produced by indistinguishable particles passing through an optical network. Loss, distinguishability, and classical simulation affect hardness claims.

Fine subcategories: Permanent estimation; Gaussian boson sampling; distinguishability; loss; classical simulation.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q0849 Experimental loopback boson sampling

Yu. A. Biriukov, R. D. Morozov, K. I. Okhlopkov, I. V. Dyakonov, N. N. Skryabin, S. A. Zhuravitskii, M. A. Dryazgov, K. V. Taratorin et al..
Journal article | 2026 | Optica Quantum | vol. 4 | no. 5 | pp. 460.
Identifier and resource: [10.1364/opticaq.599335](https://doi.org/10.1364/opticaq.599335).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fopticaq.599335); retrieved 2026-10-08.

#### Q0850 Boson Sampling

A.P. Lund, T.C. Ralph.
Book chapter | 2025 | Encyclopedia of Mathematical Physics | pp. 42-56.
Identifier and resource: [10.1016/b978-0-323-95703-8.00111-7](https://doi.org/10.1016/b978-0-323-95703-8.00111-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-323-95703-8.00111-7); retrieved 2026-10-08.

#### Q0851 Boson Sampling Enhanced Quantum Chemistry

Zhong-Xia Shang, Yukun Zhang, Han-Sen Zhong, Cheng-Cheng Yu, Xiao Yuan, Chao-Yang Lu, Jian-Wei Pan, Ming-Cheng Chen.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 4 | article 040357.
Identifier and resource: [10.1103/gw1c-5b58](https://doi.org/10.1103/gw1c-5b58).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fgw1c-5b58); retrieved 2026-10-08.

#### Q0852 Boson sampling powered image recognition

William J. Munro, Akitada Sakurai, Aoi Hayashi, Kae Nemoto.
Conference paper | 2025 | Quantum Computing, Communication, and Simulation V | pp. 45.
Identifier and resource: [10.1117/12.3038939](https://doi.org/10.1117/12.3038939).
Conference metadata: Quantum Computing, Communication, and Simulation V.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3038939); retrieved 2026-10-08.

#### Q0853 Unified boson sampling

Luca Bianchi, Carlo Marconi, Laura Ares, Davide Bacco, Jan Sperling.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 4 | article L042068.
Identifier and resource: [10.1103/8hy1-m5gg](https://doi.org/10.1103/8hy1-m5gg).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8hy1-m5gg); retrieved 2026-10-08.

#### Q0854 Classical sampling from noisy boson sampling and negative probabilities

V. S. Shchesnovich.
Journal article | 2024 | Physical Review A | vol. 109 | no. 3 | article 032610.
Identifier and resource: [10.1103/physreva.109.032610](https://doi.org/10.1103/physreva.109.032610).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.032610); retrieved 2026-10-08.

#### Q0855 Extending classical boson sampling techniques

S. N. van den Hoven, E. Kanis, J. J. Renema.
Conference paper | 2024 | Quantum 2.0 Conference and Exhibition | pp. QW4A.10.
Identifier and resource: [10.1364/quantum.2024.qw4a.10](https://doi.org/10.1364/quantum.2024.qw4a.10).
Conference metadata: Quantum 2.0.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fquantum.2024.qw4a.10); retrieved 2026-10-08.

#### Q0856 Faster classical boson sampling

Peter Clifford, Raphaël Clifford.
Journal article | 2024 | Physica Scripta | vol. 99 | no. 6 | pp. 065121.
Identifier and resource: [10.1088/1402-4896/ad4688](https://doi.org/10.1088/1402-4896/ad4688).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fad4688); retrieved 2026-10-08.

#### Q0857 Gaussian boson sampling at finite temperature

Gabriele Bressanini, Hyukjoon Kwon, M. S. Kim.
Journal article | 2024 | Physical Review A | vol. 109 | no. 1 | article 013707.
Identifier and resource: [10.1103/physreva.109.013707](https://doi.org/10.1103/physreva.109.013707).
Fine tags: Gaussian boson sampling.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.013707); retrieved 2026-10-08.

#### Q0858 Hybrid Boson Sampling

Vitaly Kocharovsky.
Journal article | 2024 | Entropy | vol. 26 | no. 11 | pp. 926.
Identifier and resource: [10.3390/e26110926](https://doi.org/10.3390/e26110926).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fe26110926); retrieved 2026-10-08.

#### Q0859 Gaussian Boson Sampling

Claudio Conti.
Book chapter | 2023 | Quantum Science and Technology | pp. 301-346.
Identifier and resource: [10.1007/978-3-031-44226-1_12](https://doi.org/10.1007/978-3-031-44226-1_12).
Fine tags: Gaussian boson sampling.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-44226-1_12); retrieved 2026-10-08.

#### Q0860 Non-linear Boson Sampling

Nicolò Spagnolo, Daniel J. Brod, Ernesto F. Galvão, Fabio Sciarrino.
Journal article | 2023 | npj Quantum Information | vol. 9 | no. 1 | article 3.
Identifier and resource: [10.1038/s41534-023-00676-x](https://doi.org/10.1038/s41534-023-00676-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-023-00676-x); retrieved 2026-10-08.

#### Q0861 Programmability empowering quantum boson sampling

Zhaorong Fu, Jueming Bao, Jianwei Wang.
Journal article | 2023 | Nature Computational Science | vol. 3 | no. 10 | pp. 819-820.
Identifier and resource: [10.1038/s43588-023-00534-y](https://doi.org/10.1038/s43588-023-00534-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs43588-023-00534-y); retrieved 2026-10-08.

#### Q0862 Boson sampling for generalized bosons

En-Jui Kuo, Yijia Xu, Dominik Hangleiter, Andrey Grankin, Mohammad Hafezi.
Journal article | 2022 | Physical Review Research | vol. 4 | no. 4 | article 043096.
Identifier and resource: [10.1103/physrevresearch.4.043096](https://doi.org/10.1103/physrevresearch.4.043096).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.4.043096); retrieved 2026-10-08.

#### Q0863 Timestamp boson sampling

Wen-Hao Zhou, Jun Gao, Zhi-Qiang Jiao, Xiao-Wei Wang, Ruo-Jing Ren, Xiao-Ling Pang, Lu-Feng Qiao, Chao-Ni Zhang et al..
Journal article | 2022 | Applied Physics Reviews | vol. 9 | no. 3 | article 031408.
Identifier and resource: [10.1063/5.0066103](https://doi.org/10.1063/5.0066103).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0066103); retrieved 2026-10-08.

### D16T03 Integrated quantum photonics

Integrated photonics places optical components on chips. Loss, phase stability, fabrication variation, and coupling to sources and detectors determine usable performance.

Fine subcategories: Waveguides; interferometer meshes; phase shifters; material platforms; packaging.

Primary resources: 13. Additional related assignments can be found in the interactive HTML.

#### Q0864 Programmable integrated quantum photonics

Igor Aharonovich, Kenneth B. Crozier, Dragomir Neshev.
Journal article | 2026 | Nature Photonics | vol. 20 | no. 3 | pp. 254-265.
Identifier and resource: [10.1038/s41566-025-01830-x](https://doi.org/10.1038/s41566-025-01830-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41566-025-01830-x); retrieved 2026-10-08.

#### Q0865 Diamond integrated quantum photonics

Lin Jin, Wolfram H.P. Pernice.
Book chapter | 2025 | Nanophotonics with Diamond and Silicon Carbide for Quantum Technologies | pp. 143-170.
Identifier and resource: [10.1016/b978-0-443-13717-4.00008-6](https://doi.org/10.1016/b978-0-443-13717-4.00008-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-13717-4.00008-6); retrieved 2026-10-08.

#### Q0866 Distributed quantum sensing with integrated quantum photonics

Jonathan C. F. Matthews, Beth Puzio.
Conference paper | 2025 | Quantum Sensing, Imaging, and Precision Metrology III | pp. 33.
Identifier and resource: [10.1117/12.3053407](https://doi.org/10.1117/12.3053407).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology III.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3053407); retrieved 2026-10-08.

#### Q0867 Enabling quantum sensors with integrated photonics

Neal E. Solmeyer, Argyrios Dellis, Javad Dowran, Chad Fertig, Luke Horstman, Chad Hoyt, Wei Jiang, Karl Nelson et al..
Conference paper | 2025 | Quantum Sensing and Nano Electronics and Photonics XXI | pp. 22.
Identifier and resource: [10.1117/12.3042528](https://doi.org/10.1117/12.3042528).
Conference metadata: Quantum Sensing and Nano Electronics and Photonics XXI.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3042528); retrieved 2026-10-08.

#### Q0868 Integrated Quantum Photonics

Krishna Thyagarajan.
Book | 2025 | Graduate Texts in Physics.
Identifier and resource: [10.1007/978-3-031-85728-7](https://doi.org/10.1007/978-3-031-85728-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-85728-7); retrieved 2026-10-08.

#### Q0869 Quantum integrated photonics chips and packaging

Stefan F. Preble.
Conference paper | 2024 | Quantum Information Science, Sensing, and Computation XVI | pp. 34.
Identifier and resource: [10.1117/12.3021843](https://doi.org/10.1117/12.3021843).
Conference metadata: Quantum Information Science, Sensing, and Computation XVI.
Fine tags: packaging.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3021843); retrieved 2026-10-08.

#### Q0870 Integrated Quantum Photonics

Author metadata not supplied.
Edited book | 2023 | Frontiers Research Topics.
Identifier and resource: [10.3389/978-2-88974-074-1](https://doi.org/10.3389/978-2-88974-074-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2F978-2-88974-074-1); retrieved 2026-10-08.

#### Q0871 Integrated photonics in quantum technologies

Taira Giordani, Francesco Hoch, Gonzalo Carvacho, Nicolò Spagnolo, Fabio Sciarrino.
Journal article | 2023 | La Rivista del Nuovo Cimento | vol. 46 | no. 2 | pp. 71-103.
Identifier and resource: [10.1007/s40766-023-00040-x](https://doi.org/10.1007/s40766-023-00040-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs40766-023-00040-x); retrieved 2026-10-08.

#### Q0872 QUANTUM INTEGRATED PHOTONICS

Ryszard Romaniuk.
Journal article | 2023 | ELEKTRONIKA - KONSTRUKCJE, TECHNOLOGIE, ZASTOSOWANIA | vol. 1 | no. 8 | pp. 19-26.
Identifier and resource: [10.15199/13.2023.8.4](https://doi.org/10.15199/13.2023.8.4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15199%2F13.2023.8.4); retrieved 2026-10-08.

#### Q0873 Quantum Information with Integrated Photonics

Paolo Piergentili, Francesco Amanti, Greta Andrini, Fabrizio Armani, Vittorio Bellani, Vincenzo Bonaiuto, Simone Cammarata, Matteo Campostrini et al..
Journal article | 2023 | Applied Sciences | vol. 14 | no. 1 | pp. 387.
Identifier and resource: [10.3390/app14010387](https://doi.org/10.3390/app14010387).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fapp14010387); retrieved 2026-10-08.

#### Q0874 ScAlN integrated quantum photonics

Zetian Mi.
Conference paper | 2023 | Quantum Sensing and Nano Electronics and Photonics XIX | pp. 1.
Identifier and resource: [10.1117/12.2646611](https://doi.org/10.1117/12.2646611).
Conference metadata: Quantum Sensing and Nano Electronics and Photonics XIX.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2646611); retrieved 2026-10-08.

#### Q0875 Silicon Nitride Integrated Quantum Photonics

Khaled Mnaymneh, Edith Yeung, David B. Northeast, Jeongwan Jin, Patrick Laferrière, Sofiane Haffouz, Philip J. Poole, Dan Dalacu et al..
Conference paper | 2023 | 2023 23rd International Conference on Transparent Optical Networks (ICTON) | pp. 1-3.
Identifier and resource: [10.1109/icton59386.2023.10207494](https://doi.org/10.1109/icton59386.2023.10207494).
Conference metadata: 2023 23rd International Conference on Transparent Optical Networks (ICTON).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficton59386.2023.10207494); retrieved 2026-10-08.

#### Q0876 2022 Roadmap on integrated quantum photonics

Galan Moody, Volker J Sorger, Daniel J Blumenthal, Paul W Juodawlkis, William Loh, Cheryl Sorace-Agaskar, Alex E Jones, Krishna C Balram et al..
Journal article | 2022 | Journal of Physics: Photonics | vol. 4 | no. 1 | pp. 012501.
Identifier and resource: [10.1088/2515-7647/ac1ef4](https://doi.org/10.1088/2515-7647/ac1ef4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2515-7647%2Fac1ef4); retrieved 2026-10-08.

### D16T04 Single photon sources and detectors

Photon sources and detectors supply and measure optical quantum resources. Efficiency, purity, timing, and indistinguishability directly influence system scale.

Fine subcategories: Heralded sources; quantum dots; SNSPDs; number resolution; efficiency.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0877 Improved Heralded Single-Photon Source with a Photon-Number-Resolving Superconducting Nanowire Detector

Samantha I. Davis, Andrew Mueller, Raju Valivarthi, Nikolai Lauk, Lautaro Narvaez, Boris Korzh, Andrew D. Beyer, Olmo Cerri et al..
Journal article | 2022 | Physical Review Applied | vol. 18 | no. 6 | article 064007.
Identifier and resource: [10.1103/physrevapplied.18.064007](https://doi.org/10.1103/physrevapplied.18.064007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.18.064007); retrieved 2026-10-08.

#### Q0878 Absolute calibration of a single-photon avalanche detector using a bright triggered single-photon source based on an InGaAs quantum dot

Hristina Georgieva, Marco López, Helmuth Hofer, Niklas Kanold, Arsenty Kaganskiy, Sven Rodt, Stephan Reitzenstein, Stefan Kück.
Journal article | 2021 | Optics Express | vol. 29 | no. 15 | pp. 23500.
Identifier and resource: [10.1364/oe.430680](https://doi.org/10.1364/oe.430680).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Foe.430680); retrieved 2026-10-08.

#### Q0879 Light Source Monitoring in Quantum Key Distribution With Single-Photon Detector at Room Temperature

Gan Wang, Zhengyu Li, Yucheng Qiao, Ziyang Chen, Xiang Peng, Hong Guo.
Journal article | 2018 | IEEE Journal of Quantum Electronics | vol. 54 | no. 3 | pp. 1-10.
Identifier and resource: [10.1109/jqe.2018.2827569](https://doi.org/10.1109/jqe.2018.2827569).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjqe.2018.2827569); retrieved 2026-10-08.

#### Q0880 A flat spectral photon flux source for single photon detector quantum efficiency calibration

Haiyong Gan, Ruoduan Sun, Nan Xu, Jianwei Li, Yanfei Wang, Guojin Feng, Chundi Zheng, Chong Ma et al..
Conference paper | 2015 | 2015 11th Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR) | pp. 1-2.
Identifier and resource: [10.1109/cleopr.2015.7375863](https://doi.org/10.1109/cleopr.2015.7375863).
Conference metadata: 2015 11th Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR).
Fine tags: efficiency.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcleopr.2015.7375863); retrieved 2026-10-08.

#### Q0881 A superconducting nanowire single-photon detector system for single-photon source characterization

C. R. Fitzpatrick, C. M. Natarajan, R. E. Warburton, G. S. Buller, B. Baek, S. Nam, S. Miki, Z. Wang et al..
Conference paper | 2010 | SPIE Proceedings | vol. 7681 | pp. 76810H.
Identifier and resource: [10.1117/12.851892](https://doi.org/10.1117/12.851892).
Conference metadata: SPIE Defense, Security, and Sensing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.851892); retrieved 2026-10-08.

#### Q0882 Quantum key distribution with a heralded single photon source and a photon number resolving detector

Tomoyuki Horikiri, Yuishi Takeno, Atsushi Yabushita, Haibo Wang, Takayoshi Kobayashi.
Conference paper | 2006 | 2006 Conference on Lasers and Electro-Optics and 2006 Quantum Electronics and Laser Science Conference | pp. 1-2.
Identifier and resource: [10.1109/cleo.2006.4628716](https://doi.org/10.1109/cleo.2006.4628716).
Conference metadata: 2006 Conference on Lasers and Electro-Optics and 2006 Quantum Electronics and Laser Science Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcleo.2006.4628716); retrieved 2026-10-08.

#### Q0883 Single photon source characterization with a superconducting single photon detector

Robert H. Hadfield, Martin J. Stevens, Steven S. Gruber, Aaron J. Miller, Robert E. Schwall, Richard P. Mirin, Sae Woo Nam.
Conference paper | 2006 | 2006 Conference on Lasers and Electro-Optics and 2006 Quantum Electronics and Laser Science Conference | pp. 1-2.
Identifier and resource: [10.1109/cleo.2006.4628701](https://doi.org/10.1109/cleo.2006.4628701).
Conference metadata: 2006 Conference on Lasers and Electro-Optics and 2006 Quantum Electronics and Laser Science Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcleo.2006.4628701); retrieved 2026-10-08.

#### Q0884 Single photon source characterization with a superconducting single photon detector

Robert H. Hadfield, Martin J. Stevens, Steven S. Gruber, Aaron J. Miller, Robert E. Schwall, Richard P. Mirin, Sae Woo Nam.
Journal article | 2005 | Optics Express | vol. 13 | no. 26 | pp. 10846.
Identifier and resource: [10.1364/opex.13.010846](https://doi.org/10.1364/opex.13.010846).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fopex.13.010846); retrieved 2026-10-08.

### D16T05 Photonic cluster and fusion computing

Fusion based schemes combine smaller entangled states into computational resources. Loss tolerance and resource factory overhead are central design questions.

Fine subcategories: Fusion gates; graph states; resource factories; loss tolerance; multiplexing.

Primary resources: 3. Additional related assignments can be found in the interactive HTML.

#### Q0885 Next-Gen Quantum Computing—The Fusion of Atoms and Photonic Innovation

Ashok Kumar Patel, K. Saradhi, Gudditi Chetan, Ganesuni Aasish Chowdary, Beebi Naseeba, Nagendra Panini Challa.
Book chapter | 2025 | Quantum Computing | pp. 330-351.
Identifier and resource: [10.1201/9781003538950-13](https://doi.org/10.1201/9781003538950-13).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003538950-13); retrieved 2026-10-08.

#### Q0886 Tailoring Fusion-Based Photonic Quantum Computing Schemes to Quantum Emitters

Ming Lai Chan, Thomas J. Bell, Love A. Pettersson, Susan X. Chen, Patrick Yard, Anders S. Sørensen, Stefano Paesani.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 2 | article 020304.
Identifier and resource: [10.1103/prxquantum.6.020304](https://doi.org/10.1103/prxquantum.6.020304).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.6.020304); retrieved 2026-10-08.

#### Q0887 Path Qubit Fusion for Photonic Cluster State Generation

Hee Su Park, Sang Min Lee, Jaeyoon Cho, Yoonshik Kang, Sang-Kyung Choi.
Conference paper | 2011 | International Conference on Quantum Information | pp. QMI2.
Identifier and resource: [10.1364/icqi.2011.qmi2](https://doi.org/10.1364/icqi.2011.qmi2).
Conference metadata: International Conference on Quantum Information.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ficqi.2011.qmi2); retrieved 2026-10-08.

### D16T06 Squeezing and Gaussian optics

Gaussian optics controls continuous variable modes with squeezing and linear transformations. Non Gaussian resources determine capabilities beyond Gaussian simulation.

Fine subcategories: Squeezed states; optical quadratures; Gaussian transformations; homodyne detection.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0888 Hyperbolic Distance Governs Gaussian Quantum Squeezing

Kenneth A. Menard.
Posted content | 2026 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.6985762](https://doi.org/10.2139/ssrn.6985762).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.6985762); retrieved 2026-10-08.

#### Q0889 Hyperbolic Distance Governs Gaussian Quantum Squeezing

Kenneth Menard.
Posted content | 2026 | Optica Publishing Group.
Identifier and resource: [10.1364/opticaopen.32051823.v1](https://doi.org/10.1364/opticaopen.32051823.v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fopticaopen.32051823.v1); retrieved 2026-10-08.

#### Q0890 Quantum squeezing and sensing with anti-parity-time symmetric quantum optics

Shengwang Du, Chuanwei Zhang.
Conference paper | 2023 | Quantum Sensing, Imaging, and Precision Metrology | pp. 73.
Identifier and resource: [10.1117/12.2657379](https://doi.org/10.1117/12.2657379).
Conference metadata: Quantum Sensing, Imaging, and Precision Metrology.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2657379); retrieved 2026-10-08.

#### Q0891 Onset of non-Gaussian quantum physics in pulsed squeezing with mesoscopic fields

Ryotatsu Yanagimoto, Edwin Ng, Atsushi Yamamura, Tatsuhiro Onodera, Logan G. Wright, Marc Jankowski, M. M. Fejer, Peter L. McMahon et al..
Journal article | 2022 | Optica | vol. 9 | no. 4 | pp. 379.
Identifier and resource: [10.1364/optica.447782](https://doi.org/10.1364/optica.447782).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Foptica.447782); retrieved 2026-10-08.

#### Q0892 Non-Gaussian quantum states generation and robust quantum non-Gaussianity via squeezing field

Xu-Bing Tang, Fang Gao, Yao-Xiong Wang, Sen Kuang, Feng Shuang.
Journal article | 2015 | Chinese Physics B | vol. 24 | no. 3 | pp. 034208.
Identifier and resource: [10.1088/1674-1056/24/3/034208](https://doi.org/10.1088/1674-1056/24/3/034208).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2F24%2F3%2F034208); retrieved 2026-10-08.

#### Q0893 Surmounting intrinsic quantum-measurement uncertainties in Gaussian-state tomography with quadrature squeezing

Jaroslav Řeháček, Yong Siah Teo, Zdeněk Hradil, Sascha Wallentowitz.
Journal article | 2015 | Scientific Reports | vol. 5 | no. 1 | article 12289.
Identifier and resource: [10.1038/srep12289](https://doi.org/10.1038/srep12289).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fsrep12289); retrieved 2026-10-08.

#### Q0894 Gaussian entanglement for quantum key distribution from a single-mode squeezing source

Tobias Eberle, Vitus Händchen, Jörg Duhme, Torsten Franz, Fabian Furrer, Roman Schnabel, Reinhard F Werner.
Journal article | 2013 | New Journal of Physics | vol. 15 | no. 5 | pp. 053049.
Identifier and resource: [10.1088/1367-2630/15/5/053049](https://doi.org/10.1088/1367-2630/15/5/053049).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2F15%2F5%2F053049); retrieved 2026-10-08.

#### Q0895 Fisher Information and Quantum Squeezing Properties of Gaussian Pure States

Jia Qiang Zhao, Lian Zhen Cao, Huai Xin Lu.
Journal article | 2012 | Advanced Materials Research | vol. 571 | pp. 283-286.
Identifier and resource: [10.4028/www.scientific.net/amr.571.283](https://doi.org/10.4028/www.scientific.net/amr.571.283).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4028%2Fwww.scientific.net%2Famr.571.283); retrieved 2026-10-08.

## D17 Other qubit platforms and transduction

Additional platforms offer different routes to coherence, control, and connectivity. Quantum transduction connects devices that operate at different physical frequencies.

Prerequisites: Solid state or molecular physics and quantum control.

Assessment focus: Platform specific evidence, scalability, conversion efficiency, and added noise.

Primary catalog resources in this category: 57.

### D17T01 Diamond NV centers

NV centers combine electronic and nuclear spins with optical interfaces in diamond. Their computing and sensing uses should be distinguished when reading application claims.

Fine subcategories: Electronic spins; nuclear registers; optical interfaces; spin control; fabrication.

Primary resources: 14. Additional related assignments can be found in the interactive HTML.

#### Q0896 Low-Frequency Current Detection via Diamond Nitrogen-Vacancy Center Quantum Sensing

Tianfu Huang, Tongrao Lin, Xiaoxu Hu, Xiaofei Li, Han Wang.
Book chapter | 2026 | Lecture Notes in Electrical Engineering | pp. 261-268.
Identifier and resource: [10.1007/978-981-95-5304-4_23](https://doi.org/10.1007/978-981-95-5304-4_23).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-5304-4_23); retrieved 2026-10-08.

#### Q0897 Nitrogen-vacancy centers in diamond: From fundamental principles to quantum sensing

Yuehui LI, Shaobo CHENG, Chongxin SHAN.
Journal article | 2026 | Acta Physica Sinica | vol. 75 | no. 8 | article 080702.
Identifier and resource: [10.7498/aps.75.20251531](https://doi.org/10.7498/aps.75.20251531).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.75.20251531); retrieved 2026-10-08.

#### Q0898 Probing quantum resources in nitrogen-vacancy centers in diamond

Aicha Chouiba, Samira Elghaayda, Mostafa Mansour.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 21 | pp. 215108.
Identifier and resource: [10.1088/1402-4896/ae6e2d](https://doi.org/10.1088/1402-4896/ae6e2d).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae6e2d); retrieved 2026-10-08.

#### Q0899 Quantum co-magnetometer using diamond nitrogen-vacancy centers and Rubidium cells

Nir Bar-Gill.
Conference paper | 2026 | Optical Sensing and Precision Metrology II | pp. 3.
Identifier and resource: [10.1117/12.3092404](https://doi.org/10.1117/12.3092404).
Conference metadata: Optical Sensing and Precision Metrology II.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3092404); retrieved 2026-10-08.

#### Q0900 Unraveling quantum dephasing of nitrogen-vacancy center ensembles in diamond

Jixing Zhang, Cheuk Kit Cheung, Michael Kübler, Magnus Benke, Mathis Brossaud, Yihua Wang, Andrej Denisenko, Ruoming Peng et al..
Journal article | 2026 | npj Quantum Materials | vol. 11 | no. 1 | article 27.
Identifier and resource: [10.1038/s41535-026-00869-5](https://doi.org/10.1038/s41535-026-00869-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41535-026-00869-5); retrieved 2026-10-08.

#### Q0901 Oxygen-terminated hexagonal diamond (001) surfaces for nitrogen-vacancy based quantum sensors

Bo Cui, Zhaolong Sun, Wencui Xiu, You Lv, Nan Gao, Hongdong Li.
Posted content | 2025 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.5954749](https://doi.org/10.2139/ssrn.5954749).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.5954749); retrieved 2026-10-08.

#### Q0902 Design of compact integrated diamond nitrogen–vacancy center quantum probe

Sheng-Kai 圣开 Xia 夏, Wen-Tao 文韬 Lu 卢, Xu-Tong 旭彤 Zhao 赵, Ya-Wen 雅文 Xue 薛, Zeng-Bo 增博 Xu 许, Shi-Yu 仕宇 Ge 葛, Yang 洋 Wang 汪, Lin-Yan 林嫣 Yu 虞 et al..
Journal article | 2024 | Chinese Physics B | vol. 33 | no. 5 | pp. 054202.
Identifier and resource: [10.1088/1674-1056/ad2bf6](https://doi.org/10.1088/1674-1056/ad2bf6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fad2bf6); retrieved 2026-10-08.

#### Q0903 Nitrogen-terminated diamond (111) surface for nitrogen-vacancy based quantum sensors

Li Gaoxian, Cheng Wei, Gao Nan, Cheng Shaoheng, Li Hongdong.
Journal article | 2024 | Diamond and Related Materials | vol. 142 | pp. 110813 | article 110813.
Identifier and resource: [10.1016/j.diamond.2024.110813](https://doi.org/10.1016/j.diamond.2024.110813).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.diamond.2024.110813); retrieved 2026-10-08.

#### Q0904 Quantum sensing of microRNAs with nitrogen-vacancy centers in diamond

Justas Zalieckas, Martin M. Greve, Luca Bellucci, Giuseppe Sacco, Verner Håkonsen, Valentina Tozzini, Riccardo Nifosì.
Journal article | 2024 | Communications Chemistry | vol. 7 | no. 1 | article 101.
Identifier and resource: [10.1038/s42004-024-01182-7](https://doi.org/10.1038/s42004-024-01182-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42004-024-01182-7); retrieved 2026-10-08.

#### Q0905 All-optical nuclear quantum sensing using nitrogen-vacancy centers in diamond

B. Bürgler, T. F. Sjolander, O. Brinza, A. Tallaire, J. Achard, P. Maletinsky.
Journal article | 2023 | npj Quantum Information | vol. 9 | no. 1 | article 56.
Identifier and resource: [10.1038/s41534-023-00724-6](https://doi.org/10.1038/s41534-023-00724-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-023-00724-6); retrieved 2026-10-08.

#### Q0906 Fast Quantum State Tomography in the Nitrogen Vacancy Center of Diamond

Jingfu Zhang, Swathi S. Hegde, Dieter Suter.
Journal article | 2023 | Physical Review Letters | vol. 130 | no. 9 | article 090801.
Identifier and resource: [10.1103/physrevlett.130.090801](https://doi.org/10.1103/physrevlett.130.090801).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.130.090801); retrieved 2026-10-08.

#### Q0907 Fluorine-terminated diamond (110) surfaces for nitrogen-vacancy quantum sensors

Wei Shen, Gai Wu, Lijie Li, Hui Li, Sheng Liu, Shengnan Shen, Diwei Zou.
Journal article | 2022 | Carbon | vol. 193 | pp. 17-25.
Identifier and resource: [10.1016/j.carbon.2022.02.017](https://doi.org/10.1016/j.carbon.2022.02.017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.carbon.2022.02.017); retrieved 2026-10-08.

#### Q0908 Nitrogen Vacancy-Centered Diamond Qubit: The fabrication, design, and application in quantum computing

Ya-Chi Liu, Yi-Chung Dzeng, Chao-Cheng Ting.
Journal article | 2022 | IEEE Nanotechnology Magazine | vol. 16 | no. 4 | pp. 37-43.
Identifier and resource: [10.1109/mnano.2022.3175405](https://doi.org/10.1109/mnano.2022.3175405).
Fine tags: fabrication.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmnano.2022.3175405); retrieved 2026-10-08.

#### Q0909 Proximal nitrogen reduces the fluorescence quantum yield of nitrogen-vacancy centres in diamond

Marco Capelli, Lukas Lindner, Tingpeng Luo, Jan Jeske, Hiroshi Abe, Shinobu Onoda, Takeshi Ohshima, Brett Johnson et al..
Journal article | 2022 | New Journal of Physics | vol. 24 | no. 3 | pp. 033053.
Identifier and resource: [10.1088/1367-2630/ac5ca9](https://doi.org/10.1088/1367-2630/ac5ca9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fac5ca9); retrieved 2026-10-08.

### D17T02 Silicon carbide defects

Silicon carbide hosts optically addressable defects compatible with semiconductor fabrication. Coherence and interface properties depend on defect species and material quality.

Fine subcategories: Color centers; divacancies; spin photon interfaces; coherence; integration.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0910 In Silico Engineering of Defect Spins in Silicon Carbide for Solid-State Hybrid Quantum Technologies

Dang Huy Ngo, Huyen-Trang T. Le, Tien Lam Pham, Thi Minh Hoa Nghiem, Ngoc Linh Nguyen.
Journal article | 2026 | Journal of Physics: Conference Series | vol. 3284 | no. 1 | pp. 012019.
Identifier and resource: [10.1088/1742-6596/3284/1/012019](https://doi.org/10.1088/1742-6596/3284/1/012019).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F3284%2F1%2F012019); retrieved 2026-10-08.

#### Q0911 Silicon carbide turns quantum

Jörg Wrachtrup.
Journal article | 2026 | The Innovation Physics | vol. 1 | no. 1 | pp. 100003.
Identifier and resource: [10.59717/j.tip.2026.100003](https://doi.org/10.59717/j.tip.2026.100003).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.59717%2Fj.tip.2026.100003); retrieved 2026-10-08.

#### Q0912 A Suspended 4H-Silicon Carbide Membrane Platform for Defect Integration into Quantum Devices

Amberly H. Xie, Aaron M. Day, Jonathan R. Dietz, Chang Jin, Chaoshen Zhang, Eliana Mann, Zhujing Xu, Marko Loncar et al..
Journal article | 2025 | Nano Letters | vol. 25 | no. 43 | pp. 15637-15642.
Identifier and resource: [10.1021/acs.nanolett.5c04169](https://doi.org/10.1021/acs.nanolett.5c04169).
Fine tags: integration.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.nanolett.5c04169); retrieved 2026-10-08.

#### Q0913 Defects in Silicon Carbide as Quantum Qubits: Recent Advances in Defect Engineering

Ivana Capan.
Journal article | 2025 | Applied Sciences | vol. 15 | no. 10 | pp. 5606.
Identifier and resource: [10.3390/app15105606](https://doi.org/10.3390/app15105606).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fapp15105606); retrieved 2026-10-08.

#### Q0914 Wafer-scale quantum photonics in silicon carbide

Marina Radulaski.
Conference paper | 2025 | Quantum Computing, Communication, and Simulation V | pp. 23.
Identifier and resource: [10.1117/12.3042747](https://doi.org/10.1117/12.3042747).
Conference metadata: Quantum Computing, Communication, and Simulation V.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3042747); retrieved 2026-10-08.

#### Q0915 Fluorescent Silicon Carbide Quantum Dots

Mahdi Hasanzadeh Azar, Zimo Ji, Jahanbakhsh Jahanzamin, Adrian Kitai.
Book chapter | 2024 | Materials Science.
Identifier and resource: [10.5772/intechopen.1007535](https://doi.org/10.5772/intechopen.1007535).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5772%2Fintechopen.1007535); retrieved 2026-10-08.

#### Q0916 Scalable Diamond and Silicon Carbide Quantum Systems

Jelena Vuckovic, Souvik Biswas.
Conference paper | 2024 | Frontiers in Optics + Laser Science 2024 (FiO, LS) | pp. FM5A.1.
Identifier and resource: [10.1364/ls.2024.fm5a.1](https://doi.org/10.1364/ls.2024.fm5a.1).
Conference metadata: Laser Science.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fls.2024.fm5a.1); retrieved 2026-10-08.

#### Q0917 Improving Defect‐Based Quantum Emitters in Silicon Carbide via Inorganic Passivation

Mark J. Polking, Alan M. Dibos, Nathalie P. de Leon, Hongkun Park.
Journal article | 2017 | Advanced Materials | vol. 30 | no. 4 | article 1704543.
Identifier and resource: [10.1002/adma.201704543](https://doi.org/10.1002/adma.201704543).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fadma.201704543); retrieved 2026-10-08.

### D17T03 Topological superconducting devices

Majorana proposals seek protected operations using topological superconductivity. Device observations, zero mode interpretation, and demonstrated logical operations require separate evidence.

Fine subcategories: Zero mode evidence; parity measurement; braiding proposals; poisoning; experimental ambiguity.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0918 Complete description of fault-tolerant quantum gate operations for topological Majorana qubit systems

Adrian D. Scheppe, Michael V. Pak.
Journal article | 2022 | Physical Review A | vol. 105 | no. 1 | article 012415.
Identifier and resource: [10.1103/physreva.105.012415](https://doi.org/10.1103/physreva.105.012415).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.105.012415); retrieved 2026-10-08.

#### Q0919 Manipulation of Majorana-Kramers qubit and its tolerance in time-reversal invariant topological superconductor

Yuki Tanaka, Takumi Sanno, Takeshi Mizushima, Satoshi Fujimoto.
Journal article | 2022 | Physical Review B | vol. 106 | no. 1 | article 014522.
Identifier and resource: [10.1103/physrevb.106.014522](https://doi.org/10.1103/physrevb.106.014522).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.106.014522); retrieved 2026-10-08.

#### Q0920 Transport Theory for Topological Josephson Junctions with a Majorana Qubit

Zhi Wang, Jia-Jin Feng, Zhao Huang, Qian Niu.
Journal article | 2022 | Physical Review Letters | vol. 129 | no. 25 | article 257001.
Identifier and resource: [10.1103/physrevlett.129.257001](https://doi.org/10.1103/physrevlett.129.257001).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.129.257001); retrieved 2026-10-08.

#### Q0921 Z2 Topological Order and Topological Protection of Majorana Fermion Qubits

Rukhsan Ul Haq, Louis H. Kauffman.
Journal article | 2021 | Condensed Matter | vol. 6 | no. 1 | pp. 11.
Identifier and resource: [10.3390/condmat6010011](https://doi.org/10.3390/condmat6010011).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fcondmat6010011); retrieved 2026-10-08.

#### Q0922 Majorana qubits for topological quantum computing

Ramón Aguado, Leo P. Kouwenhoven.
Journal article | 2020 | Physics Today | vol. 73 | no. 6 | pp. 44-50.
Identifier and resource: [10.1063/pt.3.4499](https://doi.org/10.1063/pt.3.4499).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2Fpt.3.4499); retrieved 2026-10-08.

#### Q0923 Phonon-induced Majorana qubit relaxation in tunnel-coupled two-island topological superconductors

Yang Song, S. Das Sarma.
Journal article | 2018 | Physical Review B | vol. 98 | no. 7 | article 075159.
Identifier and resource: [10.1103/physrevb.98.075159](https://doi.org/10.1103/physrevb.98.075159).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.98.075159); retrieved 2026-10-08.

#### Q0924 Quantum simulation of topological Majorana bound states and their universal quantum operations using charge-qubit arrays

Ting Mao, Z. D. Wang.
Journal article | 2015 | Physical Review A | vol. 91 | no. 1 | article 012336.
Identifier and resource: [10.1103/physreva.91.012336](https://doi.org/10.1103/physreva.91.012336).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.91.012336); retrieved 2026-10-08.

#### Q0925 Topological protection of Majorana qubits

Meng Cheng, Roman M. Lutchyn, S. Das Sarma.
Journal article | 2012 | Physical Review B | vol. 85 | no. 16 | article 165124.
Identifier and resource: [10.1103/physrevb.85.165124](https://doi.org/10.1103/physrevb.85.165124).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.85.165124); retrieved 2026-10-08.

### D17T04 Molecular and nuclear spin processors

Molecular and NMR approaches manipulate coupled spin registers. Ensemble demonstrations can teach control and algorithms while facing distinct scalability limits.

Fine subcategories: NMR; molecular qubits; ensemble control; scalability limitations; spin registers.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0926 IMPLEMENTATION OF QUANTUM COMPUTING BASED ON PERSONAL QUANTUM COMPUTERS USING NUCLEAR MAGNETIC RESONANCE

MIREA – Russian Technology University, Moscow, Russia, Vitaly A. Peleshenko.
Journal article | 2024 | SOFT MEASUREMENTS AND COMPUTING | vol. 3 | no. 76 | pp. 14-34.
Identifier and resource: [10.36871/2618-9976.2024.03.002](https://doi.org/10.36871/2618-9976.2024.03.002).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.36871%2F2618-9976.2024.03.002); retrieved 2026-10-08.

#### Q0927 Nuclear Magnetic Resonance Quantum Computing

Chuck Easttom.
Book chapter | 2024 | Hardware for Quantum Computing | pp. 75-82.
Identifier and resource: [10.1007/978-3-031-66477-9_6](https://doi.org/10.1007/978-3-031-66477-9_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-66477-9_6); retrieved 2026-10-08.

#### Q0928 Advancements in predictive modeling of nuclear magnetic resonance parameters: integrating quantum mechanics, machine learning, and quantum computing

Jonhariono Sihotang, Patrisius Michaud Felix Marsoit.
Journal article | 2022 | Vertex | vol. 12 | no. 1 | pp. 20-29.
Identifier and resource: [10.35335/qc6shb61](https://doi.org/10.35335/qc6shb61).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.35335%2Fqc6shb61); retrieved 2026-10-08.

#### Q0929 From molecular quantum electrodynamics at finite temperatures to nuclear magnetic resonance

Kolja Them.
Journal article | 2021 | Journal of Physics Communications | vol. 5 | no. 2 | pp. 025011.
Identifier and resource: [10.1088/2399-6528/abd8c3](https://doi.org/10.1088/2399-6528/abd8c3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2399-6528%2Fabd8c3); retrieved 2026-10-08.

#### Q0930 Quantum simulations with nuclear magnetic resonance system*

Chudan Qiu, Xinfang Nie, Dawei Lu.
Journal article | 2021 | Chinese Physics B | vol. 30 | no. 4 | pp. 048201.
Identifier and resource: [10.1088/1674-1056/abe299](https://doi.org/10.1088/1674-1056/abe299).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fabe299); retrieved 2026-10-08.

#### Q0931 Nuclear magnetic resonance for quantum computing: Techniques and recent achievements

Tao Xin, Bi-Xue Wang, Ke-Ren Li, Xiang-Yu Kong, Shi-Jie Wei, Tao Wang, Dong Ruan, Gui-Lu Long.
Journal article | 2018 | Chinese Physics B | vol. 27 | no. 2 | pp. 020308.
Identifier and resource: [10.1088/1674-1056/27/2/020308](https://doi.org/10.1088/1674-1056/27/2/020308).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2F27%2F2%2F020308); retrieved 2026-10-08.

#### Q0932 Quantum Information and Nuclear Magnetic Resonance Parameters

Jéssica B. dos R. Lino, Teodorico C. Ramalho.
Journal article | 2018 | Revista Virtual de Química | vol. 10 | no. 4 | pp. 940-962.
Identifier and resource: [10.21577/1984-6835.20180067](https://doi.org/10.21577/1984-6835.20180067).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21577%2F1984-6835.20180067); retrieved 2026-10-08.

#### Q0933 Glycosaminoglycan Monosaccharide Blocks Analysis by Quantum Mechanics, Molecular Dynamics, and Nuclear Magnetic Resonance

Sergey A. Samsonov, Stephan Theisgen, Thomas Riemer, Daniel Huster, M. Teresa Pisabarro.
Journal article | 2014 | BioMed Research International | vol. 2014 | pp. 1-11.
Identifier and resource: [10.1155/2014/808071](https://doi.org/10.1155/2014/808071).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1155%2F2014%2F808071); retrieved 2026-10-08.

### D17T05 Quantum transduction

Transducers convert quantum information between physical frequencies or platforms. Conversion efficiency and added noise jointly determine whether a link is useful.

Fine subcategories: Microwave to optical conversion; efficiency; added noise; piezoelectricity; optomechanics.

Primary resources: 19. Additional related assignments can be found in the interactive HTML.

#### Q0934 Microwave-to-optical quantum transduction of photons for quantum interconnects

Akihiko Sekine, Ryo Murakami, Yoshiyasu Doi.
Journal article | 2026 | npj Nanophotonics | vol. 3 | no. 1 | article 42.
Identifier and resource: [10.1038/s44310-026-00130-8](https://doi.org/10.1038/s44310-026-00130-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs44310-026-00130-8); retrieved 2026-10-08.

#### Q0935 Nonlinear quantum transduction of weak topological impurities

Jiahao Duan, Maomao Gong, Yongjun Cheng, Song Bin Zhang.
Journal article | 2026 | APS Open Science | vol. 1 | article 000157.
Identifier and resource: [10.1103/8tqj-y91q](https://doi.org/10.1103/8tqj-y91q).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8tqj-y91q); retrieved 2026-10-08.

#### Q0936 Quantum Transduction: Enabling Quantum Networking

Marcello Caleffi, Laura d’Avossa, Xu Han, Angela Sara Cacciapuoti.
Journal article | 2026 | IEEE Communications Surveys &amp; Tutorials | vol. 28 | pp. 4195-4214.
Identifier and resource: [10.1109/comst.2025.3631150](https://doi.org/10.1109/comst.2025.3631150).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcomst.2025.3631150); retrieved 2026-10-08.

#### Q0937 Quantum transduction via generalized continuous-variable teleportation

Quntao Zhuang.
Journal article | 2026 | Physical Review A | vol. 113 | no. 1 | article 012623.
Identifier and resource: [10.1103/qwm4-8vxd](https://doi.org/10.1103/qwm4-8vxd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fqwm4-8vxd); retrieved 2026-10-08.

#### Q0938 Quantum-memory-assisted on-demand microwave-optical transduction

Hai-Tao Tu, Kai-Yu Liao, Si-Yuan Qiu, Xiao-Hong Liu, Yi-Qi Guo, Zheng-Qi Du, Yang Xu, Xin-Ding Zhang et al..
Journal article | 2026 | Nature Communications | vol. 17 | no. 1 | article 9397.
Identifier and resource: [10.1038/s41467-026-75752-9](https://doi.org/10.1038/s41467-026-75752-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-026-75752-9); retrieved 2026-10-08.

#### Q0939 Antidegradable quantum channel with additional entanglement for quantum transduction

Changchun Zhong.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 2 | article 024065.
Identifier and resource: [10.1103/4g6d-6cmg](https://doi.org/10.1103/4g6d-6cmg).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F4g6d-6cmg); retrieved 2026-10-08.

#### Q0940 Microwave-to-optical quantum transduction with antiferromagnets

Akihiko Sekine, Ryo Murakami, Yoshiyasu Doi.
Journal article | 2025 | Physical Review B | vol. 112 | no. 9 | article 094413.
Identifier and resource: [10.1103/m52p-sp6d](https://doi.org/10.1103/m52p-sp6d).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fm52p-sp6d); retrieved 2026-10-08.

#### Q0941 Modeling Quantum Transduction for Multipartite Entanglement Distribution

Laura d'Avossa, Angela Sara Cacciapuoti, Marcello Caleffi.
Journal article | 2025 | IEEE Transactions on Communications | vol. 73 | no. 11 | pp. 11707-11721.
Identifier and resource: [10.1109/tcomm.2025.3566987](https://doi.org/10.1109/tcomm.2025.3566987).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcomm.2025.3566987); retrieved 2026-10-08.

#### Q0942 Simulation of Quantum Transduction Strategies for Quantum Networks

Laura d'Avossa, Caitao Zhan, Joaquin Chung, Rajkumar Kettimuthu, Angela Sara Cacciapuoti, Marcello Caleffi.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1274-1282.
Identifier and resource: [10.1109/qce65121.2025.00142](https://doi.org/10.1109/qce65121.2025.00142).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00142); retrieved 2026-10-08.

#### Q0943 Tunable superconducting microwave resonator for quantum transduction

Hana K. Warner, Shima Rajabali, Seunghyun Park, Nayely Rolon-Gomez, Donald Witt, Amir Yacoby, Marko Lončar.
Journal article | 2025 | EPJ Web of Conferences | vol. 335 | pp. 06012.
Identifier and resource: [10.1051/epjconf/202533506012](https://doi.org/10.1051/epjconf/202533506012).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1051%2Fepjconf%2F202533506012); retrieved 2026-10-08.

#### Q0944 A two-dimensional optomechanical crystal for quantum transduction

Felix M. Mayor, Sultan Malik, André G. Primo, Samuel Gyger, Wentao Jiang, Thiago P. M. Alegre, Amir H. Safavi-Naeini.
Conference paper | 2024 | Quantum 2.0 Conference and Exhibition | pp. QTu4A.3.
Identifier and resource: [10.1364/quantum.2024.qtu4a.3](https://doi.org/10.1364/quantum.2024.qtu4a.3).
Conference metadata: Quantum 2.0.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fquantum.2024.qtu4a.3); retrieved 2026-10-08.

#### Q0945 Efficient quantum transduction using antiferromagnetic topological insulators

Haowei Xu, Changhao Li, Guoqing Wang, Hao Tang, Paola Cappellaro, Ju Li.
Journal article | 2024 | Physical Review B | vol. 110 | no. 8 | article 085136.
Identifier and resource: [10.1103/physrevb.110.085136](https://doi.org/10.1103/physrevb.110.085136).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.110.085136); retrieved 2026-10-08.

#### Q0946 Hybrid Quantum Transduction Systems Based on Magnonic Materials

S. Kazan, N. G. Saribas, S. Ç. Yorulmaz, M. Maksutoglu, E. Avinca, F. Yıldız, S. I. Tarapov, B. Rami.
Book chapter | 2024 | NATO Science for Peace and Security Series B: Physics and Biophysics | pp. 207-219.
Identifier and resource: [10.1007/978-94-024-2254-2_10](https://doi.org/10.1007/978-94-024-2254-2_10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-94-024-2254-2_10); retrieved 2026-10-08.

#### Q0947 Quantum Transduction Models for Multipartite Entanglement Distribution

Laura d'Avossa, Angela Sara Cacciapuoti, Marcello Caleffi.
Conference paper | 2024 | 2024 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 1-8.
Identifier and resource: [10.1109/qcnc62729.2024.00011](https://doi.org/10.1109/qcnc62729.2024.00011).
Conference metadata: 2024 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc62729.2024.00011); retrieved 2026-10-08.

#### Q0948 Time-correlation Transduction in Strong-field Quantum Electrodynamics

zairui li, Wesley Sims, Mirali Shariatdoust, Gabriel Howell, Thomas Searles, Linshan Sun, Sergio Carbajo.
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-5124844/v1](https://doi.org/10.21203/rs.3.rs-5124844/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-5124844%2Fv1); retrieved 2026-10-08.

#### Q0949 MW-Magnon Systems for Quantum Transduction Applications

B. Rameev.
Conference paper | 2023 | 2023 Photonics &amp; Electromagnetics Research Symposium (PIERS) | pp. 2086-2092.
Identifier and resource: [10.1109/piers59004.2023.10221301](https://doi.org/10.1109/piers59004.2023.10221301).
Conference metadata: 2023 Photonics & Electromagnetics Research Symposium (PIERS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fpiers59004.2023.10221301); retrieved 2026-10-08.

#### Q0950 Optimized Protocols for Duplex Quantum Transduction

Zhaoyou Wang, Mengzhen Zhang, Yat Wong, Changchun Zhong, Liang Jiang.
Journal article | 2023 | Physical Review Letters | vol. 131 | no. 22 | article 220802.
Identifier and resource: [10.1103/physrevlett.131.220802](https://doi.org/10.1103/physrevlett.131.220802).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.131.220802); retrieved 2026-10-08.

#### Q0951 Python in Quantum Transduction

Erica Garcia Badaracco.
Conference paper | 2023 | Python in Quantum Transduction.
Identifier and resource: [10.2172/1974707](https://doi.org/10.2172/1974707).
Conference metadata: Python in Quantum Transduction.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F1974707); retrieved 2026-10-08.

#### Q0952 Ultrahigh-precision Mechanical Platform for Quantum Transduction

Julian Delgado.
Conference paper | 2023 | Ultrahigh-precision Mechanical Platform for Quantum Transduction.
Identifier and resource: [10.2172/1996938](https://doi.org/10.2172/1996938).
Conference metadata: Ultrahigh-precision Mechanical Platform for Quantum Transduction.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F1996938); retrieved 2026-10-08.

## D18 Control calibration and noise characterization

Control engineering links physical devices to reliable operations. A noise model should be measured and tested rather than assumed to describe all operating regimes.

Prerequisites: Control theory, stochastic processes, and experimental statistics.

Assessment focus: Model identification, robustness, drift, calibration effort, and correlated noise.

Primary catalog resources in this category: 46.

### D18T01 Optimal quantum control

Optimal control searches for pulses that implement target transformations under constraints. Robustness to parameter errors and hardware bandwidth should be tested.

Fine subcategories: GRAPE; CRAB; bandwidth constraints; robust pulse design; control landscapes.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0953 Quantum Measurement and Control

Howard M. Wiseman, Gerard J. Milburn.
Book | 2009 | Cambridge University Press.
Identifier and resource: [10.1017/cbo9780511813948](https://doi.org/10.1017/cbo9780511813948).
ISBN: 9780521804424; 9780511813948; 9781107424159.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2Fcbo9780511813948); retrieved 2026-10-08.

#### Q0954 Machine-learning optimal control pulses in an optical quantum memory experiment

Elizabeth Robertson, Luisa Esguerra, Leon Meßner, Guillermo Gallego, Janik Wolters.
Journal article | 2024 | Physical Review Applied | vol. 22 | no. 2 | article 024026.
Identifier and resource: [10.1103/physrevapplied.22.024026](https://doi.org/10.1103/physrevapplied.22.024026).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.22.024026); retrieved 2026-10-08.

#### Q0955 Machine Learning Optimal Control Pulses in an Optical Quantum Memory

Elizabeth Robertson, Luisa Esguerra, Leon Meßner, Guillermo Gallego, Janik Wolters.
Conference paper | 2023 | 2023 Conference on Lasers and Electro-Optics Europe & European Quantum Electronics Conference (CLEO/Europe-EQEC) | pp. 1-1.
Identifier and resource: [10.1109/cleo/europe-eqec57999.2023.10232106](https://doi.org/10.1109/cleo/europe-eqec57999.2023.10232106).
Conference metadata: 2023 Conference on Lasers and Electro-Optics Europe & European Quantum Electronics Conference (CLEO/Europe-EQEC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcleo%2Feurope-eqec57999.2023.10232106); retrieved 2026-10-08.

#### Q0956 Time-optimal control of two-level quantum systems by piecewise constant pulses

E. Dionis, D. Sugny.
Journal article | 2023 | Physical Review A | vol. 107 | no. 3 | article 032613.
Identifier and resource: [10.1103/physreva.107.032613](https://doi.org/10.1103/physreva.107.032613).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.107.032613); retrieved 2026-10-08.

#### Q0957 From Pulses to Circuits and Back Again: A Quantum Optimal Control Perspective on Variational Quantum Algorithms

Alicia B. Magann, Christian Arenz, Matthew D. Grace, Tak-San Ho, Robert L. Kosut, Jarrod R. McClean, Herschel A. Rabitz, Mohan Sarovar.
Journal article | 2021 | PRX Quantum | vol. 2 | no. 1 | article 010101.
Identifier and resource: [10.1103/prxquantum.2.010101](https://doi.org/10.1103/prxquantum.2.010101).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.2.010101); retrieved 2026-10-08.

#### Q0958 Optimal control of quantum systems with ultrashort laser pulses and non-adiabatic interactions

José L. Sanz-Vicario, Mariana Ramírez Quiceno.
Conference paper | 2018 | Active Photonic Platforms X | pp. 85.
Identifier and resource: [10.1117/12.2320752](https://doi.org/10.1117/12.2320752).
Conference metadata: Active Photonic Platforms X.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2320752); retrieved 2026-10-08.

#### Q0959 Errors in quantum optimal control and strategy for the search of easily implementable control pulses

Antonio Negretti, Rosario Fazio, Tommaso Calarco.
Journal article | 2011 | Journal of Physics B: Atomic, Molecular and Optical Physics | vol. 44 | no. 15 | pp. 154012.
Identifier and resource: [10.1088/0953-4075/44/15/154012](https://doi.org/10.1088/0953-4075/44/15/154012).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F0953-4075%2F44%2F15%2F154012); retrieved 2026-10-08.

#### Q0960 Optimal Control of Quantum Rings by Terahertz Laser Pulses

E. Räsänen, A. Castro, J. Werschnik, A. Rubio, E. K. U. Gross.
Journal article | 2007 | Physical Review Letters | vol. 98 | no. 15 | article 157404.
Identifier and resource: [10.1103/physrevlett.98.157404](https://doi.org/10.1103/physrevlett.98.157404).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.98.157404); retrieved 2026-10-08.

### D18T02 Dynamical decoupling

Dynamical decoupling suppresses selected environmental couplings through pulse sequences. Finite pulse errors and noise spectra limit its effectiveness.

Fine subcategories: Pulse sequences; filter functions; noise spectra; randomized decoupling; storage protection.

Primary resources: 13. Additional related assignments can be found in the interactive HTML.

#### Q0961 Crosstalk-robust dynamical decoupling for bipartite-topology quantum processors

Ethan Hickman, Xiaodi Wu, Gregory Quiroz.
Journal article | 2026 | Physical Review Applied | vol. 25 | no. 6 | article 064041.
Identifier and resource: [10.1103/r75m-b2d9](https://doi.org/10.1103/r75m-b2d9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fr75m-b2d9); retrieved 2026-10-08.

#### Q0962 Dynamical decoupling for quantum metrology with periodically driven Hamiltonians

Qifei Wei, Haorui Chen, Shengshi Pang.
Journal article | 2026 | Physical Review A | vol. 114 | no. 3 | article 032418.
Identifier and resource: [10.1103/lb42-hr34](https://doi.org/10.1103/lb42-hr34).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Flb42-hr34); retrieved 2026-10-08.

#### Q0963 Bath dynamical decoupling with a quantum channel

Alexander Hahn, Kazuya Yuasa, Daniel Burgarth.
Journal article | 2025 | Journal of Physics A: Mathematical and Theoretical | vol. 58 | no. 4 | pp. 045305.
Identifier and resource: [10.1088/1751-8121/ada219](https://doi.org/10.1088/1751-8121/ada219).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1751-8121%2Fada219); retrieved 2026-10-08.

#### Q0964 Dynamical-decoupling-protected unconventional nonadiabatic geometric quantum computation

Xuan Wu, Long-Yi Jin, Hong-Fu Wang.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 2 | pp. 025102.
Identifier and resource: [10.1088/1402-4896/ada203](https://doi.org/10.1088/1402-4896/ada203).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fada203); retrieved 2026-10-08.

#### Q0965 Empirical Learning of Dynamical Decoupling on Quantum Processors

Christopher Tong, Helena Zhang, Bibek Pokharel.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 3 | article 030319.
Identifier and resource: [10.1103/h7pq-s159](https://doi.org/10.1103/h7pq-s159).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fh7pq-s159); retrieved 2026-10-08.

#### Q0966 Multiple quantum many-body clustering probed by dynamical decoupling

Gerónimo Sequeiros, Claudia M. Sánchez, Lisandro Buljubasich, Ana K. Chattah, Horacio M. Pastawski, Rodolfo H. Acosta.
Journal article | 2025 | Physical Review A | vol. 112 | no. 2 | article 022617.
Identifier and resource: [10.1103/q39p-yjnm](https://doi.org/10.1103/q39p-yjnm).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fq39p-yjnm); retrieved 2026-10-08.

#### Q0967 Qudit Dynamical Decoupling on a Superconducting Quantum Processor

Vinay Tripathi, Noah Goss, Arian Vezvaee, Long B. Nguyen, Irfan Siddiqi, Daniel A. Lidar.
Journal article | 2025 | Physical Review Letters | vol. 134 | no. 5 | article 050601.
Identifier and resource: [10.1103/physrevlett.134.050601](https://doi.org/10.1103/physrevlett.134.050601).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.134.050601); retrieved 2026-10-08.

#### Q0968 Syncopated dynamical decoupling to suppress crosstalk in quantum circuits

Bram Evert, Zoe Gonzalez Izquierdo, James Sud, Hong-Ye Hu, Shon Grabbe, Eleanor G. Rieffel, Matthew J. Reagor, Zhihui Wang.
Journal article | 2025 | Physical Review Applied | vol. 24 | no. 4 | article 044025.
Identifier and resource: [10.1103/8lxc-lvv1](https://doi.org/10.1103/8lxc-lvv1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F8lxc-lvv1); retrieved 2026-10-08.

#### Q0969 Individually Addressed Quantum Gate Interactions Using Dynamical Decoupling

M.C. Smith, A.D. Leu, M.F. Gely, D.M. Lucas.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 3 | article 030321.
Identifier and resource: [10.1103/prxquantum.5.030321](https://doi.org/10.1103/prxquantum.5.030321).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.030321); retrieved 2026-10-08.

#### Q0970 Dynamical Decoupling (DD) to Improve Fidelity in Quantum Computing

Muhammad Haryo Ramadhani, Maman Abdurohman, Hilal H. Nuha.
Conference paper | 2023 | 2023 International Conference on Data Science and Its Applications (ICoDSA) | pp. 495-499.
Identifier and resource: [10.1109/icodsa58501.2023.10276898](https://doi.org/10.1109/icodsa58501.2023.10276898).
Conference metadata: 2023 International Conference on Data Science and Its Applications (ICoDSA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficodsa58501.2023.10276898); retrieved 2026-10-08.

#### Q0971 Quantum dynamical decoupling by shaking the close environment

Michiel Burgelman, Paolo Forni, Alain Sarlette.
Journal article | 2023 | Journal of the Franklin Institute | vol. 360 | no. 17 | pp. 14022-14074.
Identifier and resource: [10.1016/j.jfranklin.2022.08.011](https://doi.org/10.1016/j.jfranklin.2022.08.011).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.jfranklin.2022.08.011); retrieved 2026-10-08.

#### Q0972 Dynamical decoupling and NNN discrete quantum networks

Antonín Hoskovec, Igor Jex.
Journal article | 2022 | International Journal of Quantum Information | vol. 20 | no. 05 | article 2250009.
Identifier and resource: [10.1142/s0219749922500095](https://doi.org/10.1142/s0219749922500095).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0219749922500095); retrieved 2026-10-08.

#### Q0973 Preserving multilevel quantum coherence by dynamical decoupling

Xinxing Yuan, Yue Li, Mengxiang Zhang, Chang Liu, Mingdong Zhu, Xi Qin, Nikolay V. Vitanov, Yiheng Lin et al..
Journal article | 2022 | Physical Review A | vol. 106 | no. 2 | article 022412.
Identifier and resource: [10.1103/physreva.106.022412](https://doi.org/10.1103/physreva.106.022412).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.106.022412); retrieved 2026-10-08.

### D18T03 Quantum noise spectroscopy

Noise spectroscopy infers environmental fluctuations from controlled quantum probes. The reconstruction depends on filter functions and assumptions about noise statistics.

Fine subcategories: Filter functions; spectral reconstruction; correlated noise; non Gaussian noise.

Primary resources: 12. Additional related assignments can be found in the interactive HTML.

#### Q0974 Control-centric quantum noise spectroscopy of time-ordered polyspectra

Kaiah Steven, Elliot Coupe, Qi Yu, Gerardo A. Paz-Silva.
Journal article | 2026 | Physical Review A | vol. 114 | no. 3 | article 032606.
Identifier and resource: [10.1103/121q-3ddh](https://doi.org/10.1103/121q-3ddh).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F121q-3ddh); retrieved 2026-10-08.

#### Q0975 Fast, accurate, and error-resilient variational quantum noise spectroscopy

Nanako Shitara, Andrés Montoya-Castillo.
Journal article | 2026 | The Journal of Chemical Physics | vol. 164 | no. 6 | article 061101.
Identifier and resource: [10.1063/5.0312403](https://doi.org/10.1063/5.0312403).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0312403); retrieved 2026-10-08.

#### Q0976 Broadband spectroscopy of quantum noise

Yuanlong Wang, Gerardo A. Paz-Silva.
Journal article | 2025 | Physical Review A | vol. 111 | no. 5 | article 052407.
Identifier and resource: [10.1103/physreva.111.052407](https://doi.org/10.1103/physreva.111.052407).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.052407); retrieved 2026-10-08.

#### Q0977 Experimental Application of Variational Quantum Noise Spectroscopy to Nitrogen Vacancy Centers

Connor Desrosiers, Nanako Shitara, Andrés Montoya-Castillo, Shuo Sun.
Conference paper | 2025 | Frontiers in Optics + Laser Science 2025 (FiO, LS) | pp. FW7C.4.
Identifier and resource: [10.1364/fio.2025.fw7c.4](https://doi.org/10.1364/fio.2025.fw7c.4).
Conference metadata: Frontiers in Optics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ffio.2025.fw7c.4); retrieved 2026-10-08.

#### Q0978 Machine learning non-Markovian two-level quantum noise spectroscopy

Juan M. Scarpetta, John H. Reina, Morten Hjorth-Jensen.
Journal article | 2025 | Physical Review Research | vol. 7 | no. 4 | article 043285.
Identifier and resource: [10.1103/2lzl-vpjd](https://doi.org/10.1103/2lzl-vpjd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F2lzl-vpjd); retrieved 2026-10-08.

#### Q0979 Quantum noise spectroscopy by qudit spectators

Clara Javaherian, Chris Ferrie.
Journal article | 2025 | Physical Review A | vol. 112 | no. 3 | article 032411.
Identifier and resource: [10.1103/drc2-8qbg](https://doi.org/10.1103/drc2-8qbg).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fdrc2-8qbg); retrieved 2026-10-08.

#### Q0980 Characterization and mitigation of axial motion induced noise on trapped ions using quantum noise spectroscopy

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Matthew Chow, Advanced Scientific Computing Research, Vivian Maloney, Ashlyn Burch, Megan Ivory, Daniel Lobser, Gregory Quiroz et al..
Report | 2024 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/2585236](https://doi.org/10.2172/2585236).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2585236); retrieved 2026-10-08.

#### Q0981 Digital noise spectroscopy with a quantum sensor

Guoqing Wang (王国庆), Yuan Zhu, Boning Li, Changhao Li, Lorenza Viola, Alexandre Cooper, Paola Cappellaro.
Journal article | 2024 | Quantum Science and Technology | vol. 9 | no. 3 | pp. 035006.
Identifier and resource: [10.1088/2058-9565/ad3846](https://doi.org/10.1088/2058-9565/ad3846).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad3846); retrieved 2026-10-08.

#### Q0982 Electrical noise spectroscopy of magnons in a quantum Hall ferromagnet

Ravi Kumar, Saurabh Kumar Srivastav, Ujjal Roy, Jinhong Park, Christian Spånslätt, K. Watanabe, T. Taniguchi, Yuval Gefen et al..
Journal article | 2024 | Nature Communications | vol. 15 | no. 1 | article 4998.
Identifier and resource: [10.1038/s41467-024-49446-z](https://doi.org/10.1038/s41467-024-49446-z).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-024-49446-z); retrieved 2026-10-08.

#### Q0983 Quantum-Enhanced Dual-Comb Spectroscopy Beyond the Shot Noise Limit

Daniel I. Herman, Mathieu Walsh, Molly Kate Kreider, Noah Lordi, Eugene J. Tsao, Alexander J. Lind, Matthew Heyrich, Joshua Combes et al..
Conference paper | 2024 | Optica Imaging Congress 2024 (3D, AOMS, COSI, ISA, pcAOP) | pp. JTu5A.3.
Identifier and resource: [10.1364/3d.2024.jtu5a.3](https://doi.org/10.1364/3d.2024.jtu5a.3).
Conference metadata: 3D Image Acquisition and Display: Technology, Perception and Applications.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2F3d.2024.jtu5a.3); retrieved 2026-10-08.

#### Q0984 Quantum Noise Spectroscopy of Dynamical Critical Phenomena

Francisco Machado, Eugene A. Demler, Norman Y. Yao, Shubhayu Chatterjee.
Journal article | 2023 | Physical Review Letters | vol. 131 | no. 7 | article 070801.
Identifier and resource: [10.1103/physrevlett.131.070801](https://doi.org/10.1103/physrevlett.131.070801).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.131.070801); retrieved 2026-10-08.

#### Q0985 Quantum noise spectroscopy as an incoherent imaging problem

Mankei Tsang.
Journal article | 2023 | Physical Review A | vol. 107 | no. 1 | article 012611.
Identifier and resource: [10.1103/physreva.107.012611](https://doi.org/10.1103/physreva.107.012611).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.107.012611); retrieved 2026-10-08.

### D18T04 Leakage crosstalk and correlated errors

Leakage and correlated errors violate simple independent Pauli models. Detection, reset, and system context are essential for realistic reliability estimates.

Fine subcategories: Leakage detection; spectator errors; spatial correlation; temporal drift; coherent errors.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q0986 Quantum sensing in the presence of pulse errors and qubit leakage

Anonymous.
Journal article | 2026 | Physical Review Research.
Identifier and resource: [10.1103/lb3n-qply](https://doi.org/10.1103/lb3n-qply).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Flb3n-qply); retrieved 2026-10-08.

#### Q0987 Secure quantum key distribution against correlated leakage source

Jia-Xuan Li, Yang-Guang Shan, Rong Wang, Feng-Yu Lu, Zhen-Qiang Yin, Shuang Wang, Wei Chen, De-Yong He et al..
Journal article | 2026 | Science Advances | vol. 12 | no. 15 | article eaed2420.
Identifier and resource: [10.1126/sciadv.aed2420](https://doi.org/10.1126/sciadv.aed2420).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fsciadv.aed2420); retrieved 2026-10-08.

#### Q0988 Characterization of leakage errors in a transmon qubit due to resonant digital control

M. A. Castellanos-Beltran, A. J. Sirois, D. I. Olaya, J. Biesecker, S. P. Benz, P. F. Hopkins.
Journal article | 2025 | Applied Physics Letters | vol. 127 | no. 23 | article 232601.
Identifier and resource: [10.1063/5.0304764](https://doi.org/10.1063/5.0304764).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0304764); retrieved 2026-10-08.

#### Q0989 Mitigating qubit leakage errors in quantum circuits with gadgets and post-selection

Karl Mayer.
Conference paper | 2022 | 2022 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 809-809.
Identifier and resource: [10.1109/qce53715.2022.00126](https://doi.org/10.1109/qce53715.2022.00126).
Conference metadata: 2022 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce53715.2022.00126); retrieved 2026-10-08.

#### Q0990 Removing leakage-induced correlated errors in superconducting quantum error correction

M. McEwen, D. Kafri, Z. Chen, J. Atalaya, K. J. Satzinger, C. Quintana, P. V. Klimov, D. Sank et al..
Journal article | 2021 | Nature Communications | vol. 12 | no. 1 | article 1761.
Identifier and resource: [10.1038/s41467-021-21982-y](https://doi.org/10.1038/s41467-021-21982-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-021-21982-y); retrieved 2026-10-08.

#### Q0991 Protecting quantum entanglement from leakage and qubit errors via repetitive parity measurements

C. C. Bultink, T. E. O’Brien, R. Vollmer, N. Muthusubramanian, M. W. Beekman, M. A. Rol, X. Fu, B. Tarasinski et al..
Journal article | 2020 | Science Advances | vol. 6 | no. 12 | article eaay3050.
Identifier and resource: [10.1126/sciadv.aay3050](https://doi.org/10.1126/sciadv.aay3050).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fsciadv.aay3050); retrieved 2026-10-08.

#### Q0992 Leakage mitigation for quantum error correction using a mixed qubit scheme

Natalie C. Brown, Kenneth R. Brown.
Journal article | 2019 | Physical Review A | vol. 100 | no. 3 | article 032325.
Identifier and resource: [10.1103/physreva.100.032325](https://doi.org/10.1103/physreva.100.032325).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.100.032325); retrieved 2026-10-08.

#### Q0993 Tradeoff between leakage and dephasing errors in the fluxonium qubit

David A. Herrera-Martí, Ahsan Nazir, Sean D. Barrett.
Journal article | 2013 | Physical Review B | vol. 88 | no. 9 | article 094512.
Identifier and resource: [10.1103/physrevb.88.094512](https://doi.org/10.1103/physrevb.88.094512).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevb.88.094512); retrieved 2026-10-08.

### D18T05 Automated quantum calibration

Automated calibration estimates and updates control parameters from measurements. Drift, latency, identifiability, and calibration cost affect closed loop performance.

Fine subcategories: Closed loop optimization; drift tracking; parameter estimation; scheduling; calibration transfer.

Primary resources: 5. Additional related assignments can be found in the interactive HTML.

#### Q0994 Qubit-efficient quantum intrusion detection using dual-parameter encoding and multi-metric calibration

Lubna Khan, Burhan Ul Islam Khan, Aabid A. Mir, Khang Wen Goh, Dwi Sudarno Putra, Uzair Ishtiaq, Mesith Chaimanee.
Journal article | 2026 | Scientific Reports | vol. 16 | no. 1 | article 23621.
Identifier and resource: [10.1038/s41598-026-55614-6](https://doi.org/10.1038/s41598-026-55614-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-026-55614-6); retrieved 2026-10-08.

#### Q0995 CaliQEC: In-situ Qubit Calibration for Surface Code Quantum Error Correction

Xiang Fang, Keyi Yin, Yuchen Zhu, Jixuan Ruan, Dean Tullsen, Zhiding Liang, Andrew Sornborger, Ang Li et al..
Conference paper | 2025 | Proceedings of the 52nd Annual International Symposium on Computer Architecture | pp. 1402-1416.
Identifier and resource: [10.1145/3695053.3731042](https://doi.org/10.1145/3695053.3731042).
Conference metadata: ISCA '25: Proceedings of the 52nd Annual International Symposium on Computer Architecture.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3695053.3731042); retrieved 2026-10-08.

#### Q0996 Realization and Calibration of Continuously Parameterized Two-Qubit Gates on a Trapped-Ion Quantum Processor

Christopher G. Yale, Ashlyn D. Burch, Matthew N. H. Chow, Brandon P. Ruzic, Daniel S. Lobser, Brian K. McFarland, Melissa C. Revelle, Susan M. Clark.
Journal article | 2025 | IEEE Transactions on Quantum Engineering | vol. 6 | pp. 1-17.
Identifier and resource: [10.1109/tqe.2025.3600216](https://doi.org/10.1109/tqe.2025.3600216).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2025.3600216); retrieved 2026-10-08.

#### Q0997 High-Speed Calibration and Characterization of Superconducting Quantum Processors without Qubit Reset

M. Werninghaus, D.J. Egger, S. Filipp.
Journal article | 2021 | PRX Quantum | vol. 2 | no. 2 | article 020324.
Identifier and resource: [10.1103/prxquantum.2.020324](https://doi.org/10.1103/prxquantum.2.020324).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.2.020324); retrieved 2026-10-08.

#### Q0998 Autonomous calibration of single spin qubit operations

Florian Frank, Thomas Unden, Jonathan Zoller, Ressa S. Said, Tommaso Calarco, Simone Montangero, Boris Naydenov, Fedor Jelezko.
Journal article | 2017 | npj Quantum Information | vol. 3 | no. 1 | article 48.
Identifier and resource: [10.1038/s41534-017-0049-8](https://doi.org/10.1038/s41534-017-0049-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-017-0049-8); retrieved 2026-10-08.

## D19 Quantum error correction codes

Error correction encodes logical information into larger physical systems and extracts error syndromes without directly measuring the logical state. Code performance depends on the physical error model and decoder.

Prerequisites: Pauli operators, circuits, and coding theory.

Assessment focus: Code distance, check structure, physical noise, syndrome extraction, and decoding.

Primary catalog resources in this category: 54.

### D19T01 Stabilizer and CSS codes

Stabilizer and CSS constructions specify logical subspaces through commuting checks. Syndrome measurement must reveal error information without revealing the logical state.

Fine subcategories: Pauli stabilizers; CSS construction; syndrome extraction; distance; logical operators.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q0999 Quantum Error Correction

Giuliano Gadioli La Guardia.
Book | 2020 | Quantum Science and Technology.
Identifier and resource: [10.1007/978-3-030-48551-1](https://doi.org/10.1007/978-3-030-48551-1).
ISBN: 9783030485504; 9783030485511.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-48551-1); retrieved 2026-10-08.

#### Q1000 Error Correcting Codes in Quantum Theory

A. M. Steane.
Journal article | 1996 | Physical Review Letters | vol. 77 | no. 5 | pp. 793-797.
Identifier and resource: [10.1103/physrevlett.77.793](https://doi.org/10.1103/physrevlett.77.793).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FPhysRevLett.77.793); retrieved 2026-10-08.

#### Q1001 Scheme for reducing decoherence in quantum computer memory

Peter W. Shor.
Journal article | 1995 | Physical Review A | vol. 52 | no. 4 | pp. R2493-R2496.
Identifier and resource: [10.1103/physreva.52.r2493](https://doi.org/10.1103/physreva.52.r2493).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FPhysRevA.52.R2493); retrieved 2026-10-08.

#### Q1002 Exploring the relationship between twisted centralizers and stabilizer codes for quantum error correction

Galih Pradananta, Rendra Erdkhadifa.
Conference paper | 2026 | AIP Conference Proceedings | vol. 3389 | pp. 020025.
Identifier and resource: [10.1063/5.0317717](https://doi.org/10.1063/5.0317717).
Conference metadata: PROCEEDINGS OF THE 7TH INTERNATIONAL CONFERENCE OF MATHEMATICS AND MATHEMATICS EDUCATION, 2024: Enhancing and Connecting Sustainable World and Future Technologies in Research of Mathematics and Mathematics Education.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0317717); retrieved 2026-10-08.

#### Q1003 Introduction to quantum error correction with stabilizer codes

Zachary P. Bradshaw, Jeffrey J. Dale, Ethan N. Evans.
Journal article | 2026 | Annals of Physics | vol. 487 | pp. 170353 | article 170353.
Identifier and resource: [10.1016/j.aop.2026.170353](https://doi.org/10.1016/j.aop.2026.170353).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.aop.2026.170353); retrieved 2026-10-08.

#### Q1004 Advancing Quantum Reliability: A Study on Topological Codes and Stabilizer Techniques for Scalable Error Correction

Krishna Kumar.
Conference paper | 2025 | 2025 International Conference on Computing Technologies (ICOCT) | pp. 1-9.
Identifier and resource: [10.1109/icoct64433.2025.11118845](https://doi.org/10.1109/icoct64433.2025.11118845).
Conference metadata: 2025 International Conference on Computing Technologies (ICOCT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficoct64433.2025.11118845); retrieved 2026-10-08.

#### Q1005 Quantum Information Science II | Physics | MIT OpenCourseWare

Author metadata not supplied.
Course | 2018 | MIT OpenCourseWare.
Identifier and resource: [Official resource](https://ocw.mit.edu/courses/8-371x-quantum-information-science-ii-spring-2018/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://ocw.mit.edu/courses/8-371x-quantum-information-science-ii-spring-2018/); retrieved 2026-10-08.

### D19T02 Surface and toric codes

Surface and toric codes use structured local checks and topological logical operators. Thresholds depend on the noise and syndrome circuit model.

Fine subcategories: Planar patches; toric boundaries; syndrome circuits; thresholds; defects.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q1006 Surface codes: Towards practical large-scale quantum computation

Austin G. Fowler, Matteo Mariantoni, John M. Martinis, Andrew N. Cleland.
Journal article | 2012 | Physical Review A | vol. 86 | no. 3 | article 032324.
Identifier and resource: [10.1103/physreva.86.032324](https://doi.org/10.1103/physreva.86.032324).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FPhysRevA.86.032324); retrieved 2026-10-08.

#### Q1007 Quantum error correction with the surface code

Author metadata not supplied.
Book chapter | 2025 | Quantum Algorithms | pp. 320-324.
Identifier and resource: [10.1017/9781009639651.030](https://doi.org/10.1017/9781009639651.030).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1017%2F9781009639651.030); retrieved 2026-10-08.

#### Q1008 FPGA-Based Quantum Emulator for Surface Code

Youngchul Kim, Gyuil Cha.
Conference paper | 2024 | 2024 15th International Conference on Information and Communication Technology Convergence (ICTC) | pp. 1320-1324.
Identifier and resource: [10.1109/ictc62082.2024.10827261](https://doi.org/10.1109/ictc62082.2024.10827261).
Conference metadata: 2024 15th International Conference on Information and Communication Technology Convergence (ICTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fictc62082.2024.10827261); retrieved 2026-10-08.

#### Q1009 Quantum double aspects of surface code models

Alexander Cowtan, Shahn Majid.
Journal article | 2022 | Journal of Mathematical Physics | vol. 63 | no. 4 | pp. 042202.
Identifier and resource: [10.1063/5.0063768](https://doi.org/10.1063/5.0063768).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0063768); retrieved 2026-10-08.

#### Q1010 A silicon-based surface code quantum computer

Joe O’Gorman, Naomi H Nickerson, Philipp Ross, John JL Morton, Simon C Benjamin.
Journal article | 2016 | npj Quantum Information | vol. 2 | no. 1 | article 15019.
Identifier and resource: [10.1038/npjqi.2015.19](https://doi.org/10.1038/npjqi.2015.19).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fnpjqi.2015.19); retrieved 2026-10-08.

#### Q1011 A surface code quantum computer in silicon

Charles D. Hill, Eldad Peretz, Samuel J. Hile, Matthew G. House, Martin Fuechsle, Sven Rogge, Michelle Y. Simmons, Lloyd C. L. Hollenberg.
Journal article | 2015 | Science Advances | vol. 1 | no. 9 | article e1500707.
Identifier and resource: [10.1126/sciadv.1500707](https://doi.org/10.1126/sciadv.1500707).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fsciadv.1500707); retrieved 2026-10-08.

#### Q1012 INTRODUCTION TO SURFACE CODE QUANTUM COMPUTATION

YIDUN WAN.
Conference paper | 2012 | Quantum Information and Quantum Computing | pp. 63-65.
Identifier and resource: [10.1142/9789814425223_0004](https://doi.org/10.1142/9789814425223_0004).
Conference metadata: Symposium on Quantum Information and Quantum Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2F9789814425223_0004); retrieved 2026-10-08.

### D19T03 Quantum LDPC codes

Quantum LDPC codes aim for sparse checks and improved encoding efficiency. Required connectivity, measurement circuits, and decoding are important implementation constraints.

Fine subcategories: Sparse checks; hypergraph products; lifted products; bivariate bicycle codes; connectivity.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1013 ADMM Decoding of Quantum LDPC Codes

Jiaxin Lyu, Guanghui He.
Conference paper | 2026 | 2026 IEEE International Symposium on Information Theory (ISIT) | pp. 1-6.
Identifier and resource: [10.1109/isit62367.2026.11653953](https://doi.org/10.1109/isit62367.2026.11653953).
Conference metadata: 2026 IEEE International Symposium on Information Theory (ISIT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisit62367.2026.11653953); retrieved 2026-10-08.

#### Q1014 Absorbing sets in quantum LDPC codes

Kirsten D. Morris, Tefjol Pllaha, Christine A. Kelley.
Journal article | 2026 | Advances in Mathematics of Communications | vol. 23 | no. 0 | pp. 234-254.
Identifier and resource: [10.3934/amc.2026023](https://doi.org/10.3934/amc.2026023).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3934%2Famc.2026023); retrieved 2026-10-08.

#### Q1015 Breaking the Orthogonality Barrier in Quantum LDPC Codes

Kenta Kasai.
Journal article | 2026 | Quantum | vol. 10 | pp. 2205 | article 2205.
Identifier and resource: [10.22331/q-2026-09-09-2205](https://doi.org/10.22331/q-2026-09-09-2205).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-09-09-2205); retrieved 2026-10-08.

#### Q1016 Decoding correlated errors in quantum LDPC codes

Arshpreet Singh Maan, Francisco Miguel Garcia Herrero, Alexandru Paler, Valentin Savin.
Journal article | 2026 | Nature Communications | vol. 17 | no. 1 | article 3965.
Identifier and resource: [10.1038/s41467-026-70556-3](https://doi.org/10.1038/s41467-026-70556-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41467-026-70556-3); retrieved 2026-10-08.

#### Q1017 Efficient post-selection for general quantum LDPC Codes

Seok-Hyung Lee, Lucas H. English, Stephen D. Bartlett.
Journal article | 2026 | npj Quantum Information | vol. 12 | no. 1 | article 96.
Identifier and resource: [10.1038/s41534-026-01242-x](https://doi.org/10.1038/s41534-026-01242-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-026-01242-x); retrieved 2026-10-08.

#### Q1018 Quantum stabilizer and quantum LDPC codes

Ivan B. Djordjevic.
Book chapter | 2026 | Quantum Communication, Quantum Networks, and Quantum Sensing | pp. 305-365.
Identifier and resource: [10.1016/b978-0-443-40568-6.00005-7](https://doi.org/10.1016/b978-0-443-40568-6.00005-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-40568-6.00005-7); retrieved 2026-10-08.

#### Q1019 Quantum CSS LDPC Codes with Quasi-Dyadic Structure

Alessio Baldelli, Massimo Battaglioni, Paolo Santini.
Conference paper | 2025 | 2025 13th International Symposium on Topics in Coding (ISTC) | pp. 1-5.
Identifier and resource: [10.1109/istc65386.2025.11154589](https://doi.org/10.1109/istc65386.2025.11154589).
Conference metadata: 2025 13th International Symposium on Topics in Coding (ISTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fistc65386.2025.11154589); retrieved 2026-10-08.

#### Q1020 Decoding Quantum LDPC Codes Using Graph Neural Networks

Vukan Ninkovic, Ognjen Kundacina, Dejan Vukobratovic, Christian Häger, Alexandre Graell i Amat.
Conference paper | 2024 | GLOBECOM 2024 - 2024 IEEE Global Communications Conference | pp. 3479-3484.
Identifier and resource: [10.1109/globecom52923.2024.10901425](https://doi.org/10.1109/globecom52923.2024.10901425).
Conference metadata: GLOBECOM 2024 - 2024 IEEE Global Communications Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fglobecom52923.2024.10901425); retrieved 2026-10-08.

#### Q1021 Decoding Quasi-Cyclic Quantum LDPC Codes

Louis Golowich, Venkatesan Guruswami.
Conference paper | 2024 | 2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS) | pp. 344-368.
Identifier and resource: [10.1109/focs61266.2024.00029](https://doi.org/10.1109/focs61266.2024.00029).
Conference metadata: 2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ffocs61266.2024.00029); retrieved 2026-10-08.

#### Q1022 Girth Analysis of Quantum Quasi-Cyclic LDPC Codes

Farzane Amirzade, Daniel Panario, Mohammad-Reza Sadeghi.
Journal article | 2024 | Problems of Information Transmission | vol. 60 | no. 2 | pp. 71-89.
Identifier and resource: [10.1134/s0032946024020017](https://doi.org/10.1134/s0032946024020017).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs0032946024020017); retrieved 2026-10-08.

#### Q1023 New quantum LDPC codes based on Euclidean Geometry

Ya’nan Feng, Chuchen Tang, Chenming Bai.
Journal article | 2024 | Laser Physics | vol. 34 | no. 6 | pp. 065201.
Identifier and resource: [10.1088/1555-6611/ad3aed](https://doi.org/10.1088/1555-6611/ad3aed).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1555-6611%2Fad3aed); retrieved 2026-10-08.

#### Q1024 New quantum LDPC codes based on projective geometry

Chuchen Tang, Chenming Bai, Ya’nan Feng.
Journal article | 2024 | Scientific Reports | vol. 14 | no. 1 | article 17014.
Identifier and resource: [10.1038/s41598-024-67786-0](https://doi.org/10.1038/s41598-024-67786-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-024-67786-0); retrieved 2026-10-08.

#### Q1025 Quantum LDPC Codes From Intersecting Subsets

Dimiter Ostrev.
Journal article | 2024 | IEEE Transactions on Information Theory | vol. 70 | no. 8 | pp. 5692-5709.
Identifier and resource: [10.1109/tit.2024.3402091](https://doi.org/10.1109/tit.2024.3402091).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftit.2024.3402091); retrieved 2026-10-08.

#### Q1026 Rateless Protograph LDPC Codes for Quantum Key Distribution

Alberto Tarable, Rudi Paolo Paganelli, Marco Ferrari.
Journal article | 2024 | IEEE Transactions on Quantum Engineering | vol. 5 | pp. 1-11.
Identifier and resource: [10.1109/tqe.2024.3361810](https://doi.org/10.1109/tqe.2024.3361810).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2024.3361810); retrieved 2026-10-08.

#### Q1027 Single-Shot Decoding of Good Quantum LDPC Codes

Shouzhen Gu, Eugene Tang, Libor Caha, Shin Ho Choe, Zhiyang He, Aleksander Kubica.
Journal article | 2024 | Communications in Mathematical Physics | vol. 405 | no. 3 | article 85.
Identifier and resource: [10.1007/s00220-024-04951-6](https://doi.org/10.1007/s00220-024-04951-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00220-024-04951-6); retrieved 2026-10-08.

#### Q1028 Viderman's algorithm for quantum LDPC codes

Anirudh Krishna, Inbal Livni Navon, Mary Wootters.
Book chapter | 2024 | Proceedings of the 2024 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | pp. 2481-2507.
Identifier and resource: [10.1137/1.9781611977912.88](https://doi.org/10.1137/1.9781611977912.88).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F1.9781611977912.88); retrieved 2026-10-08.

### D19T04 Bosonic error correction

Bosonic codes encode a logical system into oscillator states. Photon loss, finite energy, state preparation, and syndrome extraction determine protection.

Fine subcategories: Cat codes; GKP codes; binomial codes; oscillators; photon loss.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1029 Bosonic quantum error correction with microwave cavities for quantum repeaters

S. Siddardha Chelluri, Sanchar Sharma, Frank Schmidt, Silvia Viola Kusminskiy, Peter van Loock.
Journal article | 2026 | Physical Review A | vol. 114 | no. 1 | article 012616.
Identifier and resource: [10.1103/hkvx-rks6](https://doi.org/10.1103/hkvx-rks6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fhkvx-rks6); retrieved 2026-10-08.

#### Q1030 Holonomic quantum gates via continuous measurement in bosonic codes: GKP and cat states

Juan Garcia Nila, Anirudh Lanka, Todd Brun.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-10693919/v1](https://doi.org/10.21203/rs.3.rs-10693919/v1).
Fine tags: Cat codes; GKP codes.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-10693919%2Fv1); retrieved 2026-10-08.

#### Q1031 Temporal Susceptibility Feedback for Hardware-efficient Bosonic Quantum Error Correction beyond Markovian Approximation

Isamu Ohnishi.
Posted content | 2026 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.7422499](https://doi.org/10.2139/ssrn.7422499).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.7422499); retrieved 2026-10-08.

#### Q1032 Bosonic quantum error correction using squeezed Fock states

E. N. Bashmakova, S. B. Korolev, T. Yu. Golubeva.
Journal article | 2025 | Physical Review A | vol. 112 | no. 3 | article 032434.
Identifier and resource: [10.1103/97yt-nzg2](https://doi.org/10.1103/97yt-nzg2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F97yt-nzg2); retrieved 2026-10-08.

#### Q1033 Bosonic quantum error correction with neutral atoms in optical dipole traps

Leon H. Bohnmann, David F. Locher, Johannes Zeiher, Markus Müller.
Journal article | 2025 | Physical Review A | vol. 111 | no. 2 | article 022432.
Identifier and resource: [10.1103/physreva.111.022432](https://doi.org/10.1103/physreva.111.022432).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.111.022432); retrieved 2026-10-08.

#### Q1034 Hardware-efficient quantum error correction via concatenated bosonic qubits

Harald Putterman, Kyungjoo Noh, Connor T. Hann, Gregory S. MacCabe, Shahriar Aghaeimeibodi, Rishi N. Patel, Menyoung Lee, William M. Jones et al..
Journal article | 2025 | Nature | vol. 638 | no. 8052 | pp. 927-934.
Identifier and resource: [10.1038/s41586-025-08642-7](https://doi.org/10.1038/s41586-025-08642-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-025-08642-7); retrieved 2026-10-08.

#### Q1035 Quantum logic with bosonic error correction

Zhubing Jia.
Journal article | 2025 | Nature Physics | vol. 21 | no. 10 | pp. 1528-1529.
Identifier and resource: [10.1038/s41567-025-03011-7](https://doi.org/10.1038/s41567-025-03011-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-025-03011-7); retrieved 2026-10-08.

#### Q1036 Continuous-variable quantum repeaters based on bosonic error-correction and teleportation: architecture and applications

Bo-Han Wu, Zheshen Zhang, Quntao Zhuang.
Journal article | 2022 | Quantum Science and Technology | vol. 7 | no. 2 | pp. 025018.
Identifier and resource: [10.1088/2058-9565/ac4f6b](https://doi.org/10.1088/2058-9565/ac4f6b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fac4f6b); retrieved 2026-10-08.

### D19T05 Subsystem and color codes

Subsystem and color codes offer alternative check and logical gate structures. Gauge choices and measurement schedules affect both error correction and computation.

Fine subcategories: Gauge fixing; Bacon Shor; gauge color codes; transversal structure; local checks.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1037 Distributed Realization of Color Codes for Quantum Error Correction

Nitish Kumar Chandra, David Tipper, Reza Nejabati, Eneet Kaur, Kaushik P. Seshadreesan.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 2482-2492.
Identifier and resource: [10.1109/qce65121.2025.00269](https://doi.org/10.1109/qce65121.2025.00269).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00269); retrieved 2026-10-08.

#### Q1038 Decoding quantum color codes with MaxSAT

Lucas Berent, Lukas Burgholzer, Peter-Jan H.S. Derks, Jens Eisert, Robert Wille.
Journal article | 2024 | Quantum | vol. 8 | pp. 1506 | article 1506.
Identifier and resource: [10.22331/q-2024-10-23-1506](https://doi.org/10.22331/q-2024-10-23-1506).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-10-23-1506); retrieved 2026-10-08.

#### Q1039 Facilitating practical fault-tolerant quantum computing based on color codes

Jiaxuan Zhang, Yu-Chun Wu, Guo-Ping Guo.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 3 | article 033086.
Identifier and resource: [10.1103/physrevresearch.6.033086](https://doi.org/10.1103/physrevresearch.6.033086).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.033086); retrieved 2026-10-08.

#### Q1040 Construction of New Quantum Color Codes

Author metadata not supplied.
Journal article | 2022 | Quantum Physics Letters | vol. 11 | no. 3 | pp. 45-51.
Identifier and resource: [10.18576/qpl/110302](https://doi.org/10.18576/qpl/110302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.18576%2Fqpl%2F110302); retrieved 2026-10-08.

#### Q1041 Construction of new quantum color codes

Avaz Naghipour, Duc Manh Nguyen.
Posted content | 2022 | Research Square Platform LLC.
Identifier and resource: [10.21203/rs.3.rs-1633740/v1](https://doi.org/10.21203/rs.3.rs-1633740/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-1633740%2Fv1); retrieved 2026-10-08.

#### Q1042 New Quantum Color Codes Based on Hyperbolic Geometry

Avaz Naghipour, Duc Manh Nguyen.
Journal article | 2022 | Journal of Quantum Computing | vol. 4 | no. 2 | pp. 113-120.
Identifier and resource: [10.32604/jqc.2022.033712](https://doi.org/10.32604/jqc.2022.033712).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.32604%2Fjqc.2022.033712); retrieved 2026-10-08.

#### Q1043 Quantum computation with charge-and-color-permuting twists in qudit color codes

Manoj G. Gowda, Pradeep Kiran Sarvepalli.
Journal article | 2022 | Physical Review A | vol. 105 | no. 2 | article 022621.
Identifier and resource: [10.1103/physreva.105.022621](https://doi.org/10.1103/physreva.105.022621).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.105.022621); retrieved 2026-10-08.

#### Q1044 Pseudocodeword-based Decoding of Quantum Color Codes

July X. Li, Joseph M. Renes, Pascal O. Vontobel.
Conference paper | 2021 | 2021 IEEE International Symposium on Information Theory (ISIT) | pp. 1558-1563.
Identifier and resource: [10.1109/isit45174.2021.9518077](https://doi.org/10.1109/isit45174.2021.9518077).
Conference metadata: 2021 IEEE International Symposium on Information Theory (ISIT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisit45174.2021.9518077); retrieved 2026-10-08.

### D19T06 Erasure and biased noise codes

Tailored codes exploit information about erasures or noise bias. Their benefit can disappear if detection or bias assumptions fail.

Fine subcategories: Loss detection; XZZX codes; biased dephasing; erasure conversion; tailored decoding.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1045 Developments in superconducting erasure qubits for hardware-efficient quantum error correction

Maria Violaris, Luciana Henaut, James Wills, Gioele Consani, Jamie Friel, Brian Vlastakis.
Journal article | 2026 | Materials for Quantum Technology | vol. 6 | no. 3 | pp. 033001.
Identifier and resource: [10.1088/2633-4356/ae9236](https://doi.org/10.1088/2633-4356/ae9236).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2633-4356%2Fae9236); retrieved 2026-10-08.

#### Q1046 Erasure Minesweeper: Exploring Hybrid-Erasure Surface Code Architectures for Efficient Quantum Error Correction

Jason D. Chadwick, Mariesa H. Teo, Joshua Viszlai, Willers Yang, Frederic T. Chong.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 658-669.
Identifier and resource: [10.1109/qce65121.2025.00077](https://doi.org/10.1109/qce65121.2025.00077).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00077); retrieved 2026-10-08.

#### Q1047 Fault-Tolerant Quantum Architectures Based on Erasure Qubits:Optimizing Code Conversion for Biased Noise Environments

Anand Thipperudra, Randeep Singh, Shambhulinga Aralekallu.
Posted content | 2025 | Elsevier BV.
Identifier and resource: [10.2139/ssrn.5750803](https://doi.org/10.2139/ssrn.5750803).
Fine tags: erasure conversion.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2139%2Fssrn.5750803); retrieved 2026-10-08.

#### Q1048 Optimizing Quantum Error-Correction Protocols with Erasure Qubits

Shouzhen Gu, Yotam Vaknin, Alex Retzker, Aleksander Kubica.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 4 | article 040354.
Identifier and resource: [10.1103/985g-58gd](https://doi.org/10.1103/985g-58gd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F985g-58gd); retrieved 2026-10-08.

#### Q1049 Erasure Qubits for Abridged Error Correction

Matteo Rini.
Journal article | 2024 | Physics | vol. 17 | article s35.
Identifier and resource: [10.1103/physics.17.s35](https://doi.org/10.1103/physics.17.s35).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysics.17.s35); retrieved 2026-10-08.

#### Q1050 Quantum Error Correction with Metastable States of Trapped Ions Using Erasure Conversion

Mingyu Kang, Wesley C. Campbell, Kenneth R. Brown.
Journal article | 2023 | PRX Quantum | vol. 4 | no. 2 | article 020358.
Identifier and resource: [10.1103/prxquantum.4.020358](https://doi.org/10.1103/prxquantum.4.020358).
Fine tags: erasure conversion.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.4.020358); retrieved 2026-10-08.

#### Q1051 Channel Correction via Quantum Erasure

Francesco Buscemi.
Journal article | 2007 | Physical Review Letters | vol. 99 | no. 18 | article 180501.
Identifier and resource: [10.1103/physrevlett.99.180501](https://doi.org/10.1103/physrevlett.99.180501).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.99.180501); retrieved 2026-10-08.

#### Q1052 Landauer's erasure, error correction and entanglement

Vlatko Vedral.
Journal article | 2000 | Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences | vol. 456 | no. 1996 | pp. 969-984.
Identifier and resource: [10.1098/rspa.2000.0545](https://doi.org/10.1098/rspa.2000.0545).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1098%2Frspa.2000.0545); retrieved 2026-10-08.

## D20 Fault tolerance and logical operations

Fault tolerance ensures that errors during correction and computation do not spread uncontrollably. Logical gates and routing must be evaluated with the entire correction cycle.

Prerequisites: Quantum error correction and logical circuits.

Assessment focus: Logical error budgets, gate factories, connectivity, decoder latency, and runtime.

Primary catalog resources in this category: 60.

### D20T01 Thresholds and logical error scaling

Threshold analyses determine when larger encodings can suppress logical error. Finite distance performance and realistic correlations are needed for engineering decisions.

Fine subcategories: Threshold theorems; pseudothresholds; finite size scaling; correlated noise; logical error budgets.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1053 The Decade of Fault-Tolerant Quantum Computing: From Threshold Crossing to Scalable Logical Qubits

Volkan Erol.
Posted content | 2025 | MDPI AG.
Identifier and resource: [10.20944/preprints202509.2238.v1](https://doi.org/10.20944/preprints202509.2238.v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.20944%2Fpreprints202509.2238.v1); retrieved 2026-10-08.

#### Q1054 Fast universal quantum gate above the fault-tolerance threshold in silicon

Akito Noiri, Kenta Takeda, Takashi Nakajima, Takashi Kobayashi, Amir Sammak, Giordano Scappucci, Seigo Tarucha.
Journal article | 2022 | Nature | vol. 601 | no. 7893 | pp. 338-342.
Identifier and resource: [10.1038/s41586-021-04182-y](https://doi.org/10.1038/s41586-021-04182-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-021-04182-y); retrieved 2026-10-08.

#### Q1055 High-Threshold Fault-Tolerant Quantum Computation with Analog Quantum Error Correction

Kosuke Fukui, Akihisa Tomita, Atsushi Okamoto, Keisuke Fujii.
Journal article | 2018 | Physical Review X | vol. 8 | no. 2 | article 021054.
Identifier and resource: [10.1103/physrevx.8.021054](https://doi.org/10.1103/physrevx.8.021054).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.8.021054); retrieved 2026-10-08.

#### Q1056 Superconducting quantum circuits at the surface code threshold for fault tolerance

R. Barends, J. Kelly, A. Megrant, A. Veitia, D. Sank, E. Jeffrey, T. C. White, J. Mutus et al..
Journal article | 2014 | Nature | vol. 508 | no. 7497 | pp. 500-503.
Identifier and resource: [10.1038/nature13171](https://doi.org/10.1038/nature13171).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fnature13171); retrieved 2026-10-08.

#### Q1057 Error-Detection-Based Quantum Fault-Tolerance Threshold

Ben W. Reichardt.
Journal article | 2007 | Algorithmica | vol. 55 | no. 3 | pp. 517-556.
Identifier and resource: [10.1007/s00453-007-9069-7](https://doi.org/10.1007/s00453-007-9069-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs00453-007-9069-7); retrieved 2026-10-08.

#### Q1058 Fault-Tolerance Threshold for a Distance-Three Quantum Code

Ben W. Reichardt.
Book chapter | 2006 | Lecture Notes in Computer Science | pp. 50-61.
Identifier and resource: [10.1007/11786986_6](https://doi.org/10.1007/11786986_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F11786986_6); retrieved 2026-10-08.

#### Q1059 Threshold error penalty for fault-tolerant quantum computation with nearest neighbor communication

T. Szkopek, P.O. Boykin, Heng Fan, V.P. Roychowdhury, E. Yablonovitch, G. Simms, M. Gyure, B. Fong.
Journal article | 2006 | IEEE Transactions On Nanotechnology | vol. 5 | no. 1 | pp. 42-49.
Identifier and resource: [10.1109/tnano.2005.861402](https://doi.org/10.1109/tnano.2005.861402).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftnano.2005.861402); retrieved 2026-10-08.

#### Q1060 Microscopic quantum dynamics study on the noise threshold of fault-tolerant quantum error correction

Y. C. Cheng, R. J. Silbey.
Journal article | 2005 | Physical Review A | vol. 72 | no. 1 | article 012320.
Identifier and resource: [10.1103/physreva.72.012320](https://doi.org/10.1103/physreva.72.012320).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.72.012320); retrieved 2026-10-08.

### D20T02 Magic state distillation

Magic state factories produce resources for non Clifford logical gates. Distillation yield, scheduling, and physical volume can dominate a large computation.

Fine subcategories: T factories; distillation protocols; acceptance rates; factory scheduling; space time cost.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1061 Fragility of Magic State Distillation under Imperfect Measurements

Yunzhe Zheng, Yuanchen Zhao, Dong E. Liu.
Journal article | 2026 | npj Quantum Information.
Identifier and resource: [10.1038/s41534-026-01373-1](https://doi.org/10.1038/s41534-026-01373-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-026-01373-1); retrieved 2026-10-08.

#### Q1062 High-threshold magic state distillation with quantum quadratic residue codes

Michael Zurel, Santanil Jana, Nadish de Silva.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 4 | pp. 045052.
Identifier and resource: [10.1088/2058-9565/aea362](https://doi.org/10.1088/2058-9565/aea362).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faea362); retrieved 2026-10-08.

#### Q1063 Magic state injection on IBM quantum processors above the distillation threshold

Younghun Kim, Martin Sevior, Muhammad Usman.
Journal article | 2026 | Scientific Reports | vol. 16 | no. 1 | article 11189.
Identifier and resource: [10.1038/s41598-026-40381-1](https://doi.org/10.1038/s41598-026-40381-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-026-40381-1); retrieved 2026-10-08.

#### Q1064 Noise-canceling quantum feedback: Non-Hermitian dynamics with applications to state preparation and magic state distillation

Tathagata Karmakar, Philippe Lewalle, Yipei Zhang, K. Birgitta Whaley.
Journal article | 2026 | Physical Review A | vol. 113 | no. 4 | article 042403.
Identifier and resource: [10.1103/cnxj-m1wn](https://doi.org/10.1103/cnxj-m1wn).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fcnxj-m1wn); retrieved 2026-10-08.

#### Q1065 Search for high-threshold qutrit magic-state distillation routines

Shiroman Prakash, Rishabh Singhal.
Journal article | 2026 | Physical Review A | vol. 113 | no. 4 | article 042404.
Identifier and resource: [10.1103/61q5-f754](https://doi.org/10.1103/61q5-f754).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F61q5-f754); retrieved 2026-10-08.

#### Q1066 Constant-overhead magic state distillation

Adam Wills, Min-Hsiu Hsieh, Hayata Yamasaki.
Journal article | 2025 | Nature Physics | vol. 21 | no. 11 | pp. 1842-1846.
Identifier and resource: [10.1038/s41567-025-03026-0](https://doi.org/10.1038/s41567-025-03026-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-025-03026-0); retrieved 2026-10-08.

#### Q1067 Efficient Magic State Distillation by Zero-Level Distillation

Tomohiro Itogawa, Yugo Takada, Yutaka Hirano, Keisuke Fujii.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 2 | article 020356.
Identifier and resource: [10.1103/thxx-njr6](https://doi.org/10.1103/thxx-njr6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fthxx-njr6); retrieved 2026-10-08.

#### Q1068 Experimental demonstration of logical magic state distillation

Pedro Sales Rodriguez, John M. Robinson, Paul Niklas Jepsen, Zhiyang He, Casey Duckering, Chen Zhao, Kai-Hsin Wu, Joseph Campo et al..
Journal article | 2025 | Nature | vol. 645 | no. 8081 | pp. 620-625.
Identifier and resource: [10.1038/s41586-025-09367-3](https://doi.org/10.1038/s41586-025-09367-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41586-025-09367-3); retrieved 2026-10-08.

#### Q1069 From Magic State Distillation to Dynamical Systems

Yunzhe Zheng, Dong E. Liu.
Journal article | 2025 | Quantum | vol. 9 | pp. 1858 | article 1858.
Identifier and resource: [10.22331/q-2025-09-15-1858](https://doi.org/10.22331/q-2025-09-15-1858).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-09-15-1858); retrieved 2026-10-08.

#### Q1070 Low Overhead Qutrit Magic State Distillation

Shiroman Prakash, Tanay Saha.
Journal article | 2025 | Quantum | vol. 9 | pp. 1768 | article 1768.
Identifier and resource: [10.22331/q-2025-06-12-1768](https://doi.org/10.22331/q-2025-06-12-1768).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-06-12-1768); retrieved 2026-10-08.

#### Q1071 Low-Overhead Magic State Distillation with Color Codes

Seok-Hyung Lee, Felix Thomsen, Nicholas Fazio, Benjamin J. Brown, Stephen D. Bartlett.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 3 | article 030317.
Identifier and resource: [10.1103/ch5r-cnfq](https://doi.org/10.1103/ch5r-cnfq).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fch5r-cnfq); retrieved 2026-10-08.

#### Q1072 Magic State Injection on IBM Quantum Processors Above the Distillation Threshold

Younghun Kim, Martin Sevior, Muhammad Usman.
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-8303387/v1](https://doi.org/10.21203/rs.3.rs-8303387/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-8303387%2Fv1); retrieved 2026-10-08.

#### Q1073 Magic state distillation without measurements and post-selection

Sascha Heußen.
Journal article | 2025 | APL Quantum | vol. 2 | no. 4 | article 046113.
Identifier and resource: [10.1063/5.0280551](https://doi.org/10.1063/5.0280551).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0280551); retrieved 2026-10-08.

#### Q1074 Evaluation of $\vert\mathrm{Y} >$ Magic State Distillation Circuit

Youngchul Kim, Soo-Cheol Oh, Sangmin Lee, Ki-Sung Jin, Gyuil Cha.
Conference paper | 2024 | 2024 26th International Conference on Advanced Communications Technology (ICACT) | pp. 221-225.
Identifier and resource: [10.23919/icact60172.2024.10471972](https://doi.org/10.23919/icact60172.2024.10471972).
Conference metadata: 2024 26th International Conference on Advanced Communications Technology (ICACT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Ficact60172.2024.10471972); retrieved 2026-10-08.

#### Q1075 Magic State Distillation from Qudit Stabilizer Codes

Abhi Kumar Sharma, Shayan Srinivasa Garani.
Conference paper | 2024 | ICC 2024 - IEEE International Conference on Communications | pp. 1-6.
Identifier and resource: [10.1109/icc51166.2024.10623071](https://doi.org/10.1109/icc51166.2024.10623071).
Conference metadata: ICC 2024 - IEEE International Conference on Communications.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficc51166.2024.10623071); retrieved 2026-10-08.

#### Q1076 Magic State Distillation with Reduced Time Cost

Yujin Kang, Youshin Chung, Huidan Zheng, Sungyeon Kook, Jun Heo.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 416-417.
Identifier and resource: [10.1109/qce60285.2024.10333](https://doi.org/10.1109/qce60285.2024.10333).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.10333); retrieved 2026-10-08.

### D20T03 Lattice surgery

Lattice surgery implements logical parity operations through changing code boundaries. Routing and time steps must be included in algorithm mapping.

Fine subcategories: Parity measurements; patch merging; patch splitting; logical routing; surgery scheduling.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q1077 Non-Clifford quantum gate teleportation with generalized lattice surgery

Yifei Wang, Yingfei Gu.
Journal article | 2026 | Physical Review A | vol. 113 | no. 6 | article 062410.
Identifier and resource: [10.1103/1xq4-856m](https://doi.org/10.1103/1xq4-856m).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F1xq4-856m); retrieved 2026-10-08.

#### Q1078 Quantum Resource Comparison for Two Leading Surface Code Lattice Surgery Approaches

Tyler LeBlond, Ryan S. Bennink.
Journal article | 2026 | Quantum | vol. 10 | pp. 2187 | article 2187.
Identifier and resource: [10.22331/q-2026-08-10-2187](https://doi.org/10.22331/q-2026-08-10-2187).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-08-10-2187); retrieved 2026-10-08.

#### Q1079 Ultra-Low Logical Depth Fault-Tolerant Quantum Circuit Synthesis via Lattice Surgery

Chien-Tung Cherie Kuo, Cheng-En Tsai, Chung-Yang Ric Huang.
Conference paper | 2026 | 2026 Design, Automation & Test in Europe Conference (DATE) | pp. 1-7.
Identifier and resource: [10.23919/date69613.2026.11539371](https://doi.org/10.23919/date69613.2026.11539371).
Conference metadata: 2026 Design, Automation & Test in Europe Conference (DATE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Fdate69613.2026.11539371); retrieved 2026-10-08.

#### Q1080 Lattice Surgery for Dummies

Avimita Chatterjee, Subrata Das, Swaroop Ghosh.
Journal article | 2025 | Sensors | vol. 25 | no. 6 | pp. 1854.
Identifier and resource: [10.3390/s25061854](https://doi.org/10.3390/s25061854).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fs25061854); retrieved 2026-10-08.

#### Q1081 Network-Integrated Decoding System for Real-Time Quantum Error Correction with Lattice Surgery

Namitha Liyanage, Yue Wu, Emmet Houghton, Lin Zhong.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1148-1159.
Identifier and resource: [10.1109/qce65121.2025.00129](https://doi.org/10.1109/qce65121.2025.00129).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00129); retrieved 2026-10-08.

#### Q1082 Multi-FPGA System for Quantum Error Correction with Lattice Surgery

Namitha Liyanage, Yue Wu, Emmet Houghton, Lin Zhong.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 622-623.
Identifier and resource: [10.1109/qce60285.2024.10435](https://doi.org/10.1109/qce60285.2024.10435).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.10435); retrieved 2026-10-08.

#### Q1083 Lattice surgery-based logical operations in a fault-tolerant quantum software framework

Youngchul Kim, Soo-Cheol Oh, Sangmin Lee, Ki-Sung Jin, Gyuil Cha.
Conference paper | 2023 | 2023 14th International Conference on Information and Communication Technology Convergence (ICTC) | pp. 173-176.
Identifier and resource: [10.1109/ictc58733.2023.10393193](https://doi.org/10.1109/ictc58733.2023.10393193).
Conference metadata: 2023 14th International Conference on Information and Communication Technology Convergence (ICTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fictc58733.2023.10393193); retrieved 2026-10-08.

#### Q1084 Universal Quantum Computing with Twist-Free and Temporally Encoded Lattice Surgery

Christopher Chamberland, Earl T. Campbell.
Journal article | 2022 | PRX Quantum | vol. 3 | no. 1 | article 010331.
Identifier and resource: [10.1103/prxquantum.3.010331](https://doi.org/10.1103/prxquantum.3.010331).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.3.010331); retrieved 2026-10-08.

#### Q1085 Surface code quantum computing by lattice surgery

Dominic Horsman, Austin G Fowler, Simon Devitt, Rodney Van Meter.
Journal article | 2012 | New Journal of Physics | vol. 14 | no. 12 | pp. 123011.
Identifier and resource: [10.1088/1367-2630/14/12/123011](https://doi.org/10.1088/1367-2630/14/12/123011).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2F14%2F12%2F123011); retrieved 2026-10-08.

### D20T04 Transversal gates and code switching

Transversal gates and code switching manage logical operations while limiting error spread. Universality restrictions motivate combining multiple methods.

Fine subcategories: Eastin Knill limits; gauge fixing; code conversion; logical Clifford gates.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1086 Co-Designing Quantum Codes with Transversal Diagonal Gates via Multi-Agent Systems

Xi He, Sirui Lu, Bei Zeng.
Conference paper | 2026 | 2026 IEEE 19th Dallas Circuits and Systems Conference (DCAS) | pp. 1-6.
Identifier and resource: [10.1109/dcas69364.2026.11544392](https://doi.org/10.1109/dcas69364.2026.11544392).
Conference metadata: 2026 IEEE 19th Dallas Circuits and Systems Conference (DCAS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fdcas69364.2026.11544392); retrieved 2026-10-08.

#### Q1087 Homological Origin of the Transversal Implementability of Logical Diagonal Gates in Quantum CSS Codes

Junichi Haruna.
Journal article | 2026 | Progress of Theoretical and Experimental Physics | vol. 2026 | no. 8 | article 083A03.
Identifier and resource: [10.1093/ptep/ptag133](https://doi.org/10.1093/ptep/ptag133).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Fptep%2Fptag133); retrieved 2026-10-08.

#### Q1088 Asymptotically Good Quantum Codes with Transversal Non-Clifford Gates

Louis Golowich, Venkatesan Guruswami.
Conference paper | 2025 | Proceedings of the 57th Annual ACM Symposium on Theory of Computing | pp. 707-717.
Identifier and resource: [10.1145/3717823.3718234](https://doi.org/10.1145/3717823.3718234).
Conference metadata: STOC '25: 57th Annual ACM Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3717823.3718234); retrieved 2026-10-08.

#### Q1089 Near-Asymptotically-Good Quantum Codes with Transversal CCZ Gates and Sublinear-Weight Parity-Checks

Louis Golowich, Venkatesan Guruswami.
Conference paper | 2025 | 2025 IEEE 66th Annual Symposium on Foundations of Computer Science (FOCS) | pp. 1561-1569.
Identifier and resource: [10.1109/focs63196.2025.00082](https://doi.org/10.1109/focs63196.2025.00082).
Conference metadata: 2025 IEEE 66th Annual Symposium on Foundations of Computer Science (FOCS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ffocs63196.2025.00082); retrieved 2026-10-08.

#### Q1090 Permutation-Invariant Quantum Codes With Transversal Generalized Phase Gates

Eric Kubischta, Ian Teixeira.
Journal article | 2025 | IEEE Transactions on Information Theory | vol. 71 | no. 1 | pp. 485-498.
Identifier and resource: [10.1109/tit.2024.3487964](https://doi.org/10.1109/tit.2024.3487964).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftit.2024.3487964); retrieved 2026-10-08.

#### Q1091 Quantum LDPC Codes with Transversal Non-Clifford Gates via Products of Algebraic Codes

Louis Golowich, Ting-Chun Lin.
Conference paper | 2025 | Proceedings of the 57th Annual ACM Symposium on Theory of Computing | pp. 689-696.
Identifier and resource: [10.1145/3717823.3718139](https://doi.org/10.1145/3717823.3718139).
Conference metadata: STOC '25: 57th Annual ACM Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3717823.3718139); retrieved 2026-10-08.

#### Q1092 Fold-Transversal Clifford Gates for Quantum Codes

Nikolas P. Breuckmann, Simon Burton.
Journal article | 2024 | Quantum | vol. 8 | pp. 1372 | article 1372.
Identifier and resource: [10.22331/q-2024-06-13-1372](https://doi.org/10.22331/q-2024-06-13-1372).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-06-13-1372); retrieved 2026-10-08.

#### Q1093 Family of Quantum Codes with Exotic Transversal Gates

Eric Kubischta, Ian Teixeira.
Journal article | 2023 | Physical Review Letters | vol. 131 | no. 24 | article 240601.
Identifier and resource: [10.1103/physrevlett.131.240601](https://doi.org/10.1103/physrevlett.131.240601).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.131.240601); retrieved 2026-10-08.

### D20T05 Fault tolerant resource estimation

Resource estimation turns logical circuits into physical hardware and runtime requirements. Error budgets, code distance, connectivity, and factory assumptions should be explicit.

Fine subcategories: Physical qubits; logical qubits; T depth; runtime; code distance; architectural assumptions.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q1094 Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers

Shiro KAWABATA.
Journal article | 2026 | IEICE Transactions on Electronics | vol. E109.C | no. 10 | pp. 512-520 | article 2025SEI0001.
Identifier and resource: [10.1587/transele.2025sei0001](https://doi.org/10.1587/transele.2025sei0001).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1587%2Ftransele.2025sei0001); retrieved 2026-10-08.

#### Q1095 Optomechanical Resource for Fault-Tolerant Quantum Computing

Margaret Pavlovich, Peter T. Rakich, Shruti Puri.
Journal article | 2026 | PRX Quantum | vol. 7 | no. 1 | article 010316.
Identifier and resource: [10.1103/4k7h-4vwc](https://doi.org/10.1103/4k7h-4vwc).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F4k7h-4vwc); retrieved 2026-10-08.

#### Q1096 Resource Allocation for Distributed Fault-Tolerant Quantum Computing With Surface Codes

Xu Xu, Yu Liu, Yingling Mao, Yuanyuan Yang.
Conference paper | 2026 | 2026 IEEE 46th International Conference on Distributed Computing Systems (ICDCS) | pp. 1004-1014.
Identifier and resource: [10.1109/2575-8411.2026.00100](https://doi.org/10.1109/2575-8411.2026.00100).
Conference metadata: 2026 IEEE 46th International Conference on Distributed Computing Systems (ICDCS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2F2575-8411.2026.00100); retrieved 2026-10-08.

#### Q1097 Photon distillation with reduced resource costs for fault-tolerant quantum computation

Frank Somhorst, Kite Sauër, Stefan van den Hoven, Jelmer Renema.
Conference paper | 2025 | Quantum Computing, Communication, and Simulation V | pp. 79.
Identifier and resource: [10.1117/12.3041144](https://doi.org/10.1117/12.3041144).
Conference metadata: Quantum Computing, Communication, and Simulation V.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3041144); retrieved 2026-10-08.

#### Q1098 Resource-efficient fault-tolerant one-way quantum repeater with code concatenation

Kah Jen Wo, Guus Avis, Filip Rozpędek, Maria Flors Mor-Ruiz, Gregor Pieplow, Tim Schröder, Liang Jiang, Anders S. Sørensen et al..
Journal article | 2023 | npj Quantum Information | vol. 9 | no. 1 | article 123.
Identifier and resource: [10.1038/s41534-023-00792-8](https://doi.org/10.1038/s41534-023-00792-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-023-00792-8); retrieved 2026-10-08.

#### Q1099 Using Azure Quantum Resource Estimator for Assessing Performance of Fault Tolerant Quantum Computation

Wim van Dam, Mariia Mykhailova, Mathias Soeken.
Conference paper | 2023 | Proceedings of the SC '23 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis | pp. 1414-1419.
Identifier and resource: [10.1145/3624062.3624211](https://doi.org/10.1145/3624062.3624211).
Conference metadata: SC-W 2023: Workshops of The International Conference on High Performance Computing, Network, Storage, and Analysis.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3624062.3624211); retrieved 2026-10-08.

#### Q1100 Fault-Tolerant Resource Estimation of Quantum Random-Access Memories

Olivia Di Matteo, Vlad Gheorghiu, Michele Mosca.
Journal article | 2020 | IEEE Transactions on Quantum Engineering | vol. 1 | pp. 1-13.
Identifier and resource: [10.1109/tqe.2020.2965803](https://doi.org/10.1109/tqe.2020.2965803).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2020.2965803); retrieved 2026-10-08.

### D20T06 Quantum error decoding

Decoders infer likely errors from noisy syndrome data. Accuracy must be evaluated together with throughput, latency, and robustness to model mismatch.

Fine subcategories: Matching; belief propagation; union find; neural decoders; latency; streaming inference.

Primary resources: 12. Additional related assignments can be found in the interactive HTML.

#### Q1101 Backlog Metastability in Windowed Quantum Error Correction Decoding

Jean-Jacques Dubray.
Posted content | 2026 | MDPI AG.
Identifier and resource: [10.20944/preprints202608.1425.v3](https://doi.org/10.20944/preprints202608.1425.v3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.20944%2Fpreprints202608.1425.v3); retrieved 2026-10-08.

#### Q1102 Two-Stage Neural Residual Decoding for FastSurface-Code Quantum Error Correction

Jiajun Chen, Jierui Peng, Jingyi Liu.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-10123128/v1](https://doi.org/10.21203/rs.3.rs-10123128/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-10123128%2Fv1); retrieved 2026-10-08.

#### Q1103 Vibe Decoding Quantum Error Correction with CUDA

Stergios Koutsioumpas, Joschka Roffe.
Posted content | 2026 | Front Matter.
Identifier and resource: [10.59350/qxsf5-r9s02](https://doi.org/10.59350/qxsf5-r9s02).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.59350%2Fqxsf5-r9s02); retrieved 2026-10-08.

#### Q1104 Estimating decoding graphs and hypergraphs of memory quantum error-correction experiments

Evangelia Takou, Kenneth R. Brown.
Journal article | 2025 | Physical Review A | vol. 112 | no. 5 | article 052414.
Identifier and resource: [10.1103/qcz4-nx4r](https://doi.org/10.1103/qcz4-nx4r).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fqcz4-nx4r); retrieved 2026-10-08.

#### Q1105 Parallel Minimum-Weight Parity Factor Decoding for Quantum Error Correction

Liu Yang, Yue Wu, Lin Zhong.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 581-582.
Identifier and resource: [10.1109/qce60285.2024.10415](https://doi.org/10.1109/qce60285.2024.10415).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.10415); retrieved 2026-10-08.

#### Q1106 Better Than Worst-Case Decoding for Quantum Error Correction

Gokul Subramanian Ravi, Jonathan M. Baker, Arash Fayyazi, Sophia Fuhui Lin, Ali Javadi-Abhari, Massoud Pedram, Frederic T. Chong.
Conference paper | 2023 | Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2 | pp. 88-102.
Identifier and resource: [10.1145/3575693.3575733](https://doi.org/10.1145/3575693.3575733).
Conference metadata: ASPLOS '23: 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3575693.3575733); retrieved 2026-10-08.

#### Q1107 Quantum Error Correction Via Noise Guessing Decoding

Diogo Cruz, Francisco A. Monteiro, Bruno C. Coutinho.
Journal article | 2023 | IEEE Access | vol. 11 | pp. 119446-119461.
Identifier and resource: [10.1109/access.2023.3327214](https://doi.org/10.1109/access.2023.3327214).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Faccess.2023.3327214); retrieved 2026-10-08.

#### Q1108 Decoding Quantum Error Correction Codes With Local Variation

Michael Hanks, William J. Munro, Kae Nemoto.
Journal article | 2020 | IEEE Transactions on Quantum Engineering | vol. 1 | pp. 1-8.
Identifier and resource: [10.1109/tqe.2020.2967890](https://doi.org/10.1109/tqe.2020.2967890).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2020.2967890); retrieved 2026-10-08.

#### Q1109 Error correction and decoding for quantum stabilizer codes

Xiao Fang-Ying, Chen Han-Wu, School of Computer Science and Engineering, Southeast University, Nanjing 211189, China; Key Laboratory of Computer Network and Information Integration of Ministry of Education, Southeast University, Nanjing 211189, China.
Journal article | 2011 | Acta Physica Sinica | vol. 60 | no. 8 | pp. 080303.
Identifier and resource: [10.7498/aps.60.080303](https://doi.org/10.7498/aps.60.080303).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.60.080303); retrieved 2026-10-08.

#### Q1110 GitHub - oscarhiggott/PyMatching: PyMatching: A Python/C++ library for decoding quantum error correcting codes with minimum-weight perfect matching. · GitHub

Author metadata not supplied.
Software repository | Undated | PyMatching.
Identifier and resource: [Official resource](https://github.com/oscarhiggott/PyMatching).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/oscarhiggott/PyMatching); retrieved 2026-10-08.

#### Q1111 GitHub - quantumlib/Stim: A fast stabilizer circuit library. · GitHub

Author metadata not supplied.
Software repository | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://github.com/quantumlib/Stim).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/quantumlib/Stim); retrieved 2026-10-08.

#### Q1112 PyMatching 2 — PyMatching 2.1.0 documentation

Author metadata not supplied.
Documentation | Undated | PyMatching.
Identifier and resource: [Official resource](https://pymatching.readthedocs.io/en/stable/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://pymatching.readthedocs.io/en/stable/); retrieved 2026-10-08.

## D21 Error mitigation and near term reliability

Error mitigation changes estimators or experiments to reduce bias without providing the full protection of a fault tolerant encoding. Sampling overhead and assumptions must be reported.

Prerequisites: Noise channels, statistical estimation, and circuit execution.

Assessment focus: Estimator bias, variance, model mismatch, calibration drift, and shot overhead.

Primary catalog resources in this category: 39.

### D21T01 Zero noise extrapolation

Zero noise extrapolation fits results measured at increased noise to estimate a lower noise limit. Extrapolation introduces variance and model dependent bias.

Fine subcategories: Noise scaling; folding; regression; bias; variance; extrapolation failure.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1113 A useful metric for the NISQ era: Qubit error probability and its role in zero noise extrapolation

Nahual Sobrino, Unai Aseginolaza, Joaquim Jornet-Somoza, Juan Borge.
Journal article | 2026 | AVS Quantum Science | vol. 8 | no. 1 | article 013803.
Identifier and resource: [10.1116/5.0287324](https://doi.org/10.1116/5.0287324).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1116%2F5.0287324); retrieved 2026-10-08.

#### Q1114 Improving Zero-Noise Extrapolation for Quantum-Gate Error Mitigation Using a Noise-Aware Folding Method

Leanghok Hour, Myeongseong Go, Youngsun Han.
Journal article | 2026 | IEEE Access | vol. 14 | pp. 37362-37372.
Identifier and resource: [10.1109/access.2026.3672056](https://doi.org/10.1109/access.2026.3672056).
Fine tags: folding.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Faccess.2026.3672056); retrieved 2026-10-08.

#### Q1115 QNBAD: Quantum Noise-induced Backdoor Attacks against Zero Noise Extrapolation

Cheng Chu, Qian Lou, Fan Chen, Lei Jiang.
Conference paper | 2026 | Proceedings 2026 Network and Distributed System Security Symposium.
Identifier and resource: [10.14722/ndss.2026.241665](https://doi.org/10.14722/ndss.2026.241665).
Conference metadata: Network and Distributed System Security Symposium.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.14722%2Fndss.2026.241665); retrieved 2026-10-08.

#### Q1116 Quantum Noise Mitigation With Adaptive Zero-Noise Extrapolation: A Contextual Multi-Armed Bandits Approach

Ratun Rahman, Dinh C. Nguyen.
Journal article | 2026 | IEEE Journal on Selected Areas in Communications | vol. 44 | pp. 5600-5614.
Identifier and resource: [10.1109/jsac.2026.3721807](https://doi.org/10.1109/jsac.2026.3721807).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjsac.2026.3721807); retrieved 2026-10-08.

#### Q1117 Zero-noise extrapolation via cyclic permutations of quantum circuit layouts

Zahar Sayapin, Daniil Rabinovich, Nikita Korolev, Kirill Lakhmanskiy.
Journal article | 2026 | Physical Review A | vol. 114 | no. 1 | article 012620.
Identifier and resource: [10.1103/wb3p-1sm4](https://doi.org/10.1103/wb3p-1sm4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fwb3p-1sm4); retrieved 2026-10-08.

#### Q1118 A Novel Approach for Mitigating Gate- Level Noise in IBM Quantum Hardware via Zero Noise Extrapolation (ZNE) and Probabilistic Error Cancellation (PEC) Techniques

Mohammed Suhaib, V. Karthick, Monica D.
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-7883122/v1](https://doi.org/10.21203/rs.3.rs-7883122/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-7883122%2Fv1); retrieved 2026-10-08.

#### Q1119 Application of zero-noise-extrapolation-based quantum error mitigation to a silicon spin qubit

Hanseo Sohn, Jaewon Jung, Jaemin Park, Hyeongyu Jang, Lucas E. A. Stehouwer, Davide Degli Esposti, Giordano Scappucci, Dohun Kim.
Journal article | 2025 | Physical Review A | vol. 112 | no. 1 | article 012408.
Identifier and resource: [10.1103/925y-b4s1](https://doi.org/10.1103/925y-b4s1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F925y-b4s1); retrieved 2026-10-08.

#### Q1120 Digital Zero-Noise Extrapolation with Quantum Circuit Unoptimization

Elijah Pelofske, Vincent Russo.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 01-13.
Identifier and resource: [10.1109/qce65121.2025.00020](https://doi.org/10.1109/qce65121.2025.00020).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00020); retrieved 2026-10-08.

#### Q1121 Evaluating the Role of Noise Mitigation in QAOA: A Study of Zero-Noise Extrapolation and CVaR

Adriano Lusso, Marco Venere, Victor Onofre, Alberto Maldonado-Romo, Alejandro Montanez-Barrera, Marco D. Santambrogio.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 602-603.
Identifier and resource: [10.1109/qce65121.2025.10466](https://doi.org/10.1109/qce65121.2025.10466).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.10466); retrieved 2026-10-08.

#### Q1122 ML-Driven Quantum Portfolio Optimization: Hybrid CNN-LSTM Architecture with Adaptive Zero-Noise Extrapolation on NISQ Devices

Maryam Arif, Soban Saeed.
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-8423464/v1](https://doi.org/10.21203/rs.3.rs-8423464/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-8423464%2Fv1); retrieved 2026-10-08.

#### Q1123 Noise-Mitigated Variational Quantum Eigensolver with Pre-training and Zero-Noise Extrapolation

Wanqi Sun, Jungang Xu, Chenghua Duan.
Conference paper | 2025 | ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) | pp. 1-5.
Identifier and resource: [10.1109/icassp49660.2025.10887977](https://doi.org/10.1109/icassp49660.2025.10887977).
Conference metadata: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficassp49660.2025.10887977); retrieved 2026-10-08.

#### Q1124 Back Cover: Purity‐Assisted Zero‐Noise Extrapolation for Quantum Error Mitigation (Adv. Quantum Technol. 12/2024)

Tian‐Ren Jin, Yun‐Hao Shi, Zheng‐An Wang, Tian‐Ming Li, Kai Xu, Heng Fan.
Journal article | 2024 | Advanced Quantum Technologies | vol. 7 | no. 12 | article 2470037.
Identifier and resource: [10.1002/qute.202470037](https://doi.org/10.1002/qute.202470037).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202470037); retrieved 2026-10-08.

#### Q1125 Increasing the Measured Effective Quantum Volume with Zero Noise Extrapolation

Elijah Pelofske, Vincent Russo, Ryan Larose, Andrea Mari, Dan Strano, Andreas Bärtschi, Stephan Eidenbenz, William Zeng.
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 3 | pp. 1-18.
Identifier and resource: [10.1145/3680290](https://doi.org/10.1145/3680290).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3680290); retrieved 2026-10-08.

#### Q1126 Inverted-circuit zero-noise extrapolation for quantum-gate error mitigation

Kathrin F. Koenig, Finn Reinecke, Walter Hahn, Thomas Wellens.
Journal article | 2024 | Physical Review A | vol. 110 | no. 4 | article 042625.
Identifier and resource: [10.1103/physreva.110.042625](https://doi.org/10.1103/physreva.110.042625).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.042625); retrieved 2026-10-08.

#### Q1127 Mitigating quantum gate errors for variational eigensolvers using hardware-inspired zero-noise extrapolation

Alexey Uvarov, Daniil Rabinovich, Olga Lakhmanskaya, Kirill Lakhmanskiy, Jacob Biamonte, Soumik Adhikary.
Journal article | 2024 | Physical Review A | vol. 110 | no. 1 | article 012404.
Identifier and resource: [10.1103/physreva.110.012404](https://doi.org/10.1103/physreva.110.012404).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.012404); retrieved 2026-10-08.

#### Q1128 Purity‐Assisted Zero‐Noise Extrapolation for Quantum Error Mitigation

Tian‐Ren Jin, Yun‐Hao Shi, Zheng‐An Wang, Tian‐Ming Li, Kai Xu, Heng Fan.
Journal article | 2024 | Advanced Quantum Technologies | vol. 7 | no. 12 | article 2400150.
Identifier and resource: [10.1002/qute.202400150](https://doi.org/10.1002/qute.202400150).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202400150); retrieved 2026-10-08.

### D21T02 Probabilistic error cancellation

Probabilistic cancellation represents an inverse noise process through weighted sampling. Reliable channel knowledge and sampling overhead limit applicability.

Fine subcategories: Quasiprobabilities; channel learning; sampling overhead; model mismatch.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q1129 CV4Quantum: Reducing the Sampling Overhead in Probabilistic Error Cancellation

US Department of Energy, Prasanth Shyamsundar, Fermi National Accelerator Laboratory (FNAL), Batavia, IL (United States).
Report | 2025 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/2568558](https://doi.org/10.2172/2568558).
Fine tags: sampling overhead.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2568558); retrieved 2026-10-08.

#### Q1130 Variational quantum algorithms with invariant probabilistic error cancellation on noisy quantum processors

Yulin Chi, Hongyi Shi, Wen Zheng, Haoyang Cai, Yu Zhang, Xinsheng Tan, Shaoxiong Li, Jianwei Wang et al..
Journal article | 2025 | Science China Physics, Mechanics & Astronomy | vol. 69 | no. 1 | article 210312.
Identifier and resource: [10.1007/s11433-025-2779-x](https://doi.org/10.1007/s11433-025-2779-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11433-025-2779-x); retrieved 2026-10-08.

#### Q1131 Probabilistic error cancellation for dynamic quantum circuits

Riddhi S. Gupta, Ewout van den Berg, Maika Takita, Diego Ristè, Kristan Temme, Abhinav Kandala.
Journal article | 2024 | Physical Review A | vol. 109 | no. 6 | article 062617.
Identifier and resource: [10.1103/physreva.109.062617](https://doi.org/10.1103/physreva.109.062617).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.062617); retrieved 2026-10-08.

#### Q1132 Noise-Assisted Digital Quantum Simulation of Open Systems Using Partial Probabilistic Error Cancellation

José D. Guimarães, James Lim, Mikhail I. Vasilevskiy, Susana F. Huelga, Martin B. Plenio.
Journal article | 2023 | PRX Quantum | vol. 4 | no. 4 | article 040329.
Identifier and resource: [10.1103/prxquantum.4.040329](https://doi.org/10.1103/prxquantum.4.040329).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.4.040329); retrieved 2026-10-08.

#### Q1133 Probabilistic error cancellation with sparse Pauli–Lindblad models on noisy quantum processors

Ewout van den Berg, Zlatko K. Minev, Abhinav Kandala, Kristan Temme.
Journal article | 2023 | Nature Physics | vol. 19 | no. 8 | pp. 1116-1121.
Identifier and resource: [10.1038/s41567-023-02042-2](https://doi.org/10.1038/s41567-023-02042-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41567-023-02042-2); retrieved 2026-10-08.

#### Q1134 Automated quantum error mitigation based on probabilistic error reduction

Benjamin McDonough, Andrea Mari, Nathan Shammah, Nathaniel T. Stemen, Misty Wahl, William J. Zeng, Peter P. Orth.
Conference paper | 2022 | 2022 IEEE/ACM Third International Workshop on Quantum Computing Software (QCS) | pp. 83-93.
Identifier and resource: [10.1109/qcs56647.2022.00015](https://doi.org/10.1109/qcs56647.2022.00015).
Conference metadata: 2022 IEEE/ACM Third International Workshop on Quantum Computing Software (QCS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcs56647.2022.00015); retrieved 2026-10-08.

#### Q1135 Extending quantum probabilistic error cancellation by noise scaling

Andrea Mari, Nathan Shammah, William J. Zeng.
Journal article | 2021 | Physical Review A | vol. 104 | no. 5 | article 052607.
Identifier and resource: [10.1103/physreva.104.052607](https://doi.org/10.1103/physreva.104.052607).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.104.052607); retrieved 2026-10-08.

### D21T03 Readout error mitigation

Readout mitigation adjusts observed outcome statistics using a measurement error model. Correlated errors and calibration drift can invalidate simple assignment matrices.

Fine subcategories: Assignment matrices; correlated readout; unfolding; scalable calibration.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1136 Improving VQE parameter quality on noisy quantum processors with cost-effective readout error mitigation

Nacer Eddine Belaloui, Abdellah Tounsi, Abdelmouheymen Rabah Khamadja, Hamza Benkadour, Mohamed Messaoud Louamri, Achour Benslama, Mohamed Taha Rouabah.
Journal article | 2026 | Physica Scripta | vol. 101 | no. 3 | pp. 035101.
Identifier and resource: [10.1088/1402-4896/ae2f3e](https://doi.org/10.1088/1402-4896/ae2f3e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fae2f3e); retrieved 2026-10-08.

#### Q1137 Adaptive Quantum Readout Error Mitigation with Transfer Learning

Usama Inam Paracha, Syed Muhammad Abuzar Rizvi, Muhammad Mustafa Umar Gondel, Wook Park, Hyundong Shin.
Conference paper | 2024 | 2024 15th International Conference on Information and Communication Technology Convergence (ICTC) | pp. 506-511.
Identifier and resource: [10.1109/ictc62082.2024.10826964](https://doi.org/10.1109/ictc62082.2024.10826964).
Conference metadata: 2024 15th International Conference on Information and Communication Technology Convergence (ICTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fictc62082.2024.10826964); retrieved 2026-10-08.

#### Q1138 Quantum generative adversarial networks based on a readout error mitigation method with fault tolerant mechanism

Run-Sheng 润盛 Zhao 赵, Hong-Yang 鸿洋 Ma 马, Tao 涛 Cheng 程, Shuang 爽 Wang 王, Xing-Kui 兴奎 Fan 范.
Journal article | 2024 | Chinese Physics B | vol. 33 | no. 4 | pp. 040304.
Identifier and resource: [10.1088/1674-1056/ad02e7](https://doi.org/10.1088/1674-1056/ad02e7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fad02e7); retrieved 2026-10-08.

#### Q1139 SpREM: Exploiting Hamming Sparsity for Fast Quantum Readout Error Mitigation

Hanyu Zhang, Liqiang Lu, Siwei Tan, Size Zheng, Jia Yu, Jianwei Yin.
Conference paper | 2024 | Proceedings of the 61st ACM/IEEE Design Automation Conference | pp. 1-6.
Identifier and resource: [10.1145/3649329.3655675](https://doi.org/10.1145/3649329.3655675).
Conference metadata: DAC '24: 61st ACM/IEEE Design Automation Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3649329.3655675); retrieved 2026-10-08.

#### Q1140 Information-theoretic approach to readout-error mitigation for quantum computers

Hai-Chau Nguyen.
Journal article | 2023 | Physical Review A | vol. 108 | no. 5 | article 052419.
Identifier and resource: [10.1103/physreva.108.052419](https://doi.org/10.1103/physreva.108.052419).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.108.052419); retrieved 2026-10-08.

#### Q1141 Perturbative readout-error mitigation for near-term quantum computers

Evan Peters, Andy C. Y. Li, Gabriel N. Perdue.
Journal article | 2023 | Physical Review A | vol. 107 | no. 6 | article 062426.
Identifier and resource: [10.1103/physreva.107.062426](https://doi.org/10.1103/physreva.107.062426).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.107.062426); retrieved 2026-10-08.

#### Q1142 Configurable Readout Error Mitigation in Quantum Workflows

Martin Beisel, Johanna Barzen, Frank Leymann, Felix Truger, Benjamin Weder, Vladimir Yussupov.
Journal article | 2022 | Electronics | vol. 11 | no. 19 | pp. 2983.
Identifier and resource: [10.3390/electronics11192983](https://doi.org/10.3390/electronics11192983).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Felectronics11192983); retrieved 2026-10-08.

#### Q1143 Quantum readout error mitigation via deep learning

Jihye Kim, Byungdu Oh, Yonuk Chong, Euyheon Hwang, Daniel K Park.
Journal article | 2022 | New Journal of Physics | vol. 24 | no. 7 | pp. 073009.
Identifier and resource: [10.1088/1367-2630/ac7b3d](https://doi.org/10.1088/1367-2630/ac7b3d).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fac7b3d); retrieved 2026-10-08.

### D21T04 Symmetry verification and postselection

Symmetry checks reject or reweight outcomes that violate a known constraint. Acceptance probability and postselection bias must be reported.

Fine subcategories: Conserved quantities; acceptance rates; bias; verification checks.

Primary resources: 4. Additional related assignments can be found in the interactive HTML.

#### Q1144 Symmetry verification for noisy quantum simulations of non-Abelian lattice gauge theories

Edoardo Ballini, Julius Mildenberger, Matteo M. Wauters, Philipp Hauke.
Journal article | 2025 | Quantum | vol. 9 | pp. 1802 | article 1802.
Identifier and resource: [10.22331/q-2025-07-22-1802](https://doi.org/10.22331/q-2025-07-22-1802).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-07-22-1802); retrieved 2026-10-08.

#### Q1145 Circuit Symmetry Verification Mitigates Quantum-Domain Impairments

Yifeng Xiong, Daryus Chandra, Soon Xin Ng, Lajos Hanzo.
Journal article | 2023 | IEEE Transactions on Signal Processing | vol. 71 | pp. 477-493.
Identifier and resource: [10.1109/tsp.2023.3244666](https://doi.org/10.1109/tsp.2023.3244666).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftsp.2023.3244666); retrieved 2026-10-08.

#### Q1146 Experimental error mitigation via symmetry verification in a variational quantum eigensolver

R. Sagastizabal, X. Bonet-Monroig, M. Singh, M. A. Rol, C. C. Bultink, X. Fu, C. H. Price, V. P. Ostroukh et al..
Journal article | 2019 | Physical Review A | vol. 100 | no. 1 | article 010302.
Identifier and resource: [10.1103/physreva.100.010302](https://doi.org/10.1103/physreva.100.010302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.100.010302); retrieved 2026-10-08.

#### Q1147 Quantum symmetry

Murray Gerstenhaber, Anthony Giaquinto, Samuel D. Schack.
Book chapter | 1992 | Lecture Notes in Mathematics | pp. 9-46.
Identifier and resource: [10.1007/bfb0101176](https://doi.org/10.1007/bfb0101176).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbfb0101176); retrieved 2026-10-08.

### D21T05 Virtual distillation and purification

Virtual distillation uses multiple copies or related estimators to suppress some mixed state errors. Coherent errors and measurement costs remain relevant.

Fine subcategories: Multiple copies; purity estimation; coherent errors; measurement cost.

Primary resources: 4. Additional related assignments can be found in the interactive HTML.

#### Q1148 Low depth virtual distillation of quantum circuits by deterministic circuit decomposition

Akib Karim, Shaobo Zhang, Muhammad Usman.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 3 | article 033223.
Identifier and resource: [10.1103/physrevresearch.6.033223](https://doi.org/10.1103/physrevresearch.6.033223).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.033223); retrieved 2026-10-08.

#### Q1149 Study of noise in virtual distillation circuits for quantum error mitigation

Pontus Vikstål, Giulia Ferrini, Shruti Puri.
Journal article | 2024 | Quantum | vol. 8 | pp. 1441 | article 1441.
Identifier and resource: [10.22331/q-2024-08-14-1441](https://doi.org/10.22331/q-2024-08-14-1441).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-08-14-1441); retrieved 2026-10-08.

#### Q1150 Enhancing Virtual Distillation with Circuit Cutting for Quantum Error Mitigation

Peiyi Li, Ji Liu, Hrushikesh Pramod Patil, Paul Hovland, Huiyang Zhou.
Conference paper | 2023 | 2023 IEEE 41st International Conference on Computer Design (ICCD) | pp. 94-101.
Identifier and resource: [10.1109/iccd58817.2023.00024](https://doi.org/10.1109/iccd58817.2023.00024).
Conference metadata: 2023 IEEE 41st International Conference on Computer Design (ICCD).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcd58817.2023.00024); retrieved 2026-10-08.

#### Q1151 Virtual Distillation for Quantum Error Mitigation

William J. Huggins, Sam McArdle, Thomas E. O’Brien, Joonho Lee, Nicholas C. Rubin, Sergio Boixo, K. Birgitta Whaley, Ryan Babbush et al..
Journal article | 2021 | Physical Review X | vol. 11 | no. 4 | article 041036.
Identifier and resource: [10.1103/physrevx.11.041036](https://doi.org/10.1103/physrevx.11.041036).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.11.041036); retrieved 2026-10-08.

## D22 Characterization verification and benchmarks

Characterization measures device behavior; verification tests specified claims; benchmarking compares workloads. Each answers a different question and needs an appropriate uncertainty model.

Prerequisites: Quantum measurements, estimation, and statistics.

Assessment focus: Identifiability, confidence intervals, trust assumptions, and workload definition.

Primary catalog resources in this category: 50.

### D22T01 Quantum state and process tomography

Tomography reconstructs a state or channel from informationally complete data. Reconstruction method, confidence, and physical constraints affect the estimate.

Fine subcategories: Informational completeness; reconstruction; compressed sensing; confidence regions.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q1152 Efficient noisy quantum state and process tomography

Chenyang Li, Shengxin Zhuang, Yukun Zhang, Jingbo B Wang, Xiao Yuan, Yusen Wu, Chuan Wang.
Journal article | 2026 | Quantum Science and Technology.
Identifier and resource: [10.1088/2058-9565/aeae6e](https://doi.org/10.1088/2058-9565/aeae6e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faeae6e); retrieved 2026-10-08.

#### Q1153 Wigner state and process tomography on near-term quantum devices

Amit Devra, Niklas J. Glaser, Dennis Huber, Steffen J. Glaser.
Journal article | 2024 | Quantum Information Processing | vol. 23 | no. 10 | article 359.
Identifier and resource: [10.1007/s11128-024-04550-3](https://doi.org/10.1007/s11128-024-04550-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-024-04550-3); retrieved 2026-10-08.

#### Q1154 Scheme for coherent-state quantum process tomography via normally-ordered moments

M. Ghalaii, A. T. Rezakhani.
Journal article | 2017 | Physical Review A | vol. 95 | no. 3 | article 032336.
Identifier and resource: [10.1103/physreva.95.032336](https://doi.org/10.1103/physreva.95.032336).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.95.032336); retrieved 2026-10-08.

#### Q1155 Quantum state and process tomography via adaptive measurements

HengYan Wang, WenQiang Zheng, NengKun Yu, KeRen Li, DaWei Lu, Tao Xin, Carson Li, ZhengFeng Ji et al..
Journal article | 2016 | Science China Physics, Mechanics & Astronomy | vol. 59 | no. 10 | article 100313.
Identifier and resource: [10.1007/s11433-016-0287-y](https://doi.org/10.1007/s11433-016-0287-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11433-016-0287-y); retrieved 2026-10-08.

#### Q1156 Characterization of conditional state-engineering quantum processes by coherent state quantum process tomography

Merlin Cooper, Eirion Slade, Michał Karpiński, Brian J Smith.
Journal article | 2015 | New Journal of Physics | vol. 17 | no. 3 | pp. 033041.
Identifier and resource: [10.1088/1367-2630/17/3/033041](https://doi.org/10.1088/1367-2630/17/3/033041).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2F17%2F3%2F033041); retrieved 2026-10-08.

#### Q1157 Continuous-variable quantum process tomography with squeezed-state probes

Jaromír Fiurášek.
Journal article | 2015 | Physical Review A | vol. 92 | no. 2 | article 022101.
Identifier and resource: [10.1103/physreva.92.022101](https://doi.org/10.1103/physreva.92.022101).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.92.022101); retrieved 2026-10-08.

#### Q1158 Holistic Quantum State and Process Tomography

Nicolás Quesada, Agata M. Brańczyk, Daniel F.V. James.
Conference paper | 2013 | Frontiers in Optics 2013 | pp. FW1C.6.
Identifier and resource: [10.1364/fio.2013.fw1c.6](https://doi.org/10.1364/fio.2013.fw1c.6).
Conference metadata: Frontiers in Optics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ffio.2013.fw1c.6); retrieved 2026-10-08.

#### Q1159 Selective and efficient quantum state tomography and its application to quantum process tomography

Ariel Bendersky, Juan Pablo Paz.
Journal article | 2013 | Physical Review A | vol. 87 | no. 1 | article 012122.
Identifier and resource: [10.1103/physreva.87.012122](https://doi.org/10.1103/physreva.87.012122).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.87.012122); retrieved 2026-10-08.

#### Q1160 GitHub - qiskit-community/qiskit-experiments: Qiskit Experiments · GitHub

Author metadata not supplied.
Software repository | Undated | Qiskit Experiments.
Identifier and resource: [Official resource](https://github.com/Qiskit/qiskit-experiments).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/Qiskit/qiskit-experiments); retrieved 2026-10-08.

### D22T02 Randomized benchmarking

Randomized benchmarking estimates average error behavior through randomized sequences. Interpreting the fitted decay requires checking gate dependence and noise assumptions.

Fine subcategories: Clifford sequences; interleaved benchmarking; cycle benchmarking; gate dependence.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1161 Characterization of Quantum Gate Noise Using Randomized Benchmarking

Goutam Paul.
Book chapter | 2026 | Advanced Tutorials on Quantum Circuits | pp. 13-32.
Identifier and resource: [10.1201/9788743807087-3](https://doi.org/10.1201/9788743807087-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9788743807087-3); retrieved 2026-10-08.

#### Q1162 Quantum non-Markovian noise in randomized benchmarking of spin-boson models

Srilekha Gandhari, Michael J. Gullans.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 2 | article 023075.
Identifier and resource: [10.1103/z8zh-n1hl](https://doi.org/10.1103/z8zh-n1hl).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fz8zh-n1hl); retrieved 2026-10-08.

#### Q1163 Randomized benchmarking with synthetic quantum circuits

Yale Fan, Riley Murray, Thaddeus D Ladd, Kevin Young, Robin Blume-Kohout.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 3 | pp. 035052.
Identifier and resource: [10.1088/2058-9565/ae8b56](https://doi.org/10.1088/2058-9565/ae8b56).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae8b56); retrieved 2026-10-08.

#### Q1164 Fault-Detecting Randomized Benchmarking for Testing Quantum Processors

Cynthia Kuan, Cheng-Yun Hsieh, Shan-Chi Shih, James Chien-Mo Li.
Conference paper | 2025 | 2025 IEEE International Test Conference in Asia (ITC-Asia) | pp. 54-59.
Identifier and resource: [10.1109/itc-asia67627.2025.00018](https://doi.org/10.1109/itc-asia67627.2025.00018).
Conference metadata: 2025 IEEE International Test Conference in Asia (ITC-Asia).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fitc-asia67627.2025.00018); retrieved 2026-10-08.

#### Q1165 Modeling quantum volume using randomized benchmarking of Room-Temperature NV center quantum registers

Tom Jäger, MinSik Kwon, Max Keller, Rouven Maier, Nicholas Bronn, Regina Finsterhoelzl, Guido Burkard, Leon Büttner et al..
Journal article | 2025 | npj Quantum Information | vol. 12 | no. 1 | article 6.
Identifier and resource: [10.1038/s41534-025-01164-0](https://doi.org/10.1038/s41534-025-01164-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01164-0); retrieved 2026-10-08.

#### Q1166 Randomized Benchmarking of Local Zeroth-Order Optimizers for Variational Quantum Systems

Lucas Tecot, Cho-Jui Hsieh.
Conference paper | 2024 | 2024 IEEE 6th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA) | pp. 461-470.
Identifier and resource: [10.1109/tps-isa62245.2024.00062](https://doi.org/10.1109/tps-isa62245.2024.00062).
Conference metadata: 2024 IEEE 6th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftps-isa62245.2024.00062); retrieved 2026-10-08.

#### Q1167 Randomized benchmarking into the quantum advantage regime

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Jordan Hines, Advanced Scientific Computing Research, Daniel Hothem, Marie Lu, Ravi Naik, Akel Hashim, Jean-Loup Ville et al..
Report | 2023 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3023952](https://doi.org/10.2172/3023952).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3023952); retrieved 2026-10-08.

#### Q1168 Scalable Randomized Benchmarking of Quantum Computers Using Mirror Circuits

Timothy Proctor, Stefan Seritan, Kenneth Rudinger, Erik Nielsen, Robin Blume-Kohout, Kevin Young.
Journal article | 2022 | Physical Review Letters | vol. 129 | no. 15 | article 150502.
Identifier and resource: [10.1103/physrevlett.129.150502](https://doi.org/10.1103/physrevlett.129.150502).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.129.150502); retrieved 2026-10-08.

### D22T03 Gate set tomography

Gate set tomography jointly estimates operations and preparation and measurement errors. Gauge freedom means some fitted quantities are not uniquely identifiable.

Fine subcategories: Self consistency; gauge freedom; SPAM; long sequence experiments.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1169 A Diary of a Faulty Logical Qubit: Logical Gate Set Tomography

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Aliza Siddiqui, Intelligence Advanced Research Projects Activity, USDOE National Nuclear Security Administration (NNSA), Stefan Seritan, Kenneth Rudinger.
Report | 2025 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3023921](https://doi.org/10.2172/3023921).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3023921); retrieved 2026-10-08.

#### Q1170 Characterizing a trapped ion logical qubit with gate set tomography

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Kenneth Rudinger, Intelligence Advanced Research Projects Activity, USDOE National Nuclear Security Administration (NNSA), Piper Wysocki, Daniel Hothem, Jalan Ziyad, Aliza Siddiqui et al..
Report | 2025 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3453489](https://doi.org/10.2172/3453489).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3453489); retrieved 2026-10-08.

#### Q1171 Transformer models for quantum gate set tomography

King Yiu Yu, Aritra Sarkar, Maximilian Rimbach-Russ, Ryoichi Ishihara, Sebastian Feld.
Journal article | 2025 | Quantum Machine Intelligence | vol. 7 | no. 1 | article 10.
Identifier and resource: [10.1007/s42484-025-00237-9](https://doi.org/10.1007/s42484-025-00237-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-025-00237-9); retrieved 2026-10-08.

#### Q1172 A DIARY OF A FAULTY LOGICAL QUBIT: LOGICAL GATE SET TOMOGRAPHY

Sandia National Laboratories (SNL-NM), Albuquerque, NM (United States), Aliza Siddiqui, Intelligence Advanced Research Projects Activity, USDOE National Nuclear Security Administration (NNSA), Stefan Seritan, Kenneth Rudinger.
Report | 2024 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/3454429](https://doi.org/10.2172/3454429).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F3454429); retrieved 2026-10-08.

#### Q1173 Non-Markovian quantum gate set tomography

Ze-Tong Li, Cong-Cong Zheng, Fan-Xu Meng, Han Zeng, Tian Luan, Zai-Chen Zhang, Xu-Tao Yu.
Journal article | 2024 | Quantum Science and Technology | vol. 9 | no. 3 | pp. 035027.
Identifier and resource: [10.1088/2058-9565/ad3d80](https://doi.org/10.1088/2058-9565/ad3d80).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fad3d80); retrieved 2026-10-08.

#### Q1174 Streaming Quantum Gate Set Tomography Using the Extended Kalman Filter

J. P. Marceaux, Kevin Young.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1401-1411.
Identifier and resource: [10.1109/qce57702.2023.00159](https://doi.org/10.1109/qce57702.2023.00159).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00159); retrieved 2026-10-08.

#### Q1175 Characterizing Midcircuit Measurements on a Superconducting Qubit Using Gate Set Tomography

Kenneth Rudinger, Guilhem J. Ribeill, Luke C.G. Govia, Matthew Ware, Erik Nielsen, Kevin Young, Thomas A. Ohki, Robin Blume-Kohout et al..
Journal article | 2022 | Physical Review Applied | vol. 17 | no. 1 | article 014014.
Identifier and resource: [10.1103/physrevapplied.17.014014](https://doi.org/10.1103/physrevapplied.17.014014).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevapplied.17.014014); retrieved 2026-10-08.

#### Q1176 Gate Set Tomography of a Logical Qubit.

Kenneth Rudinger, Julie Campos, Mario Morford-Oberst, Erik Nielsen, Stefan Seritan, Tzvetan Metodi, Robin Blume-Kohout.
Conference paper | 2022 | Proposed for presentation at the American Physical Society March Meeting held March 14-18, 2022 in Chicago, IL..
Identifier and resource: [10.2172/2001890](https://doi.org/10.2172/2001890).
Conference metadata: Proposed for presentation at the American Physical Society March Meeting held March 14-18, 2022 in Chicago, IL..
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2001890); retrieved 2026-10-08.

### D22T04 Classical shadows

Classical shadows use randomized measurements to predict many observables. Sample requirements depend on the measurement ensemble and target observable family.

Fine subcategories: Random measurements; observable prediction; sample complexity; derandomization.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1177 A computationally efficient approach to quantum state reconstruction using robust classical shadows

Sanjay Sharma, Shyam Akashe, Govind Murari Upadhyay, Amanjot Kaur Lamba.
Journal article | 2026 | Scientific Reports | vol. 16 | no. 1 | article 6927.
Identifier and resource: [10.1038/s41598-026-35442-4](https://doi.org/10.1038/s41598-026-35442-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-026-35442-4); retrieved 2026-10-08.

#### Q1178 Large-scale implementation of quantum subspace expansion with classical shadows

Anonymous.
Journal article | 2026 | Physical Review Letters.
Identifier and resource: [10.1103/2w21-qs38](https://doi.org/10.1103/2w21-qs38).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F2w21-qs38); retrieved 2026-10-08.

#### Q1179 Quantum-classical auxiliary field quantum Monte Carlo with matchgate shadows on trapped ion quantum computers

Luning Zhao, Joshua J. Goings, Willie Aboumrad, Andrew Arrasmith, Lazaro Calderin, Spencer Churchill, Dor Gabay, Thea Harvey-Brown et al..
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033061.
Identifier and resource: [10.1103/n1tf-8kr7](https://doi.org/10.1103/n1tf-8kr7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fn1tf-8kr7); retrieved 2026-10-08.

#### Q1180 The efficiency frontier: Classical shadows versus direct quantum measurement

Shuowei Ma, Junyu Liu.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 2 | article 67.
Identifier and resource: [10.1007/s42484-026-00413-5](https://doi.org/10.1007/s42484-026-00413-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00413-5); retrieved 2026-10-08.

#### Q1181 Enhancing quantum state reconstruction with structured classical shadows

Zhen Qin, Joseph M. Lukens, Brian T. Kirby, Zhihui Zhu.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 147.
Identifier and resource: [10.1038/s41534-025-01101-1](https://doi.org/10.1038/s41534-025-01101-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-01101-1); retrieved 2026-10-08.

#### Q1182 Non-semisimple quantum invariants and abelian classical shadows

Renaud Detcherry.
Journal article | 2025 | Annales de la Faculté des sciences de Toulouse : Mathématiques | vol. 34 | no. 2 | pp. 395-412.
Identifier and resource: [10.5802/afst.1816](https://doi.org/10.5802/afst.1816).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5802%2Fafst.1816); retrieved 2026-10-08.

#### Q1183 Quantum Computing Approach to Fixed-Node Monte Carlo Using Classical Shadows

Nick S. Blunt, Laura Caune, Javiera Quiroz-Fernandez.
Journal article | 2025 | Journal of Chemical Theory and Computation | vol. 21 | no. 4 | pp. 1652-1666.
Identifier and resource: [10.1021/acs.jctc.4c01468](https://doi.org/10.1021/acs.jctc.4c01468).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1021%2Facs.jctc.4c01468); retrieved 2026-10-08.

#### Q1184 Quantum Phases Beyond Classical Shadows: A New Framework for Gravitational Wave Effects

Partha Nandi.
Posted content | 2025 | Cassyni.
Identifier and resource: [10.52843/cassyni.q6svlz](https://doi.org/10.52843/cassyni.q6svlz).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.52843%2Fcassyni.q6svlz); retrieved 2026-10-08.

#### Q1185 Regularizing least squares quantum state tomography with classical shadows

Zhihui Zhu, Joseph M. Lukens, Brian T. Kirby.
Conference paper | 2025 | CLEO 2025 | pp. FF120_6.
Identifier and resource: [10.1364/cleo_fs.2025.ff120_6](https://doi.org/10.1364/cleo_fs.2025.ff120_6).
Conference metadata: CLEO: Fundamental Science.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_fs.2025.ff120_6); retrieved 2026-10-08.

#### Q1186 Classical shadows for quantum process tomography on near-term quantum computers

Ryan Levy, Di Luo, Bryan K. Clark.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 1 | article 013029.
Identifier and resource: [10.1103/physrevresearch.6.013029](https://doi.org/10.1103/physrevresearch.6.013029).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.013029); retrieved 2026-10-08.

#### Q1187 Classical shadows meet quantum optimal mass transport

Giacomo De Palma, Tristan Klein, Davide Pastorello.
Journal article | 2024 | Journal of Mathematical Physics | vol. 65 | no. 9 | article 092201.
Identifier and resource: [10.1063/5.0178897](https://doi.org/10.1063/5.0178897).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0178897); retrieved 2026-10-08.

#### Q1188 Error-mitigated fermionic classical shadows on noisy quantum devices

Bujiao Wu, Dax Enshan Koh.
Journal article | 2024 | npj Quantum Information | vol. 10 | no. 1 | article 39.
Identifier and resource: [10.1038/s41534-024-00836-7](https://doi.org/10.1038/s41534-024-00836-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-024-00836-7); retrieved 2026-10-08.

#### Q1189 Evaluating a quantum-classical quantum Monte Carlo algorithm with Matchgate shadows

Benchen Huang, Yi-Ting Chen, Brajesh Gupt, Martin Suchara, Anh Tran, Sam McArdle, Giulia Galli.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 4 | article 043063.
Identifier and resource: [10.1103/physrevresearch.6.043063](https://doi.org/10.1103/physrevresearch.6.043063).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.043063); retrieved 2026-10-08.

#### Q1190 Quantum Circuit Cutting for Classical Shadows

Daniel Tzu Shiuan Chen, Zain Hamid Saleem, Michael Alexandrovich Perlin.
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 2 | pp. 1-21.
Identifier and resource: [10.1145/3665335](https://doi.org/10.1145/3665335).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3665335); retrieved 2026-10-08.

#### Q1191 Quantum Error Mitigated Classical Shadows

Hamza Jnane, Jonathan Steinberg, Zhenyu Cai, H. Chau Nguyen, Bálint Koczor.
Journal article | 2024 | PRX Quantum | vol. 5 | no. 1 | article 010324.
Identifier and resource: [10.1103/prxquantum.5.010324](https://doi.org/10.1103/prxquantum.5.010324).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.5.010324); retrieved 2026-10-08.

#### Q1192 Restoring symmetries in quantum computing using Classical Shadows

Edgar Andres Ruiz Guzman, Denis Lacroix.
Journal article | 2024 | The European Physical Journal A | vol. 60 | no. 5 | article 112.
Identifier and resource: [10.1140/epja/s10050-024-01314-6](https://doi.org/10.1140/epja/s10050-024-01314-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepja%2Fs10050-024-01314-6); retrieved 2026-10-08.

### D22T05 Quantum volume and application benchmarks

System benchmarks summarize performance on specified circuit or application families. Different metrics are complementary and do not supply a universal ranking.

Fine subcategories: Quantum volume; mirror circuits; CLOPS; application performance; statistical comparison.

Primary resources: 1. Additional related assignments can be found in the interactive HTML.

#### Q1193 Volumetric Benchmarking of IQM-Spark: Parity-Preserving Quantum Volume and Compilation Overheads in Odra 5

Andrzej Gnatowski, Jarosław Rudy, Marcin Rudziński, Rafał Bistroń, Krzysztof Świȩcicki, Teodor Niżyński, Wojciech Bożejko, Karol Życzkowski.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 171-185.
Identifier and resource: [10.1007/978-3-032-36868-3_12](https://doi.org/10.1007/978-3-032-36868-3_12).
Fine tags: Quantum volume.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-36868-3_12); retrieved 2026-10-08.

### D22T06 Verification and quantum certification

Verification and certification test a precise state or computation claim under a trust model. Protocol guarantees need to be read together with device assumptions.

Fine subcategories: Interactive verification; state certification; self testing; trusted measurements.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1194 Enhancing quantum audio watermarking security through joint verification and certification

Zheng Xing, Chan-Tong Lam, Xiaochen Yuan.
Journal article | 2026 | Scientific Reports | vol. 16 | no. 1 | article 5616.
Identifier and resource: [10.1038/s41598-026-36535-w](https://doi.org/10.1038/s41598-026-36535-w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-026-36535-w); retrieved 2026-10-08.

#### Q1195 AutoQ 2.0: From Verification of Quantum Circuits to Verification of Quantum Programs

Yu-Fang Chen, Kai-Min Chung, Min-Hsiu Hsieh, Wei-Jia Huang, Ondřej Lengál, Jyun-Ao Lin, Wei-Lun Tsai.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 87-108.
Identifier and resource: [10.1007/978-3-031-90660-2_5](https://doi.org/10.1007/978-3-031-90660-2_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-90660-2_5); retrieved 2026-10-08.

#### Q1196 Verification of Quantum Circuits

Robert Wille, Lukas Burgholzer.
Book chapter | 2024 | Handbook of Computer Architecture | pp. 1413-1440.
Identifier and resource: [10.1007/978-981-97-9314-3_43](https://doi.org/10.1007/978-981-97-9314-3_43).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-97-9314-3_43); retrieved 2026-10-08.

#### Q1197 Verification of quantum programs

Mingsheng Ying.
Book chapter | 2024 | Foundations of Quantum Programming | pp. 137-167.
Identifier and resource: [10.1016/b978-0-44-315942-8.00018-6](https://doi.org/10.1016/b978-0-44-315942-8.00018-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-44-315942-8.00018-6); retrieved 2026-10-08.

#### Q1198 Quantum Robustness Verification: A Hybrid Quantum-Classical Neural Network Certification Algorithm

Nicola Franco, Tom Wollschlager, Nicholas Gao, Jeanette Miriam Lorenz, Stephan Gunnemann.
Conference paper | 2022 | 2022 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 142-153.
Identifier and resource: [10.1109/qce53715.2022.00033](https://doi.org/10.1109/qce53715.2022.00033).
Conference metadata: 2022 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce53715.2022.00033); retrieved 2026-10-08.

#### Q1199 Sample-Efficient Device-Independent Quantum State Verification and Certification

Aleksandra Gočanin, Ivan Šupić, Borivoje Dakić.
Journal article | 2022 | PRX Quantum | vol. 3 | no. 1 | article 010317.
Identifier and resource: [10.1103/prxquantum.3.010317](https://doi.org/10.1103/prxquantum.3.010317).
Fine tags: state certification.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.3.010317); retrieved 2026-10-08.

#### Q1200 Verification of Quantum Circuits

Robert Wille, Lukas Burgholzer.
Book chapter | 2022 | Handbook of Computer Architecture | pp. 1-28.
Identifier and resource: [10.1007/978-981-15-6401-7_43-1](https://doi.org/10.1007/978-981-15-6401-7_43-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-15-6401-7_43-1); retrieved 2026-10-08.

#### Q1201 Verification of Quantum Computation

Elham Kashefi.
Conference paper | 2014 | Research in Optical Sciences | pp. QTh2A.2.
Identifier and resource: [10.1364/qim.2014.qth2a.2](https://doi.org/10.1364/qim.2014.qth2a.2).
Conference metadata: Quantum Information and Measurement.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fqim.2014.qth2a.2); retrieved 2026-10-08.

## D23 Software programming and compilation

Quantum software translates a problem into executable circuits and measured results. Compiler decisions should preserve semantics while adapting operations to hardware constraints.

Prerequisites: Programming, compiler concepts, and circuit semantics.

Assessment focus: Semantic preservation, target constraints, verification, and reproducibility.

Primary catalog resources in this category: 75.

### D23T01 Quantum programming languages

Programming languages express quantum operations alongside classical computation. Control flow, type safety, and provider execution models determine practical capabilities.

Fine subcategories: Q sharp; Qiskit; Cirq; functional languages; type systems; quantum control flow.

Primary resources: 13. Additional related assignments can be found in the interactive HTML.

#### Q1202 Fundamentals of Quantum Programming in IBM's Quantum Computers

Weng-Long Chang, Athanasios V. Vasilakos.
Book | 2021 | Studies in Big Data.
Identifier and resource: [10.1007/978-3-030-63583-1](https://doi.org/10.1007/978-3-030-63583-1).
ISBN: 9783030635824; 9783030635831.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-63583-1); retrieved 2026-10-08.

#### Q1203 Quantum Computer Programming Languages for Aerospace Applications

Fred C. Briggs.
Conference paper | 2026 | AIAA SCITECH 2026 Forum.
Identifier and resource: [10.2514/6.2026-0441](https://doi.org/10.2514/6.2026-0441).
Conference metadata: AIAA SCITECH 2026 Forum.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2514%2F6.2026-0441); retrieved 2026-10-08.

#### Q1204 Quantum Programming: Languages and Frameworks

Ashwin Prakash Nalwade, Khan Shariya Hasan Upoma.
Book chapter | 2026 | Quantum Ops | pp. 43-62.
Identifier and resource: [10.1007/978-3-032-10775-6_3](https://doi.org/10.1007/978-3-032-10775-6_3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-10775-6_3); retrieved 2026-10-08.

#### Q1205 Quantum Programming Paradigms and Description Languages

Sonia Lopez Alarcón, Elaine Wong, Travis S. Humble, Eugene Dumitrescu.
Journal article | 2023 | Computing in Science & Engineering | vol. 25 | no. 6 | pp. 33-38.
Identifier and resource: [10.1109/mcse.2024.3375432](https://doi.org/10.1109/mcse.2024.3375432).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmcse.2024.3375432); retrieved 2026-10-08.

#### Q1206 Linear Dependent Type Theory for Quantum Programming Languages

Peng Fu, Kohei Kishida, Peter Selinger.
Journal article | 2022 | Logical Methods in Computer Science | vol. Volume 18, Issue 3 | article 6930.
Identifier and resource: [10.46298/lmcs-18(3:28)2022](https://doi.org/10.46298/lmcs-18(3:28)2022).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.46298%2Flmcs-18%283%3A28%292022); retrieved 2026-10-08.

#### Q1207 Semantics of quantum programming languages: Classical control, quantum control

Benoît Valiron.
Journal article | 2022 | Journal of Logical and Algebraic Methods in Programming | vol. 128 | pp. 100790 | article 100790.
Identifier and resource: [10.1016/j.jlamp.2022.100790](https://doi.org/10.1016/j.jlamp.2022.100790).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.jlamp.2022.100790); retrieved 2026-10-08.

#### Q1208 Linear Dependent Type Theory for Quantum Programming Languages

Peng Fu, Kohei Kishida, Peter Selinger.
Conference paper | 2020 | Proceedings of the 35th Annual ACM/IEEE Symposium on Logic in Computer Science | pp. 440-453.
Identifier and resource: [10.1145/3373718.3394765](https://doi.org/10.1145/3373718.3394765).
Conference metadata: LICS '20: 35th Annual ACM/IEEE Symposium on Logic in Computer Science.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3373718.3394765); retrieved 2026-10-08.

#### Q1209 Quantum programming languages

Bettina Heim, Mathias Soeken, Sarah Marshall, Chris Granade, Martin Roetteler, Alan Geller, Matthias Troyer, Krysta Svore.
Journal article | 2020 | Nature Reviews Physics | vol. 2 | no. 12 | pp. 709-722.
Identifier and resource: [10.1038/s42254-020-00245-7](https://doi.org/10.1038/s42254-020-00245-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42254-020-00245-7); retrieved 2026-10-08.

#### Q1210 Cirq basics | Google Quantum AI

Author metadata not supplied.
Tutorial | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://quantumai.google/cirq/start/basics).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://quantumai.google/cirq/start/basics); retrieved 2026-10-08.

#### Q1211 Cirq | Google Quantum AI

Author metadata not supplied.
Documentation | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://quantumai.google/cirq).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://quantumai.google/cirq); retrieved 2026-10-08.

#### Q1212 GitHub - quantumlib/Cirq: Python framework for creating, editing, and running Noisy Intermediate-Scale Quantum (NISQ) circuits. · GitHub

Author metadata not supplied.
Software repository | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://github.com/quantumlib/Cirq).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/quantumlib/Cirq); retrieved 2026-10-08.

#### Q1213 Introduction to the Quantum Programming Language Q# - Azure Quantum | Microsoft Learn

Author metadata not supplied.
Documentation | Undated | Microsoft.
Identifier and resource: [Official resource](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview); retrieved 2026-10-08.

#### Q1214 What is Azure Quantum? - Azure Quantum | Microsoft Learn

Author metadata not supplied.
Documentation | Undated | Microsoft.
Identifier and resource: [Official resource](https://learn.microsoft.com/en-us/azure/quantum/overview-azure-quantum).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://learn.microsoft.com/en-us/azure/quantum/overview-azure-quantum); retrieved 2026-10-08.

### D23T02 Quantum intermediate representations

Intermediate representations support compilation and interchange across tools. Semantics and classical control must survive translation between representations.

Fine subcategories: OpenQASM; QIR; MLIR; classical control; interoperability.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1215 Quantum Circuit Synthesis from C via Multi-Level Intermediate Representation

Giacomo Lancellotti, Francesco Rosnati, Leonardo Ignazio Pagliochini, Giovanni Agosta.
Conference paper | 2026 | Proceedings of the 41st ACM/SIGAPP Symposium on Applied Computing | pp. 1359-1366.
Identifier and resource: [10.1145/3748522.3779947](https://doi.org/10.1145/3748522.3779947).
Conference metadata: SAC '26: 41st ACM/SIGAPP Symposium on Applied Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3748522.3779947); retrieved 2026-10-08.

#### Q1216 Quantum Oracle Synthesis from HDL Designs via Multi Level Intermediate Representation

Giacomo Lancellotti, Filippo Buda, Giacomo Carugati, Daniele Gazzola, Alessandro Barenghi, Giovanni Agosta, Gerardo Pelosi.
Conference paper | 2026 | 2026 31st Asia and South Pacific Design Automation Conference (ASP-DAC) | pp. 191-197.
Identifier and resource: [10.1109/asp-dac66049.2026.11420750](https://doi.org/10.1109/asp-dac66049.2026.11420750).
Conference metadata: 2026 31st Asia and South Pacific Design Automation Conference (ASP-DAC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fasp-dac66049.2026.11420750); retrieved 2026-10-08.

#### Q1217 QIRopt: An Optimization Method for Quantum Intermediate Representation

Junjie Luo, Haoyu Zhang, Jianjun Zhao.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 459-469.
Identifier and resource: [10.1109/qce65121.2025.00058](https://doi.org/10.1109/qce65121.2025.00058).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: QIR.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00058); retrieved 2026-10-08.

#### Q1218 Towards a Pulse-Level Intermediate Representation for Diverse Quantum Control Systems

Jude Alnas, Aniket S. Dalvi, Kenneth R. Brown.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 448-458.
Identifier and resource: [10.1109/qce65121.2025.00057](https://doi.org/10.1109/qce65121.2025.00057).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00057); retrieved 2026-10-08.

#### Q1219 Enhancing Code Safety in Quantum Intermediate Representation

Junjie Luo, Jianjun Zhao.
Conference paper | 2023 | 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE) | pp. 1771-1775.
Identifier and resource: [10.1109/ase56229.2023.00195](https://doi.org/10.1109/ase56229.2023.00195).
Conference metadata: 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fase56229.2023.00195); retrieved 2026-10-08.

#### Q1220 Retargetable Optimizing Compilers for Quantum Accelerators via a Multilevel Intermediate Representation

Thien Nguyen, Alexander McCaskey.
Journal article | 2022 | IEEE Micro | vol. 42 | no. 5 | pp. 17-33.
Identifier and resource: [10.1109/mm.2022.3179654](https://doi.org/10.1109/mm.2022.3179654).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmm.2022.3179654); retrieved 2026-10-08.

#### Q1221 GitHub - openqasm/openqasm: Quantum assembly language for extended quantum circuits · GitHub

Author metadata not supplied.
Software repository | Undated | OpenQASM.
Identifier and resource: [Official resource](https://github.com/openqasm/openqasm).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/openqasm/openqasm); retrieved 2026-10-08.

#### Q1222 GitHub - qir-alliance/qir-spec: QIR specification defining how to represent quantum programs within the LLVM IR · GitHub

Author metadata not supplied.
Software repository | Undated | QIR Alliance.
Identifier and resource: [Official resource](https://github.com/qir-alliance/qir-spec).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/qir-alliance/qir-spec); retrieved 2026-10-08.

### D23T03 Quantum circuit synthesis

Circuit synthesis decomposes target transformations into allowed operations. Approximation accuracy and target gate set determine circuit size.

Fine subcategories: Unitary decomposition; Clifford T synthesis; arithmetic circuits; gate minimization.

Primary resources: 17. Additional related assignments can be found in the interactive HTML.

#### Q1223 Error-Tolerant Quantum State Discrimination: Optimization and Quantum Circuit Synthesis

Chien-Kai Ma, Bo-Hung Chen, Tian-Fu Chen, Dah-Wei Chiou, Jie-Hong R. Jiang.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 440-458.
Identifier and resource: [10.1007/978-3-032-22749-2_22](https://doi.org/10.1007/978-3-032-22749-2_22).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-22749-2_22); retrieved 2026-10-08.

#### Q1224 Learning State Separation for Quantum Circuit Synthesis

Christoph Stein, Stefan Klikovits, Manuel Wimmer.
Conference paper | 2026 | Proceedings of the 7th IEEE/ACM International Workshop on Quantum Software Engineering | pp. 17-24.
Identifier and resource: [10.1145/3786150.3788615](https://doi.org/10.1145/3786150.3788615).
Conference metadata: Q-SE '26: IEEE/ACM International Workshop on Quantum Software Engineering.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3786150.3788615); retrieved 2026-10-08.

#### Q1225 Quantum Circuit Synthesis Based on LimTDD

Xin Hong, Chenjian Li, Aochu Dai, Runhong He, Shenggang Ying.
Conference paper | 2026 | 2026 Design, Automation &amp; Test in Europe Conference (DATE) | pp. 1-7.
Identifier and resource: [10.23919/date69613.2026.11539289](https://doi.org/10.23919/date69613.2026.11539289).
Conference metadata: 2026 Design, Automation & Test in Europe Conference (DATE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Fdate69613.2026.11539289); retrieved 2026-10-08.

#### Q1226 Revisiting Crossover Effectiveness in Quantum Circuit Synthesis

Christoph Stein, Stefan Klikovits, Manuel Wimmer.
Conference paper | 2026 | Proceedings of the Genetic and Evolutionary Computation Conference Companion | pp. 1577-1584.
Identifier and resource: [10.1145/3795101.3814690](https://doi.org/10.1145/3795101.3814690).
Conference metadata: GECCO '26 Companion: Genetic and Evolutionary Computation Conference Companion.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3795101.3814690); retrieved 2026-10-08.

#### Q1227 Synthesis of Compact and Expressive Quantum-Circuit Optimizations

Wei Qiang, Ronghui Gu.
Journal article | 2026 | Proceedings of the ACM on Programming Languages | vol. 10 | no. OOPSLA2 | pp. 91-118.
Identifier and resource: [10.1145/3839450](https://doi.org/10.1145/3839450).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3839450); retrieved 2026-10-08.

#### Q1228 Amplitude-Ensemble Quantum-Inspired Tabu Search Algorithm for Quantum Boolean Circuit Synthesis

Kuo-Chun Tseng, Zi-Yi Sun, Pei-Lun Ho, Yu-Chieh Cho, Yu-Syuan Liu, Wei-Chieh Lai, Wei-Chun Huang, Jen-Shin Hong.
Conference paper | 2025 | 2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC) | pp. 4845-4852.
Identifier and resource: [10.1109/smc58881.2025.11343273](https://doi.org/10.1109/smc58881.2025.11343273).
Conference metadata: 2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fsmc58881.2025.11343273); retrieved 2026-10-08.

#### Q1229 Quantum Circuit Synthesis Using Fuzzy-Logic-Assisted Genetic Algorithms

Ishraq Islam, Vinayak Jha, Sneha Thomas, Kieran F. Egan, Alvir Nobel, Serom Kim, Manu Chaudhary, Sunday Ogundele et al..
Journal article | 2025 | Algorithms | vol. 18 | no. 4 | pp. 178.
Identifier and resource: [10.3390/a18040178](https://doi.org/10.3390/a18040178).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fa18040178); retrieved 2026-10-08.

#### Q1230 Quantum circuit synthesis with SQiSW

Jialiang Tang, Jialin Zhang, Xiaoming Sun.
Journal article | 2025 | Quantum | vol. 9 | pp. 1889 | article 1889.
Identifier and resource: [10.22331/q-2025-10-20-1889](https://doi.org/10.22331/q-2025-10-20-1889).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-10-20-1889); retrieved 2026-10-08.

#### Q1231 Study on Machine Learning Application in Quantum Circuit Synthesis

Jyoti, Amitabh Wahi, S.B.L Tripathi.
Journal article | 2025 | RESEARCH REVIEW International Journal of Multidisciplinary | vol. 10 | no. 4 | pp. 06-13.
Identifier and resource: [10.31305/rrijm.2025.v10.n4.002](https://doi.org/10.31305/rrijm.2025.v10.n4.002).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.31305%2Frrijm.2025.v10.n4.002); retrieved 2026-10-08.

#### Q1232 Discovering quantum circuit components with program synthesis

Leopoldo Sarra, Kevin Ellis, Florian Marquardt.
Journal article | 2024 | Machine Learning: Science and Technology | vol. 5 | no. 2 | pp. 025029.
Identifier and resource: [10.1088/2632-2153/ad4252](https://doi.org/10.1088/2632-2153/ad4252).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2632-2153%2Fad4252); retrieved 2026-10-08.

#### Q1233 Optimizing Quantum Circuit Synthesis with Dominator Analysis

Giacomo Lancellotti, Giovanni Agosta, Alessandro Barenghi, Gerardo Pelosi.
Conference paper | 2024 | 2024 IEEE 42nd International Conference on Computer Design (ICCD) | pp. 24-27.
Identifier and resource: [10.1109/iccd63220.2024.00015](https://doi.org/10.1109/iccd63220.2024.00015).
Conference metadata: 2024 IEEE 42nd International Conference on Computer Design (ICCD).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcd63220.2024.00015); retrieved 2026-10-08.

#### Q1234 Quantum Circuit Partitioning for Scalable Noise-Aware Quantum Circuit Re-Synthesis

Mohammad Walid Charrwi, Georgios Ioannou, Ed Younis, Wibe Albert de Jong, Samah Mohamed Saeed.
Conference paper | 2024 | 2024 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 359-364.
Identifier and resource: [10.1109/qce60285.2024.10306](https://doi.org/10.1109/qce60285.2024.10306).
Conference metadata: 2024 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce60285.2024.10306); retrieved 2026-10-08.

#### Q1235 Quantum circuit synthesis on noisy intermediate-scale quantum devices

Shuai Yang, Guojing Tian, Jialin Zhang, Xiaoming Sun.
Journal article | 2024 | Physical Review A | vol. 109 | no. 1 | article 012602.
Identifier and resource: [10.1103/physreva.109.012602](https://doi.org/10.1103/physreva.109.012602).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.012602); retrieved 2026-10-08.

#### Q1236 Quantum circuit synthesis with diffusion models

Florian Fürrutter, Gorka Muñoz-Gil, Hans J. Briegel.
Journal article | 2024 | Nature Machine Intelligence | vol. 6 | no. 5 | pp. 515-524.
Identifier and resource: [10.1038/s42256-024-00831-9](https://doi.org/10.1038/s42256-024-00831-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42256-024-00831-9); retrieved 2026-10-08.

#### Q1237 Review Quantum Circuit Synthesis for Grover’s Algorithm Oracle

Miguel A. Naranjo, Luis A. Fletscher.
Journal article | 2024 | Algorithms | vol. 17 | no. 9 | pp. 382.
Identifier and resource: [10.3390/a17090382](https://doi.org/10.3390/a17090382).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Fa17090382); retrieved 2026-10-08.

#### Q1238 Synthetiq: Fast and Versatile Quantum Circuit Synthesis

Anouk Paradis, Jasper Dekoninck, Benjamin Bichsel, Martin Vechev.
Journal article | 2024 | Proceedings of the ACM on Programming Languages | vol. 8 | no. OOPSLA1 | pp. 55-82.
Identifier and resource: [10.1145/3649813](https://doi.org/10.1145/3649813).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3649813); retrieved 2026-10-08.

#### Q1239 GitHub - zxcalc/pyzx: Python library for quantum circuit rewriting and optimisation using the ZX-calculus · GitHub

Author metadata not supplied.
Software repository | Undated | PyZX.
Identifier and resource: [Official resource](https://github.com/zxcalc/pyzx).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/zxcalc/pyzx); retrieved 2026-10-08.

### D23T04 Qubit mapping and routing

Placement and routing adapt logical circuits to hardware connectivity. Inserted operations change depth, noise exposure, and execution cost.

Fine subcategories: Placement; SWAP insertion; topology constraints; scheduling; crosstalk awareness.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1240 DMapS: End-to-End Qubit Mapping and Routing for Distributed Quantum Computing Architectures

Tingyu Luo, Yuzhen Zheng, Yuxin Deng, X. Fu.
Journal article | 2026 | IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | vol. 45 | no. 5 | pp. 2095-2108.
Identifier and resource: [10.1109/tcad.2025.3611153](https://doi.org/10.1109/tcad.2025.3611153).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcad.2025.3611153); retrieved 2026-10-08.

#### Q1241 Generating Compilers for Qubit Mapping and Routing

Abtin Molavi, Amanda Xu, Ethan Cecchetti, Swamit Tannu, Aws Albarghouthi.
Journal article | 2026 | Proceedings of the ACM on Programming Languages | vol. 10 | no. POPL | pp. 2265-2294.
Identifier and resource: [10.1145/3776720](https://doi.org/10.1145/3776720).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3776720); retrieved 2026-10-08.

#### Q1242 Nested Qubit Routing

Harshit Dhankhar, Tristan Cazenave.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 70-81.
Identifier and resource: [10.1007/978-3-032-15931-1_6](https://doi.org/10.1007/978-3-032-15931-1_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-15931-1_6); retrieved 2026-10-08.

#### Q1243 QDP: Worst-case Fidelity-aware Qubit Mapping and Routing using Dynamic Programming

Shui Jiang, Wen Cheng, Yi-Hua Chung, Tsung-Yi Ho, Tsung-Wei Huang.
Journal article | 2026 | IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | pp. 1-1.
Identifier and resource: [10.1109/tcad.2026.3693628](https://doi.org/10.1109/tcad.2026.3693628).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcad.2026.3693628); retrieved 2026-10-08.

#### Q1244 Unifying Qubit Routing Across Diverse Quantum ISAs via Canonical Representation

Zhaohui Yang, Kai Zhang, Xinyang Tian, Xiangyu Ren, Yingjian Liu, Yunfeng Li, Dawei Ding, Jianxin Chen et al..
Conference paper | 2026 | 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA) | pp. 2302-2317.
Identifier and resource: [10.1109/isca66397.2026.00162](https://doi.org/10.1109/isca66397.2026.00162).
Conference metadata: 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisca66397.2026.00162); retrieved 2026-10-08.

#### Q1245 Robust Qubit Mapping Algorithm via Double-Source Optimal Routing on Large Quantum Circuits

Chin-Yi Cheng, Chien-Yi Yang, Yi-Hsiang Kuo, Ren-Chu Wang, Hao-Chung Cheng, Chung-Yang (Ric) Huang.
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 3 | pp. 1-26.
Identifier and resource: [10.1145/3680291](https://doi.org/10.1145/3680291).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3680291); retrieved 2026-10-08.

#### Q1246 Dynamic Qubit Routing with CNOT Circuit Synthesis for Quantum Compilation

Arianne Meijer-van de Griend, Sarah Meng Li.
Journal article | 2023 | Electronic Proceedings in Theoretical Computer Science | vol. 394 | pp. 363-399.
Identifier and resource: [10.4204/eptcs.394.18](https://doi.org/10.4204/eptcs.394.18).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4204%2Feptcs.394.18); retrieved 2026-10-08.

#### Q1247 Qubit Mapping and Routing via MaxSAT

Abtin Molavi, Amanda Xu, Martin Diges, Lauren Pick, Swamit Tannu, Aws Albarghouthi.
Conference paper | 2022 | 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO) | pp. 1078-1091.
Identifier and resource: [10.1109/micro56248.2022.00077](https://doi.org/10.1109/micro56248.2022.00077).
Conference metadata: 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmicro56248.2022.00077); retrieved 2026-10-08.

### D23T05 Quantum compiler optimization

Compiler optimizations simplify circuits or exploit device characteristics. Semantic correctness and the validity of a noise objective should be checked independently.

Fine subcategories: Rewrite rules; commutation; cancellation; approximate synthesis; noise aware passes.

Primary resources: 12. Additional related assignments can be found in the interactive HTML.

#### Q1248 Kernpiler: Compiler Optimization for Quantum Hamiltonian Simulation with Partial Trotterization

Ethan Decker, Lucas Goetz, Evan McKinney, Erik Gustafson, Junyu Zhou, Yuhao Liu, Alex K. Jones, Ang Li et al..
Conference paper | 2026 | 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA) | pp. 905-920.
Identifier and resource: [10.1109/isca66397.2026.00073](https://doi.org/10.1109/isca66397.2026.00073).
Conference metadata: 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisca66397.2026.00073); retrieved 2026-10-08.

#### Q1249 A Detailed Survey and Analysis of Recent Advancements in Quantum Compiler Optimization Techniques

Pooja Vaikar, Amol Potgantwar.
Book chapter | 2025 | Lecture Notes in Networks and Systems | pp. 681-692.
Identifier and resource: [10.1007/978-981-96-8043-6_52](https://doi.org/10.1007/978-981-96-8043-6_52).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-96-8043-6_52); retrieved 2026-10-08.

#### Q1250 A Universal Quantum Compiler GPT: Multi-Framework Optimization and Translation Using Large Language Models

Somrak Petchartee.
Conference paper | 2025 | 2025 29th International Computer Science and Engineering Conference (ICSEC) | pp. 58-63.
Identifier and resource: [10.1109/icsec67360.2025.11298108](https://doi.org/10.1109/icsec67360.2025.11298108).
Conference metadata: 2025 29th International Computer Science and Engineering Conference (ICSEC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficsec67360.2025.11298108); retrieved 2026-10-08.

#### Q1251 Inverse-Transpilation: Reverse-Engineering Quantum Compiler Optimization Passes from Circuit Snapshots

Satwik Kundu, Swaroop Ghosh.
Conference paper | 2025 | Proceedings of the Great Lakes Symposium on VLSI 2025 | pp. 273-277.
Identifier and resource: [10.1145/3716368.3735298](https://doi.org/10.1145/3716368.3735298).
Conference metadata: GLSVLSI '25: Great Lakes Symposium on VLSI 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3716368.3735298); retrieved 2026-10-08.

#### Q1252 MarQSim: Reconciling Determinism and Randomness in Compiler Optimization for Quantum Simulation

Xiuqi Cao, Junyu Zhou, Yuhao Liu, Yunong Shi, Gushu Li.
Journal article | 2025 | Proceedings of the ACM on Programming Languages | vol. 9 | no. PLDI | pp. 576-600.
Identifier and resource: [10.1145/3729269](https://doi.org/10.1145/3729269).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3729269); retrieved 2026-10-08.

#### Q1253 Quantum Software Engineering: Algorithm Design, Error Mitigation, and Compiler Optimization for Fault-Tolerant Quantum Computing

Author metadata not supplied.
Journal article | 2025 | International Journal of Computer Applications Technology and Research.
Identifier and resource: [10.7753/ijcatr1404.1003](https://doi.org/10.7753/ijcatr1404.1003).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7753%2Fijcatr1404.1003); retrieved 2026-10-08.

#### Q1254 Bosehedral: Compiler Optimization for Bosonic Quantum Computing

Junyu Zhou, Yuhao Liu, Yunong Shi, Ali Javadi-Abhari, Gushu Li.
Conference paper | 2024 | 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA) | pp. 261-276.
Identifier and resource: [10.1109/isca59077.2024.00028](https://doi.org/10.1109/isca59077.2024.00028).
Conference metadata: 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisca59077.2024.00028); retrieved 2026-10-08.

#### Q1255 Compiler Optimization for Quantum Computing Using Reinforcement Learning

Nils Quetschlich, Lukas Burgholzer, Robert Wille.
Conference paper | 2023 | 2023 60th ACM/IEEE Design Automation Conference (DAC) | pp. 1-6.
Identifier and resource: [10.1109/dac56929.2023.10248002](https://doi.org/10.1109/dac56929.2023.10248002).
Conference metadata: 2023 60th ACM/IEEE Design Automation Conference (DAC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fdac56929.2023.10248002); retrieved 2026-10-08.

#### Q1256 Parity Quantum Optimization: Compiler

Kilian Ender, Roeland ter Hoeven, Benjamin E. Niehoff, Maike Drieb-Schön, Wolfgang Lechner.
Journal article | 2023 | Quantum | vol. 7 | pp. 950 | article 950.
Identifier and resource: [10.22331/q-2023-03-17-950](https://doi.org/10.22331/q-2023-03-17-950).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-03-17-950); retrieved 2026-10-08.

#### Q1257 GitHub - Qiskit/qiskit: Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives. · GitHub

Author metadata not supplied.
Software repository | Undated | Qiskit.
Identifier and resource: [Official resource](https://github.com/Qiskit/qiskit).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/Qiskit/qiskit); retrieved 2026-10-08.

#### Q1258 GitHub - Quantinuum/tket: Source code for the TKET quantum compiler, Python bindings and utilities · GitHub

Author metadata not supplied.
Software repository | Undated | Quantinuum.
Identifier and resource: [Official resource](https://github.com/CQCL/tket).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/CQCL/tket); retrieved 2026-10-08.

#### Q1259 TKET — Quantinuum Documentation

Author metadata not supplied.
Documentation | Undated | Quantinuum.
Identifier and resource: [Official resource](https://docs.quantinuum.com/tket/).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://docs.quantinuum.com/tket/); retrieved 2026-10-08.

### D23T06 Quantum software testing and formal methods

Testing and formal methods address errors in quantum programs and compilation. Assertions, equivalence, and statistical testing have different guarantees.

Fine subcategories: Assertions; equivalence checking; program logics; property tests; debugging.

Primary resources: 17. Additional related assignments can be found in the interactive HTML.

#### Q1260 A Methodological Analysis of Empirical Studies in Quantum Software Testing

Yuechen Li, Minqi Shao, Jianjun Zhao, Qichen Wang.
Journal article | 2026 | ACM Transactions on Software Engineering and Methodology | article 3819590.
Identifier and resource: [10.1145/3819590](https://doi.org/10.1145/3819590).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3819590); retrieved 2026-10-08.

#### Q1261 A Practical Specification Language for Automatic Quantum Program Verification

Wei-Lun Tsai, Yu-Fang Chen, Ondřej Lengál.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 302-325.
Identifier and resource: [10.1007/978-3-032-32537-2_15](https://doi.org/10.1007/978-3-032-32537-2_15).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-32537-2_15); retrieved 2026-10-08.

#### Q1262 Industry Expectations and Skill Demands in Quantum Software Testing

Ronnie de Souza Santos, Maria Teresa Baldassarre, Cesar França.
Conference paper | 2026 | Proceedings of the 7th IEEE/ACM International Workshop on Quantum Software Engineering | pp. 9-16.
Identifier and resource: [10.1145/3786150.3788614](https://doi.org/10.1145/3786150.3788614).
Conference metadata: Q-SE '26: IEEE/ACM International Workshop on Quantum Software Engineering.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3786150.3788614); retrieved 2026-10-08.

#### Q1263 Relational Verification for Cost-Aware Quantum Program Optimization

Ziming Zhao, Tingting Li, Zhaoxuan Li, Jianwei Yin.
Journal article | 2026 | Proceedings of the AAAI Conference on Artificial Intelligence | vol. 40 | no. 17 | pp. 14414-14422.
Identifier and resource: [10.1609/aaai.v40i17.38457](https://doi.org/10.1609/aaai.v40i17.38457).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1609%2Faaai.v40i17.38457); retrieved 2026-10-08.

#### Q1264 Software Testing in the Quantum World

Rui Abreu, Shaukat Ali, Paolo Arcaini, José Campos, Michael Felderer, Claude Gravel, Fuyuki Ishikawa, Stefan Klikovits et al..
Journal article | 2026 | Computer | vol. 59 | no. 4 | pp. 135-138.
Identifier and resource: [10.1109/mc.2026.3655854](https://doi.org/10.1109/mc.2026.3655854).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmc.2026.3655854); retrieved 2026-10-08.

#### Q1265 Embedding Quantum Program Verification into Dafny

Feifei Cheng, Sushen Vangeepuram, Henry Allard, Seyed Mohammad Reza Jafari, Alex Potanin, Liyi Li.
Journal article | 2025 | Proceedings of the ACM on Programming Languages | vol. 9 | no. OOPSLA2 | pp. 2981-3007.
Identifier and resource: [10.1145/3763157](https://doi.org/10.1145/3763157).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3763157); retrieved 2026-10-08.

#### Q1266 Exact Inference for Quantum Circuits: A Testing Oracle for Quantum Software Stacks

Kanguk Lee, Jaemin Hong, Sukyoung Ryu.
Conference paper | 2025 | 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) | pp. 2465-2477.
Identifier and resource: [10.1109/ase63991.2025.00203](https://doi.org/10.1109/ase63991.2025.00203).
Conference metadata: 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fase63991.2025.00203); retrieved 2026-10-08.

#### Q1267 Mutation-Based Quantum Software Testing

Macario Polo-Usaola, Manuel Serrano, Ignacio García-Rodríguez de Guzmán.
Conference paper | 2025 | Proceedings of the 1st International Conference on Quantum Software | pp. 138-145.
Identifier and resource: [10.5220/0013561000004525](https://doi.org/10.5220/0013561000004525).
Conference metadata: 1st International Conference on Quantum Software.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5220%2F0013561000004525); retrieved 2026-10-08.

#### Q1268 SQUAD: software testing for quantum distributed learning software

Soohyun Park, Jae Hyun Cho, Hyun Jun Yook, Ga San Jhun, Youn Kyu Lee, Joongheon Kim.
Journal article | 2025 | The Journal of Supercomputing | vol. 81 | no. 9 | article 1071.
Identifier and resource: [10.1007/s11227-025-07556-5](https://doi.org/10.1007/s11227-025-07556-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11227-025-07556-5); retrieved 2026-10-08.

#### Q1269 The Landscape of Quantum Software Testing Tools

Xinyi Wang, Shaukat Ali, Davide Taibi.
Journal article | 2025 | IEEE Software | vol. 42 | no. 5 | pp. 136-140.
Identifier and resource: [10.1109/ms.2025.3578154](https://doi.org/10.1109/ms.2025.3578154).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fms.2025.3578154); retrieved 2026-10-08.

#### Q1270 Automated Quantum Program Verification in Dynamic Quantum Logic

Tsubasa Takagi, Canh Minh Do, Kazuhiro Ogata.
Book chapter | 2024 | Lecture Notes in Computer Science | pp. 68-84.
Identifier and resource: [10.1007/978-3-031-51777-8_5](https://doi.org/10.1007/978-3-031-51777-8_5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-51777-8_5); retrieved 2026-10-08.

#### Q1271 Gate Branch Coverage: A Metric for Quantum Software Testing

Daniel Fortunato, José Campos, Rui Abreu.
Conference paper | 2024 | Proceedings of the 1st ACM International Workshop on Quantum Software Engineering: The Next Evolution | pp. 15-18.
Identifier and resource: [10.1145/3663531.3664753](https://doi.org/10.1145/3663531.3664753).
Conference metadata: QSE-NE '24: 1st ACM International Workshop on Quantum Software Engineering: The Next Evolution.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3663531.3664753); retrieved 2026-10-08.

#### Q1272 Mitigating Noise in Quantum Software Testing Using Machine Learning

Asmar Muqeet, Tao Yue, Shaukat Ali, Paolo Arcaini.
Journal article | 2024 | IEEE Transactions on Software Engineering | vol. 50 | no. 11 | pp. 2947-2961.
Identifier and resource: [10.1109/tse.2024.3462974](https://doi.org/10.1109/tse.2024.3462974).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftse.2024.3462974); retrieved 2026-10-08.

#### Q1273 Quantum Machine Learning Techniques Integrated in Quantum Software Testing

Bala Gangadhara Gutam, Sunil Kumar Malchi.
Posted content | 2024 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-4653367/v1](https://doi.org/10.21203/rs.3.rs-4653367/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-4653367%2Fv1); retrieved 2026-10-08.

#### Q1274 Quantum Software Testing 101

Shaukat Ali.
Conference paper | 2024 | Proceedings of the 2024 IEEE/ACM 46th International Conference on Software Engineering: Companion Proceedings | pp. 426-427.
Identifier and resource: [10.1145/3639478.3643059](https://doi.org/10.1145/3639478.3643059).
Conference metadata: ICSE-Companion '24: 2024 IEEE/ACM 46th International Conference on Software Engineering: Companion Proceedings.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3639478.3643059); retrieved 2026-10-08.

#### Q1275 QuCAT: A Combinatorial Testing Tool for Quantum Software

Xinyi Wang, Paolo Arcaini, Tao Yue, Shaukat Ali.
Conference paper | 2023 | 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE) | pp. 2066-2069.
Identifier and resource: [10.1109/ase56229.2023.00062](https://doi.org/10.1109/ase56229.2023.00062).
Conference metadata: 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fase56229.2023.00062); retrieved 2026-10-08.

#### Q1276 Quantum Software Testing: A Brief Introduction

Shaukat Ali, Tao Yue.
Conference paper | 2023 | 2023 IEEE/ACM 45th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion) | pp. 332-333.
Identifier and resource: [10.1109/icse-companion58688.2023.00093](https://doi.org/10.1109/icse-companion58688.2023.00093).
Conference metadata: 2023 IEEE/ACM 45th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficse-companion58688.2023.00093); retrieved 2026-10-08.

## D24 Classical simulation and hybrid systems

Classical simulators support development, verification, and baselines. Their scalability depends on entanglement, circuit structure, precision, and memory bandwidth.

Prerequisites: Numerical linear algebra, parallel computing, and circuit structure.

Assessment focus: Memory, entanglement, precision, communication, and comparison to hardware.

Primary catalog resources in this category: 45.

### D24T01 State vector and density matrix simulation

State vector simulation tracks amplitudes, while density matrix simulation tracks mixed states. Memory grows exponentially and differs substantially between these representations.

Fine subcategories: Memory scaling; distributed state vectors; mixed states; precision; GPU execution.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1277 DAG-Aware Gate Fusion for Efficient State-Vector Quantum-Circuit Simulation

Shangshu Li, Zheng-An Wang, Heng Fan.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 1-10.
Identifier and resource: [10.1109/tqe.2026.3705783](https://doi.org/10.1109/tqe.2026.3705783).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3705783); retrieved 2026-10-08.

#### Q1278 Memory-Efficient State-Vector Simulation of Quantum Computer in Massively Parallel Supercomputers

Naoki Yoshioka, Nobuyasu Ito.
Book chapter | 2026 | Springer Proceedings in Physics | pp. 177-187.
Identifier and resource: [10.1007/978-981-92-0844-9_21](https://doi.org/10.1007/978-981-92-0844-9_21).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-92-0844-9_21); retrieved 2026-10-08.

#### Q1279 phase2: full-state vector simulation of quantum time evolution at scale

Marek Miller, Jakob Günther, Freek Witteveen, Matthew S. Teynor, Mihael Erakovic, Markus Reiher, Gemma C. Solomon, Matthias Christandl.
Journal article | 2026 | Communications AI & Computing | vol. 1 | no. 1 | article 5.
Identifier and resource: [10.1038/s44488-026-00002-2](https://doi.org/10.1038/s44488-026-00002-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs44488-026-00002-2); retrieved 2026-10-08.

#### Q1280 Lazy Qubit Reordering for Accelerating Parallel State-Vector-based Quantum Circuit Simulation

Yusuke Teranishi, Shoma Hiraoka, Wataru Mizukami, Masao Okita, Fumihiko Ino.
Journal article | 2025 | ACM Transactions on Quantum Computing | vol. 6 | no. 4 | pp. 1-33.
Identifier and resource: [10.1145/3748261](https://doi.org/10.1145/3748261).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3748261); retrieved 2026-10-08.

#### Q1281 Q2SV: A High‐Level Synthesis Approach for State Vector Quantum Simulation

Ahmad Bennakhi, Gregory T. Byrd, Paul Franzon.
Journal article | 2025 | Quantum Engineering | vol. 2025 | no. 1 | article 9017796.
Identifier and resource: [10.1155/que2/9017796](https://doi.org/10.1155/que2/9017796).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1155%2Fque2%2F9017796); retrieved 2026-10-08.

#### Q1282 GitHub - Qiskit/qiskit-aer: Aer is a high performance simulator for quantum circuits that includes noise models · GitHub

Author metadata not supplied.
Software repository | Undated | Qiskit Aer.
Identifier and resource: [Official resource](https://github.com/Qiskit/qiskit-aer).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/Qiskit/qiskit-aer); retrieved 2026-10-08.

#### Q1283 GitHub - quantumlib/qsim: Fast C++ and Python library for state-vector simulation of quantum circuits. · GitHub

Author metadata not supplied.
Software repository | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://github.com/quantumlib/qsim).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/quantumlib/qsim); retrieved 2026-10-08.

#### Q1284 Simulate a circuit | Cirq | Google Quantum AI

Author metadata not supplied.
Documentation | Undated | Google Quantum AI.
Identifier and resource: [Official resource](https://quantumai.google/cirq/simulate).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://quantumai.google/cirq/simulate); retrieved 2026-10-08.

### D24T02 Tensor network simulation

Tensor network methods exploit circuit structure and limited entanglement. Bond dimensions and contraction order control practical cost.

Fine subcategories: MPS; PEPS; contraction order; bond dimension; circuit contraction.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q1285 Scalable Quantum Molecular Generation via GPU-Accelerated Tensor-Network Simulation

Yu-Cheng Xiao, Jen-Yu Chang, Tzu-Ling Kuo, Aninda Astuti, Shu-Chi Wu, Ka-Lok Ng, Yun-Yuan Wang, Yu-Ze Chen et al..
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 852-856.
Identifier and resource: [10.1109/qcnc69040.2026.00140](https://doi.org/10.1109/qcnc69040.2026.00140).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00140); retrieved 2026-10-08.

#### Q1286 Scalable Tensor Network Simulation for Quantum-Classical Dual Kernel

Mei Ian Sam, Tai-Yu Li.
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 900-905.
Identifier and resource: [10.1109/qcnc69040.2026.00148](https://doi.org/10.1109/qcnc69040.2026.00148).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00148); retrieved 2026-10-08.

#### Q1287 Sparse Tensor-Network Quantum Machine Learning for Simulation, Cybersecurity and Scientific Discovery

Murali Krishna Pasupuleti.
Reference book | 2026 | National Education Services.
Identifier and resource: [10.62311/nesx/rb8jy-978-81-688729-2-9](https://doi.org/10.62311/nesx/rb8jy-978-81-688729-2-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62311%2Fnesx%2Frb8jy-978-81-688729-2-9); retrieved 2026-10-08.

#### Q1288 Tensor-Network Neural Operators for Quantum-AI Scientific Simulation

Murali Krishna Pasupuleti.
Reference book | 2026 | National Education Services.
Identifier and resource: [10.62311/nesx/rb8m-978-81-686966-2-4](https://doi.org/10.62311/nesx/rb8m-978-81-686966-2-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62311%2Fnesx%2Frb8m-978-81-686966-2-4); retrieved 2026-10-08.

#### Q1289 Approximate Quantum Compiling for Quantum Simulation: A Tensor Network Based Approach

Niall Robertson, Albert Akhriev, Jiri Vala, Sergiy Zhuk.
Journal article | 2025 | ACM Transactions on Quantum Computing | vol. 6 | no. 3 | pp. 1-15.
Identifier and resource: [10.1145/3731251](https://doi.org/10.1145/3731251).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3731251); retrieved 2026-10-08.

#### Q1290 Efficient simulation of leakage errors in quantum error correcting codes using tensor network methods

Hidetaka Manabe, Yasunari Suzuki, Andrew S Darmawan.
Journal article | 2025 | New Journal of Physics | vol. 27 | no. 11 | pp. 114512.
Identifier and resource: [10.1088/1367-2630/ae1529](https://doi.org/10.1088/1367-2630/ae1529).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fae1529); retrieved 2026-10-08.

#### Q1291 Hybrid Tree Tensor Networks for Quantum Simulation

Julian Schuhmacher, Marco Ballarin, Alberto Baiardi, Giuseppe Magnifico, Francesco Tacchino, Simone Montangero, Ivano Tavernelli.
Journal article | 2025 | PRX Quantum | vol. 6 | no. 1 | article 010320.
Identifier and resource: [10.1103/prxquantum.6.010320](https://doi.org/10.1103/prxquantum.6.010320).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fprxquantum.6.010320); retrieved 2026-10-08.

#### Q1292 Numerical Simulation of Two-Dimensional Quantum XYX Model Based on Tensor Network Algorithm

Sheng-Hao Li, Yuan-Cheng Luo, Yuan-Yuan Wu.
Conference paper | 2025 | 2025 2nd International Conference on Intelligent Computing and Robotics (ICICR) | pp. 1208-1212.
Identifier and resource: [10.1109/icicr65456.2025.00214](https://doi.org/10.1109/icicr65456.2025.00214).
Conference metadata: 2025 2nd International Conference on Intelligent Computing and Robotics (ICICR).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficicr65456.2025.00214); retrieved 2026-10-08.

#### Q1293 Parallel Tensor Network Contraction for Efficient Quantum Circuit Simulation on Multicore CPUs and GPUs

Alfred Pastor, Maribel Castillo, Jose Badia.
Conference paper | 2025 | Proceedings of the 1st International Conference on Quantum Software | pp. 120-127.
Identifier and resource: [10.5220/0013551400004525](https://doi.org/10.5220/0013551400004525).
Conference metadata: 1st International Conference on Quantum Software.
Fine tags: circuit contraction.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5220%2F0013551400004525); retrieved 2026-10-08.

#### Q1294 Coded Computing Meets Quantum Circuit Simulation: Coded Parallel Tensor Network Contraction Algorithm

Jin Lee, Zheng Zhang, Sofía González-García, Haewon Jeong.
Conference paper | 2024 | 2024 IEEE International Symposium on Information Theory (ISIT) | pp. 3095-3100.
Identifier and resource: [10.1109/isit57864.2024.10619404](https://doi.org/10.1109/isit57864.2024.10619404).
Conference metadata: 2024 IEEE International Symposium on Information Theory (ISIT).
Fine tags: circuit contraction.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisit57864.2024.10619404); retrieved 2026-10-08.

#### Q1295 Efficient Quantum Circuit Simulation by Tensor Network Methods on Modern GPUs

Feng Pan, Hanfeng Gu, Lvlin Kuang, Bing Liu, Pan Zhang.
Journal article | 2024 | ACM Transactions on Quantum Computing | vol. 5 | no. 4 | pp. 1-26.
Identifier and resource: [10.1145/3696465](https://doi.org/10.1145/3696465).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3696465); retrieved 2026-10-08.

#### Q1296 Efficient tensor network simulation of IBM's largest quantum processors

Siddhartha Patra, Saeed S. Jahromi, Sukhbinder Singh, Román Orús.
Journal article | 2024 | Physical Review Research | vol. 6 | no. 1 | article 013326.
Identifier and resource: [10.1103/physrevresearch.6.013326](https://doi.org/10.1103/physrevresearch.6.013326).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.6.013326); retrieved 2026-10-08.

#### Q1297 Optimal tree tensor network operators for tensor network simulations: Applications to open quantum systems

Weitang Li, Jiajun Ren, Hengrui Yang, Haobin Wang, Zhigang Shuai.
Journal article | 2024 | The Journal of Chemical Physics | vol. 161 | no. 5 | article 054116.
Identifier and resource: [10.1063/5.0218773](https://doi.org/10.1063/5.0218773).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0218773); retrieved 2026-10-08.

#### Q1298 Tensor network simulation of chains of non-Markovian open quantum systems

Gerald E. Fux, Dainius Kilda, Brendon W. Lovett, Jonathan Keeling.
Journal article | 2023 | Physical Review Research | vol. 5 | no. 3 | article 033078.
Identifier and resource: [10.1103/physrevresearch.5.033078](https://doi.org/10.1103/physrevresearch.5.033078).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevresearch.5.033078); retrieved 2026-10-08.

#### Q1299 GitHub - jcmgray/quimb: A python library for quantum information and many-body calculations including tensor networks. · GitHub

Author metadata not supplied.
Software repository | Undated | Quimb.
Identifier and resource: [Official resource](https://github.com/jcmgray/quimb).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/jcmgray/quimb); retrieved 2026-10-08.

### D24T03 Stabilizer circuit simulation

Stabilizer simulation efficiently handles Clifford operations and suitable states. Non Clifford extensions require additional resources or approximation.

Fine subcategories: Gottesman Knill; tableau methods; Clifford circuits; non Clifford extensions.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1300 GPU-Accelerated Quantum Simulation of Stabilizer Circuits

Muhammad Osama, Dimitrios Thanos, Alfons Laarman.
Journal article | 2026 | Quantum | vol. 10 | pp. 2225 | article 2225.
Identifier and resource: [10.22331/q-2026-10-01-2225](https://doi.org/10.22331/q-2026-10-01-2225).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2026-10-01-2225); retrieved 2026-10-08.

#### Q1301 Hybrid variational quantum circuit approach for stabilizer-state classifiers

Hamna Aslam, Frédéric Holweck.
Journal article | 2026 | Physical Review A | vol. 113 | no. 5 | article 052429.
Identifier and resource: [10.1103/tl4h-vs8y](https://doi.org/10.1103/tl4h-vs8y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ftl4h-vs8y); retrieved 2026-10-08.

#### Q1302 quEStab: Towards Scalable Quantum Circuit Simulation on Multi-GPU using an Extended Stabilizer Formalism

Hyunjoon Shin, Seokhyeon Lee, Myeongjin Kwak, Yongtae Kim.
Conference paper | 2026 | Proceedings of the 40th ACM International Conference on Supercomputing | pp. 1296-1309.
Identifier and resource: [10.1145/3797905.3816723](https://doi.org/10.1145/3797905.3816723).
Conference metadata: ICS '26: 2026 International Conference on Supercomputing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3797905.3816723); retrieved 2026-10-08.

#### Q1303 Abstraqt: Analysis of Quantum Circuits via Abstract Stabilizer Simulation

Benjamin Bichsel, Anouk Paradis, Maximilian Baader, Martin Vechev.
Journal article | 2023 | Quantum | vol. 7 | pp. 1185 | article 1185.
Identifier and resource: [10.22331/q-2023-11-20-1185](https://doi.org/10.22331/q-2023-11-20-1185).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-11-20-1185); retrieved 2026-10-08.

#### Q1304 SIMULATION OF THE STABILIZER BOOST CIRCUIT FROM A CAPACITIVE STORAGE

Kamchatka State Technical University, Sergei Yu. Trudnev, Kamchatka State Technical University, Aleksei A. Marchenko.
Journal article | 2020 | Vestnik Gosudarstvennogo universiteta morskogo i rechnogo flota imeni admirala S. O. Makarova | vol. 12 | no. 6 | pp. 1118-1127.
Identifier and resource: [10.21821/2309-5180-2020-12-6-1118-1127](https://doi.org/10.21821/2309-5180-2020-12-6-1118-1127).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21821%2F2309-5180-2020-12-6-1118-1127); retrieved 2026-10-08.

#### Q1305 Simulation of quantum circuits by low-rank stabilizer decompositions

Sergey Bravyi, Dan Browne, Padraic Calpin, Earl Campbell, David Gosset, Mark Howard.
Journal article | 2019 | Quantum | vol. 3 | pp. 181 | article 181.
Identifier and resource: [10.22331/q-2019-09-02-181](https://doi.org/10.22331/q-2019-09-02-181).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2019-09-02-181); retrieved 2026-10-08.

#### Q1306 Simulation of Quantum Circuits via Stabilizer Frames

Hector J. Garcia, Igor L. Markov.
Journal article | 2015 | IEEE Transactions on Computers | vol. 64 | no. 8 | pp. 2323-2336.
Identifier and resource: [10.1109/tc.2014.2360532](https://doi.org/10.1109/tc.2014.2360532).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftc.2014.2360532); retrieved 2026-10-08.

#### Q1307 Quipu: High-performance simulation of quantum circuits using stabilizer frames

Héctor J. García, Igor L. Markov.
Conference paper | 2013 | 2013 IEEE 31st International Conference on Computer Design (ICCD) | pp. 404-410.
Identifier and resource: [10.1109/iccd.2013.6657072](https://doi.org/10.1109/iccd.2013.6657072).
Conference metadata: 2013 IEEE 31st International Conference on Computer Design (ICCD).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficcd.2013.6657072); retrieved 2026-10-08.

### D24T04 Quantum GPU and HPC integration

GPU and distributed HPC methods accelerate selected classical simulation operations. Memory bandwidth, communication, and precision determine real performance.

Fine subcategories: Accelerators; distributed memory; kernels; HPC scheduling; numerical validation.

Primary resources: 6. Additional related assignments can be found in the interactive HTML.

#### Q1308 Performance analysis and modeling for quantum computing simulation on distributed GPU platforms

Armin Ahmadzadeh, Hamid Sarbazi-Azad.
Journal article | 2024 | Quantum Information Processing | vol. 23 | no. 11 | article 373.
Identifier and resource: [10.1007/s11128-024-04580-x](https://doi.org/10.1007/s11128-024-04580-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-024-04580-x); retrieved 2026-10-08.

#### Q1309 High performance computing and quantum trajectory method in CPU and GPU systems

Joanna Wiśniewska, Marek Sawerwain, Wiesław Leoński.
Journal article | 2015 | Journal of Physics: Conference Series | vol. 574 | pp. 012127.
Identifier and resource: [10.1088/1742-6596/574/1/012127](https://doi.org/10.1088/1742-6596/574/1/012127).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F574%2F1%2F012127); retrieved 2026-10-08.

#### Q1310 GPU-aware distributed quantum simulation

Anderson Avila, Adriano Maron, Renata Reiser, Mauricio Pilla, Adenauer Yamin.
Conference paper | 2014 | Proceedings of the 29th Annual ACM Symposium on Applied Computing | pp. 860-865.
Identifier and resource: [10.1145/2554850.2554892](https://doi.org/10.1145/2554850.2554892).
Conference metadata: SAC 2014: Symposium on Applied Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F2554850.2554892); retrieved 2026-10-08.

#### Q1311 CUDA-Q — NVIDIA CUDA-Q documentation

Author metadata not supplied.
Documentation | Undated | NVIDIA.
Identifier and resource: [Official resource](https://nvidia.github.io/cuda-quantum/latest/index.html).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://nvidia.github.io/cuda-quantum/latest/index.html); retrieved 2026-10-08.

#### Q1312 Getting Started — NVIDIA cuQuantum

Author metadata not supplied.
Documentation | Undated | NVIDIA.
Identifier and resource: [Official resource](https://docs.nvidia.com/cuda/cuquantum/latest/getting-started/index.html).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://docs.nvidia.com/cuda/cuquantum/latest/getting-started/index.html); retrieved 2026-10-08.

#### Q1313 Quick Start — NVIDIA CUDA-Q documentation

Author metadata not supplied.
Tutorial | Undated | NVIDIA.
Identifier and resource: [Official resource](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html); retrieved 2026-10-08.

### D24T05 Hybrid quantum classical workflows

Hybrid workflows coordinate classical processing with quantum execution. Batching, data movement, scheduling, and asynchronous control affect end to end cost.

Fine subcategories: Batching; asynchronous jobs; optimization loops; data movement; heterogeneous computing.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1314 Hybrid Quantum Classical Integration

Aayushee G.
Journal article | 2026 | International Journal of Creative and Open Research in Engineering and Management | vol. 02 | no. 08 | pp. 1-9.
Identifier and resource: [10.55041/ijcope.v2i8.063](https://doi.org/10.55041/ijcope.v2i8.063).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55041%2Fijcope.v2i8.063); retrieved 2026-10-08.

#### Q1315 Hybrid Quantum Computing Workflow Optimization

Khalid Abdul Jaleel, Gold Sharon R, Nivi V.
Conference paper | 2026 | 2026 International Conference on Innovative Trends in Information Technology (ICITIIT) | pp. 1-6.
Identifier and resource: [10.1109/icitiit68860.2026.11499461](https://doi.org/10.1109/icitiit68860.2026.11499461).
Conference metadata: 2026 International Conference on Innovative Trends in Information Technology (ICITIIT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficitiit68860.2026.11499461); retrieved 2026-10-08.

#### Q1316 Hybrid Quantum–Classical Pipelines for Big Data Analytics: Workflow Design with Resource and Throughput Analyses

Laith S. Ismail, Bushra Jabbar Abdul-Kareem, Doaa Thamer Mohammed, Hussain Kassim Ahmad, Alona Desiatko.
Book chapter | 2026 | Communications in Computer and Information Science | pp. 431-457.
Identifier and resource: [10.1007/978-3-032-39708-9_22](https://doi.org/10.1007/978-3-032-39708-9_22).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-39708-9_22); retrieved 2026-10-08.

#### Q1317 Hybrid quantum–classical machine translation

Mina Abbaszadeh, Mariam Zomorodi, Mehrnoosh Sadrzadeh, Vahid Salari, Philip Kurian.
Journal article | 2026 | Quantum Information Processing | vol. 25 | no. 2 | article 49.
Identifier and resource: [10.1007/s11128-025-05032-w](https://doi.org/10.1007/s11128-025-05032-w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-025-05032-w); retrieved 2026-10-08.

#### Q1318 QSplit: A Workflow-Oriented Hybrid Quantum–Classical Optimization Framework

Mario Bifulco, Francesco Medina, Doriana Medić, Luca Roversi, Marco Aldinucci.
Book chapter | 2026 | Lecture Notes in Computer Science | pp. 195-209.
Identifier and resource: [10.1007/978-3-032-35251-4_14](https://doi.org/10.1007/978-3-032-35251-4_14).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-35251-4_14); retrieved 2026-10-08.

#### Q1319 RIGOLETTO: A Workflow Definition Language for Hybrid Quantum-Classical Scientific Applications

Vincenzo De Maio, Dominik Bork, Ivona Brandic.
Conference paper | 2024 | 2024 26th International Conference on Business Informatics (CBI) | pp. 40-49.
Identifier and resource: [10.1109/cbi62504.2024.00015](https://doi.org/10.1109/cbi62504.2024.00015).
Conference metadata: 2024 26th International Conference on Business Informatics (CBI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcbi62504.2024.00015); retrieved 2026-10-08.

#### Q1320 A hybrid classical-quantum workflow for natural language processing

Lee J O’Riordan, Myles Doyle, Fabio Baruffa, Venkatesh Kannan.
Journal article | 2020 | Machine Learning: Science and Technology | vol. 2 | no. 1 | pp. 015011.
Identifier and resource: [10.1088/2632-2153/abbd2e](https://doi.org/10.1088/2632-2153/abbd2e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2632-2153%2Fabbd2e); retrieved 2026-10-08.

#### Q1321 GitHub - NVIDIA/cuda-quantum: C++ and Python support for the CUDA Quantum programming model for heterogeneous quantum-classical workflows · GitHub

Author metadata not supplied.
Software repository | Undated | NVIDIA.
Identifier and resource: [Official resource](https://github.com/NVIDIA/cuda-quantum).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/NVIDIA/cuda-quantum); retrieved 2026-10-08.

## D25 Architecture cloud and distributed computing

Architecture combines qubits, classical control, compilation, and communication into a system. Distributed designs must include entanglement costs, synchronization, and failures.

Prerequisites: Quantum hardware, compilation, and distributed systems.

Assessment focus: Connectivity, scheduling, communication, queueing, and complete system cost.

Primary catalog resources in this category: 65.

### D25T01 Quantum processor architecture

Processor architecture combines connectivity, instruction execution, control, and packaging. The best design depends on the workload and error correction strategy.

Fine subcategories: Connectivity; modularity; instruction sets; control planes; co design.

Primary resources: 9. Additional related assignments can be found in the interactive HTML.

#### Q1322 Quantum Computing: An Applied Approach

Jack D. Hidary.
Book | 2021 | Springer International Publishing.
Identifier and resource: [10.1007/978-3-030-83274-2](https://doi.org/10.1007/978-3-030-83274-2).
ISBN: 9783030832735; 9783030832742.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-83274-2); retrieved 2026-10-08.

#### Q1323 Differentiable architecture search for adversarially robust quantum computer vision

Mohamed Afane, Quanjiang Long, Haoting Shen, Ying Mao, Junaid Farooq, Ying Wang, Juntao Chen.
Journal article | 2026 | Quantum Machine Intelligence | vol. 8 | no. 1 | article 2.
Identifier and resource: [10.1007/s42484-026-00353-0](https://doi.org/10.1007/s42484-026-00353-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-026-00353-0); retrieved 2026-10-08.

#### Q1324 Quantum Computer Hardware and Architecture—An Overview

Hiu Yung Wong.
Book chapter | 2025 | Quantum Computing Architecture and Hardware for Engineers | pp. 3-11.
Identifier and resource: [10.1007/978-3-031-78219-0_1](https://doi.org/10.1007/978-3-031-78219-0_1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-78219-0_1); retrieved 2026-10-08.

#### Q1325 The Tri-Computer Architecture: Unifying Space, Time, and Quantum Dimensions

Ethereum Computer, Jameson Joseph Bednarski, Rafael Henrique do Nascimento Oliveira.
Posted content | 2025 | DeSci Labs AG.
Identifier and resource: [10.62891/3b97db99](https://doi.org/10.62891/3b97db99).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62891%2F3b97db99); retrieved 2026-10-08.

#### Q1326 A modular entanglement-based quantum computer architecture

Ferran Riera-Sàbat, Wolfgang Dür.
Journal article | 2024 | New Journal of Physics | vol. 26 | no. 12 | pp. 123015.
Identifier and resource: [10.1088/1367-2630/ad9945](https://doi.org/10.1088/1367-2630/ad9945).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fad9945); retrieved 2026-10-08.

#### Q1327 Quantum Computing Impact on Traditional Computer Architecture Models

Alnoor University, Salih Mahmoud Attya, Suhad Qasim G. Haddad, Al Mansour University College, Hamid Kareem Radam Al-Zaidi, Al Hikma University College, Wafaa Mustafa Hameed, Cihan University Sulaimaniya et al..
Journal article | 2024 | Radioelectronics. Nanosystems. Information Technologies. | vol. 16 | no. 5 | pp. 691-704.
Identifier and resource: [10.17725/j.rensit.2024.16.691](https://doi.org/10.17725/j.rensit.2024.16.691).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.17725%2Fj.rensit.2024.16.691); retrieved 2026-10-08.

#### Q1328 Quantum Computing Impact on Traditional Computer Architecture Models

Университет Алнур, Салих Махмуд Аттья, Сухад Касим Дж. Хаддад, Университетский колледж Аль-Мансура, Хамид Карим Радам Аль-Заиди, Университетский колледж Аль-Хикма, Вафаа Мустафа Хамид, Университет Джихан et al..
Journal article | 2024 | Radioelectronics. Nanosystems. Information Technologies. | vol. 16 | no. 5 | pp. 691-704.
Identifier and resource: [10.17725/rensit.2024.16.691](https://doi.org/10.17725/rensit.2024.16.691).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.17725%2Frensit.2024.16.691); retrieved 2026-10-08.

#### Q1329 ION TRAP QUANTUM COMPUTER ARCHITECTURE

Grzegorz Kasprowicz.
Journal article | 2023 | ELEKTRONIKA - KONSTRUKCJE, TECHNOLOGIE, ZASTOSOWANIA | vol. 1 | no. 8 | pp. 14-18.
Identifier and resource: [10.15199/13.2023.8.3](https://doi.org/10.15199/13.2023.8.3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.15199%2F13.2023.8.3); retrieved 2026-10-08.

#### Q1330 Quantum Computer Architecture: A Quantum Circuit-Based Approach Towards Quantum Neural Network

Tariq Mahmood, Talab Hussain, Maqsood Ahmed.
Journal article | 2023 | Proceedings of the Pakistan Academy of Sciences: A. Physical and Computational Sciences | vol. 60 | no. 2.
Identifier and resource: [10.53560/ppasa(60-2)668](https://doi.org/10.53560/ppasa(60-2)668).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.53560%2Fppasa%2860-2%29668); retrieved 2026-10-08.

### D25T02 Distributed quantum computing

Distributed computation uses entanglement or remote operations across processors. Partitioning and communication overhead must be included in scaling claims.

Fine subcategories: Remote gates; partitioning; entanglement consumption; synchronization; latency.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1331 A Quantum Circuit Optimization Framework for Distributed Quantum Computing

Fengsheng Liu, Fudong Liu, Yangyang Fei, Hong Wang, Junchao Wang, Haodong Jiang, Zhi Ma.
Journal article | 2026 | IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | vol. 45 | no. 10 | pp. 4762-4771.
Identifier and resource: [10.1109/tcad.2026.3656760](https://doi.org/10.1109/tcad.2026.3656760).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftcad.2026.3656760); retrieved 2026-10-08.

#### Q1332 Cost-Aware Quantum Bit Mapping for Distributed Quantum Computing

Furong Zhan, Xiaoyu Wang, Yangming Zhao, Hongli Xu.
Conference paper | 2026 | 2026 International Wireless Communications and Mobile Computing (IWCMC) | pp. 857-862.
Identifier and resource: [10.1109/iwcmc69287.2026.11580025](https://doi.org/10.1109/iwcmc69287.2026.11580025).
Conference metadata: 2026 International Wireless Communications and Mobile Computing (IWCMC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fiwcmc69287.2026.11580025); retrieved 2026-10-08.

#### Q1333 Distributed Quantum Computing for Scalable Systems

Daniel Casado Faulí, Parfait Atchade-Adelomou, David Pérez de Lara, Rodrigo Gil-Merino.
Book chapter | 2026 | Lecture Notes in Networks and Systems | pp. 243-253.
Identifier and resource: [10.1007/978-3-032-05748-8_20](https://doi.org/10.1007/978-3-032-05748-8_20).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-05748-8_20); retrieved 2026-10-08.

#### Q1334 On Distributed Quantum Computing with Distributed Fan-Out Operations

Seng W. Loke.
Conference paper | 2026 | 2026 IEEE International Conference on Quantum Software (QSW) | pp. 1-6.
Identifier and resource: [10.1109/qsw72780.2026.00034](https://doi.org/10.1109/qsw72780.2026.00034).
Conference metadata: 2026 IEEE International Conference on Quantum Software (QSW).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqsw72780.2026.00034); retrieved 2026-10-08.

#### Q1335 Optimized Compilation for Distributed Quantum Computing

Michele Bandini, Davide Ferrari, Stefano Carretta, Michele Amoretti.
Journal article | 2026 | IEEE Access | vol. 14 | pp. 97220-97231.
Identifier and resource: [10.1109/access.2026.3706203](https://doi.org/10.1109/access.2026.3706203).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Faccess.2026.3706203); retrieved 2026-10-08.

#### Q1336 Distributed Quantum Computing: Applications and Challenges

Juan C. Boschero, Niels M. P. Neumann, Ward van der Schoot, Thom Sijpesteijn, Robert Wezeman.
Book chapter | 2025 | Lecture Notes in Networks and Systems | pp. 100-116.
Identifier and resource: [10.1007/978-3-031-92602-0_6](https://doi.org/10.1007/978-3-031-92602-0_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-92602-0_6); retrieved 2026-10-08.

#### Q1337 Distributed Quantum Neural Networks on Distributed Photonic Quantum Computing

Kuan-Cheng Chen, Chen-Yu Liu, Yu Shang, Felix Burt, Kin K. Leung.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1477-1488.
Identifier and resource: [10.1109/qce65121.2025.00165](https://doi.org/10.1109/qce65121.2025.00165).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00165); retrieved 2026-10-08.

#### Q1338 Error correction for distributed quantum computing

Daowen Qiu, Ligang Xiao, Le Luo, Paulo Mateus.
Journal article | 2025 | EPJ Quantum Technology | vol. 12 | no. 1 | article 142.
Identifier and resource: [10.1140/epjqt/s40507-025-00455-x](https://doi.org/10.1140/epjqt/s40507-025-00455-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjqt%2Fs40507-025-00455-x); retrieved 2026-10-08.

#### Q1339 Evaluating Variational Quantum Circuit Architectures for Distributed Quantum Computing

Leo Sünkel, Jonas Stein, Jonas Nüßlein, Tobias Rohe, Claudia Linnhoff-Popien.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Artificial Intelligence (QAI) | pp. 343-350.
Identifier and resource: [10.1109/qai63978.2025.00060](https://doi.org/10.1109/qai63978.2025.00060).
Conference metadata: 2025 IEEE International Conference on Quantum Artificial Intelligence (QAI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqai63978.2025.00060); retrieved 2026-10-08.

#### Q1340 Online Locality Meets Distributed Quantum Computing

Amirreza Akbari, Xavier Coiteux-Roy, Francesco d'Amore, François Le Gall, Henrik Lievonen, Darya Melnyk, Augusto Modanese, Shreyas Pai et al..
Conference paper | 2025 | Proceedings of the 57th Annual ACM Symposium on Theory of Computing | pp. 1295-1306.
Identifier and resource: [10.1145/3717823.3718211](https://doi.org/10.1145/3717823.3718211).
Conference metadata: STOC '25: 57th Annual ACM Symposium on Theory of Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3717823.3718211); retrieved 2026-10-08.

#### Q1341 Optimizing Distributed Systems With Quantum Computing

Manish Patil, Shraddha Sanjay Mhetre.
Journal article | 2025 | INTERNATIONAL JOURNAL OF ADVANCES IN SIGNAL AND IMAGE SCIENCES | vol. 11 | no. 5s | pp. 683-700.
Identifier and resource: [10.29284/4rsdh697](https://doi.org/10.29284/4rsdh697).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.29284%2F4rsdh697); retrieved 2026-10-08.

#### Q1342 Review of Distributed Quantum Computing: From single QPU to High Performance Quantum Computing

David Barral, F. Javier Cardama, Guillermo Díaz-Camacho, Daniel Faílde, Iago F. Llovo, Mariamo Mussa-Juane, Jorge Vázquez-Pérez, Juan Villasuso et al..
Journal article | 2025 | Computer Science Review | vol. 57 | pp. 100747 | article 100747.
Identifier and resource: [10.1016/j.cosrev.2025.100747](https://doi.org/10.1016/j.cosrev.2025.100747).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.cosrev.2025.100747); retrieved 2026-10-08.

#### Q1343 Towards Distributed Quantum Error Correction for Distributed Quantum Computing

Shahram Babaie, Chunming Qiao.
Conference paper | 2025 | 2025 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 66-73.
Identifier and resource: [10.1109/qcnc64685.2025.00019](https://doi.org/10.1109/qcnc64685.2025.00019).
Conference metadata: 2025 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc64685.2025.00019); retrieved 2026-10-08.

#### Q1344 Transversal Fault Tolerant Distributed Quantum Computing Operations

Frank Mueller, Ming Wang, John Stack.
Posted content | 2025 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-7633777/v1](https://doi.org/10.21203/rs.3.rs-7633777/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-7633777%2Fv1); retrieved 2026-10-08.

#### Q1345 Distributed Quantum Computing via Integrating Quantum and Classical Computing

Wei Tang, Margaret Martonosi.
Journal article | 2024 | Computer | vol. 57 | no. 4 | pp. 131-136.
Identifier and resource: [10.1109/mc.2024.3360569](https://doi.org/10.1109/mc.2024.3360569).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmc.2024.3360569); retrieved 2026-10-08.

#### Q1346 Distributed quantum computing: A survey

Marcello Caleffi, Michele Amoretti, Davide Ferrari, Jessica Illiano, Antonio Manzalini, Angela Sara Cacciapuoti.
Journal article | 2024 | Computer Networks | vol. 254 | pp. 110672 | article 110672.
Identifier and resource: [10.1016/j.comnet.2024.110672](https://doi.org/10.1016/j.comnet.2024.110672).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.comnet.2024.110672); retrieved 2026-10-08.

### D25T03 Quantum cloud execution

Cloud execution provides remote access and job orchestration for quantum devices. Queue delays, device changes, and preserved experiment metadata affect reproducibility.

Fine subcategories: Queues; job orchestration; access models; reproducibility; provider abstraction.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1347 Cloud Quantum Computing

Marcus Stephen Edwards.
Book chapter | 2026 | An Introduction to Quantum Computing for Computer Engineers | pp. 265-295.
Identifier and resource: [10.1007/978-3-032-03650-6_10](https://doi.org/10.1007/978-3-032-03650-6_10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03650-6_10); retrieved 2026-10-08.

#### Q1348 Distributed Scheduling for Modular Quantum Computing in Cloud

Vinooth Rao Kulkarni, Vipin Chaudhary.
Conference paper | 2026 | Proceedings of the 35th International Symposium on High-Performance Parallel and Distributed Computing | pp. 572-574.
Identifier and resource: [10.1145/3806645.3820071](https://doi.org/10.1145/3806645.3820071).
Conference metadata: HPDC '26: 35th International Symposium on High-Performance Parallel and Distributed Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3806645.3820071); retrieved 2026-10-08.

#### Q1349 Quantum Computing and Cloud

Premanand Narasimhan, Aruna Buvaneswari.
Journal article | 2026 | International Journal of Scientific Research in Computer Science, Engineering and Information Technology | vol. 12 | no. 2 | pp. 56-61.
Identifier and resource: [10.32628/cseit26121327](https://doi.org/10.32628/cseit26121327).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.32628%2Fcseit26121327); retrieved 2026-10-08.

#### Q1350 Cloud Computing Framework based on Quantum-Neuromorphic Technology

Surya Bhushan Kumar, Kuntal Mukherjee, Swapan Dey.
Conference paper | 2025 | 2025 International Conference on Sustainability, Innovation &amp; Technology (ICSIT) | pp. 1-6.
Identifier and resource: [10.1109/icsit65336.2025.11295176](https://doi.org/10.1109/icsit65336.2025.11295176).
Conference metadata: 2025 International Conference on Sustainability, Innovation & Technology (ICSIT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficsit65336.2025.11295176); retrieved 2026-10-08.

#### Q1351 Enhancing Cloud Security Via Quantum Computing

Praveen Chaitanya Jakku, Prasad Sundaramoorthy, Sharath Chandra Kondaparthy, Tanvi Desai, Rohit Jarubula, Anusha Nerella.
Book chapter | 2025 | Lecture Notes in Networks and Systems | pp. 377-386.
Identifier and resource: [10.1007/978-3-032-03558-5_31](https://doi.org/10.1007/978-3-032-03558-5_31).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-03558-5_31); retrieved 2026-10-08.

#### Q1352 Qonductor: A Cloud Orchestrator for Quantum Computing

Emmanouil Giortamis, Francisco Romao, Nathaniel Tornow, Dmitry Lugovoy, Pramod Bhatotia.
Conference paper | 2025 | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis | pp. 728-745.
Identifier and resource: [10.1145/3712285.3759785](https://doi.org/10.1145/3712285.3759785).
Conference metadata: SC '25: The International Conference for High Performance Computing, Networking, Storage and Analysis.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3712285.3759785); retrieved 2026-10-08.

#### Q1353 Quantum Cloud Computing Breakthrough

MCA, Zeal Institute of Business Administration, Computer Application & Research, Prof. Nitin Ramarao Yadav, Anurag Omprakash Shastri.
Journal article | 2025 | INTERNATIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT | vol. 09 | no. 11 | pp. 1-9.
Identifier and resource: [10.55041/ijsrem54158](https://doi.org/10.55041/ijsrem54158).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55041%2Fijsrem54158); retrieved 2026-10-08.

#### Q1354 Quantum Cloud Ecosystems: Building Scalable, Multi-Tenant Quantum Computing Platforms

Murali Krishna Pasupuleti.
Reference book | 2025 | National Education Services.
Identifier and resource: [10.62311/nesx/rb68](https://doi.org/10.62311/nesx/rb68).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62311%2Fnesx%2Frb68); retrieved 2026-10-08.

#### Q1355 Quantum Computing, AI, ML, and the Cloud

Arthur M. Langer.
Book chapter | 2025 | Analysis and Design of Next-Generation Software Architectures | pp. 167-181.
Identifier and resource: [10.1007/978-3-031-76212-3_8](https://doi.org/10.1007/978-3-031-76212-3_8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-76212-3_8); retrieved 2026-10-08.

#### Q1356 Quantum Edge Cloud Computing: Revolutionizing IoT

Aanya Tiwari, Ahsaan Ahmad Ahanger, Anjali Meena, Pawan Singh Mehra.
Conference paper | 2025 | 2025 3rd International Conference on Device Intelligence, Computing and Communication Technologies (DICCT) | pp. 626-631.
Identifier and resource: [10.1109/dicct64131.2025.10986380](https://doi.org/10.1109/dicct64131.2025.10986380).
Conference metadata: 2025 3rd International Conference on Device Intelligence, Computing and Communication Technologies (DICCT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fdicct64131.2025.10986380); retrieved 2026-10-08.

#### Q1357 Quantum as a Service in Cloud Computing

Abdelkader Laouid, Mostefa Kara, Khaled Chait.
Book chapter | 2025 | Quantum Technology Applications, Impact, and Future Challenges | pp. 124-140.
Identifier and resource: [10.1201/9781003537243-8](https://doi.org/10.1201/9781003537243-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003537243-8); retrieved 2026-10-08.

#### Q1358 Quantum cloud computing: Enterprise strategies for hybrid quantum-classical workloads

Clement Praveen Xavier Pakkam Isaac.
Journal article | 2025 | World Journal of Advanced Research and Reviews | vol. 26 | no. 1 | pp. 2245-2262.
Identifier and resource: [10.30574/wjarr.2025.26.1.1248](https://doi.org/10.30574/wjarr.2025.26.1.1248).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.30574%2Fwjarr.2025.26.1.1248); retrieved 2026-10-08.

#### Q1359 Quantum Process Tomography on Cloud-accessible Quantum Computing Platforms

P. E. Vedrukov, A. D. Ivlev, A. V. Liniov, I. B. Meyerov, M. V. Ivanchenko.
Journal article | 2024 | Lobachevskii Journal of Mathematics | vol. 45 | no. 1 | pp. 119-129.
Identifier and resource: [10.1134/s1995080224010529](https://doi.org/10.1134/s1995080224010529).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1134%2Fs1995080224010529); retrieved 2026-10-08.

#### Q1360 Quantum cloud computing: Trends and challenges

Muhammed Golec, Emir Sahin Hatay, Mustafa Golec, Murat Uyar, Merve Golec, Sukhpal Singh Gill.
Journal article | 2024 | Journal of Economy and Technology | vol. 2 | pp. 190-199.
Identifier and resource: [10.1016/j.ject.2024.05.001](https://doi.org/10.1016/j.ject.2024.05.001).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.ject.2024.05.001); retrieved 2026-10-08.

#### Q1361 Secure Quantum Cloud Computing

Ming-Xing Luo.
Book chapter | 2024 | Quantum Networks | pp. 249-291.
Identifier and resource: [10.1007/978-981-97-6226-2_7](https://doi.org/10.1007/978-981-97-6226-2_7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-97-6226-2_7); retrieved 2026-10-08.

#### Q1362 Universal terminal for cloud quantum computing

Mohammadsadegh Khazali.
Journal article | 2024 | Scientific Reports | vol. 14 | no. 1 | article 15412.
Identifier and resource: [10.1038/s41598-024-65899-0](https://doi.org/10.1038/s41598-024-65899-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-024-65899-0); retrieved 2026-10-08.

### D25T04 Quantum circuit cutting

Circuit cutting reconstructs a larger circuit from smaller experiments and classical postprocessing. Sampling overhead can grow rapidly with the number and type of cuts.

Fine subcategories: Wire cutting; gate cutting; reconstruction; shot overhead; partitioning.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1363 Co-design threading model and circuit cutting for static and adaptive quantum circuits

Waldemir Cambiucci, Regina Melo Silveira, Wilson Vicente Ruggiero.
Journal article | 2026 | Quantum Information Processing | vol. 25 | no. 4 | article 118.
Identifier and resource: [10.1007/s11128-026-05136-x](https://doi.org/10.1007/s11128-026-05136-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-026-05136-x); retrieved 2026-10-08.

#### Q1364 DAScut: density-and-structure-aware circuit cutting for scalable quantum simulations

Theodora Adufu, Yoonhee Kim.
Journal article | 2026 | Cluster Computing | vol. 29 | no. 3 | article 163.
Identifier and resource: [10.1007/s10586-025-05911-y](https://doi.org/10.1007/s10586-025-05911-y).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10586-025-05911-y); retrieved 2026-10-08.

#### Q1365 Gate Teleportation vs. Circuit Cutting in Distributed Quantum Computing

Shobhit Gupta, Daniel J. Dilley, Nikolay Sheshko, Alvin Gonzales, Sean E. Sullivan, Manish K. Singh, Zain H. Saleem.
Journal article | 2026 | Advanced Quantum Technologies | vol. 9 | no. 9 | article e70424.
Identifier and resource: [10.1002/qute.70424](https://doi.org/10.1002/qute.70424).
Fine tags: gate cutting.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.70424); retrieved 2026-10-08.

#### Q1366 QCutSim: Accelerating Quantum Circuit Cutting Simulation on Consumer-Grade Classical Systems

Po-Hsuan Huang, Chun-Yen Tai, Chia-Heng Tu, Shih-Hao Hung.
Journal article | 2026 | ACM Transactions on Design Automation of Electronic Systems | article 3833423.
Identifier and resource: [10.1145/3833423](https://doi.org/10.1145/3833423).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3833423); retrieved 2026-10-08.

#### Q1367 QuMod: Parallel Quantum Job Scheduling on Modular QPUs Using Circuit Cutting

Vinooth Kulkarni, Aaron Orenstein, Xinpeng Li, Shuai Xu, Daniel Blankenberg, Vipin Chaudhary.
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 75-82.
Identifier and resource: [10.1109/qcnc69040.2026.00020](https://doi.org/10.1109/qcnc69040.2026.00020).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00020); retrieved 2026-10-08.

#### Q1368 Reducing Maximum Subcircuits Depth in Quantum Circuit Cutting

Milad Eslaminia, Sébastien Le Beux.
Journal article | 2026 | IEEE Transactions on Quantum Engineering | vol. 7 | pp. 3103209-3103209.
Identifier and resource: [10.1109/tqe.2026.3690593](https://doi.org/10.1109/tqe.2026.3690593).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2026.3690593); retrieved 2026-10-08.

#### Q1369 Scalable Quantum Circuit Simulation via Circuit Cutting and FPGA Acceleration

Xiaokun Yang, Xinpeng Li, Jeremy W Turner, Cameron D Disomma, Yunhe Feng, Xuechen Zhang, Vipin Chaudhary, Shuai Xu.
Conference paper | 2026 | Proceedings of the 35th International Symposium on High-Performance Parallel and Distributed Computing | pp. 642-650.
Identifier and resource: [10.1145/3806645.3816155](https://doi.org/10.1145/3806645.3816155).
Conference metadata: HPDC '26: 35th International Symposium on High-Performance Parallel and Distributed Computing.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3806645.3816155); retrieved 2026-10-08.

#### Q1370 A generalized reconstruction model in circuit cutting and nonlocal-gate-based distributed quantum computation

Yi Sun, Changhua Zhu, Yuan Zhao, Guangwu Hou.
Journal article | 2025 | New Journal of Physics | vol. 27 | no. 11 | pp. 114508.
Identifier and resource: [10.1088/1367-2630/ae1866](https://doi.org/10.1088/1367-2630/ae1866).
Fine tags: gate cutting; reconstruction.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fae1866); retrieved 2026-10-08.

#### Q1371 DevQCC: Device-Aware Quantum Circuit Cutting framework with applications in quantum machine learning

Himanshu Sahu, Hari Prabhat Gupta, Vishnu Vardhan Puvvada, Rahul Mishra.
Journal article | 2025 | Quantum Machine Intelligence | vol. 7 | no. 2 | article 89.
Identifier and resource: [10.1007/s42484-025-00313-0](https://doi.org/10.1007/s42484-025-00313-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs42484-025-00313-0); retrieved 2026-10-08.

#### Q1372 Improved sampling bounds and scalable partitioning for quantum circuit cutting beyond bipartitions

Junya Nakamura, Takahiko Satoh, Shinichiro Sanji.
Journal article | 2025 | Physical Review A | vol. 112 | no. 4 | article 042422.
Identifier and resource: [10.1103/xnw7-mtbd](https://doi.org/10.1103/xnw7-mtbd).
Fine tags: partitioning.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fxnw7-mtbd); retrieved 2026-10-08.

#### Q1373 Is Circuit Cutting Scalable for Practical Quantum Applications?

Songqinghao Yang, Prakash Murali.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 428-438.
Identifier and resource: [10.1109/qce65121.2025.00055](https://doi.org/10.1109/qce65121.2025.00055).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00055); retrieved 2026-10-08.

#### Q1374 Orchestrating Quantum-HPC Workflows with Distributed Quantum Circuit Cutting

Mar Tejedor, Berta Casas, Javier Conejero, Alba Cervera-Lierta, Rosa M. Badia.
Conference paper | 2025 | Proceedings of the SC '25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis | pp. 1898-1906.
Identifier and resource: [10.1145/3731599.3767547](https://doi.org/10.1145/3731599.3767547).
Conference metadata: SC Workshops '25: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3731599.3767547); retrieved 2026-10-08.

#### Q1375 QuFlex: Parallel Quantum Job Scheduling using Adaptive Circuit Cutting

Vinooth Kulkarni, Aaron Orenstein, Xinpeng Li, Shuai Xu, Daniel Blankenberg, Vipin Chaudhary.
Conference paper | 2025 | 2025 Supercomputing India (SCI) | pp. 1-8.
Identifier and resource: [10.1109/sci68648.2025.11333863](https://doi.org/10.1109/sci68648.2025.11333863).
Conference metadata: 2025 Supercomputing India (SCI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fsci68648.2025.11333863); retrieved 2026-10-08.

#### Q1376 Quantum Circuit Cutting: A Security Methodology

George Typaldos, Theodoros Trochatos, Jakub Szefer.
Conference paper | 2025 | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 417-427.
Identifier and resource: [10.1109/qce65121.2025.00054](https://doi.org/10.1109/qce65121.2025.00054).
Conference metadata: 2025 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce65121.2025.00054); retrieved 2026-10-08.

#### Q1377 State Dependent Optimization with Quantum Circuit Cutting

Xinpeng Li, Ji Liu, Jeffrey M. Larson, Shuai Xu, Sundararaja Sitharama Iyengar, Paul Hovland, Vipin Chaudhary.
Conference paper | 2025 | 2025 IEEE Computer Society Annual Symposium on VLSI (ISVLSI) | pp. 1-6.
Identifier and resource: [10.1109/isvlsi65124.2025.11130234](https://doi.org/10.1109/isvlsi65124.2025.11130234).
Conference metadata: 2025 IEEE Computer Society Annual Symposium on VLSI (ISVLSI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisvlsi65124.2025.11130234); retrieved 2026-10-08.

#### Q1378 Patterns for Quantum Circuit Cutting

Author metadata not supplied.
Conference paper | 2024 | Proceedings of the 30th Conference on Pattern Languages of Programs.
Identifier and resource: [10.64346/plop2023p25](https://doi.org/10.64346/plop2023p25).
Conference metadata: 30th Conference on Pattern Languages of Programs.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.64346%2Fplop2023p25); retrieved 2026-10-08.

### D25T05 Quantum memory architecture

Quantum memories preserve states for later operations or communication. Lifetime, retrieval efficiency, fidelity, and interface compatibility determine their role.

Fine subcategories: Storage fidelity; memory lifetime; interfaces; multiplexing; logical memory.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1379 Photonic Quantum Computing on Spin Memory Architecture with Tree-Encoded Fusion

Xiangyu Ren, Yuexun Huang, Zhemin Zhang, Yuchen Zhu, Tsung-Yi Ho, Antonio Barbalace, Zhiding Liang.
Conference paper | 2026 | 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA) | pp. 2333-2348.
Identifier and resource: [10.1109/isca66397.2026.00164](https://doi.org/10.1109/isca66397.2026.00164).
Conference metadata: 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisca66397.2026.00164); retrieved 2026-10-08.

#### Q1380 Quantum-enhanced reconfigurable in-memory stochastic computing

Hong-Zhe Yang, Jian-Peng Dou, Feng Lu, Xiao-Wen Shang, Chao-Ni Zhang, Heng Zhou, Hao Tang, Xian-Min Jin.
Journal article | 2026 | Light: Science & Applications | vol. 15 | no. 1 | article 178.
Identifier and resource: [10.1038/s41377-025-02181-6](https://doi.org/10.1038/s41377-025-02181-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41377-025-02181-6); retrieved 2026-10-08.

#### Q1381 Quantum Cognition: A Cognitive Architecture for Human-AI and In-Memory Computing

Fariborz Farahmand.
Journal article | 2023 | Computer | vol. 56 | no. 4 | pp. 135-138.
Identifier and resource: [10.1109/mc.2023.3242056](https://doi.org/10.1109/mc.2023.3242056).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmc.2023.3242056); retrieved 2026-10-08.

#### Q1382 Quantum memory decoherence-mitigating architecture for quantum repeaters

Siddhartha Santra, Liang Jiang, Vladimir S. Malinovsky.
Conference paper | 2019 | Quantum Information and Measurement (QIM) V: Quantum Technologies | pp. S1D.4.
Identifier and resource: [10.1364/qim.2019.s1d.4](https://doi.org/10.1364/qim.2019.s1d.4).
Conference metadata: Quantum Information and Measurement.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fqim.2019.s1d.4); retrieved 2026-10-08.

#### Q1383 Quantum probabilistic associative memory architecture

Fernando M de Paula Neto, Adenilton J da Silva, Wilson R de Oliveira, Teresa B. Ludermir.
Journal article | 2019 | Neurocomputing | vol. 351 | pp. 101-110.
Identifier and resource: [10.1016/j.neucom.2019.03.078](https://doi.org/10.1016/j.neucom.2019.03.078).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.neucom.2019.03.078); retrieved 2026-10-08.

#### Q1384 Architectures of Quantum Memory-driven Computing

Vladimir Hahanov, Svetlana Chumachenko, Eugenia Litvinova, Hanna Khakhanova.
Conference paper | 2018 | 2018 IEEE East-West Design & Test Symposium (EWDTS) | pp. 1-7.
Identifier and resource: [10.1109/ewdts.2018.8524843](https://doi.org/10.1109/ewdts.2018.8524843).
Conference metadata: 2018 IEEE East-West Design & Test Symposium (EWDTS).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fewdts.2018.8524843); retrieved 2026-10-08.

#### Q1385 Realization of processing In-memory computing architecture using Quantum Dot Cellular Automata

P.P. Chougule, B. Sen, T.D. Dongale.
Journal article | 2017 | Microprocessors and Microsystems | vol. 52 | pp. 49-58.
Identifier and resource: [10.1016/j.micpro.2017.04.022](https://doi.org/10.1016/j.micpro.2017.04.022).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.micpro.2017.04.022); retrieved 2026-10-08.

#### Q1386 Single-flux-quantum cache memory architecture

Koki Ishida, Masamitsu Tanaka, Takatsugu Ono, Koji Inoue.
Conference paper | 2016 | 2016 International SoC Design Conference (ISOCC) | pp. 105-106.
Identifier and resource: [10.1109/isocc.2016.7799755](https://doi.org/10.1109/isocc.2016.7799755).
Conference metadata: 2016 International SoC Design Conference (ISOCC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisocc.2016.7799755); retrieved 2026-10-08.

## D26 Quantum networks and communication

Quantum networking distributes quantum states or entanglement between nodes. Protocols and hardware must account for loss, timing, storage, and classical coordination.

Prerequisites: Quantum channels, entanglement, and networking.

Assessment focus: Loss, memory lifetime, heralding, synchronization, and capacity assumptions.

Primary catalog resources in this category: 52.

### D26T01 Quantum teleportation

Teleportation transfers a state using shared entanglement, measurements, and classical messages. It does not transmit usable information faster than light.

Fine subcategories: Bell measurements; classical feed forward; fidelity; network teleportation.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1387 Quantum Teleportation

F. J. Duarte.
Book chapter | 2026 | Quantum Clear | pp. 55-56.
Identifier and resource: [10.1201/9781003649434-13](https://doi.org/10.1201/9781003649434-13).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003649434-13); retrieved 2026-10-08.

#### Q1388 Quantum Teleportation

Meryem El Kirdi, Hanane El Hadfi, Lalla Btissam Drissi, Rachid Ahl Laamara, Abdallah Slaoui.
Book chapter | 2026 | Quantum Computing for Multimedia Processing, Teleportation, and Secure Networks | pp. 173-199.
Identifier and resource: [10.1201/9781003621423-11](https://doi.org/10.1201/9781003621423-11).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003621423-11); retrieved 2026-10-08.

#### Q1389 Boosted quantum teleportation

Simone E. D’Aurelio, Matthias J. Bayerbach, Stefanie Barz.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 37.
Identifier and resource: [10.1038/s41534-025-00992-4](https://doi.org/10.1038/s41534-025-00992-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-025-00992-4); retrieved 2026-10-08.

#### Q1390 Quantum Cryptography and Quantum Teleportation

F.J. Duarte.
Book chapter | 2024 | Quantum Optics for Engineers | pp. 258-268.
Identifier and resource: [10.1201/9781003398707-20](https://doi.org/10.1201/9781003398707-20).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003398707-20); retrieved 2026-10-08.

#### Q1391 Quantum Energy Teleportation versus Information Teleportation

Jinzhao Wang, Shunyu Yao.
Journal article | 2024 | Quantum | vol. 8 | pp. 1564 | article 1564.
Identifier and resource: [10.22331/q-2024-12-12-1564](https://doi.org/10.22331/q-2024-12-12-1564).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2024-12-12-1564); retrieved 2026-10-08.

#### Q1392 Multiphoton quantum teleportation

A.V. Belinsky, A.P. Grigorieva, I.I. Dzhadan.
Journal article | 2023 | Vestnik Moskovskogo Universiteta, Seriya 3: Fizika, Astronomiya | no. №5_2023 | pp. 2350104–1-2350104–6.
Identifier and resource: [10.55959/msu0579-9392.78.2350104](https://doi.org/10.55959/msu0579-9392.78.2350104).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55959%2Fmsu0579-9392.78.2350104); retrieved 2026-10-08.

#### Q1393 Quantum Teleportation

Ahmed Banafa.
Book chapter | 2023 | Introduction to Quantum Computing | pp. 13-16.
Identifier and resource: [10.1201/9781003440239-4](https://doi.org/10.1201/9781003440239-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003440239-4); retrieved 2026-10-08.

#### Q1394 Quantum Teleportation

Reinhold A. Bertlmann, Nicolai Friis.
Book chapter | 2023 | Modern Quantum Theory | pp. 403-433.
Identifier and resource: [10.1093/oso/9780199683338.003.0014](https://doi.org/10.1093/oso/9780199683338.003.0014).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Foso%2F9780199683338.003.0014); retrieved 2026-10-08.

### D26T02 Quantum repeaters

Repeaters extend entanglement distribution beyond direct transmission limits. Rates depend on memories, losses, purification or coding, and coordination.

Fine subcategories: Heralding; purification; error corrected repeaters; rate loss tradeoffs.

Primary resources: 12. Additional related assignments can be found in the interactive HTML.

#### Q1395 Merging-based quantum repeater

Maria Flors Mor-Ruiz, Jorge Miguel-Ramiro, Julius Wallnöfer, Tim Coopmans, Wolfgang Dür.
Journal article | 2026 | npj Quantum Information.
Identifier and resource: [10.1038/s41534-026-01340-w](https://doi.org/10.1038/s41534-026-01340-w).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-026-01340-w); retrieved 2026-10-08.

#### Q1396 Quantum Repeater Protocol Using Quantum Error Correction for Distillation

Ashlesha Patil, Michele Pacenti, Bane Vasić, Saikat Guha, Narayanan Rengaswamy.
Journal article | 2026 | IEEE Internet Computing | vol. 30 | no. 1 | pp. 38-46.
Identifier and resource: [10.1109/mic.2026.3656561](https://doi.org/10.1109/mic.2026.3656561).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fmic.2026.3656561); retrieved 2026-10-08.

#### Q1397 Continuous-variable multiplexed quantum repeater networks

Pei-Zhe Li, William J Munro, Kae Nemoto, Nicolò Lo Piparo.
Journal article | 2025 | Quantum Science and Technology | vol. 10 | no. 2 | pp. 025057.
Identifier and resource: [10.1088/2058-9565/adc500](https://doi.org/10.1088/2058-9565/adc500).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fadc500); retrieved 2026-10-08.

#### Q1398 Finding the perfect quantum dot for a quantum repeater

Katie McDonnell, Sai Sreesh Venuturumilli, Bera Yavuz, Rubayet Al Maruf, Dan Dalacu, Philip J. Poole, Michael E. Reimer, Michal Bajcsy.
Conference paper | 2025 | Photonics for Quantum 2025 | pp. 15.
Identifier and resource: [10.1117/12.3063250](https://doi.org/10.1117/12.3063250).
Conference metadata: Photonics for Quantum 2025.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3063250); retrieved 2026-10-08.

#### Q1399 Generalized Quantum Repeater Graph States

Bikun Li, Kenneth Goodenough, Filip Rozpędek, Liang Jiang.
Journal article | 2025 | Physical Review Letters | vol. 134 | no. 19 | article 190801.
Identifier and resource: [10.1103/physrevlett.134.190801](https://doi.org/10.1103/physrevlett.134.190801).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.134.190801); retrieved 2026-10-08.

#### Q1400 Imbalanced Quantum Channels in Quantum Teleportation and Quantum Repeater Schemes

Lucas Vogeli, Phillip Cornett, Albert B. Dinkins V, Kwang-Cheng Chen.
Conference paper | 2025 | 2025 28th International Symposium on Wireless Personal Multimedia Communications (WPMC) | pp. 1-6.
Identifier and resource: [10.1109/wpmc67460.2025.11351266](https://doi.org/10.1109/wpmc67460.2025.11351266).
Conference metadata: 2025 28th International Symposium on Wireless Personal Multimedia Communications (WPMC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fwpmc67460.2025.11351266); retrieved 2026-10-08.

#### Q1401 Teleportation fidelity of quantum repeater networks

Ganesh Mylavarapu, Subrata Ghosh, Chittaranjan Hens, Indranil Chakrabarty, Subhadip Mitra.
Journal article | 2025 | Physical Review A | vol. 112 | no. 3 | article 032618.
Identifier and resource: [10.1103/72jp-37k6](https://doi.org/10.1103/72jp-37k6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F72jp-37k6); retrieved 2026-10-08.

#### Q1402 Towards a spectrally multiplexed quantum repeater

Tanmoy Chakraborty, Antariksha Das, Hedser van Brug, Oriol Pietx-Casas, Peng-Cheng Wang, Gustavo Castro do Amaral, Anna L. Tchebotareva, Wolfgang Tittel.
Journal article | 2025 | npj Quantum Information | vol. 11 | no. 1 | article 3.
Identifier and resource: [10.1038/s41534-024-00946-2](https://doi.org/10.1038/s41534-024-00946-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-024-00946-2); retrieved 2026-10-08.

#### Q1403 Asynchronous quantum repeater using multiple quantum memory

Chen-Long Li, Hua-Lei Yin, Zeng-Bing Chen.
Journal article | 2024 | Reports on Progress in Physics | vol. 87 | no. 12 | pp. 127901.
Identifier and resource: [10.1088/1361-6633/ad91de](https://doi.org/10.1088/1361-6633/ad91de).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1361-6633%2Fad91de); retrieved 2026-10-08.

#### Q1404 Towards a Practical Quantum Repeater

Mehdi Namazi.
Conference paper | 2024 | Frontiers in Optics + Laser Science 2024 (FiO, LS) | pp. FM5A.2.
Identifier and resource: [10.1364/ls.2024.fm5a.2](https://doi.org/10.1364/ls.2024.fm5a.2).
Conference metadata: Laser Science.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fls.2024.fm5a.2); retrieved 2026-10-08.

#### Q1405 Quantum Repeater Goes the Distance

Michal Hajdušek.
Journal article | 2023 | Physics | vol. 16 | article 84.
Identifier and resource: [10.1103/physics.16.84](https://doi.org/10.1103/physics.16.84).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysics.16.84); retrieved 2026-10-08.

#### Q1406 Scaling Limits of Quantum Repeater Networks

Mahdi Chehimi, Shahrooz Pouryousef, Nitish K. Panigrahy, Don Towsley, Walid Saad.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1205-1210.
Identifier and resource: [10.1109/qce57702.2023.00136](https://doi.org/10.1109/qce57702.2023.00136).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00136); retrieved 2026-10-08.

### D26T03 Entanglement distribution and routing

Entanglement routing allocates links and swapping operations to network tasks. Probabilistic success and memory decoherence require different metrics from ordinary packet routing.

Fine subcategories: Entanglement swapping; routing metrics; scheduling; multipath distribution.

Primary resources: 16. Additional related assignments can be found in the interactive HTML.

#### Q1407 Asynchronous Routing for Multipartite Entanglement in Quantum Networks

Chenliang Tian, Zebo Yang, Raj Jain, Ramana Kompella, Reza Nejabati, Eneet Kaur, Aiman Erbad, Mounir Hamdi et al..
Conference paper | 2026 | 2026 IEEE 16th Annual Computing and Communication Workshop and Conference (CCWC) | pp. 0533-0541.
Identifier and resource: [10.1109/ccwc67433.2026.11393739](https://doi.org/10.1109/ccwc67433.2026.11393739).
Conference metadata: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference (CCWC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fccwc67433.2026.11393739); retrieved 2026-10-08.

#### Q1408 Improved Routing of Multiparty Entanglement over Quantum Networks

Nirupam Basak, Goutam Paul.
Journal article | 2026 | ACM Transactions on Quantum Computing | vol. 7 | no. 3 | pp. 1-26.
Identifier and resource: [10.1145/3811537](https://doi.org/10.1145/3811537).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3811537); retrieved 2026-10-08.

#### Q1409 Maximize Quantum Network Throughput via EPS Placement and Lightweight Entanglement Routing

Yangming Zhao, Qiucheng Zhu, Bingyi Liu, Nai Xia, Chen Tian, Hongli Xu, Liusheng Huang, Kun Yang et al..
Journal article | 2026 | IEEE Transactions on Networking | vol. 34 | pp. 5349-5364.
Identifier and resource: [10.1109/ton.2026.3696466](https://doi.org/10.1109/ton.2026.3696466).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fton.2026.3696466); retrieved 2026-10-08.

#### Q1410 On Utility-Optimal Entanglement Routing in Quantum Networks

Sounak Kar, Arpan Mukhopadhyay.
Conference paper | 2026 | 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC) | pp. 457-464.
Identifier and resource: [10.1109/qcnc69040.2026.00082](https://doi.org/10.1109/qcnc69040.2026.00082).
Conference metadata: 2026 International Conference on Quantum Communications, Networking, and Computing (QCNC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqcnc69040.2026.00082); retrieved 2026-10-08.

#### Q1411 Optimal Multipartite Entanglement Routing Model in Quantum Networks

Yudai Ogata, Imran Ahmed, Eiji Oki.
Conference paper | 2026 | 2026 IEEE 27th International Conference on High Performance Switching and Routing (HPSR) | pp. 1-6.
Identifier and resource: [10.1109/hpsr68369.2026.11615194](https://doi.org/10.1109/hpsr68369.2026.11615194).
Conference metadata: 2026 IEEE 27th International Conference on High Performance Switching and Routing (HPSR).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fhpsr68369.2026.11615194); retrieved 2026-10-08.

#### Q1412 Resource estimation for entanglement routing in quantum networks

Manik Dawar, Ralf Riedinger, Nilesh Vyas, Paulo Mendes.
Journal article | 2026 | Physical Review A | vol. 113 | no. 2 | article 022622.
Identifier and resource: [10.1103/vf4x-rjsd](https://doi.org/10.1103/vf4x-rjsd).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fvf4x-rjsd); retrieved 2026-10-08.

#### Q1413 Routing entanglement through quantum networks

Karl Pelka, Matteo Aquilina, André Xuereb.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 2 | article L022062.
Identifier and resource: [10.1103/hsc8-pv2s](https://doi.org/10.1103/hsc8-pv2s).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fhsc8-pv2s); retrieved 2026-10-08.

#### Q1414 Differentiated service entanglement routing for quantum networks

Hui Han, Bo Liu, Bang-Ying Tang, Si-Yu Xiong, Jin-Quan Huang, Wan-Rong Yu, Shu-Hui Chen.
Journal article | 2025 | Quantum Science and Technology | vol. 10 | no. 3 | pp. 035013.
Identifier and resource: [10.1088/2058-9565/adc82b](https://doi.org/10.1088/2058-9565/adc82b).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fadc82b); retrieved 2026-10-08.

#### Q1415 DyQNet: Optimizing Dynamic Entanglement Routing with Online Request in Quantum Network

Tianyao Chu, Liqiang Lu, Shiyu Li, Xinghui Jia, Chenren Xu, Siwei Tan, Jianwei Yin.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 186-200.
Identifier and resource: [10.1007/978-981-95-1021-4_14](https://doi.org/10.1007/978-981-95-1021-4_14).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-95-1021-4_14); retrieved 2026-10-08.

#### Q1416 Entanglement Routing in Quantum Networks: A Comprehensive Survey

Amar Abane, Michael Cubeddu, Van Sy Mai, Abdella Battou.
Journal article | 2025 | IEEE Transactions on Quantum Engineering | vol. 6 | pp. 1-39.
Identifier and resource: [10.1109/tqe.2025.3541123](https://doi.org/10.1109/tqe.2025.3541123).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftqe.2025.3541123); retrieved 2026-10-08.

#### Q1417 Entanglement-Reusable Dynamic Routing for Quantum Networks

Junwei Wu, Songshi Dou, Kwan L. Yeung.
Conference paper | 2025 | 2025 IEEE International Conference on Consumer Electronics (ICCE) | pp. 1-4.
Identifier and resource: [10.1109/icce63647.2025.10929901](https://doi.org/10.1109/icce63647.2025.10929901).
Conference metadata: 2025 IEEE International Conference on Consumer Electronics (ICCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficce63647.2025.10929901); retrieved 2026-10-08.

#### Q1418 Optimizing qubit transfer in multi-host quantum network using security-oriented entanglement routing algorithm

Saumya Priyadarshini, Chandrashekar Jatoth, Rajesh Doriya, Rajkumar Buyya.
Journal article | 2025 | Optics Communications | vol. 596 | pp. 132549 | article 132549.
Identifier and resource: [10.1016/j.optcom.2025.132549](https://doi.org/10.1016/j.optcom.2025.132549).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.optcom.2025.132549); retrieved 2026-10-08.

#### Q1419 Entanglement Routing Design Over Quantum Networks

Yiming Zeng, Jiarui Zhang, Ji Liu, Zhenhua Liu, Yuanyuan Yang.
Journal article | 2024 | IEEE/ACM Transactions on Networking | vol. 32 | no. 1 | pp. 352-367.
Identifier and resource: [10.1109/tnet.2023.3282560](https://doi.org/10.1109/tnet.2023.3282560).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ftnet.2023.3282560); retrieved 2026-10-08.

#### Q1420 High-fidelity entanglement routing in quantum networks

HaoRan Hu, HuaZhi Lun, ZhiFeng Deng, Jie Tang, JiaHao Li, YueXiang Cao, Ya Wang, Ying Liu et al..
Journal article | 2024 | Results in Physics | vol. 60 | pp. 107682 | article 107682.
Identifier and resource: [10.1016/j.rinp.2024.107682](https://doi.org/10.1016/j.rinp.2024.107682).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.rinp.2024.107682); retrieved 2026-10-08.

#### Q1421 Quantum Error Correction Based Entanglement Routing in Socially-Aware Quantum Networks

Shao-Min Huang, Ming-Huang Chien, Ting-Yuan Wen, Qian-Jing Wang, Jian-Jhih Kuo.
Conference paper | 2024 | GLOBECOM 2024 - 2024 IEEE Global Communications Conference | pp. 4503-4508.
Identifier and resource: [10.1109/globecom52923.2024.10901515](https://doi.org/10.1109/globecom52923.2024.10901515).
Conference metadata: GLOBECOM 2024 - 2024 IEEE Global Communications Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fglobecom52923.2024.10901515); retrieved 2026-10-08.

#### Q1422 qRL: Reinforcement Learning Routing for Quantum Entanglement Networks

Diego Abreu, Antonio Abelém.
Conference paper | 2024 | 2024 IEEE Symposium on Computers and Communications (ISCC) | pp. 1-6.
Identifier and resource: [10.1109/iscc61673.2024.10733623](https://doi.org/10.1109/iscc61673.2024.10733623).
Conference metadata: 2024 IEEE Symposium on Computers and Communications (ISCC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fiscc61673.2024.10733623); retrieved 2026-10-08.

### D26T04 Quantum internet protocols

Quantum network protocols coordinate physical links, entanglement, and applications. Layer interfaces must represent limited and consumable quantum resources.

Fine subcategories: Link layers; network stacks; resource management; control planes; application interfaces.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1423 Efficient and Quantum-Safe Internet Key Exchange Protocols for Satellite Communications

Davide De Zuane, Marco Baldi, Paolo Santini, Grégoire Anchelergues, Daniele Romano.
Conference paper | 2026 | 2026 IEEE 32nd International Symposium on Local and Metropolitan Area Networks (LANMAN) | pp. 1-6.
Identifier and resource: [10.1109/lanman69841.2026.11623493](https://doi.org/10.1109/lanman69841.2026.11623493).
Conference metadata: 2026 IEEE 32nd International Symposium on Local and Metropolitan Area Networks (LANMAN).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Flanman69841.2026.11623493); retrieved 2026-10-08.

#### Q1424 Quantum Internet: Technologies, Protocols, and Research Challenges

Vinay Kumar, Claudio Cicconetti, Marco Conti, Andrea Passarella.
Journal article | 2025 | International Journal of Networked and Distributed Computing | vol. 13 | no. 2 | article 22.
Identifier and resource: [10.1007/s44227-025-00060-5](https://doi.org/10.1007/s44227-025-00060-5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs44227-025-00060-5); retrieved 2026-10-08.

#### Q1425 A Survey of Quantum Internet Protocols From a Layered Perspective

Yuan Li, Hao Zhang, Chen Zhang, Tao Huang, F. Richard Yu.
Journal article | 2024 | IEEE Communications Surveys & Tutorials | vol. 26 | no. 3 | pp. 1606-1634.
Identifier and resource: [10.1109/comst.2024.3361662](https://doi.org/10.1109/comst.2024.3361662).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fcomst.2024.3361662); retrieved 2026-10-08.

#### Q1426 Guest Editorial The Quantum Internet: Principles, Protocols and Architectures

Angela Sara Cacciapuoti, Anne Broadbent, Eleni Diamanti, Jacquiline Romero, Stephanie Wehner.
Journal article | 2024 | IEEE Journal on Selected Areas in Communications | vol. 42 | no. 7 | pp. 1719-1722.
Identifier and resource: [10.1109/jsac.2024.3379106](https://doi.org/10.1109/jsac.2024.3379106).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjsac.2024.3379106); retrieved 2026-10-08.

#### Q1427 Quantum Internet: Functionalities, Protocols and Applications

Eftekar Abdulaziz, Khalid Al-Hussaini, Fua’Ad Abdulrazzak.
Conference paper | 2024 | 2024 1st International Conference on Emerging Technologies for Dependable Internet of Things (ICETI) | pp. 1-6.
Identifier and resource: [10.1109/iceti63946.2024.10777267](https://doi.org/10.1109/iceti63946.2024.10777267).
Conference metadata: 2024 1st International Conference on Emerging Technologies for Dependable Internet of Things (ICETI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficeti63946.2024.10777267); retrieved 2026-10-08.

#### Q1428 Secure and Efficient Entanglement Distribution Protocols for Near-Term Quantum Internet

Nicholas Skjellum, Mohamed Shaban, Muhammad Ismail.
Conference paper | 2024 | 2024 33rd International Conference on Computer Communications and Networks (ICCCN) | pp. 1-9.
Identifier and resource: [10.1109/icccn61486.2024.10637640](https://doi.org/10.1109/icccn61486.2024.10637640).
Conference metadata: 2024 33rd International Conference on Computer Communications and Networks (ICCCN).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficccn61486.2024.10637640); retrieved 2026-10-08.

#### Q1429 Towards Secure and Efficient Practical Consensus Protocols in Quantum Internet

Woonghee Lee, Donghee Kim, Junbeom Hur.
Conference paper | 2024 | 2024 15th International Conference on Information and Communication Technology Convergence (ICTC) | pp. 759-761.
Identifier and resource: [10.1109/ictc62082.2024.10826676](https://doi.org/10.1109/ictc62082.2024.10826676).
Conference metadata: 2024 15th International Conference on Information and Communication Technology Convergence (ICTC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fictc62082.2024.10826676); retrieved 2026-10-08.

#### Q1430 Use of hybrid post-quantum key exchange in internet protocols

Valery Smyslov.
Journal article | 2024 | Journal of Computer Virology and Hacking Techniques | vol. 20 | no. 3 | pp. 447-454.
Identifier and resource: [10.1007/s11416-024-00515-3](https://doi.org/10.1007/s11416-024-00515-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11416-024-00515-3); retrieved 2026-10-08.

### D26T05 Quantum communication capacity

Channel capacities quantify asymptotic communication rates under specified assistance. Classical, quantum, and private capacities answer different coding questions.

Fine subcategories: Classical capacity; quantum capacity; private capacity; coding theorems.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1431 Channel capacity of relativistic quantum communication with rapid interaction

Erickson Tjoa, Kensuke Gallock-Yoshimura.
Journal article | 2022 | Physical Review D | vol. 105 | no. 8 | article 085011.
Identifier and resource: [10.1103/physrevd.105.085011](https://doi.org/10.1103/physrevd.105.085011).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevd.105.085011); retrieved 2026-10-08.

#### Q1432 Drastic increase of channel capacity in quantum secure direct communication using masking

Gui-Lu Long, Haoran Zhang.
Journal article | 2021 | Science Bulletin | vol. 66 | no. 13 | pp. 1267-1269.
Identifier and resource: [10.1016/j.scib.2021.04.016](https://doi.org/10.1016/j.scib.2021.04.016).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.scib.2021.04.016); retrieved 2026-10-08.

#### Q1433 Quantum-channel capacity of distributing orbital-angular-momentum states for underwater optical quantum communication

Shuang Zhai, Jicheng Wang, Yun Zhu, Yixin Zhang, Zheng-Da Hu.
Journal article | 2020 | Journal of the Optical Society of America A | vol. 38 | no. 1 | pp. 36.
Identifier and resource: [10.1364/josaa.402794](https://doi.org/10.1364/josaa.402794).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fjosaa.402794); retrieved 2026-10-08.

#### Q1434 Classical communication with quantum receivers: towards violating classical Shannon channel capacity (Conference Presentation)

Ivan Burenkov, Sergey V. Polyakov.
Conference paper | 2019 | Advances in Photonics of Quantum Computing, Memory, and Communication XII | pp. 17.
Identifier and resource: [10.1117/12.2510091](https://doi.org/10.1117/12.2510091).
Conference metadata: Advances in Photonics of Quantum Computing, Memory, and Communication XII.
Fine tags: Classical capacity; quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2510091); retrieved 2026-10-08.

#### Q1435 Cluster state based controlled quantum secure direct communication protocol with controllable channel capacity

Zheng Xiao-Yi, Long Yin-Xiang, Automation Engineering Department, Guangdong Technical College of Water Resource and Electric Engineering, Guangzhou 510635, China.
Journal article | 2017 | Acta Physica Sinica | vol. 66 | no. 18 | pp. 180303.
Identifier and resource: [10.7498/aps.66.180303](https://doi.org/10.7498/aps.66.180303).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.66.180303); retrieved 2026-10-08.

#### Q1436 Capacity of Quantum Erasure Channel Assisted by Backwards Classical Communication

Debbie Leung, Joungkeun Lim, Peter Shor.
Journal article | 2009 | Physical Review Letters | vol. 103 | no. 24 | article 240505.
Identifier and resource: [10.1103/physrevlett.103.240505](https://doi.org/10.1103/physrevlett.103.240505).
Fine tags: Classical capacity; quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.103.240505); retrieved 2026-10-08.

#### Q1437 Quantum Communication with Zero-Capacity Channels

Graeme Smith, Jon Yard.
Journal article | 2008 | Science | vol. 321 | no. 5897 | pp. 1812-1815.
Identifier and resource: [10.1126/science.1162242](https://doi.org/10.1126/science.1162242).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fscience.1162242); retrieved 2026-10-08.

#### Q1438 Information capacity of a quantum communication channel. II.

R. L. Stratonovich.
Journal article | 1966 | Soviet Radiophysics | vol. 8 | no. 1 | pp. 92-101.
Identifier and resource: [10.1007/bf01038471](https://doi.org/10.1007/bf01038471).
Fine tags: quantum capacity.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fbf01038471); retrieved 2026-10-08.

## D27 Quantum cryptography and security

Quantum cryptography uses quantum systems for security tasks, while post quantum cryptography uses classical algorithms designed to resist quantum attacks. Their mechanisms and deployment requirements are different.

Prerequisites: Cryptographic definitions, probability, and quantum algorithms.

Assessment focus: Threat model, composable security, finite size effects, and implementation attacks.

Primary catalog resources in this category: 61.

### D27T01 Quantum key distribution

QKD establishes secret keys under a stated device and security model. Finite size analysis, authentication, and side channels are part of practical security.

Fine subcategories: BB84; decoy states; finite keys; composable security; implementation attacks.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1439 Quantum cryptography

Nicolas Gisin, Grégoire Ribordy, Wolfgang Tittel, Hugo Zbinden.
Journal article | 2002 | Reviews of Modern Physics | vol. 74 | no. 1 | pp. 145-195.
Identifier and resource: [10.1103/revmodphys.74.145](https://doi.org/10.1103/revmodphys.74.145).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FRevModPhys.74.145); retrieved 2026-10-08.

#### Q1440 Quantum Key Distribution

R. Naveenkumar, N. M. Sivamangai, C. M. Lingesh, G. Saranya, G. Indhumathi, N. Vini Antony Grace.
Book chapter | 2026 | Quantum Computing | pp. 207-234.
Identifier and resource: [10.1201/9781003587835-10](https://doi.org/10.1201/9781003587835-10).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003587835-10); retrieved 2026-10-08.

#### Q1441 Quantum key distribution

Ivan B. Djordjevic.
Book chapter | 2026 | Quantum Communication, Quantum Networks, and Quantum Sensing | pp. 257-304.
Identifier and resource: [10.1016/b978-0-443-40568-6.00001-x](https://doi.org/10.1016/b978-0-443-40568-6.00001-x).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-443-40568-6.00001-x); retrieved 2026-10-08.

#### Q1442 Quantum Key Distribution

Ray LaPierre.
Book chapter | 2025 | The Materials Research Society Series | pp. 97-105.
Identifier and resource: [10.1007/978-3-031-90731-9_6](https://doi.org/10.1007/978-3-031-90731-9_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-90731-9_6); retrieved 2026-10-08.

#### Q1443 Quantum Key Distribution

Ri-Gui Zhou, Xiao-Xue Zhang, Lin-Tao Du.
Book chapter | 2024 | Design and Analysis of Secure Quantum Communication Schemes | pp. 35-46.
Identifier and resource: [10.1007/978-3-031-78428-6_3](https://doi.org/10.1007/978-3-031-78428-6_3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-78428-6_3); retrieved 2026-10-08.

#### Q1444 Quantum Key Distribution

Jasper Rödiger.
Book chapter | 2023 | Trends in Data Protection and Encryption Technologies | pp. 41-45.
Identifier and resource: [10.1007/978-3-031-33386-6_9](https://doi.org/10.1007/978-3-031-33386-6_9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-33386-6_9); retrieved 2026-10-08.

#### Q1445 Quantum Key Distribution

Filip Wojcieszyn.
Book chapter | 2022 | Quantum Science and Technology | pp. 181-211.
Identifier and resource: [10.1007/978-3-030-99379-5_6](https://doi.org/10.1007/978-3-030-99379-5_6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-99379-5_6); retrieved 2026-10-08.

#### Q1446 Quantum key distribution

Ivan B. Djordjevic.
Book chapter | 2022 | Quantum Communication, Quantum Networks, and Quantum Sensing | pp. 215-272.
Identifier and resource: [10.1016/b978-0-12-822942-2.00012-1](https://doi.org/10.1016/b978-0-12-822942-2.00012-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fb978-0-12-822942-2.00012-1); retrieved 2026-10-08.

### D27T02 Device independent cryptography

Device independent protocols infer security from observed nonlocal correlations. Loophole closure, randomness, and finite statistics are demanding requirements.

Fine subcategories: Bell violations; loophole closure; entropy accumulation; security assumptions.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1447 Partially device-independent quantum cryptography in asymmetric networks

Jun-Hao Wei, Shu-Ming Hu, Nuo-Ya Yang, Shuai Zhao, Li Li, Nai-Le Liu, Kai Chen.
Journal article | 2026 | Physical Review Research | vol. 8 | no. 3 | article 033060.
Identifier and resource: [10.1103/53w8-6v5z](https://doi.org/10.1103/53w8-6v5z).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F53w8-6v5z); retrieved 2026-10-08.

#### Q1448 A Direct Product Theorem for Quantum Communication Complexity with Applications to Device-Independent Cryptography

Rahul Jain, Srijita Kundu.
Journal article | 2025 | SIAM Journal on Computing | vol. 54 | no. 4 | pp. 964-1020.
Identifier and resource: [10.1137/23m1549353](https://doi.org/10.1137/23m1549353).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1137%2F23m1549353); retrieved 2026-10-08.

#### Q1449 Seedless extractors for device-independent quantum cryptography

Cameron Foreman, Lluis Masanes.
Journal article | 2025 | Quantum | vol. 9 | pp. 1654 | article 1654.
Identifier and resource: [10.22331/q-2025-03-06-1654](https://doi.org/10.22331/q-2025-03-06-1654).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2025-03-06-1654); retrieved 2026-10-08.

#### Q1450 Boosting device-independent cryptography with tripartite nonlocality

Federico Grasselli, Gláucia Murta, Hermann Kampermann, Dagmar Bruß.
Journal article | 2023 | Quantum | vol. 7 | pp. 980 | article 980.
Identifier and resource: [10.22331/q-2023-04-13-980](https://doi.org/10.22331/q-2023-04-13-980).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2023-04-13-980); retrieved 2026-10-08.

#### Q1451 Autocompensating Measurement-Device-Independent Quantum Cryptography in Space Division Multiplexing Optical Fibers

Jesús Liñares, Gabriel M. Carral, Xesús Prieto-Blanco, Daniel Balado.
Posted content | 2021 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-141385/v1](https://doi.org/10.21203/rs.3.rs-141385/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-141385%2Fv1); retrieved 2026-10-08.

#### Q1452 Autocompensating measurement-device-independent quantum cryptography in space division multiplexing optical fibers

J. Liñares, G. M. Carral, X. Prieto-Blanco, D. Balado.
Journal article | 2021 | Journal of the European Optical Society-Rapid Publications | vol. 17 | no. 1 | article 19.
Identifier and resource: [10.1186/s41476-021-00166-7](https://doi.org/10.1186/s41476-021-00166-7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1186%2Fs41476-021-00166-7); retrieved 2026-10-08.

#### Q1453 Device-Independent Quantum Cryptography

Federico Grasselli.
Book chapter | 2021 | Quantum Science and Technology | pp. 105-148.
Identifier and resource: [10.1007/978-3-030-64360-7_7](https://doi.org/10.1007/978-3-030-64360-7_7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-030-64360-7_7); retrieved 2026-10-08.

#### Q1454 Autocompensating Measurement-Device-Independent quantum cryptography in few-mode optical fibers

Jesús Liñares-Beiras, Xesús Prieto-Blanco, Daniel Balado, Gabriel M. Carral.
Journal article | 2020 | EPJ Web of Conferences | vol. 238 | pp. 09002.
Identifier and resource: [10.1051/epjconf/202023809002](https://doi.org/10.1051/epjconf/202023809002).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1051%2Fepjconf%2F202023809002); retrieved 2026-10-08.

### D27T03 Blind and delegated computing

Blind computing hides some information about a delegated task, while verifiable protocols also test correctness. Client capability and server trust distinguish protocols.

Fine subcategories: Hidden circuits; verifiable delegation; trap protocols; server trust.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1455 Blind quantum computing with different qudit resource state architectures

Alena Romanova, Wolfgang Dür.
Journal article | 2026 | Physical Review A | vol. 113 | no. 3 | article 032606.
Identifier and resource: [10.1103/1p5p-zywx](https://doi.org/10.1103/1p5p-zywx).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2F1p5p-zywx); retrieved 2026-10-08.

#### Q1456 Practical blind quantum computation with parity quantum computing framework

Yuxun Wang, Qin Li, Shao-Ming Fei, Vlatko Vedral.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 2 | pp. 025033.
Identifier and resource: [10.1088/2058-9565/ae54c5](https://doi.org/10.1088/2058-9565/ae54c5).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae54c5); retrieved 2026-10-08.

#### Q1457 Secure Multi-Party Computation Based on Blind Quantum Computing

Yongli Wang, Tianci Cao, Yixin Wang, Rui Zhang, Yinghui Yang, Yongli Tang.
Posted content | 2026 | Springer Science and Business Media LLC.
Identifier and resource: [10.21203/rs.3.rs-9186808/v1](https://doi.org/10.21203/rs.3.rs-9186808/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-9186808%2Fv1); retrieved 2026-10-08.

#### Q1458 Blind quantum computation with fewer quantum and delegated cost of client

Yu-Zhan Yan, Zhen Yang, Guang-Yang Wu, Yuan-Mao Luo, Ming-Qiang Bai, Zhi-Wen Mo.
Journal article | 2025 | International Journal of Quantum Information | vol. 23 | no. 02 | article 2530001.
Identifier and resource: [10.1142/s0219749925300013](https://doi.org/10.1142/s0219749925300013).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1142%2Fs0219749925300013); retrieved 2026-10-08.

#### Q1459 Universal blind quantum computing assisted by quantum teleportation

Xiaoqian Zhang.
Journal article | 2025 | Quantum Information Processing | vol. 24 | no. 6 | article 182.
Identifier and resource: [10.1007/s11128-025-04798-3](https://doi.org/10.1007/s11128-025-04798-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-025-04798-3); retrieved 2026-10-08.

#### Q1460 Universal distributed blind quantum computing with solid-state qubits

Y.-C. Wei, P.-J. Stas, A. Suleymanzade, G. Baranes, F. Machado, Y. Q. Huan, C. M. Knaut, S. W. Ding et al..
Journal article | 2025 | Science | vol. 388 | no. 6746 | pp. 509-513.
Identifier and resource: [10.1126/science.adu6894](https://doi.org/10.1126/science.adu6894).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fscience.adu6894); retrieved 2026-10-08.

#### Q1461 Private Set Intersection with Delegated Blind Quantum Computing

Michele Amoretti.
Conference paper | 2021 | 2021 IEEE Global Communications Conference (GLOBECOM) | pp. 1-6.
Identifier and resource: [10.1109/globecom46510.2021.9685125](https://doi.org/10.1109/globecom46510.2021.9685125).
Conference metadata: GLOBECOM 2021 - 2021 IEEE Global Communications Conference.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fglobecom46510.2021.9685125); retrieved 2026-10-08.

#### Q1462 Delegated Preparation of Quantum Error Correction Code for Blind Quantum Computation

Qiang Zhao, Qiong Li.
Book chapter | 2019 | Smart Innovation, Systems and Technologies | pp. 147-154.
Identifier and resource: [10.1007/978-981-13-9710-3_15](https://doi.org/10.1007/978-981-13-9710-3_15).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-981-13-9710-3_15); retrieved 2026-10-08.

### D27T04 Quantum cryptanalysis

Quantum cryptanalysis studies attacks on classical or quantum security systems. Algorithmic complexity and physical fault tolerant cost should both be considered.

Fine subcategories: Factoring attacks; discrete logarithms; Grover search; resource estimates.

Primary resources: 14. Additional related assignments can be found in the interactive HTML.

#### Q1463 Cryptanalysis of Post-Quantum Cryptographic Schemes

Veda Chatiyode, Baghavathi Priya S..
Book chapter | 2025 | Post-Quantum Cryptography and IoT Communications for Sustainable Urban Development | pp. 171-204.
Identifier and resource: [10.4018/979-8-3373-3166-9.ch007](https://doi.org/10.4018/979-8-3373-3166-9.ch007).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4018%2F979-8-3373-3166-9.ch007); retrieved 2026-10-08.

#### Q1464 Quantum Cryptanalysis: Breaking Classical Encryption with Shor's and Grover's Algorithms

Godwin Olaoye.
Posted content | 2025 | Wiley.
Identifier and resource: [10.22541/au.174431280.02434905/v1](https://doi.org/10.22541/au.174431280.02434905/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22541%2Fau.174431280.02434905%2Fv1); retrieved 2026-10-08.

#### Q1465 Quantum Cryptanalysis: Evaluating the Impact of Shor’s and Grover’s Algorithms on Modern Encryption Standards

Mithal Hadi Jebur, Sumar Khaleel.
Journal article | 2025 | CyberSystem Journal | vol. 2 | no. 2 | pp. 41-55.
Identifier and resource: [10.57238/csj.2025.1012](https://doi.org/10.57238/csj.2025.1012).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.57238%2Fcsj.2025.1012); retrieved 2026-10-08.

#### Q1466 Scalable, Fault-Tolerant Quantum Algorithms for Cryptanalysis-Resistant Communications

Ankith Konda.
Conference paper | 2025 | 2025 13th International Conference on Intelligent Systems and Embedded Design (ISED) | pp. 936-943.
Identifier and resource: [10.1109/ised67359.2025.11405294](https://doi.org/10.1109/ised67359.2025.11405294).
Conference metadata: 2025 13th International Conference on Intelligent Systems and Embedded Design (ISED).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fised67359.2025.11405294); retrieved 2026-10-08.

#### Q1467 Lattice-Based Cryptosystems and Quantum Cryptanalysis

Bruce Schneier.
Journal article | 2024 | Communications of the ACM | article 3665224.
Identifier and resource: [10.1145/3665224](https://doi.org/10.1145/3665224).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3665224); retrieved 2026-10-08.

#### Q1468 Quantum Cryptanalysis of Affine Cipher

Mahima Mary Mathews, Panchami V, Vishnu Ajith.
Journal article | 2024 | IEEE Journal on Emerging and Selected Topics in Circuits and Systems | vol. 14 | no. 3 | pp. 507-519.
Identifier and resource: [10.1109/jetcas.2024.3428436](https://doi.org/10.1109/jetcas.2024.3428436).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fjetcas.2024.3428436); retrieved 2026-10-08.

#### Q1469 Quantum cryptanalysis

Author metadata not supplied.
Book chapter | 2024 | Mathematical Surveys and Monographs | pp. 53-62.
Identifier and resource: [10.1090/surv/278/06](https://doi.org/10.1090/surv/278/06).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1090%2Fsurv%2F278%2F06); retrieved 2026-10-08.

#### Q1470 Quantum related-key differential cryptanalysis

Hongyu Wu, Xiaoning Feng.
Journal article | 2024 | Quantum Information Processing | vol. 23 | no. 7 | article 269.
Identifier and resource: [10.1007/s11128-024-04472-0](https://doi.org/10.1007/s11128-024-04472-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-024-04472-0); retrieved 2026-10-08.

#### Q1471 The problem of finding periodicity in quantum cryptanalysis of group cryptography algorithms

Y. Kotukh, G. Khalimov, I. Dzhura.
Journal article | 2024 | Radiotekhnika | no. 218 | pp. 103-109.
Identifier and resource: [10.30837/rt.2024.3.218.08](https://doi.org/10.30837/rt.2024.3.218.08).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.30837%2Frt.2024.3.218.08); retrieved 2026-10-08.

#### Q1472 Applied Quantum Cryptanalysis

Alexei Petrenko.
Book | 2023 | River Publishers.
Identifier and resource: [10.1201/9781003392873](https://doi.org/10.1201/9781003392873).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003392873); retrieved 2026-10-08.

#### Q1473 Basic Algorithms Quantum Cryptanalysis

Saint Petersburg Electrotechnical University LETI, Alexei Petrenko, Sergei Petrenko, Saint Petersburg Electrotechnical University LETI.
Journal article | 2023 | Voprosy kiberbezopasnosti | no. 1(53) | pp. 100-115.
Identifier and resource: [10.21681/2311-3456-2023-1-100-115](https://doi.org/10.21681/2311-3456-2023-1-100-115).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21681%2F2311-3456-2023-1-100-115); retrieved 2026-10-08.

#### Q1474 Cryptanalysis of three quantum money schemes

Andriyan Bilyk, Javad Doliskani, Zhiyong Gong.
Journal article | 2023 | Quantum Information Processing | vol. 22 | no. 4 | article 177.
Identifier and resource: [10.1007/s11128-023-03919-0](https://doi.org/10.1007/s11128-023-03919-0).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-023-03919-0); retrieved 2026-10-08.

#### Q1475 Development of Quantum Cryptanalysis Algorithms

Alexei Petrenko, Sergei Petrenko.
Book chapter | 2023 | Applied Quantum Cryptanalysis | pp. 97-128.
Identifier and resource: [10.1201/9781003392873-4](https://doi.org/10.1201/9781003392873-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003392873-4); retrieved 2026-10-08.

#### Q1476 The Relevance of Quantum Cryptanalysis

Alexei Petrenko, Sergei Petrenko.
Book chapter | 2023 | Applied Quantum Cryptanalysis | pp. 7-65.
Identifier and resource: [10.1201/9781003392873-2](https://doi.org/10.1201/9781003392873-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003392873-2); retrieved 2026-10-08.

### D27T05 Post quantum cryptography interface

Post quantum cryptography uses classical schemes intended to resist quantum attacks. It is included as a security interface to quantum computing, not as a quantum hardware protocol.

Fine subcategories: Lattice schemes; code based schemes; hash signatures; migration; threat models.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1477 Post-Quantum Cryptography

Author metadata not supplied.
Book | 2026 | Lecture Notes in Computer Science.
Identifier and resource: [10.1007/978-3-032-22698-3](https://doi.org/10.1007/978-3-032-22698-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-22698-3); retrieved 2026-10-08.

#### Q1478 Post-Quantum Cryptography: can Classical Algorithms Resist Quantum Attacks

Dinh Doan Xuan Phuong, Pham Truong Son.
Conference paper | 2025 | 2025 RIVF International Conference on Computing and Communication Technologies (RIVF) | pp. 717-722.
Identifier and resource: [10.1109/rivf68649.2025.11365084](https://doi.org/10.1109/rivf68649.2025.11365084).
Conference metadata: 2025 RIVF International Conference on Computing and Communication Technologies (RIVF).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Frivf68649.2025.11365084); retrieved 2026-10-08.

#### Q1479 Cryptographic Protocols Resilient to Quantum Attacks: Advancements in Post-Quantum Cryptography

Pallavi Niraj Vithalkar.
Journal article | 2024 | Communications on Applied Nonlinear Analysis | vol. 31 | no. 3s | pp. 520-532.
Identifier and resource: [10.52783/cana.v31.805](https://doi.org/10.52783/cana.v31.805).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.52783%2Fcana.v31.805); retrieved 2026-10-08.

#### Q1480 FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard | CSRC

Author metadata not supplied.
Standard | 2024 | NIST.
Identifier and resource: [Official resource](https://csrc.nist.gov/pubs/fips/203/final).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://csrc.nist.gov/pubs/fips/203/final); retrieved 2026-10-08.

#### Q1481 FIPS 204, Module-Lattice-Based Digital Signature Standard | CSRC

Author metadata not supplied.
Standard | 2024 | NIST.
Identifier and resource: [Official resource](https://csrc.nist.gov/pubs/fips/204/final).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://csrc.nist.gov/pubs/fips/204/final); retrieved 2026-10-08.

#### Q1482 FIPS 205, Stateless Hash-Based Digital Signature Standard | CSRC

Author metadata not supplied.
Standard | 2024 | NIST.
Identifier and resource: [Official resource](https://csrc.nist.gov/pubs/fips/205/final).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://csrc.nist.gov/pubs/fips/205/final); retrieved 2026-10-08.

#### Q1483 Post-Quantum Cryptography: Securing Future Communication Networks Against Quantum Attacks

Dr. N Krishnamoorthy, Dr. S. Subbaiah, J Revathi.
Journal article | 2024 | Nanotechnology Perceptions | pp. 264-278.
Identifier and resource: [10.62441/nano-ntp.vi.2774](https://doi.org/10.62441/nano-ntp.vi.2774).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62441%2Fnano-ntp.vi.2774); retrieved 2026-10-08.

#### Q1484 Post-Quantum Cryptography: Securing Future Communication Networks Against Quantum Attacks

Author metadata not supplied.
Journal article | 2024 | Nanotechnology Perceptions | vol. 20 | no. S14.
Identifier and resource: [10.62441/nano-ntp.v20is14.16](https://doi.org/10.62441/nano-ntp.v20is14.16).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.62441%2Fnano-ntp.v20is14.16); retrieved 2026-10-08.

### D27T06 Quantum random number generation

Quantum random number generators estimate and extract entropy from measured quantum processes. Security depends on the source model and the amount of trusted hardware.

Fine subcategories: Entropy sources; extractors; certification; device trust; finite size analysis.

Primary resources: 15. Additional related assignments can be found in the interactive HTML.

#### Q1485 Interferometric Quantum Random Number Generation via Michelson Configuration

Ram Soorat, Aakash Chilakamarri, Priyanka, Barath Sai Kumar Jakkuva, Syed Areebuddin.
Journal article | 2026 | International Journal of Theoretical Physics | vol. 65 | no. 6 | article 169.
Identifier and resource: [10.1007/s10773-026-06369-3](https://doi.org/10.1007/s10773-026-06369-3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs10773-026-06369-3); retrieved 2026-10-08.

#### Q1486 Quantum random number generation using spatial quantum noise of light

Mohamed Armoon Shaliq, Ashok Kumar.
Journal article | 2026 | Applied Physics Letters | vol. 129 | no. 7 | article 074002.
Identifier and resource: [10.1063/5.0342762](https://doi.org/10.1063/5.0342762).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0342762); retrieved 2026-10-08.

#### Q1487 Certified random number generation using quantum computers

Pingal Pratyush Nath, Aninda Sinha, Urbasi Sinha.
Journal article | 2025 | Frontiers in Quantum Science and Technology | vol. 4 | article 1661544.
Identifier and resource: [10.3389/frqst.2025.1661544](https://doi.org/10.3389/frqst.2025.1661544).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffrqst.2025.1661544); retrieved 2026-10-08.

#### Q1488 Quantum Random Number Generation and ML-Based Authentication

Liviu Ionut Epure.
Posted content | 2025 | Wiley.
Identifier and resource: [10.22541/au.176281462.20133004/v1](https://doi.org/10.22541/au.176281462.20133004/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22541%2Fau.176281462.20133004%2Fv1); retrieved 2026-10-08.

#### Q1489 Quantum Random Number Generation via Von Neumann Projection

Nawres A. Alwan, Suzan J. Obaiys, Nadia M. G. Al-Saidi, Nurul Fazmidar Binti Mohd Noor.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 176-193.
Identifier and resource: [10.1007/978-3-031-97000-9_11](https://doi.org/10.1007/978-3-031-97000-9_11).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-97000-9_11); retrieved 2026-10-08.

#### Q1490 Exploring quantum systems for pseudo-random number generation

Luis José Mantilla Santa Cruz, Luis Fernando Faina, João Henrique de Souza Pereira.
Journal article | 2024 | Quantum Studies: Mathematics and Foundations | vol. 12 | no. 1 | article 3.
Identifier and resource: [10.1007/s40509-024-00348-1](https://doi.org/10.1007/s40509-024-00348-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs40509-024-00348-1); retrieved 2026-10-08.

#### Q1491 Investigating device-independent quantum random number generation

Vardaan Mongia, Abhishek Kumar, Shashi Prabhakar, Anindya Banerji, R.P. Singh.
Journal article | 2024 | Physics Letters A | vol. 526 | pp. 129954 | article 129954.
Identifier and resource: [10.1016/j.physleta.2024.129954](https://doi.org/10.1016/j.physleta.2024.129954).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.physleta.2024.129954); retrieved 2026-10-08.

#### Q1492 Quantum Random Number Generation

Christoph Capellaro, Mohammad Hammoudeh.
Book chapter | 2024 | Quantum Computing | pp. 132-141.
Identifier and resource: [10.1201/9781003475286-8](https://doi.org/10.1201/9781003475286-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003475286-8); retrieved 2026-10-08.

#### Q1493 Quantum random number generation based on phase reconstruction

Jialiang Li, Zitao Huang, Chunlin Yu, Jiajie Wu, Tongge Zhao, Xiangwei Zhu, Shihai Sun.
Journal article | 2024 | Optics Express | vol. 32 | no. 4 | pp. 5056.
Identifier and resource: [10.1364/oe.515390](https://doi.org/10.1364/oe.515390).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Foe.515390); retrieved 2026-10-08.

#### Q1494 Quantum random number generation using Quandela photonic quantum computer

Muriel A. de Souza, Flavia P. Agostini, Luiz Vicente G. Tarelho.
Journal article | 2024 | Quantum Information Processing | vol. 23 | no. 11 | article 381.
Identifier and resource: [10.1007/s11128-024-04593-6](https://doi.org/10.1007/s11128-024-04593-6).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11128-024-04593-6); retrieved 2026-10-08.

#### Q1495 Secure quantum random number generation with perovskite photonics

Joakim Argillander, Alvaro Alarcon, Chunxiong Bao, Chaoyang Kuang, Gustavo Lima, Feng Gao, Guilherme B. Xavier.
Conference paper | 2024 | Quantum Computing, Communication, and Simulation IV | pp. 103.
Identifier and resource: [10.1117/12.2692061](https://doi.org/10.1117/12.2692061).
Conference metadata: Quantum Computing, Communication, and Simulation IV.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2692061); retrieved 2026-10-08.

#### Q1496 Exploring Quantum Systems for Pseudo-Random Number Generation

Luis José Mantilla Santa Cruz, Luis F. Faina, João Henrique de Souza Pereira.
Posted content | 2023 | Research Square Platform LLC.
Identifier and resource: [10.21203/rs.3.rs-3630730/v1](https://doi.org/10.21203/rs.3.rs-3630730/v1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21203%2Frs.3.rs-3630730%2Fv1); retrieved 2026-10-08.

#### Q1497 Multiplexing quantum tunneling diodes for random number generation

Kanin Aungskunsiri, Ratthasart Amarit, Sakdinan Jantarachote, Kruawan Wongpanya, Pongpun Punpetch, Sarun Sumriddetchkajorn.
Journal article | 2023 | Review of Scientific Instruments | vol. 94 | no. 1 | pp. 014704.
Identifier and resource: [10.1063/5.0113995](https://doi.org/10.1063/5.0113995).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0113995); retrieved 2026-10-08.

#### Q1498 Quantum random number generation with uncharacterised homodyne detection

Chao Wang, Ignatius William Primaatmaja, Hong Jie Ng, Jing Yan Haw, Raymond Ho, Jianran Zhang, Gong Zhang, Charles Lim.
Conference paper | 2023 | CLEO 2023 | pp. JTh2A.20.
Identifier and resource: [10.1364/cleo_at.2023.jth2a.20](https://doi.org/10.1364/cleo_at.2023.jth2a.20).
Conference metadata: CLEO: Applications and Technology.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_at.2023.jth2a.20); retrieved 2026-10-08.

#### Q1499 Semi-Quantum Random Number Generation

Julia Guskind, Walter O. Krawec.
Conference paper | 2023 | 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) | pp. 1211-1219.
Identifier and resource: [10.1109/qce57702.2023.00137](https://doi.org/10.1109/qce57702.2023.00137).
Conference metadata: 2023 IEEE International Conference on Quantum Computing and Engineering (QCE).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fqce57702.2023.00137); retrieved 2026-10-08.

## D28 Quantum sensing and metrology

Sensing is an adjacent quantum technology rather than a synonym for computation. It is included because control, estimation, and quantum resources connect it to computing research.

Prerequisites: Quantum mechanics, parameter estimation, and experimental physics.

Assessment focus: Sensitivity, bandwidth, noise, trust, and whether bounds are attainable.

Primary catalog resources in this category: 44.

### D28T01 Quantum parameter estimation

Quantum estimation studies how states and measurements encode unknown parameters. Bounds do not automatically imply an experimentally achievable estimator.

Fine subcategories: Quantum Fisher information; Cramer Rao bounds; multiparameter estimation; estimators.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1500 Quantum sensing

C. L. Degen, F. Reinhard, P. Cappellaro.
Journal article | 2017 | Reviews of Modern Physics | vol. 89 | no. 3 | article 035002.
Identifier and resource: [10.1103/revmodphys.89.035002](https://doi.org/10.1103/revmodphys.89.035002).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2FRevModPhys.89.035002); retrieved 2026-10-08.

#### Q1501 Channel correlation effects on quantum Fisher information in channel parameter estimation

Min Yu, Youneng Guo.
Journal article | 2025 | Physica Scripta | vol. 100 | no. 6 | pp. 065101.
Identifier and resource: [10.1088/1402-4896/add05b](https://doi.org/10.1088/1402-4896/add05b).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1402-4896%2Fadd05b); retrieved 2026-10-08.

#### Q1502 Simulated Annealing-Assisted GRAPE for Superior Quantum Fisher Information in Quantum Parameter Estimation

Yi Zhang, Zibo Miao, Zigui Zhang.
Conference paper | 2025 | 2025 IEEE 26th China Conference on System Simulation Technology and its Applications (CCSSTA) | pp. 649-654.
Identifier and resource: [10.1109/ieeeconf65522.2025.11137080](https://doi.org/10.1109/ieeeconf65522.2025.11137080).
Conference metadata: 2025 IEEE 26th China Conference on System Simulation Technology and its Applications (CCSSTA).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fieeeconf65522.2025.11137080); retrieved 2026-10-08.

#### Q1503 Fisher-information susceptibility for multiparameter quantum estimation

Francesco Albarelli, Ilaria Gianani, Marco G. Genoni, Marco Barbieri.
Journal article | 2024 | Physical Review A | vol. 110 | no. 3 | article 032436.
Identifier and resource: [10.1103/physreva.110.032436](https://doi.org/10.1103/physreva.110.032436).
Fine tags: Quantum Fisher information; multiparameter estimation.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.032436); retrieved 2026-10-08.

#### Q1504 Fisher information analysis for quantum-enhanced parameter estimation in an electromagnetically-induced-transparency spectrum with single photons

Pin-Ju Tsai, Lun-Ping Yuan, Ying-Cheng Chen.
Journal article | 2023 | Physical Review A | vol. 108 | no. 3 | article 033711.
Identifier and resource: [10.1103/physreva.108.033711](https://doi.org/10.1103/physreva.108.033711).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.108.033711); retrieved 2026-10-08.

#### Q1505 Quantum Fisher information and parameter estimation in non-Hermitian Hamiltonians

Jing Li, Hai-Tao Ding, Dan-Wei Zhang, Key Laboratory of Atomic and Subatomic Structure and Quantum Control, Ministry of Education, School of Physics, South China Normal University, Guangzhou 510006, China, National Key Laboratory of Solid State Microstructures, School of Physics, Nanjing University, Nanjing 210093, China.
Journal article | 2023 | Acta Physica Sinica | vol. 72 | no. 20 | pp. 200601.
Identifier and resource: [10.7498/aps.72.20230862](https://doi.org/10.7498/aps.72.20230862).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.72.20230862); retrieved 2026-10-08.

#### Q1506 Quantum Reservoir Parameter Estimation via Fisher Information

Ufuk KORKMAZ, Deniz TÜRKPENÇE.
Journal article | 2022 | Sakarya University Journal of Science | vol. 26 | no. 2 | pp. 388-396.
Identifier and resource: [10.16984/saufenbilder.1018716](https://doi.org/10.16984/saufenbilder.1018716).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.16984%2Fsaufenbilder.1018716); retrieved 2026-10-08.

#### Q1507 Coherence and quantum Fisher information in general single-qubit parameter estimation processes

Jun-Long Zhao, Dong-Xu Chen, Yu Zhang, Yu-Liang Fang, Ming Yang, Qi-Cheng Wu, Chui-Ping Yang.
Journal article | 2021 | Physical Review A | vol. 104 | no. 6 | article 062608.
Identifier and resource: [10.1103/physreva.104.062608](https://doi.org/10.1103/physreva.104.062608).
Fine tags: Quantum Fisher information.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.104.062608); retrieved 2026-10-08.

### D28T02 Quantum magnetometry

Magnetometry estimates fields using spin or other quantum probes. Sensitivity must be quoted with bandwidth, integration time, and spatial resolution.

Fine subcategories: NV sensing; spin ensembles; sensitivity; bandwidth; spatial resolution.

Primary resources: 17. Additional related assignments can be found in the interactive HTML.

#### Q1508 Operando Quantum Magnetometry for Battery Diagnostics

Avetik R. Harutyunyan.
Journal article | 2026 | ECS Meeting Abstracts | vol. MA2026-01 | no. 17 | pp. 1143-1143.
Identifier and resource: [10.1149/ma2026-01171143mtgabs](https://doi.org/10.1149/ma2026-01171143mtgabs).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1149%2Fma2026-01171143mtgabs); retrieved 2026-10-08.

#### Q1509 Quantum entanglement for magnetometry

Vladimir Slepnev, Azat Gubaydullin, Valerii Vinokur.
Journal article | 2026 | EPJ Quantum Technology | vol. 13 | no. 1 | article 76.
Identifier and resource: [10.1140/epjqt/s40507-026-00524-9](https://doi.org/10.1140/epjqt/s40507-026-00524-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1140%2Fepjqt%2Fs40507-026-00524-9); retrieved 2026-10-08.

#### Q1510 Quantum magnetometry enhanced by machine learning

Isabell Jauch, Thomas Strohm, Tino Fuchs, Fedor Jelezko.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 1 | pp. 015055.
Identifier and resource: [10.1088/2058-9565/ae3acf](https://doi.org/10.1088/2058-9565/ae3acf).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae3acf); retrieved 2026-10-08.

#### Q1511 Massively Multiplexed Nanoscale Magnetometry with Diamond Quantum Sensors

Kai-Hung Cheng, Zeeshawn Kazi, Jared Rovny, Bichen Zhang, Lila S. Nassar, Jeff D. Thompson, Nathalie P. de Leon.
Journal article | 2025 | Physical Review X | vol. 15 | no. 3 | article 031014.
Identifier and resource: [10.1103/t8fz-3tzs](https://doi.org/10.1103/t8fz-3tzs).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ft8fz-3tzs); retrieved 2026-10-08.

#### Q1512 Real Time Vector Magnetometry with Quantum Diamond Sensor

Napoom Thooppanom, Rapeephat Yodsungnoen, Natakorn Sapermsap, Sorawis Sangtawesin.
Journal article | 2025 | Journal of Physics: Conference Series | vol. 2934 | no. 1 | pp. 012022.
Identifier and resource: [10.1088/1742-6596/2934/1/012022](https://doi.org/10.1088/1742-6596/2934/1/012022).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1742-6596%2F2934%2F1%2F012022); retrieved 2026-10-08.

#### Q1513 Towards robust quantum diamond magnetometry for industrial applications

Sourav Chatterjee, Shashank Kumar, S John Sharon Sandeep, Pralekh Dubey, Phani Peddibhotla.
Conference paper | 2025 | CLEO 2025 | pp. JPS200_163.
Identifier and resource: [10.1364/cleo_at.2025.jps200_163](https://doi.org/10.1364/cleo_at.2025.jps200_163).
Conference metadata: CLEO: Applications and Technology.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fcleo_at.2025.jps200_163); retrieved 2026-10-08.

#### Q1514 Doppler-enhanced quantum magnetometry with thermal Rydberg atoms

Shovan Kanti Barik, Silpa B S, M Venkat Ramana, Shovan Dutta, Sanjukta Roy.
Journal article | 2024 | New Journal of Physics | vol. 26 | no. 7 | pp. 073036.
Identifier and resource: [10.1088/1367-2630/ad6179](https://doi.org/10.1088/1367-2630/ad6179).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fad6179); retrieved 2026-10-08.

#### Q1515 Electron beam characterization via quantum coherent optical magnetometry

Nicolas DeStefano, Saeed Pegahan, Aneesh Ramaswamy, Seth Aubin, T. Averett, Alexandre Camsonne, Svetlana Malinovskaya, Eugeniy E. Mikhailov et al..
Journal article | 2024 | Applied Physics Letters | vol. 125 | no. 26 | article 264001.
Identifier and resource: [10.1063/5.0234219](https://doi.org/10.1063/5.0234219).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0234219); retrieved 2026-10-08.

#### Q1516 H3 diamond color centers for quantum magnetometry

E.I. Lipatov, O.I. Lyga, V.V. Chashchin, M.A. Shulepov, V.G. Vins, A.P. Yelisseyev.
Conference paper | 2024 | 2024 International Conference Laser Optics (ICLO) | pp. 437-437.
Identifier and resource: [10.1109/iclo59702.2024.10624291](https://doi.org/10.1109/iclo59702.2024.10624291).
Conference metadata: 2024 International Conference Laser Optics (ICLO).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficlo59702.2024.10624291); retrieved 2026-10-08.

#### Q1517 Nanoscale covariance magnetometry with diamond quantum sensors

Nathalie de Leon.
Conference paper | 2024 | Integrated Optics: Devices, Materials, and Technologies XXVIII | pp. 22.
Identifier and resource: [10.1117/12.3008902](https://doi.org/10.1117/12.3008902).
Conference metadata: Integrated Optics: Devices, Materials, and Technologies XXVIII.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.3008902); retrieved 2026-10-08.

#### Q1518 Precision magnetometry exploiting excited state quantum phase transitions

Wang Qian, Ugo Marzolino.
Journal article | 2024 | SciPost Physics | vol. 17 | no. 2 | article 043.
Identifier and resource: [10.21468/scipostphys.17.2.043](https://doi.org/10.21468/scipostphys.17.2.043).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21468%2Fscipostphys.17.2.043); retrieved 2026-10-08.

#### Q1519 Quantum magnetometry using discrete-time quantum walk

Kunal Shukla, C. M. Chandrashekar.
Journal article | 2024 | Physical Review A | vol. 109 | no. 3 | article 032608.
Identifier and resource: [10.1103/physreva.109.032608](https://doi.org/10.1103/physreva.109.032608).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.109.032608); retrieved 2026-10-08.

#### Q1520 Quantum vector DC magnetometry via selective phase accumulation

Min Zhuang, Sijie Chen, Jiahao Huang, Chaohong Lee.
Journal article | 2024 | Science China Physics, Mechanics & Astronomy | vol. 67 | no. 10 | article 100312.
Identifier and resource: [10.1007/s11433-024-2400-1](https://doi.org/10.1007/s11433-024-2400-1).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11433-024-2400-1); retrieved 2026-10-08.

#### Q1521 A6.3 - Quantum Magnetometry for Material Testing

K. Thiemann, A. Blug, A. Bertz.
Conference paper | 2023 | Lectures | pp. 73-74.
Identifier and resource: [10.5162/smsi2023/a6.3](https://doi.org/10.5162/smsi2023/a6.3).
Conference metadata: SMSI 2023.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5162%2Fsmsi2023%2Fa6.3); retrieved 2026-10-08.

#### Q1522 Quantum magnetometry for space

C. Deans, T. Valenzuela, M. G. Bason.
Conference paper | 2023 | International Conference on Space Optics — ICSO 2022 | pp. 248.
Identifier and resource: [10.1117/12.2691360](https://doi.org/10.1117/12.2691360).
Conference metadata: International Conference on Space Optics — ICSO 2022.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2691360); retrieved 2026-10-08.

#### Q1523 Quantum-Enhanced Magnetometry at Optimal Number Density

Charikleia Troullinou, Vito Giovanni Lucivero, Morgan W. Mitchell.
Journal article | 2023 | Physical Review Letters | vol. 131 | no. 13 | article 133602.
Identifier and resource: [10.1103/physrevlett.131.133602](https://doi.org/10.1103/physrevlett.131.133602).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevlett.131.133602); retrieved 2026-10-08.

#### Q1524 Quantum Sensing Explained | NIST

Author metadata not supplied.
Institutional resource | Undated | NIST.
Identifier and resource: [Official resource](https://www.nist.gov/quantum-information-science/quantum-sensing-explained).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://www.nist.gov/quantum-information-science/quantum-sensing-explained); retrieved 2026-10-08.

### D28T03 Atomic clocks and interferometry

Clocks and interferometers exploit controlled phase accumulation for precise measurement. Stability, systematic shifts, and entangled probe preparation set limits.

Fine subcategories: Clock stability; atom interferometers; squeezing; systematic errors.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1525 Detectability of post-Newtonian classical and quantum gravity via quantum clock interferometry

Eyuri Wakakuwa.
Journal article | 2026 | Physical Review D | vol. 113 | no. 8 | article 086008.
Identifier and resource: [10.1103/hjfx-rlfj](https://doi.org/10.1103/hjfx-rlfj).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fhjfx-rlfj); retrieved 2026-10-08.

#### Q1526 Gravitational time dilation in quantum clock interferometry with entangled multi-photon states and quantum memories

Mustafa Gündoğan, Roy Barzel, Dennis Rätzel.
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 4 | pp. 045047.
Identifier and resource: [10.1088/2058-9565/aea2c3](https://doi.org/10.1088/2058-9565/aea2c3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Faea2c3); retrieved 2026-10-08.

#### Q1527 Atomic clock interferometry using optical tweezers

Ilan Meltzer, Yoav Sagi.
Journal article | 2024 | Physical Review A | vol. 110 | no. 3 | article 032602.
Identifier and resource: [10.1103/physreva.110.032602](https://doi.org/10.1103/physreva.110.032602).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.110.032602); retrieved 2026-10-08.

#### Q1528 Finite pulse-time effects in long-baseline quantum clock interferometry

Gregor Janson, Alexander Friedrich, Richard Lopp.
Journal article | 2024 | AVS Quantum Science | vol. 6 | no. 2 | article 024403.
Identifier and resource: [10.1116/5.0178230](https://doi.org/10.1116/5.0178230).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1116%2F5.0178230); retrieved 2026-10-08.

#### Q1529 Enhancing strontium clock atom interferometry using quantum optimal control

Zilin Chen, Garrett Louie, Yiping Wang, Tejas Deshpande, Tim Kovachy.
Journal article | 2023 | Physical Review A | vol. 107 | no. 6 | article 063302.
Identifier and resource: [10.1103/physreva.107.063302](https://doi.org/10.1103/physreva.107.063302).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysreva.107.063302); retrieved 2026-10-08.

#### Q1530 Quantum clock interferometry and violations of the equivalence principle

Enno Giese, Fabio Di Pumpo, Christian Ufrecht, Alexander Friedrich, Wolfgang Schleich, William Unruh.
Posted content | 2022 | Morressier.
Identifier and resource: [10.26226/m.6275705d66d5dcf63a3115f7](https://doi.org/10.26226/m.6275705d66d5dcf63a3115f7).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.26226%2Fm.6275705d66d5dcf63a3115f7); retrieved 2026-10-08.

#### Q1531 Quantum navigation with multi-axis atomic interferometry and hybrid&#160;

Yueyang Zou, Mouine Abidi, Philipp Barbey, Ashwin Rajagopalan, Christian Schubert, Matthias Gersemann, Dennis Schlippert, Sven Abend et al..
Posted content | 2022 | Copernicus GmbH.
Identifier and resource: [10.5194/egusphere-egu22-5697](https://doi.org/10.5194/egusphere-egu22-5697).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.5194%2Fegusphere-egu22-5697); retrieved 2026-10-08.

#### Q1532 Quantum Variational Optimization of Ramsey Interferometry and Atomic Clocks

Raphael Kaubruegger, Denis V. Vasilyev, Marius Schulte, Klemens Hammerer, Peter Zoller.
Journal article | 2021 | Physical Review X | vol. 11 | no. 4 | article 041045.
Identifier and resource: [10.1103/physrevx.11.041045](https://doi.org/10.1103/physrevx.11.041045).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevx.11.041045); retrieved 2026-10-08.

### D28T04 Quantum imaging and illumination

Quantum imaging and illumination use correlations for specified detection or imaging tasks. Advantages depend on the noise, receiver, and comparison model.

Fine subcategories: Correlation imaging; illumination receivers; resolution; noise; classical comparisons.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1533 Quantum illumination for scanning imaging under amplitude and phase noise

Jing Gao, Zhiming Qing, Jing Wang, He Jiang, Ming Zhang, Wenzheng Zhu, Hao Li, Shuangyin Huang et al..
Journal article | 2026 | Advanced Imaging | vol. 3 | no. 4 | pp. B00004.
Identifier and resource: [10.3788/ai.2026.10006](https://doi.org/10.3788/ai.2026.10006).
Fine tags: noise.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3788%2Fai.2026.10006); retrieved 2026-10-08.

#### Q1534 High-fidelity single-pixel imaging through scattering media using quantum-state encoded illumination

Cecilia Z. C. Yu, Weiming Song, Keng C. Chou.
Journal article | 2025 | Optics Letters | vol. 50 | no. 8 | pp. 2594.
Identifier and resource: [10.1364/ol.544494](https://doi.org/10.1364/ol.544494).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fol.544494); retrieved 2026-10-08.

#### Q1535 Using cyclic Hadamard masks for single-pixel quantum imaging under entangled photon illumination

Shuhang Bie, Xiaoxi Tong, Ziyang Lv, Hanyu Ye, Tun Cao.
Journal article | 2025 | Science Advances | vol. 11 | no. 34 | article eadw4799.
Identifier and resource: [10.1126/sciadv.adw4799](https://doi.org/10.1126/sciadv.adw4799).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fsciadv.adw4799); retrieved 2026-10-08.

#### Q1536 Quantum-illumination-inspired active single-pixel imaging with structured illumination

Tiantian Zhang, Zhiyuan Ye, Hai-Bo Wang, Jun Xiong.
Journal article | 2021 | Applied Optics | vol. 60 | no. 32 | pp. 10151.
Identifier and resource: [10.1364/ao.438642](https://doi.org/10.1364/ao.438642).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Fao.438642); retrieved 2026-10-08.

#### Q1537 Full-Field Imaging With Quantum Illumination

T. Gregory, P.-A. Moreau, E. Toninelli, M.J. Padgett.
Conference paper | 2020 | 2020 Photonics North (PN) | pp. 1-1.
Identifier and resource: [10.1109/pn50013.2020.9166939](https://doi.org/10.1109/pn50013.2020.9166939).
Conference metadata: 2020 Photonics North (PN).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fpn50013.2020.9166939); retrieved 2026-10-08.

#### Q1538 Imaging through noise with quantum illumination

T. Gregory, P.-A. Moreau, E. Toninelli, M. J. Padgett.
Journal article | 2020 | Science Advances | vol. 6 | no. 6 | article eaay2652.
Identifier and resource: [10.1126/sciadv.aay2652](https://doi.org/10.1126/sciadv.aay2652).
Fine tags: noise.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1126%2Fsciadv.aay2652); retrieved 2026-10-08.

#### Q1539 Simultaneous multicolour imaging using quantum dot structured illumination microscopy

HUI ZENG, HUAIDONG YANG, GUOXUAN LIU, SICHUN ZHANG, XINRONG ZHANG, YINXIN ZHANG.
Journal article | 2020 | Journal of Microscopy | vol. 277 | no. 1 | pp. 32-41.
Identifier and resource: [10.1111/jmi.12862](https://doi.org/10.1111/jmi.12862).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1111%2Fjmi.12862); retrieved 2026-10-08.

#### Q1540 Single-photon quantum imaging via single-photon illumination

Jia-Zhi Yang, Ming-Fei Li, Xiao-Xiao Chen, Wen-Kai Yu, An-Ning Zhang.
Journal article | 2020 | Applied Physics Letters | vol. 117 | no. 21 | article 214001.
Identifier and resource: [10.1063/5.0021214](https://doi.org/10.1063/5.0021214).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0021214); retrieved 2026-10-08.

### D28T05 Quantum sensing with error correction

Error corrected sensing seeks to protect useful signal accumulation while rejecting noise. The signal and noise operators must satisfy relevant conditions.

Fine subcategories: Logical sensors; noise filtering; Hamiltonian conditions; ancilla assistance.

Primary resources: 3. Additional related assignments can be found in the interactive HTML.

#### Q1541 Quantum sensing with Rydberg atoms enhanced by quantum error correction

Stanisław Kurzyna, Bartosz Niewelt, Mateusz Mazelanik, Wojciech Wasilewski, Rafał Demkowicz-Dobrzański, Michał Parniak.
Conference paper | 2025 | Frontiers in Optics + Laser Science 2025 (FiO, LS) | pp. FTu6C.4.
Identifier and resource: [10.1364/fio.2025.ftu6c.4](https://doi.org/10.1364/fio.2025.ftu6c.4).
Conference metadata: Frontiers in Optics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1364%2Ffio.2025.ftu6c.4); retrieved 2026-10-08.

#### Q1542 Distributed quantum sensing enhanced by continuous-variable error correction

Quntao Zhuang, John Preskill, Liang Jiang.
Journal article | 2020 | New Journal of Physics | vol. 22 | no. 2 | pp. 022001.
Identifier and resource: [10.1088/1367-2630/ab7257](https://doi.org/10.1088/1367-2630/ab7257).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1367-2630%2Fab7257); retrieved 2026-10-08.

#### Q1543 Spatial noise filtering through error correction for quantum sensing

David Layden, Paola Cappellaro.
Journal article | 2018 | npj Quantum Information | vol. 4 | no. 1 | article 30.
Identifier and resource: [10.1038/s41534-018-0082-2](https://doi.org/10.1038/s41534-018-0082-2).
Fine tags: noise filtering.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41534-018-0082-2); retrieved 2026-10-08.

## D29 Specialized scientific applications

Scientific applications must specify the observable or decision task and account for preparation and readout. These categories organize exploratory work without claiming universal practical advantage.

Prerequisites: Relevant scientific model and quantum algorithm prerequisites.

Assessment focus: Observable definition, model error, preparation, readout, and domain validation.

Primary catalog resources in this category: 31.

### D29T01 Quantum algorithms for high energy physics

High energy applications include field simulation and selected analysis tasks. Physical observable, truncation, and classical verification define the computational problem.

Fine subcategories: Field theory; scattering; event analysis; neutrinos; gauge dynamics.

Primary resources: 5. Additional related assignments can be found in the interactive HTML.

#### Q1544 Quantum Computing for High Energy Density Science

Lawrence Livermore National Laboratory (LLNL), Livermore, CA (United States), Yujin Cho, USDOE National Nuclear Security Administration (NNSA), Kristi Beck, Zachary Espley.
Report | 2026 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/17019150](https://doi.org/10.2172/17019150).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F17019150); retrieved 2026-10-08.

#### Q1545 Quantum computing for energy correlators

Kyle Lee, Francesco Turro, Xiaojun Yao.
Journal article | 2025 | Physical Review D | vol. 111 | no. 5 | article 054514.
Identifier and resource: [10.1103/physrevd.111.054514](https://doi.org/10.1103/physrevd.111.054514).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Fphysrevd.111.054514); retrieved 2026-10-08.

#### Q1546 Quantum Computing and High Energy Physics

Prasanth Shyamsundar.
Conference paper | 2024 | Quantum Computing and High Energy Physics.
Identifier and resource: [10.2172/2426500](https://doi.org/10.2172/2426500).
Conference metadata: Quantum Computing and High Energy Physics.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F2426500); retrieved 2026-10-08.

#### Q1547 Hunting Quantum Gravity with Analogs: The Case of High-Energy Particle Physics

Paolo Castorina, Alfredo Iorio, Helmut Satz.
Journal article | 2022 | Universe | vol. 8 | no. 9 | pp. 482.
Identifier and resource: [10.3390/universe8090482](https://doi.org/10.3390/universe8090482).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Funiverse8090482); retrieved 2026-10-08.

#### Q1548 Quantum Systems for Enhanced High Energy Particle Physics Detectors

M. Doser, E. Auffray, F.M. Brunbauer, I. Frank, H. Hillemanns, G. Orlandini, G. Kornakov.
Journal article | 2022 | Frontiers in Physics | vol. 10 | article 887738.
Identifier and resource: [10.3389/fphy.2022.887738](https://doi.org/10.3389/fphy.2022.887738).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffphy.2022.887738); retrieved 2026-10-08.

### D29T02 Quantum algorithms for nuclear physics

Nuclear applications target states, reactions, and observables of interacting particles. Model spaces and controlled physical approximations accompany circuit errors.

Fine subcategories: Nuclear structure; reactions; few body systems; interactions; spectroscopy.

Primary resources: 7. Additional related assignments can be found in the interactive HTML.

#### Q1549 Nuclear Physics in the Era of Quantum Computing and Quantum Machine Learning

José‐Enrique García‐Ramos, Álvaro Sáiz, José M. Arias, Lucas Lamata, Pedro Pérez‐Fernández.
Journal article | 2024 | Advanced Quantum Technologies | vol. 8 | no. 12 | article 2300219.
Identifier and resource: [10.1002/qute.202300219](https://doi.org/10.1002/qute.202300219).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.202300219); retrieved 2026-10-08.

#### Q1550 Quantum computing for nuclear physics

Martin J. Savage.
Journal article | 2024 | EPJ Web of Conferences | vol. 296 | pp. 01025.
Identifier and resource: [10.1051/epjconf/202429601025](https://doi.org/10.1051/epjconf/202429601025).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1051%2Fepjconf%2F202429601025); retrieved 2026-10-08.

#### Q1551 Quantum computing based high-energy nuclear physics

Tian-Yin Li, Hong-Xi Xing, Dan-Bo Zhang, Key Laboratory of Atomic and Subatomic Structure and Quantum Control (Ministry of Education), Institute of Quantum Matter, South China Normal University, Guangzhou 510006, China, Guangdong Provincial Key Laboratory of Nuclear Science, Institute of Quantum Matter, South China Normal University, Guangzhou 510006, China, Guangdong-Hong Kong Joint Laboratory of Quantum Matter, Southern Nuclear Science Computing Center, South China Normal University, Guangzhou 510006, China, Key Laboratory of Atomic and Subatomic Structure and Quantum Control (Ministry of Education), Guangdong Basic Research Center of Excellence for Structure and Fundamental Interactions of Matter, School of Physics, South China Normal University, Guangzhou 510006, China.
Journal article | 2023 | Acta Physica Sinica | vol. 72 | no. 20 | pp. 200303.
Identifier and resource: [10.7498/aps.72.20230907](https://doi.org/10.7498/aps.72.20230907).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.7498%2Faps.72.20230907); retrieved 2026-10-08.

#### Q1552 Quantum Computing for Quantum Dynamics in Nuclear Physics [Slides]

Alessandro Baroni.
Report | 2022 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/1846882](https://doi.org/10.2172/1846882).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F1846882); retrieved 2026-10-08.

#### Q1553 Selected topics of quantum computing for nuclear physics*

Dan-Bo Zhang, Hongxi Xing, Hui Yan, Enke Wang, Shi-Liang Zhu.
Journal article | 2021 | Chinese Physics B | vol. 30 | no. 2 | pp. 020306.
Identifier and resource: [10.1088/1674-1056/abd761](https://doi.org/10.1088/1674-1056/abd761).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F1674-1056%2Fabd761); retrieved 2026-10-08.

#### Q1554 Quantum Computing for Theoretical Nuclear Physics, A White Paper prepared for the U.S. Department of Energy, Office of Science, Office of Nuclear Physics

Joseph Carlson, David Dean, Morten Hjorth-Jensen, David Kaplan, John Preskill, Kenneth Roche, Martin Savage, Matthias Troyer.
Report | 2018 | Office of Scientific and Technical Information (OSTI).
Identifier and resource: [10.2172/1631143](https://doi.org/10.2172/1631143).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2172%2F1631143); retrieved 2026-10-08.

#### Q1555 Quantum algorithms for computational nuclear physics

Jakub Višňák.
Journal article | 2015 | EPJ Web of Conferences | vol. 100 | pp. 01008.
Identifier and resource: [10.1051/epjconf/201510001008](https://doi.org/10.1051/epjconf/201510001008).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1051%2Fepjconf%2F201510001008); retrieved 2026-10-08.

### D29T03 Quantum algorithms for numerical integration

Integration algorithms often build on amplitude estimation. The input oracle and required precision determine whether a query benefit survives end to end accounting.

Fine subcategories: Quadrature; Monte Carlo; dimensionality; oracle access; precision.

Primary resources: 3. Additional related assignments can be found in the interactive HTML.

#### Q1556 Spectral quantum algorithm for numerical differentiation and integration

Jordan Cioni, Fabio Semperlotti.
Journal article | 2026 | Physical Review Applied | vol. 26 | no. 1 | article 014063.
Identifier and resource: [10.1103/t8kt-5f2n](https://doi.org/10.1103/t8kt-5f2n).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1103%2Ft8kt-5f2n); retrieved 2026-10-08.

#### Q1557 A general quantum algorithm for numerical integration

Guoqiang Shu, Zheng Shan, Jinchen Xu, Jie Zhao, Shuya Wang.
Journal article | 2024 | Scientific Reports | vol. 14 | no. 1 | article 10432.
Identifier and resource: [10.1038/s41598-024-61010-9](https://doi.org/10.1038/s41598-024-61010-9).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs41598-024-61010-9); retrieved 2026-10-08.

#### Q1558 Quantum Coin Method for Numerical Integration

N. H. Shimada, T. Hachisuka.
Journal article | 2020 | Computer Graphics Forum | vol. 39 | no. 6 | pp. 243-257.
Identifier and resource: [10.1111/cgf.14015](https://doi.org/10.1111/cgf.14015).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1111%2Fcgf.14015); retrieved 2026-10-08.

### D29T04 Quantum algorithms for engineering

Engineering applications connect quantum algorithms to discretized models and inverse tasks. Conditioning and output extraction can dominate the workflow.

Fine subcategories: Finite elements; fluid models; differential equations; inverse problems; discretization.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1559 Variational quantum algorithms for computational fluid dynamics

Dieter Jaksch.
Posted content | 2025 | Cassyni.
Identifier and resource: [10.52843/cassyni.qx2xbp](https://doi.org/10.52843/cassyni.qx2xbp).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.52843%2Fcassyni.qx2xbp); retrieved 2026-10-08.

#### Q1560 A hybrid quantum-classical framework for computational fluid dynamics

Chuang-Chao Ye, Ning-Bo An, Teng-Yang Ma, Meng-Han Dou, Wen Bai, De-Jun Sun, Zhao-Yun Chen, Guo-Ping Guo.
Journal article | 2024 | Physics of Fluids | vol. 36 | no. 12 | article 127111.
Identifier and resource: [10.1063/5.0238193](https://doi.org/10.1063/5.0238193).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0238193); retrieved 2026-10-08.

#### Q1561 Computational Fluid Dynamics on Quantum Computers

Madhava Syamlal, Carter Copen, Masashi Takahashi, Benjamin Hall.
Conference paper | 2024 | AIAA AVIATION FORUM AND ASCEND 2024.
Identifier and resource: [10.2514/6.2024-3534](https://doi.org/10.2514/6.2024-3534).
Conference metadata: AIAA AVIATION FORUM AND ASCEND 2024.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2514%2F6.2024-3534); retrieved 2026-10-08.

#### Q1562 Quantum-inspired framework for computational fluid dynamics

Raghavendra Dheeraj Peddinti, Stefano Pisoni, Alessandro Marini, Philippe Lott, Henrique Argentieri, Egor Tiunov, Leandro Aolita.
Journal article | 2024 | Communications Physics | vol. 7 | no. 1 | article 135.
Identifier and resource: [10.1038/s42005-024-01623-8](https://doi.org/10.1038/s42005-024-01623-8).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1038%2Fs42005-024-01623-8); retrieved 2026-10-08.

#### Q1563 Variational Quantum Algorithms for Computational Fluid Dynamics

Dieter Jaksch, Peyman Givi, Andrew J. Daley, Thomas Rung.
Journal article | 2023 | AIAA Journal | vol. 61 | no. 5 | pp. 1885-1894.
Identifier and resource: [10.2514/1.j062426](https://doi.org/10.2514/1.j062426).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2514%2F1.j062426); retrieved 2026-10-08.

#### Q1564 Opportunities for quantum computation in computational fluid dynamics

Yan Li.
Conference paper | 2022 | 2nd International Conference on Applied Mathematics, Modelling, and Intelligent Computing (CAMMIC 2022) | pp. 205.
Identifier and resource: [10.1117/12.2639351](https://doi.org/10.1117/12.2639351).
Conference metadata: 2nd International Conference on Applied Mathematics, Modelling, and Intelligent Computing (CAMMIC 2022).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1117%2F12.2639351); retrieved 2026-10-08.

#### Q1565 Parallel evaluation of quantum algorithms for computational fluid dynamics

René Steijl, George N. Barakos.
Journal article | 2018 | Computers &amp; Fluids | vol. 173 | pp. 22-28.
Identifier and resource: [10.1016/j.compfluid.2018.03.080](https://doi.org/10.1016/j.compfluid.2018.03.080).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.compfluid.2018.03.080); retrieved 2026-10-08.

#### Q1566 Quantum Fluid Dynamics and Quantum Computational Fluid Dynamics

C. T. Lin, J. K. Kuo, T. H. Yen.
Journal article | 2009 | Journal of Computational and Theoretical Nanoscience | vol. 6 | no. 5 | pp. 1090-1108.
Identifier and resource: [10.1166/jctn.2009.1149](https://doi.org/10.1166/jctn.2009.1149).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1166%2Fjctn.2009.1149); retrieved 2026-10-08.

### D29T05 Quantum algorithms for biology and drug discovery

Biological and drug discovery proposals often depend on quantum chemistry subproblems. Chemical accuracy and downstream biological validation should be assessed separately.

Fine subcategories: Molecular energies; docking proposals; chemistry pipelines; validation; biological relevance.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1567 Quantum Computing and Drug Discovery: Current Trends and Future

Yashraj Mukherjee, Praveen Pathak, Shweta Sinha.
Journal article | 2026 | International Journal For Multidisciplinary Research | vol. 8 | no. 1 | article 65289.
Identifier and resource: [10.36948/ijfmr.2026.v08i01.65289](https://doi.org/10.36948/ijfmr.2026.v08i01.65289).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.36948%2Fijfmr.2026.v08i01.65289); retrieved 2026-10-08.

#### Q1568 Quantum Computing in Drug Discovery

Nilesh Ingale Nilesh Ingale.
Journal article | 2026 | International Journal of Scientific Research in Engineering and Management | vol. 10 | no. 9.
Identifier and resource: [10.55041/ijsrem.istcesd038](https://doi.org/10.55041/ijsrem.istcesd038).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.55041%2Fijsrem.istcesd038); retrieved 2026-10-08.

#### Q1569 Quantum Computing in Drug Discovery Techniques, Challenges, and Emerging Opportunities

Virendra S. Gomase, Arjun P. Ghatule, Rupali Sharma, Suchita P. Dhamane.
Journal article | 2026 | Current Drug Discovery Technologies | vol. 23 | no. 4 | article e15701638371707.
Identifier and resource: [10.2174/0115701638371707250729040426](https://doi.org/10.2174/0115701638371707250729040426).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.2174%2F0115701638371707250729040426); retrieved 2026-10-08.

#### Q1570 Quantum Computing: Revolutionizing Drug Discovery and Battery Development

G. Deepalakshmi, S.K. Sunori, K.V. Padmavathi, P. Balaramesh, M. Kathiravan, V. Venkatesh.
Book chapter | 2026 | Advanced Transportation Systems in the Field of Engineering and Technology | pp. 249-252.
Identifier and resource: [10.1201/9781003598312-79](https://doi.org/10.1201/9781003598312-79).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003598312-79); retrieved 2026-10-08.

#### Q1571 Quantum computing applications in drug discovery

Jing Li, Leyi Wei, Henry H Y Tong, Quan Zou.
Journal article | 2026 | Briefings in Bioinformatics | vol. 27 | no. 3 | article bbag274.
Identifier and resource: [10.1093/bib/bbag274](https://doi.org/10.1093/bib/bbag274).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1093%2Fbib%2Fbbag274); retrieved 2026-10-08.

#### Q1572 Quantum computing applications in drug discovery: Unraveling complex molecular interactions

Anagha Deepak Kulkarni, Tejasvini Rahul Katkar, Smita Jadhav, Pranali Anandrao Jadhav.
Conference paper | 2026 | AIP Conference Proceedings | vol. 3445 | pp. 030122.
Identifier and resource: [10.1063/5.0327515](https://doi.org/10.1063/5.0327515).
Conference metadata: INTERNATIONAL CONFERENCE ON RECENT TRENDS IN MATERIALS SCIENCE AND MECHANICAL ENGINEERING (ICRMSME 2025).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1063%2F5.0327515); retrieved 2026-10-08.

#### Q1573 Quantum computing in drug discovery

Harshraj Gadbail, Rajendra Rewatkar, Nishant Jumde, Mrinal Manker, Pratik Nagre, Sujal Zade.
Journal article | 2026 | Frontiers in Drug Discovery | vol. 6 | article 1815176.
Identifier and resource: [10.3389/fddsv.2026.1815176](https://doi.org/10.3389/fddsv.2026.1815176).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3389%2Ffddsv.2026.1815176); retrieved 2026-10-08.

#### Q1574 Quantum computing-driven evolution of drug discovery paradigms

Lu Han, Zhipeng Ke, Liying Liu, Liang Cao, Zhenzhong Wang, Xinzhuang Zhang, Wenxia Zhou, Wei Xiao.
Journal article | 2026 | Chinese Science Bulletin.
Identifier and resource: [10.1360/csb-2026-0450](https://doi.org/10.1360/csb-2026-0450).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1360%2Fcsb-2026-0450); retrieved 2026-10-08.

## D30 Education research practice and ecosystem

Research practice includes learning, reproducing results, documenting limitations, and judging evidence. Roadmaps and standards describe plans or interfaces rather than proof that a device meets them.

Prerequisites: Basic quantum computing and critical reading.

Assessment focus: Source quality, environment records, fair baselines, versioning, and full system cost.

Primary catalog resources in this category: 26.

### D30T01 Quantum computing education

Education resources teach prerequisites, conceptual models, and executable experiments. Curriculum scope and assessment quality determine how to use them.

Fine subcategories: Prerequisites; laboratories; assessments; visual explanations; curriculum design.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1575 Quantum-Ready Education: Preparing Students for Post-Quantum Computing Societies

Wai Yie Leong.
Conference paper | 2026 | 2026 15th International Conference on Educational and Information Technology (ICEIT) | pp. 926-930.
Identifier and resource: [10.1109/iceit68991.2026.11521622](https://doi.org/10.1109/iceit68991.2026.11521622).
Conference metadata: 2026 15th International Conference on Educational and Information Technology (ICEIT).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficeit68991.2026.11521622); retrieved 2026-10-08.

#### Q1576 BETTER VISUAL METAPHORS FOR QUANTUM COMPUTING EDUCATION

Barry Fagin.
Conference paper | 2025 | EDULEARN Proceedings | vol. 1 | pp. 8543-8552.
Identifier and resource: [10.21125/edulearn.2025.2222](https://doi.org/10.21125/edulearn.2025.2222).
Conference metadata: 17th International Conference on Education and New Learning Technologies.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.21125%2Fedulearn.2025.2222); retrieved 2026-10-08.

#### Q1577 Enhancing Quantum Computing Education Through Virtual Reality

Yu Yan, Jeannie S. Lee, Kan Chen, Nicholas H.L. Wong.
Conference paper | 2025 | Proceedings of the 2025 20th ACM SIGGRAPH International Conference on Virtual-Reality Continuum and its Applications in Industry | pp. 1-2.
Identifier and resource: [10.1145/3779232.3779282](https://doi.org/10.1145/3779232.3779282).
Conference metadata: VRCAI '25: The 20th ACM SIGGRAPH International Conference on Virtual-Reality Continuum and its Applications in Industry.
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1145%2F3779232.3779282); retrieved 2026-10-08.

#### Q1578 Enhancing Quantum Literacy in Secondary Education Through Quantum Computing and Quantum Key Distribution

Aspasia V. Oikonomou, Ilias K. Savvas, Omiros Iatrellis.
Journal article | 2025 | Education Sciences | vol. 15 | no. 9 | pp. 1167.
Identifier and resource: [10.3390/educsci15091167](https://doi.org/10.3390/educsci15091167).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.3390%2Feducsci15091167); retrieved 2026-10-08.

#### Q1579 Integrating Quantum Computing into STEM Education via Personalized Learning

Oluwatoyin Akinbi, Mozhgan N. Entekhabi, Hongmei Chi.
Conference paper | 2025 | 2025 Interdisciplinary Conference on Electrics and Computer (INTCEC) | pp. 1-7.
Identifier and resource: [10.1109/intcec65580.2025.11256059](https://doi.org/10.1109/intcec65580.2025.11256059).
Conference metadata: 2025 Interdisciplinary Conference on Electrics and Computer (INTCEC).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fintcec65580.2025.11256059); retrieved 2026-10-08.

#### Q1580 Pedagogical Approach for Quantum Computing in Engineering Education

Francisco Orts.
Journal article | 2025 | Computer Applications in Engineering Education | vol. 33 | no. 2 | article e70004.
Identifier and resource: [10.1002/cae.70004](https://doi.org/10.1002/cae.70004).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fcae.70004); retrieved 2026-10-08.

#### Q1581 GitHub - NVIDIA/cuda-q-academic: This repo contains CUDA-Q Academic materials, including self-paced Jupyter notebook modules for building and optimizing hybrid quantum-classical algorithms using CUDA-Q. · GitHub

Author metadata not supplied.
Software repository | Undated | NVIDIA.
Identifier and resource: [Official resource](https://github.com/NVIDIA/cuda-q-academic).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://github.com/NVIDIA/cuda-q-academic); retrieved 2026-10-08.

#### Q1582 Part III Quantum Computation | Centre for Quantum Information and Foundations

Author metadata not supplied.
Course | Undated | University of Cambridge.
Identifier and resource: [Official resource](https://www.qi.damtp.cam.ac.uk/part-iii-quantum-computation).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://www.qi.damtp.cam.ac.uk/part-iii-quantum-computation); retrieved 2026-10-08.

### D30T02 Quantum computing surveys and roadmaps

Surveys and roadmaps organize a fast moving field and identify bottlenecks. Roadmap milestones are plans rather than demonstrated capabilities.

Fine subcategories: Hardware surveys; algorithm surveys; milestones; uncertainty; scaling bottlenecks.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1583 Quantum Computing in the NISQ era and beyond

John Preskill.
Journal article | 2018 | Quantum | vol. 2 | pp. 79 | article 79.
Identifier and resource: [10.22331/q-2018-08-06-79](https://doi.org/10.22331/q-2018-08-06-79).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.22331%2Fq-2018-08-06-79); retrieved 2026-10-08.

#### Q1584 Classical Intelligence For Quantum Technologies: An Evidence Roadmap For AI‐Enabled Quantum‐Computing Workflows

Amar Singh, Vinod Kumar Shukla, Sahraoui Dhelim, Chatter Singh.
Journal article | 2026 | Advanced Quantum Technologies | vol. 9 | no. 10 | article e70495.
Identifier and resource: [10.1002/qute.70495](https://doi.org/10.1002/qute.70495).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1002%2Fqute.70495); retrieved 2026-10-08.

#### Q1585 Impact of Quantum Computing on Asymmetric Cryptography Infrastructures: Prospective Study and Post-Quantum Transition Roadmap

João Manuel Marques Lucas, Carlos Caleiro, António Leonardo Gonçalves, Laercio Cruvinel Júnior.
Conference paper | 2026 | 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET) | pp. 1-6.
Identifier and resource: [10.1109/icecet65726.2026.11633187](https://doi.org/10.1109/icecet65726.2026.11633187).
Conference metadata: 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Ficecet65726.2026.11633187); retrieved 2026-10-08.

#### Q1586 Quantum Computing and Information Technology: A Roadmap for the Next Decade

Author metadata not supplied.
Book chapter | 2026 | Advanced Studies in Multidisciplinary Research and Innovation (ASMRI).
Identifier and resource: [10.59646/745/21](https://doi.org/10.59646/745/21).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.59646%2F745%2F21); retrieved 2026-10-08.

#### Q1587 Roadmap on quantum thermodynamics

Steve Campbell, Irene D’Amico, Mario A Ciampini, Janet Anders, Natalia Ares, Simone Artini, Alexia Auffèves, Lindsay Bassman Oftelie et al..
Journal article | 2026 | Quantum Science and Technology | vol. 11 | no. 1 | pp. 012501.
Identifier and resource: [10.1088/2058-9565/ae1e27](https://doi.org/10.1088/2058-9565/ae1e27).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Fae1e27); retrieved 2026-10-08.

#### Q1588 Quantum Computing Explained | NIST

Author metadata not supplied.
Institutional resource | Undated | NIST.
Identifier and resource: [Official resource](https://www.nist.gov/quantum-information-science/quantum-computing-explained).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://www.nist.gov/quantum-information-science/quantum-computing-explained); retrieved 2026-10-08.

#### Q1589 Quantum Information Science (QIS... | U.S. DOE Office of Science(SC)

Author metadata not supplied.
Institutional resource | Undated | US Department of Energy.
Identifier and resource: [Official resource](https://science.osti.gov/Initiatives/QIS).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://science.osti.gov/Initiatives/QIS); retrieved 2026-10-08.

#### Q1590 Quantum information science | NIST

Author metadata not supplied.
Institutional resource | Undated | NIST.
Identifier and resource: [Official resource](https://www.nist.gov/quantum-information-science).
Fine tags: Topic level only.
Verification: HTTP 200 page and title retrieved on 2026-10-08.
[Source record](https://www.nist.gov/quantum-information-science); retrieved 2026-10-08.

### D30T03 Quantum standards and interoperability

Standards and interfaces support consistent terminology and tool interoperability. The applicable version and scope should be recorded when used.

Fine subcategories: Terminology; interfaces; reference models; benchmarking definitions; interoperability.

Primary resources: 1. Additional related assignments can be found in the interactive HTML.

#### Q1591 Cryogenic RF Calibrations and Standards for Quantum Computing

Peter Hopkins, Lafe Spietz, Adam Sirois, Manuel Castellanos-Beltran, Nathan FlowersJacobs, Elyse McEntee Wei, Chris Long, Dylan Williams et al..
Conference paper | 2026 | 2026 United States National Committee of URSI National Radio Science Meeting (USNC-URSI NRSM) | pp. 235-235.
Identifier and resource: [10.23919/nrsm68586.2026.11550799](https://doi.org/10.23919/nrsm68586.2026.11550799).
Conference metadata: 2026 United States National Committee of URSI National Radio Science Meeting (USNC-URSI NRSM).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.23919%2Fnrsm68586.2026.11550799); retrieved 2026-10-08.

### D30T04 Quantum reproducibility and research methodology

Reproducible research records environments, circuits, parameters, datasets, and uncertainty. Fair benchmarks also preserve strong classical baselines and complete cost accounting.

Fine subcategories: Experiment records; seeds; environments; baselines; statistical reporting.

Primary resources: 1. Additional related assignments can be found in the interactive HTML.

#### Q1592 Reproducibility in Quantum Computing

Samudra Dasgupta, Travis S. Humble.
Conference paper | 2021 | 2021 IEEE Computer Society Annual Symposium on VLSI (ISVLSI) | pp. 458-461.
Identifier and resource: [10.1109/isvlsi51109.2021.00090](https://doi.org/10.1109/isvlsi51109.2021.00090).
Conference metadata: 2021 IEEE Computer Society Annual Symposium on VLSI (ISVLSI).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1109%2Fisvlsi51109.2021.00090); retrieved 2026-10-08.

### D30T05 Quantum economics and sustainability

Economics and sustainability studies evaluate full system cost and energy use. Cooling, classical support, runtime, and utilization matter alongside quantum device operation.

Fine subcategories: Cooling energy; runtime cost; total system accounting; scaling; economic assumptions.

Primary resources: 8. Additional related assignments can be found in the interactive HTML.

#### Q1593 Quantum Computing for a Sustainable Future: Transforming Energy Efficiency and Climate Solutions

Sreevatsa Bellary, Ananya Hadadi Raghavendra.
Book chapter | 2026 | Studies in Big Data | pp. 55-76.
Identifier and resource: [10.1007/978-3-032-00586-1_3](https://doi.org/10.1007/978-3-032-00586-1_3).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-032-00586-1_3); retrieved 2026-10-08.

#### Q1594 Application of Quantum Computing in the Energy Industry, Decarbonization, and Sustainability

Christoph Capellaro, Rafael Martín-Cuevas, Guzmán Calleja, Pascal Halffmann, Shivam Sharma.
Book chapter | 2025 | Quantum Technology Applications, Impact, and Future Challenges | pp. 9-36.
Identifier and resource: [10.1201/9781003537243-2](https://doi.org/10.1201/9781003537243-2).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1201%2F9781003537243-2); retrieved 2026-10-08.

#### Q1595 Enhancing e-commerce logistics efficiency and sustainability via quantum computing and artificial intelligence-based quantum hybrid models

Muhammad Khan, Farhan Amin, Minhaj Ud Din, Muhammad Ali Abid, Isabel de la Torre, Elisabeth Caro Montero, Irene Delgado Noya.
Journal article | 2025 | The Journal of Supercomputing | vol. 81 | no. 15 | article 1455.
Identifier and resource: [10.1007/s11227-025-07959-4](https://doi.org/10.1007/s11227-025-07959-4).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2Fs11227-025-07959-4); retrieved 2026-10-08.

#### Q1596 Power Consumption and Energy Efficiency of Quantum Computing Platforms in High Performance Computing Integration

Xiaolong Deng, Martin Schulz, Laura Schulz.
Book chapter | 2025 | Lecture Notes in Computer Science | pp. 325-337.
Identifier and resource: [10.1007/978-3-031-85700-3_24](https://doi.org/10.1007/978-3-031-85700-3_24).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1007%2F978-3-031-85700-3_24); retrieved 2026-10-08.

#### Q1597 Quantum computing: Impact on energy efficiency and sustainability

Vaishali Sood, Rishi Pal Chauhan.
Journal article | 2024 | Expert Systems with Applications | vol. 255 | pp. 124401 | article 124401.
Identifier and resource: [10.1016/j.eswa.2024.124401](https://doi.org/10.1016/j.eswa.2024.124401).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1016%2Fj.eswa.2024.124401); retrieved 2026-10-08.

#### Q1598 Towards Greener Power Grids Quantum Computing Solutions for Energy Efficiency

Kuppam Mohan Babu, M. Bhaskaraiah, Kasaram Roja, T. Chandraiah.
Book chapter | 2024 | Advances in Computational Intelligence and Robotics | pp. 392-406.
Identifier and resource: [10.4018/979-8-3693-4001-1.ch026](https://doi.org/10.4018/979-8-3693-4001-1.ch026).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.4018%2F979-8-3693-4001-1.ch026); retrieved 2026-10-08.

#### Q1599 Enhancing Cannabis Extraction Efficiency and Sustainability through Quantum Computing: A Review

Mokhlesur R. M, Tahmid C. A, Hassan S, Zubaer M, Awang M, Hasan M.
Journal article | 2023 | Oriental Journal Of Chemistry | vol. 39 | no. 6 | pp. 1419-1436.
Identifier and resource: [10.13005/ojc/390604](https://doi.org/10.13005/ojc/390604).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.13005%2Fojc%2F390604); retrieved 2026-10-08.

#### Q1600 Is quantum computing green? An estimate for an energy-efficiency quantum advantage

Daniel Jaschke, Simone Montangero.
Journal article | 2023 | Quantum Science and Technology | vol. 8 | no. 2 | pp. 025001.
Identifier and resource: [10.1088/2058-9565/acae3e](https://doi.org/10.1088/2058-9565/acae3e).
Fine tags: Topic level only.
Verification: DOI registered in retrieved Crossref record; resolver not individually checked.
[Source record](https://api.crossref.org/works/10.1088%2F2058-9565%2Facae3e); retrieved 2026-10-08.

## Catalog field definitions

| Field | Meaning |
| --- | --- |
| ID | Stable resource identifier shared by the editions |
| Major category | Broad subject area |
| Topic | Primary title screened or curated subject assignment |
| Fine tag | Supported lexical subcategory or topic level only |
| Related topics | Additional supported discovery assignments in HTML and JSON |
| Year | Published or issued year in metadata; explicit year for a small number of courses and standards |
| Venue | Journal, proceedings, book container, or official provider as supplied |
| Conference | Event or proceedings venue, when supplied |
| DOI | Retrieved scholarly identifier |
| Source record | Bibliographic API record or official web page |
| Verification | Registered metadata or successful first party page retrieval |

## Acknowledgments

OpenAI 6.1 sol was used to obtain and organize the initial resource collection and to assist with taxonomy development, documentation, and repository preparation. Source records support bibliographic identity; AI assistance does not imply publisher endorsement or universal full-text verification.
