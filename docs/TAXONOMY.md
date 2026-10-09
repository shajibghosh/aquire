# Subject taxonomy

Fine vocabulary is scoped to each topic. Related technologies are included explicitly; this is a broad map rather than an exhaustive classification.

## D01 — Foundations and mathematical tools

The language of quantum information connects linear algebra, probability, physical states, and measurements. These resources build the prerequisites needed to read algorithm and hardware papers.

**Prerequisites:** Linear algebra, probability, and introductory quantum mechanics

**Assessment:** State normalization, operator properties, measurement definitions, and physical interpretation

### D01T01 — Linear algebra and Hilbert spaces

Hilbert spaces provide the state space for quantum systems; tensor products describe composition. Linear algebra is also the implementation language of gates and many simulators.

- State vectors
- inner products
- tensor products
- eigenvalues
- spectral decomposition
- unitary operators

### D01T02 — Quantum states and density operators

Density operators represent both pure states and statistical mixtures. Reduced states are essential when only part of a larger system is measured or controlled.

- Pure states
- mixed states
- Bloch sphere
- partial trace
- reduced states
- purification

### D01T03 — Quantum measurements

Measurements convert quantum states into classical outcomes according to a specified measurement model. General measurements require POVMs and instruments rather than only orthogonal projectors.

- Projective measurements
- POVMs
- weak measurement
- quantum instruments
- measurement disturbance

### D01T04 — Quantum channels and open systems

Quantum channels describe physical transformations including noise and discarded subsystems. Open system models connect microscopic dynamics to experimentally observed decoherence.

- Kraus representations
- completely positive maps
- Lindblad equations
- Stinespring dilation
- non Markovian dynamics

### D01T05 — Quantum entropy and information measures

Information measures quantify uncertainty, correlations, and distinguishability. Operational meanings depend on the coding, estimation, or security task being studied.

- Von Neumann entropy
- relative entropy
- mutual information
- min entropy
- data processing inequalities

## D02 — Entanglement and quantum resources

Entanglement and other nonclassical resources supply capabilities that must be characterized separately from hardware size. Resource theory studies what operations can generate or consume each resource.

**Prerequisites:** Density operators, composite systems, and basic information measures

**Assessment:** Allowed operations, resource monotones, witness validity, and operational task

### D02T01 — Entanglement detection and quantification

Entanglement criteria test whether a state is separable, while monotones quantify particular resources. Different measures need not order mixed states in the same way.

- Witnesses
- separability criteria
- negativity
- concurrence
- entanglement entropy

### D02T02 — Bell nonlocality and contextuality

Bell nonlocality concerns correlations incompatible with local hidden variable models. Contextuality concerns dependence on measurement context and requires its own experimental assumptions.

- Bell inequalities
- loopholes
- device independence
- contextuality inequalities
- self testing

### D02T03 — Coherence and resource theories

Resource theories specify free states and operations before defining a resource. Coherence, asymmetry, and entanglement are related but distinct examples.

- Incoherent operations
- asymmetry
- conversion rates
- resource monotones
- coherence distillation

### D02T04 — Magic and stabilizer resources

Magic characterizes resources outside stabilizer computation. It matters both for non Clifford computation and for the cost of classical simulation.

- Nonstabilizer states
- mana
- robustness of magic
- stabilizer rank
- simulation costs

### D02T05 — Entanglement distillation

Distillation converts noisy shared resources into fewer high quality ones. Rates and achievable fidelities depend on allowed communication and operation classes.

- Purification
- hashing
- bound entanglement
- one shot protocols
- network resource conversion

## D03 — Models of quantum computation

Different models specify the available operations and how an algorithm is executed. Equivalence of models does not imply identical engineering costs or noise tolerance.

**Prerequisites:** Qubits, unitary operations, and measurement

**Assessment:** Model assumptions, universality, resource generation, and noise constraints

### D03T01 — Circuit and universal gate models

A circuit is an ordered composition of gates and measurements. Universality describes what transformations can be approximated, while compilation determines their actual cost.

- Universal gate sets
- reversible circuits
- qudit gates
- multi controlled gates
- universality proofs

### D03T02 — Measurement based computing

Measurement based computation processes an entangled resource state through adaptive local measurements. Classical feed forward and resource generation are part of the computation.

- Cluster states
- graph states
- adaptive measurements
- feed forward
- one way computing

### D03T03 — Adiabatic quantum computing

Adiabatic computation evolves a Hamiltonian along a path whose low energy states encode the answer. Gap behavior and schedule assumptions determine the required runtime.

- Spectral gaps
- adiabatic theorems
- schedule design
- universality
- diabatic effects

### D03T04 — Quantum annealing

Annealing seeks low energy solutions of an encoded optimization problem. Embedding, temperature, open system dynamics, and solution sampling distinguish hardware annealers from ideal adiabatic algorithms.

- Ising encoding
- QUBO
- minor embedding
- anneal offsets
- reverse annealing

### D03T05 — Continuous variable computing

Continuous variable systems encode information in modes with continuous quadratures. Universal computation generally needs suitable non Gaussian resources as well as Gaussian control.

- Quadratures
- Gaussian states
- non Gaussian operations
- squeezing
- continuous variable universality

### D03T06 — Topological computation and anyons

Topological schemes encode and manipulate information using anyonic degrees of freedom. Mathematical universality and experimental identification of the required excitations are separate questions.

- Braiding
- fusion rules
- non Abelian statistics
- topological gates
- Majorana proposals

## D04 — Quantum complexity and limitations

Complexity theory identifies conditional speedups and lower bounds. It also explains why a problem being quantum does not automatically make it efficiently solvable.

**Prerequisites:** Algorithms, asymptotic analysis, and discrete mathematics

**Assessment:** Oracle model, complexity assumptions, lower bounds, and input access

### D04T01 — Quantum complexity classes

Complexity classes formalize efficiently solvable and verifiable quantum problems. A class inclusion or separation should be read together with its error and oracle model.

- BQP
- QMA
- QCMA
- interactive proofs
- promise problems
- oracle separations

### D04T02 — Query complexity and lower bounds

Query complexity counts accesses to an input oracle. This isolates useful theoretical questions but does not include the physical cost of constructing that oracle.

- Polynomial method
- adversary method
- oracle models
- decision trees
- bounded error queries

### D04T03 — Quantum communication complexity

Communication complexity asks how much information must be exchanged to solve a distributed task. Prior entanglement and classical side channels change the model.

- One way communication
- simultaneous messages
- entanglement assisted protocols
- lower bounds

### D04T04 — Quantum advantage and sampling hardness

Sampling advantage compares specified quantum distributions with classical algorithms under stated assumptions. A sampling demonstration is not by itself evidence of useful application advantage.

- Circuit sampling
- complexity assumptions
- classical baselines
- verification gaps
- asymptotic advantage

### D04T05 — Dequantization and classical limitations

Dequantization identifies classical algorithms that reproduce a claimed benefit under comparable access assumptions. Input preparation and low rank structure often determine the comparison.

- Sample query access
- low rank assumptions
- classical emulation
- input access costs
- quantum inspired algorithms

## D05 — Core quantum algorithms

Primitive algorithms form reusable components of larger workflows. Their complexity must include data preparation, oracle construction, accuracy, and measurement costs.

**Prerequisites:** Quantum circuits, probability, and eigenvalue problems

**Assessment:** Oracle construction, precision, state overlap, and output readout

### D05T01 — Quantum Fourier transform

The quantum Fourier transform changes between computational and Fourier bases. It is a primitive in phase estimation and order finding rather than a general replacement for classical FFT output.

- Phase kickback
- approximate transforms
- semiclassical transforms
- arithmetic circuits
- Fourier sampling

### D05T02 — Phase estimation

Phase estimation extracts eigenphase information from controlled dynamics. Precision, coherent evolution time, and state overlap control its cost and success probability.

- Iterative estimation
- Bayesian estimation
- robust estimation
- spectral resolution
- controlled evolution

### D05T03 — Amplitude amplification and search

Amplitude amplification raises the probability of a marked outcome. Search speedups are measured in oracle queries and must include the implementation of the marking operation.

- Grover search
- fixed point amplification
- search lower bounds
- unknown success probability

### D05T04 — Amplitude estimation

Amplitude estimation estimates a probability or expectation using structured quantum access. Near term variants trade coherent depth for sampling and inference.

- Monte Carlo estimation
- maximum likelihood estimation
- iterative methods
- confidence intervals

### D05T05 — Quantum walks

Quantum walks use interference in graph or configuration space to design algorithms. Walk dynamics, graph access, and hitting or detection tasks need separate definitions.

- Discrete time walks
- continuous time walks
- hitting times
- graph search
- spatial search

### D05T06 — Hidden subgroup and factoring algorithms

Order finding underlies Shor factoring and discrete logarithm algorithms. Hidden subgroup methods generalize the structure, but non abelian cases have additional obstacles.

- Shor algorithm
- order finding
- discrete logarithms
- abelian subgroups
- non abelian challenges

## D06 — Advanced algorithm design

Modern algorithm frameworks organize linear algebra, simulation, and optimization around carefully controlled access models. Resource estimates depend strongly on how operators are encoded.

**Prerequisites:** Linear algebra, core quantum algorithms, and approximation theory

**Assessment:** Block encoding normalization, conditioning, polynomial degree, and total cost

### D06T01 — Block encoding and qubitization

Block encodings embed an operator into a larger unitary, and qubitization builds controlled spectral transformations. Normalization and oracle construction are central resource assumptions.

- Signal oracles
- normalization factors
- quantum walks
- Hamiltonian access
- projected unitary encodings

### D06T02 — Quantum signal processing

Quantum signal processing implements constrained polynomial transformations through phase sequences. Polynomial degree, phase synthesis, and approximation error determine algorithm costs.

- Polynomial transformations
- phase factor synthesis
- parity constraints
- approximation error

### D06T03 — Quantum singular value transformation

Singular value transformation applies polynomial functions to the singular values of a block encoded matrix. It unifies many algorithms while making access assumptions explicit.

- Matrix functions
- singular value thresholds
- pseudoinverses
- spectral filtering
- polynomial degree

### D06T04 — Linear combination of unitaries

Linear combinations of unitaries implement operators using coherent selection and state preparation. Success probability and amplification overhead affect the final resource estimate.

- PREPARE and SELECT oracles
- oblivious amplification
- Taylor series simulation
- success probability

### D06T05 — Quantum linear systems

Quantum linear systems algorithms prepare a state related to a linear system solution. Extracting every solution component can remove the intended advantage.

- HHL
- condition numbers
- sparse access
- solution observables
- preconditioning

### D06T06 — Quantum differential equations

Differential equation algorithms encode time evolution or discretized solution vectors. Stability, conditioning, boundary conditions, and output observables all enter the analysis.

- Ordinary differential equations
- partial differential equations
- stability
- boundary conditions
- solution readout

## D07 — Hamiltonian simulation and many body physics

Quantum simulation targets the evolution and observables of physical systems. Digital, analog, and hybrid approaches have different error budgets and verification methods.

**Prerequisites:** Quantum mechanics, Hamiltonians, and many body physics

**Assessment:** Simulation error, model truncation, observables, and classical verification

### D07T01 — Digital Hamiltonian simulation

Digital simulation approximates Hamiltonian evolution with a programmable sequence of gates. The comparison should include accuracy, sparsity, simulation time, and compilation cost.

- Trotter formulas
- error bounds
- interaction picture
- sparse Hamiltonians
- time dependent evolution

### D07T02 — Analog quantum simulation

Analog simulators engineer a physical Hamiltonian to approximate a target model. Calibration and validation are especially important when universal digital corrections are unavailable.

- Hamiltonian engineering
- cold atoms
- trapped ions
- spin models
- simulator calibration

### D07T03 — Quantum lattice and spin models

Lattice and spin models provide structured many body targets. Geometry, interactions, symmetry, and observable selection specify the actual simulation problem.

- Ising models
- Heisenberg models
- Hubbard models
- phase diagrams
- frustration

### D07T04 — Quantum thermal states

Thermal state algorithms prepare or characterize Gibbs states and finite temperature observables. Mixing, equilibration, and energy normalization can dominate costs.

- Gibbs sampling
- thermalization
- imaginary time evolution
- partition functions
- finite temperature observables

### D07T05 — Quantum dynamics and scrambling

Scrambling and transport characterize how information and operators spread through a system. Measured correlators need interpretation that accounts for noise and finite size.

- OTOCs
- operator spreading
- transport
- many body localization
- dynamical phase transitions

### D07T06 — Lattice gauge theory simulation

Gauge simulation encodes fields subject to local constraints. Truncation and gauge violation must be assessed along with gate noise and observable accuracy.

- Gauge constraints
- truncation
- real time dynamics
- link encodings
- digital gauge simulation

## D08 — Quantum chemistry and materials

Electronic structure is a major application area because quantum states can encode correlated wavefunctions. Practical workflows require molecular mappings, controlled errors, and meaningful classical comparisons.

**Prerequisites:** Electronic structure, second quantization, and quantum algorithms

**Assessment:** Basis set, active space, energy accuracy, mapping, and measured observables

### D08T01 — Electronic structure algorithms

Electronic structure algorithms estimate properties of interacting electrons in selected basis sets. The physical accuracy target and active space define the application.

- Ground states
- active spaces
- basis sets
- correlated wavefunctions
- energy accuracy

### D08T02 — Fermion to qubit mappings

Fermion mappings translate anticommutation relations into qubit operators. Operator locality, symmetry reduction, and measurement cost depend on the mapping.

- Jordan Wigner
- Bravyi Kitaev
- parity mappings
- symmetry tapering
- fermionic encodings

### D08T03 — Excited states and spectroscopy

Excited state and response algorithms target spectra beyond the ground state. State preparation and transition observable estimation are separate resource demands.

- Subspace methods
- equation of motion
- response functions
- transition amplitudes

### D08T04 — Quantum chemistry resource estimates

Chemistry estimates translate an algorithm into logical and physical resources for a chosen accuracy. Molecular basis, code assumptions, and factory architecture should be stated.

- Logical qubits
- T counts
- accuracy targets
- molecule selection
- runtime models

### D08T05 — Quantum materials and condensed matter

Materials applications study strongly correlated phases and properties. A proposed workflow should identify observables that inform a materials decision and compare against suitable classical methods.

- Strong correlation
- superconductivity models
- defects
- electronic phases
- materials observables

## D09 — Variational and hybrid quantum methods

Variational algorithms optimize a parameterized circuit with a classical loop. Trainability, sampling, noise, and optimizer costs must be evaluated along with the objective value.

**Prerequisites:** Optimization, parameterized circuits, and measurement statistics

**Assessment:** Ansatz bias, trainability, shot cost, noise, and optimizer convergence

### D09T01 — Variational quantum eigensolvers

VQE minimizes measured energy with a parameterized circuit and classical optimization. Ansatz bias, shot noise, and optimizer convergence all affect the result.

- VQE
- energy measurement
- UCC ansatz
- adaptive ansatz
- optimizer selection

### D09T02 — Quantum approximate optimization

QAOA alternates cost evolution with a mixing operation to search for good solutions. Depth, constraints, parameter selection, and classical baseline quality determine the assessment.

- QAOA
- mixers
- alternating operators
- graph problems
- approximation ratios

### D09T03 — Ansatz design and expressibility

An ansatz defines the states reachable during optimization. Expressibility alone is not a guarantee of trainability or low resource cost.

- Hardware efficient circuits
- problem inspired circuits
- symmetry preservation
- entangling structure

### D09T04 — Barren plateaus and trainability

Barren plateau analyses study exponentially small or concentrated gradients. The conclusion depends on circuit ensembles, cost locality, initialization, and noise.

- Gradient concentration
- depth dependence
- local costs
- initialization
- noise induced plateaus

### D09T05 — Quantum gradients and optimization

Gradient rules and optimization methods control the classical loop around a quantum circuit. Measurement complexity and gradient variance must accompany iteration counts.

- Parameter shift rules
- finite differences
- stochastic gradients
- quantum natural gradients

### D09T06 — Quantum imaginary time evolution

Imaginary time methods project toward low energy states through nonunitary evolution or approximations. Normalization and locality assumptions determine what is implementable.

- QITE
- variational imaginary time
- imaginary time filtering
- normalization
- thermal preparation

## D10 — Quantum machine learning

Quantum machine learning includes learning with quantum circuits and learning about quantum systems. Input encoding, sample complexity, classical comparisons, and trainability determine whether a method is useful.

**Prerequisites:** Machine learning, statistics, and quantum circuits

**Assessment:** Input encoding, sample complexity, generalization, and classical comparison

### D10T01 — Quantum data encoding

Data encodings specify how classical or quantum inputs enter a circuit. State preparation cost and repeated access must be included in learning complexity.

- Amplitude encoding
- angle encoding
- basis encoding
- data reuploading
- state preparation costs

### D10T02 — Quantum kernels

Quantum kernels estimate similarities using quantum feature maps. Expressive features can still yield concentrated kernels or costly training measurements.

- Fidelity kernels
- projected kernels
- kernel concentration
- support vector machines
- feature maps

### D10T03 — Quantum neural networks and classifiers

Quantum neural networks use trainable quantum circuits as learning models. Their evaluation requires held out data, noise analysis, and comparable classical baselines.

- Variational classifiers
- quantum convolution
- circuit architectures
- supervised learning

### D10T04 — Quantum generative models

Generative quantum models represent or sample data distributions. Training objectives, sample quality, likelihood access, and the data source define the task.

- Born machines
- quantum GANs
- sampling models
- generative benchmarks
- likelihood estimation

### D10T05 — Quantum reinforcement learning

Quantum reinforcement learning studies quantum resources in sequential decision tasks. Coherent access to an environment is a substantial assumption and is not always physically available.

- Agents
- policies
- value functions
- environment access
- exploration
- speedup assumptions

### D10T06 — Quantum learning theory

Quantum learning theory analyzes sample complexity and generalization under explicit learning models. Results differ for classical data, quantum examples, and unknown quantum states.

- PAC models
- sample complexity
- generalization
- learnability
- quantum examples

### D10T07 — Machine learning for quantum systems

Machine learning can assist calibration, control, characterization, and decoding of quantum hardware. This direction can be useful without claiming a speedup from a quantum learning model.

- Control optimization
- calibration models
- learned decoders
- state classification
- scientific discovery

## D11 — Optimization and operations research

Quantum optimization includes annealing, variational methods, and algorithms with provable guarantees. Application results should report feasible solutions and comparisons to strong classical solvers.

**Prerequisites:** Optimization, constraint modeling, and algorithm analysis

**Assessment:** Feasibility, approximation quality, embedding overhead, and solver baselines

### D11T01 — Combinatorial optimization

Combinatorial methods encode discrete decisions and constraints into quantum workflows. Feasibility, approximation quality, and problem size must be reported.

- MaxCut
- satisfiability
- graph coloring
- constraint satisfaction
- approximation guarantees

### D11T02 — Quantum semidefinite programming

Quantum SDP solvers use structured access to matrices and constraints. Their advantage depends on sparsity, rank, input models, and the required output.

- Matrix access
- feasibility
- trace constraints
- solver accuracy
- oracle costs

### D11T03 — Quantum scheduling and routing

Routing and scheduling applications combine difficult constraints with discrete optimization. Penalties and embedding can create substantial overhead or infeasible solutions.

- Vehicle routing
- job shop scheduling
- logistics
- constraints
- feasibility repair

### D11T04 — Quantum portfolio and financial estimation

Financial algorithms include estimation, pricing, and portfolio models. Model calibration, input access, error tolerances, and real computational costs determine relevance.

- Portfolio optimization
- option pricing
- risk estimation
- Monte Carlo
- data costs

### D11T05 — Quantum optimization benchmarks

Optimization benchmarking compares solution quality, runtime, and scaling against strong classical solvers. A quantum label or a favorable small instance is insufficient evidence of advantage.

- Classical baselines
- scaling
- solution quality
- wall time
- statistical uncertainty

## D12 — Superconducting qubit hardware

Superconducting circuits combine microwave control, cryogenics, fabrication, and readout. Device coherence and gate fidelity must be distinguished from logical error performance.

**Prerequisites:** Microwave circuits, cryogenics, and solid state physics

**Assessment:** Coherence, leakage, crosstalk, fabrication variation, and system wiring

### D12T01 — Transmon and circuit QED

Transmons reduce charge sensitivity through circuit design and couple to microwave resonators. Coherence, anharmonicity, coupling, and control tradeoffs shape performance.

- Josephson junctions
- anharmonicity
- dispersive coupling
- charge noise
- resonators

### D12T02 — Flux and fluxonium qubits

Flux based circuits use magnetic flux and specialized inductive elements to define qubit transitions. Sweet spots and device parameters affect both noise and control.

- Flux bias
- superinductors
- sweet spots
- tunneling
- circuit design

### D12T03 — Superconducting gates and couplers

Couplers and entangling gates control interactions between superconducting qubits. Gate error, residual coupling, leakage, and spectator effects require joint calibration.

- Cross resonance
- controlled phase
- parametric gates
- tunable coupling
- leakage

### D12T04 — Superconducting readout

Dispersive readout infers a qubit state from a coupled resonator response. Measurement speed, fidelity, backaction, and multiplexing compete.

- Dispersive measurement
- Purcell filters
- parametric amplifiers
- multiplexing
- assignment errors

### D12T05 — Cryogenic circuits and packaging

Cryogenic packaging delivers signals while removing heat and controlling electromagnetic environments. System scaling includes wiring, thermal budgets, and electronics placement.

- Dilution refrigeration
- microwave wiring
- interposers
- thermal budgets
- cryogenic electronics

### D12T06 — Superconducting fabrication and loss

Fabrication and materials affect loss, disorder, yield, and device uniformity. A scalable process must control interfaces as well as individual junction properties.

- Surface loss
- materials interfaces
- junction yield
- quasiparticles
- process control

## D13 — Trapped ion quantum computing

Ion processors use internal states coupled through collective motion. Scaling requires high quality gates, optical control, shuttling, and modular interconnects.

**Prerequisites:** Atomic physics, optics, and motional dynamics

**Assessment:** Gate fidelity, mode management, optical stability, and transport cost

### D13T01 — Ion traps and architectures

Ion trap architectures confine and address charged atoms used as qubits. Trap geometry, motional modes, and modular organization affect scaling.

- Paul traps
- Penning traps
- surface traps
- ion chains
- modular architectures

### D13T02 — Ion entangling gates

Entangling ion gates typically use shared motion or geometric phases. Mode crowding, heating, optical noise, and pulse design determine achievable fidelity.

- Molmer Sorensen gates
- geometric phase gates
- motional modes
- pulse shaping

### D13T03 — Ion transport and QCCD

QCCD architectures move ions between operation regions. Transport must preserve quantum information and manage motional excitation and cooling.

- Junction transport
- sympathetic cooling
- motional excitation
- trap scheduling

### D13T04 — Ion optical control and readout

Laser control and fluorescence readout link ion states to optical hardware. Addressing errors, stability, collection efficiency, and crosstalk matter.

- Laser addressing
- fluorescence
- optical stability
- crosstalk
- state preparation

### D13T05 — Photonic links between ions

Photonic links generate entanglement between distant ion modules. Heralding rates, photon collection, indistinguishability, and memory lifetime constrain execution.

- Remote entanglement
- collection optics
- heralding
- frequency conversion
- modular links

## D14 — Neutral atom and Rydberg processors

Neutral atom arrays offer reconfigurable geometries and interactions controlled by optical fields. Coherent gates, atom loss, rearrangement, and measurement determine computational reliability.

**Prerequisites:** Atomic physics, optical trapping, and interacting spin models

**Assessment:** Atom loading, loss, gate error, geometry, and measurement backaction

### D14T01 — Optical tweezer arrays

Optical tweezers create reconfigurable arrays of individual atoms. Loading and rearrangement establish the geometry used by later simulation or gate operations.

- Loading
- rearrangement
- trapping
- addressing
- geometry control

### D14T02 — Rydberg blockade gates

Rydberg excitation enables strong interactions and blockade gates. Decay, motion, pulse control, and blockade imperfections determine gate error.

- Blockade interactions
- excitation errors
- entangling gates
- pulse design
- decay

### D14T03 — Neutral atom analog simulation

Neutral atom simulators realize programmable interacting spin systems. Interpretation depends on the realized Hamiltonian and measured observable rather than array size alone.

- Rydberg Hamiltonians
- spin systems
- many body dynamics
- programmable geometry

### D14T04 — Neutral atom error correction

Neutral atom error correction combines logical encodings with atom transport and syndrome measurement. Atom loss and measurement backaction require platform aware analysis.

- Logical arrays
- atom loss
- syndrome extraction
- transport
- transversal gates

### D14T05 — Alkaline earth atomic qubits

Alkaline earth and related atoms offer nuclear spin and optical transition resources. Storage, control, readout, and metastable state lifetimes must be considered together.

- Nuclear spins
- optical clocks
- metastable states
- qubit storage
- control transitions

## D15 — Spin qubits and semiconductor platforms

Spin qubits connect quantum control to semiconductor materials and nanofabrication. Scaling involves disorder, charge noise, wiring, exchange coupling, and readout.

**Prerequisites:** Semiconductor physics, spin dynamics, and nanofabrication

**Assessment:** Disorder, charge noise, valley structure, readout, and array wiring

### D15T01 — Silicon spin qubits

Silicon spin qubits combine quantum dot confinement with magnetic or electrical control. Valley structure, isotopic purity, and disorder are key device variables.

- Quantum dots
- valley splitting
- spin orbit coupling
- enriched silicon
- gate fidelity

### D15T02 — Germanium hole qubits

Germanium hole systems provide strong electric control through spin orbit coupling. Strain, confinement, charge noise, and interactions determine operation quality.

- Heavy holes
- strong spin orbit coupling
- planar dots
- strain
- electric control

### D15T03 — Donor qubits

Donor processors use localized electron and nuclear spins in semiconductors. Placement, hyperfine control, and readout interfaces affect scalability.

- Phosphorus donors
- nuclear spins
- hyperfine coupling
- atom placement
- donor readout

### D15T04 — Spin readout and exchange gates

Exchange operations couple nearby spins, while spin to charge conversion enables readout. Control uniformity and charge noise connect gate and measurement performance.

- Pauli blockade
- charge sensing
- exchange coupling
- resonator readout
- spin to charge conversion

### D15T05 — Spin shuttling and scalable arrays

Shuttling and array control seek to connect spin qubits beyond immediate neighbors. Transport coherence and wiring complexity become system level constraints.

- Electron transport
- crossbar control
- long range coupling
- arrays
- cryogenic interfaces

## D16 — Photonic quantum computing

Photonic approaches encode information in optical modes and use interference, measurements, and sometimes nonlinear interactions. Loss and resource generation are central engineering constraints.

**Prerequisites:** Quantum optics, interference, and photodetection

**Assessment:** Loss, indistinguishability, source rate, detector efficiency, and resource overhead

### D16T01 — Linear optical computation

Linear optics uses interference, measurement, and ancillary photons for computation. Probabilistic operations require resource accounting and feed forward.

- KLM
- interferometers
- photon counting
- postselection
- feed forward

### D16T02 — Boson sampling

Boson sampling samples distributions produced by indistinguishable particles passing through an optical network. Loss, distinguishability, and classical simulation affect hardness claims.

- Permanent estimation
- Gaussian boson sampling
- distinguishability
- loss
- classical simulation

### D16T03 — Integrated quantum photonics

Integrated photonics places optical components on chips. Loss, phase stability, fabrication variation, and coupling to sources and detectors determine usable performance.

- Waveguides
- interferometer meshes
- phase shifters
- material platforms
- packaging

### D16T04 — Single photon sources and detectors

Photon sources and detectors supply and measure optical quantum resources. Efficiency, purity, timing, and indistinguishability directly influence system scale.

- Heralded sources
- quantum dots
- SNSPDs
- number resolution
- efficiency

### D16T05 — Photonic cluster and fusion computing

Fusion based schemes combine smaller entangled states into computational resources. Loss tolerance and resource factory overhead are central design questions.

- Fusion gates
- graph states
- resource factories
- loss tolerance
- multiplexing

### D16T06 — Squeezing and Gaussian optics

Gaussian optics controls continuous variable modes with squeezing and linear transformations. Non Gaussian resources determine capabilities beyond Gaussian simulation.

- Squeezed states
- optical quadratures
- Gaussian transformations
- homodyne detection

## D17 — Other qubit platforms and transduction

Additional platforms offer different routes to coherence, control, and connectivity. Quantum transduction connects devices that operate at different physical frequencies.

**Prerequisites:** Solid state or molecular physics and quantum control

**Assessment:** Platform specific evidence, scalability, conversion efficiency, and added noise

### D17T01 — Diamond NV centers

NV centers combine electronic and nuclear spins with optical interfaces in diamond. Their computing and sensing uses should be distinguished when reading application claims.

- Electronic spins
- nuclear registers
- optical interfaces
- spin control
- fabrication

### D17T02 — Silicon carbide defects

Silicon carbide hosts optically addressable defects compatible with semiconductor fabrication. Coherence and interface properties depend on defect species and material quality.

- Color centers
- divacancies
- spin photon interfaces
- coherence
- integration

### D17T03 — Topological superconducting devices

Majorana proposals seek protected operations using topological superconductivity. Device observations, zero mode interpretation, and demonstrated logical operations require separate evidence.

- Zero mode evidence
- parity measurement
- braiding proposals
- poisoning
- experimental ambiguity

### D17T04 — Molecular and nuclear spin processors

Molecular and NMR approaches manipulate coupled spin registers. Ensemble demonstrations can teach control and algorithms while facing distinct scalability limits.

- NMR
- molecular qubits
- ensemble control
- scalability limitations
- spin registers

### D17T05 — Quantum transduction

Transducers convert quantum information between physical frequencies or platforms. Conversion efficiency and added noise jointly determine whether a link is useful.

- Microwave to optical conversion
- efficiency
- added noise
- piezoelectricity
- optomechanics

## D18 — Control calibration and noise characterization

Control engineering links physical devices to reliable operations. A noise model should be measured and tested rather than assumed to describe all operating regimes.

**Prerequisites:** Control theory, stochastic processes, and experimental statistics

**Assessment:** Model identification, robustness, drift, calibration effort, and correlated noise

### D18T01 — Optimal quantum control

Optimal control searches for pulses that implement target transformations under constraints. Robustness to parameter errors and hardware bandwidth should be tested.

- GRAPE
- CRAB
- bandwidth constraints
- robust pulse design
- control landscapes

### D18T02 — Dynamical decoupling

Dynamical decoupling suppresses selected environmental couplings through pulse sequences. Finite pulse errors and noise spectra limit its effectiveness.

- Pulse sequences
- filter functions
- noise spectra
- randomized decoupling
- storage protection

### D18T03 — Quantum noise spectroscopy

Noise spectroscopy infers environmental fluctuations from controlled quantum probes. The reconstruction depends on filter functions and assumptions about noise statistics.

- Filter functions
- spectral reconstruction
- correlated noise
- non Gaussian noise

### D18T04 — Leakage crosstalk and correlated errors

Leakage and correlated errors violate simple independent Pauli models. Detection, reset, and system context are essential for realistic reliability estimates.

- Leakage detection
- spectator errors
- spatial correlation
- temporal drift
- coherent errors

### D18T05 — Automated quantum calibration

Automated calibration estimates and updates control parameters from measurements. Drift, latency, identifiability, and calibration cost affect closed loop performance.

- Closed loop optimization
- drift tracking
- parameter estimation
- scheduling
- calibration transfer

## D19 — Quantum error correction codes

Error correction encodes logical information into larger physical systems and extracts error syndromes without directly measuring the logical state. Code performance depends on the physical error model and decoder.

**Prerequisites:** Pauli operators, circuits, and coding theory

**Assessment:** Code distance, check structure, physical noise, syndrome extraction, and decoding

### D19T01 — Stabilizer and CSS codes

Stabilizer and CSS constructions specify logical subspaces through commuting checks. Syndrome measurement must reveal error information without revealing the logical state.

- Pauli stabilizers
- CSS construction
- syndrome extraction
- distance
- logical operators

### D19T02 — Surface and toric codes

Surface and toric codes use structured local checks and topological logical operators. Thresholds depend on the noise and syndrome circuit model.

- Planar patches
- toric boundaries
- syndrome circuits
- thresholds
- defects

### D19T03 — Quantum LDPC codes

Quantum LDPC codes aim for sparse checks and improved encoding efficiency. Required connectivity, measurement circuits, and decoding are important implementation constraints.

- Sparse checks
- hypergraph products
- lifted products
- bivariate bicycle codes
- connectivity

### D19T04 — Bosonic error correction

Bosonic codes encode a logical system into oscillator states. Photon loss, finite energy, state preparation, and syndrome extraction determine protection.

- Cat codes
- GKP codes
- binomial codes
- oscillators
- photon loss

### D19T05 — Subsystem and color codes

Subsystem and color codes offer alternative check and logical gate structures. Gauge choices and measurement schedules affect both error correction and computation.

- Gauge fixing
- Bacon Shor
- gauge color codes
- transversal structure
- local checks

### D19T06 — Erasure and biased noise codes

Tailored codes exploit information about erasures or noise bias. Their benefit can disappear if detection or bias assumptions fail.

- Loss detection
- XZZX codes
- biased dephasing
- erasure conversion
- tailored decoding

## D20 — Fault tolerance and logical operations

Fault tolerance ensures that errors during correction and computation do not spread uncontrollably. Logical gates and routing must be evaluated with the entire correction cycle.

**Prerequisites:** Quantum error correction and logical circuits

**Assessment:** Logical error budgets, gate factories, connectivity, decoder latency, and runtime

### D20T01 — Thresholds and logical error scaling

Threshold analyses determine when larger encodings can suppress logical error. Finite distance performance and realistic correlations are needed for engineering decisions.

- Threshold theorems
- pseudothresholds
- finite size scaling
- correlated noise
- logical error budgets

### D20T02 — Magic state distillation

Magic state factories produce resources for non Clifford logical gates. Distillation yield, scheduling, and physical volume can dominate a large computation.

- T factories
- distillation protocols
- acceptance rates
- factory scheduling
- space time cost

### D20T03 — Lattice surgery

Lattice surgery implements logical parity operations through changing code boundaries. Routing and time steps must be included in algorithm mapping.

- Parity measurements
- patch merging
- patch splitting
- logical routing
- surgery scheduling

### D20T04 — Transversal gates and code switching

Transversal gates and code switching manage logical operations while limiting error spread. Universality restrictions motivate combining multiple methods.

- Eastin Knill limits
- gauge fixing
- code conversion
- logical Clifford gates

### D20T05 — Fault tolerant resource estimation

Resource estimation turns logical circuits into physical hardware and runtime requirements. Error budgets, code distance, connectivity, and factory assumptions should be explicit.

- Physical qubits
- logical qubits
- T depth
- runtime
- code distance
- architectural assumptions

### D20T06 — Quantum error decoding

Decoders infer likely errors from noisy syndrome data. Accuracy must be evaluated together with throughput, latency, and robustness to model mismatch.

- Matching
- belief propagation
- union find
- neural decoders
- latency
- streaming inference

## D21 — Error mitigation and near term reliability

Error mitigation changes estimators or experiments to reduce bias without providing the full protection of a fault tolerant encoding. Sampling overhead and assumptions must be reported.

**Prerequisites:** Noise channels, statistical estimation, and circuit execution

**Assessment:** Estimator bias, variance, model mismatch, calibration drift, and shot overhead

### D21T01 — Zero noise extrapolation

Zero noise extrapolation fits results measured at increased noise to estimate a lower noise limit. Extrapolation introduces variance and model dependent bias.

- Noise scaling
- folding
- regression
- bias
- variance
- extrapolation failure

### D21T02 — Probabilistic error cancellation

Probabilistic cancellation represents an inverse noise process through weighted sampling. Reliable channel knowledge and sampling overhead limit applicability.

- Quasiprobabilities
- channel learning
- sampling overhead
- model mismatch

### D21T03 — Readout error mitigation

Readout mitigation adjusts observed outcome statistics using a measurement error model. Correlated errors and calibration drift can invalidate simple assignment matrices.

- Assignment matrices
- correlated readout
- unfolding
- scalable calibration

### D21T04 — Symmetry verification and postselection

Symmetry checks reject or reweight outcomes that violate a known constraint. Acceptance probability and postselection bias must be reported.

- Conserved quantities
- acceptance rates
- bias
- verification checks

### D21T05 — Virtual distillation and purification

Virtual distillation uses multiple copies or related estimators to suppress some mixed state errors. Coherent errors and measurement costs remain relevant.

- Multiple copies
- purity estimation
- coherent errors
- measurement cost

## D22 — Characterization verification and benchmarks

Characterization measures device behavior; verification tests specified claims; benchmarking compares workloads. Each answers a different question and needs an appropriate uncertainty model.

**Prerequisites:** Quantum measurements, estimation, and statistics

**Assessment:** Identifiability, confidence intervals, trust assumptions, and workload definition

### D22T01 — Quantum state and process tomography

Tomography reconstructs a state or channel from informationally complete data. Reconstruction method, confidence, and physical constraints affect the estimate.

- Informational completeness
- reconstruction
- compressed sensing
- confidence regions

### D22T02 — Randomized benchmarking

Randomized benchmarking estimates average error behavior through randomized sequences. Interpreting the fitted decay requires checking gate dependence and noise assumptions.

- Clifford sequences
- interleaved benchmarking
- cycle benchmarking
- gate dependence

### D22T03 — Gate set tomography

Gate set tomography jointly estimates operations and preparation and measurement errors. Gauge freedom means some fitted quantities are not uniquely identifiable.

- Self consistency
- gauge freedom
- SPAM
- long sequence experiments

### D22T04 — Classical shadows

Classical shadows use randomized measurements to predict many observables. Sample requirements depend on the measurement ensemble and target observable family.

- Random measurements
- observable prediction
- sample complexity
- derandomization

### D22T05 — Quantum volume and application benchmarks

System benchmarks summarize performance on specified circuit or application families. Different metrics are complementary and do not supply a universal ranking.

- Quantum volume
- mirror circuits
- CLOPS
- application performance
- statistical comparison

### D22T06 — Verification and quantum certification

Verification and certification test a precise state or computation claim under a trust model. Protocol guarantees need to be read together with device assumptions.

- Interactive verification
- state certification
- self testing
- trusted measurements

## D23 — Software programming and compilation

Quantum software translates a problem into executable circuits and measured results. Compiler decisions should preserve semantics while adapting operations to hardware constraints.

**Prerequisites:** Programming, compiler concepts, and circuit semantics

**Assessment:** Semantic preservation, target constraints, verification, and reproducibility

### D23T01 — Quantum programming languages

Programming languages express quantum operations alongside classical computation. Control flow, type safety, and provider execution models determine practical capabilities.

- Q sharp
- Qiskit
- Cirq
- functional languages
- type systems
- quantum control flow

### D23T02 — Quantum intermediate representations

Intermediate representations support compilation and interchange across tools. Semantics and classical control must survive translation between representations.

- OpenQASM
- QIR
- MLIR
- classical control
- interoperability

### D23T03 — Quantum circuit synthesis

Circuit synthesis decomposes target transformations into allowed operations. Approximation accuracy and target gate set determine circuit size.

- Unitary decomposition
- Clifford T synthesis
- arithmetic circuits
- gate minimization

### D23T04 — Qubit mapping and routing

Placement and routing adapt logical circuits to hardware connectivity. Inserted operations change depth, noise exposure, and execution cost.

- Placement
- SWAP insertion
- topology constraints
- scheduling
- crosstalk awareness

### D23T05 — Quantum compiler optimization

Compiler optimizations simplify circuits or exploit device characteristics. Semantic correctness and the validity of a noise objective should be checked independently.

- Rewrite rules
- commutation
- cancellation
- approximate synthesis
- noise aware passes

### D23T06 — Quantum software testing and formal methods

Testing and formal methods address errors in quantum programs and compilation. Assertions, equivalence, and statistical testing have different guarantees.

- Assertions
- equivalence checking
- program logics
- property tests
- debugging

## D24 — Classical simulation and hybrid systems

Classical simulators support development, verification, and baselines. Their scalability depends on entanglement, circuit structure, precision, and memory bandwidth.

**Prerequisites:** Numerical linear algebra, parallel computing, and circuit structure

**Assessment:** Memory, entanglement, precision, communication, and comparison to hardware

### D24T01 — State vector and density matrix simulation

State vector simulation tracks amplitudes, while density matrix simulation tracks mixed states. Memory grows exponentially and differs substantially between these representations.

- Memory scaling
- distributed state vectors
- mixed states
- precision
- GPU execution

### D24T02 — Tensor network simulation

Tensor network methods exploit circuit structure and limited entanglement. Bond dimensions and contraction order control practical cost.

- MPS
- PEPS
- contraction order
- bond dimension
- circuit contraction

### D24T03 — Stabilizer circuit simulation

Stabilizer simulation efficiently handles Clifford operations and suitable states. Non Clifford extensions require additional resources or approximation.

- Gottesman Knill
- tableau methods
- Clifford circuits
- non Clifford extensions

### D24T04 — Quantum GPU and HPC integration

GPU and distributed HPC methods accelerate selected classical simulation operations. Memory bandwidth, communication, and precision determine real performance.

- Accelerators
- distributed memory
- kernels
- HPC scheduling
- numerical validation

### D24T05 — Hybrid quantum classical workflows

Hybrid workflows coordinate classical processing with quantum execution. Batching, data movement, scheduling, and asynchronous control affect end to end cost.

- Batching
- asynchronous jobs
- optimization loops
- data movement
- heterogeneous computing

## D25 — Architecture cloud and distributed computing

Architecture combines qubits, classical control, compilation, and communication into a system. Distributed designs must include entanglement costs, synchronization, and failures.

**Prerequisites:** Quantum hardware, compilation, and distributed systems

**Assessment:** Connectivity, scheduling, communication, queueing, and complete system cost

### D25T01 — Quantum processor architecture

Processor architecture combines connectivity, instruction execution, control, and packaging. The best design depends on the workload and error correction strategy.

- Connectivity
- modularity
- instruction sets
- control planes
- co design

### D25T02 — Distributed quantum computing

Distributed computation uses entanglement or remote operations across processors. Partitioning and communication overhead must be included in scaling claims.

- Remote gates
- partitioning
- entanglement consumption
- synchronization
- latency

### D25T03 — Quantum cloud execution

Cloud execution provides remote access and job orchestration for quantum devices. Queue delays, device changes, and preserved experiment metadata affect reproducibility.

- Queues
- job orchestration
- access models
- reproducibility
- provider abstraction

### D25T04 — Quantum circuit cutting

Circuit cutting reconstructs a larger circuit from smaller experiments and classical postprocessing. Sampling overhead can grow rapidly with the number and type of cuts.

- Wire cutting
- gate cutting
- reconstruction
- shot overhead
- partitioning

### D25T05 — Quantum memory architecture

Quantum memories preserve states for later operations or communication. Lifetime, retrieval efficiency, fidelity, and interface compatibility determine their role.

- Storage fidelity
- memory lifetime
- interfaces
- multiplexing
- logical memory

## D26 — Quantum networks and communication

Quantum networking distributes quantum states or entanglement between nodes. Protocols and hardware must account for loss, timing, storage, and classical coordination.

**Prerequisites:** Quantum channels, entanglement, and networking

**Assessment:** Loss, memory lifetime, heralding, synchronization, and capacity assumptions

### D26T01 — Quantum teleportation

Teleportation transfers a state using shared entanglement, measurements, and classical messages. It does not transmit usable information faster than light.

- Bell measurements
- classical feed forward
- fidelity
- network teleportation

### D26T02 — Quantum repeaters

Repeaters extend entanglement distribution beyond direct transmission limits. Rates depend on memories, losses, purification or coding, and coordination.

- Heralding
- purification
- error corrected repeaters
- rate loss tradeoffs

### D26T03 — Entanglement distribution and routing

Entanglement routing allocates links and swapping operations to network tasks. Probabilistic success and memory decoherence require different metrics from ordinary packet routing.

- Entanglement swapping
- routing metrics
- scheduling
- multipath distribution

### D26T04 — Quantum internet protocols

Quantum network protocols coordinate physical links, entanglement, and applications. Layer interfaces must represent limited and consumable quantum resources.

- Link layers
- network stacks
- resource management
- control planes
- application interfaces

### D26T05 — Quantum communication capacity

Channel capacities quantify asymptotic communication rates under specified assistance. Classical, quantum, and private capacities answer different coding questions.

- Classical capacity
- quantum capacity
- private capacity
- coding theorems

## D27 — Quantum cryptography and security

Quantum cryptography uses quantum systems for security tasks, while post quantum cryptography uses classical algorithms designed to resist quantum attacks. Their mechanisms and deployment requirements are different.

**Prerequisites:** Cryptographic definitions, probability, and quantum algorithms

**Assessment:** Threat model, composable security, finite size effects, and implementation attacks

### D27T01 — Quantum key distribution

QKD establishes secret keys under a stated device and security model. Finite size analysis, authentication, and side channels are part of practical security.

- BB84
- decoy states
- finite keys
- composable security
- implementation attacks

### D27T02 — Device independent cryptography

Device independent protocols infer security from observed nonlocal correlations. Loophole closure, randomness, and finite statistics are demanding requirements.

- Bell violations
- loophole closure
- entropy accumulation
- security assumptions

### D27T03 — Blind and delegated computing

Blind computing hides some information about a delegated task, while verifiable protocols also test correctness. Client capability and server trust distinguish protocols.

- Hidden circuits
- verifiable delegation
- trap protocols
- server trust

### D27T04 — Quantum cryptanalysis

Quantum cryptanalysis studies attacks on classical or quantum security systems. Algorithmic complexity and physical fault tolerant cost should both be considered.

- Factoring attacks
- discrete logarithms
- Grover search
- resource estimates

### D27T05 — Post quantum cryptography interface

Post quantum cryptography uses classical schemes intended to resist quantum attacks. It is included as a security interface to quantum computing, not as a quantum hardware protocol.

- Lattice schemes
- code based schemes
- hash signatures
- migration
- threat models

### D27T06 — Quantum random number generation

Quantum random number generators estimate and extract entropy from measured quantum processes. Security depends on the source model and the amount of trusted hardware.

- Entropy sources
- extractors
- certification
- device trust
- finite size analysis

## D28 — Quantum sensing and metrology

Sensing is an adjacent quantum technology rather than a synonym for computation. It is included because control, estimation, and quantum resources connect it to computing research.

**Prerequisites:** Quantum mechanics, parameter estimation, and experimental physics

**Assessment:** Sensitivity, bandwidth, noise, trust, and whether bounds are attainable

### D28T01 — Quantum parameter estimation

Quantum estimation studies how states and measurements encode unknown parameters. Bounds do not automatically imply an experimentally achievable estimator.

- Quantum Fisher information
- Cramer Rao bounds
- multiparameter estimation
- estimators

### D28T02 — Quantum magnetometry

Magnetometry estimates fields using spin or other quantum probes. Sensitivity must be quoted with bandwidth, integration time, and spatial resolution.

- NV sensing
- spin ensembles
- sensitivity
- bandwidth
- spatial resolution

### D28T03 — Atomic clocks and interferometry

Clocks and interferometers exploit controlled phase accumulation for precise measurement. Stability, systematic shifts, and entangled probe preparation set limits.

- Clock stability
- atom interferometers
- squeezing
- systematic errors

### D28T04 — Quantum imaging and illumination

Quantum imaging and illumination use correlations for specified detection or imaging tasks. Advantages depend on the noise, receiver, and comparison model.

- Correlation imaging
- illumination receivers
- resolution
- noise
- classical comparisons

### D28T05 — Quantum sensing with error correction

Error corrected sensing seeks to protect useful signal accumulation while rejecting noise. The signal and noise operators must satisfy relevant conditions.

- Logical sensors
- noise filtering
- Hamiltonian conditions
- ancilla assistance

## D29 — Specialized scientific applications

Scientific applications must specify the observable or decision task and account for preparation and readout. These categories organize exploratory work without claiming universal practical advantage.

**Prerequisites:** Relevant scientific model and quantum algorithm prerequisites

**Assessment:** Observable definition, model error, preparation, readout, and domain validation

### D29T01 — Quantum algorithms for high energy physics

High energy applications include field simulation and selected analysis tasks. Physical observable, truncation, and classical verification define the computational problem.

- Field theory
- scattering
- event analysis
- neutrinos
- gauge dynamics

### D29T02 — Quantum algorithms for nuclear physics

Nuclear applications target states, reactions, and observables of interacting particles. Model spaces and controlled physical approximations accompany circuit errors.

- Nuclear structure
- reactions
- few body systems
- interactions
- spectroscopy

### D29T03 — Quantum algorithms for numerical integration

Integration algorithms often build on amplitude estimation. The input oracle and required precision determine whether a query benefit survives end to end accounting.

- Quadrature
- Monte Carlo
- dimensionality
- oracle access
- precision

### D29T04 — Quantum algorithms for engineering

Engineering applications connect quantum algorithms to discretized models and inverse tasks. Conditioning and output extraction can dominate the workflow.

- Finite elements
- fluid models
- differential equations
- inverse problems
- discretization

### D29T05 — Quantum algorithms for biology and drug discovery

Biological and drug discovery proposals often depend on quantum chemistry subproblems. Chemical accuracy and downstream biological validation should be assessed separately.

- Molecular energies
- docking proposals
- chemistry pipelines
- validation
- biological relevance

## D30 — Education research practice and ecosystem

Research practice includes learning, reproducing results, documenting limitations, and judging evidence. Roadmaps and standards describe plans or interfaces rather than proof that a device meets them.

**Prerequisites:** Basic quantum computing and critical reading

**Assessment:** Source quality, environment records, fair baselines, versioning, and full system cost

### D30T01 — Quantum computing education

Education resources teach prerequisites, conceptual models, and executable experiments. Curriculum scope and assessment quality determine how to use them.

- Prerequisites
- laboratories
- assessments
- visual explanations
- curriculum design

### D30T02 — Quantum computing surveys and roadmaps

Surveys and roadmaps organize a fast moving field and identify bottlenecks. Roadmap milestones are plans rather than demonstrated capabilities.

- Hardware surveys
- algorithm surveys
- milestones
- uncertainty
- scaling bottlenecks

### D30T03 — Quantum standards and interoperability

Standards and interfaces support consistent terminology and tool interoperability. The applicable version and scope should be recorded when used.

- Terminology
- interfaces
- reference models
- benchmarking definitions
- interoperability

### D30T04 — Quantum reproducibility and research methodology

Reproducible research records environments, circuits, parameters, datasets, and uncertainty. Fair benchmarks also preserve strong classical baselines and complete cost accounting.

- Experiment records
- seeds
- environments
- baselines
- statistical reporting

### D30T05 — Quantum economics and sustainability

Economics and sustainability studies evaluate full system cost and energy use. Cooling, classical support, runtime, and utilization matter alongside quantum device operation.

- Cooling energy
- runtime cost
- total system accounting
- scaling
- economic assumptions
