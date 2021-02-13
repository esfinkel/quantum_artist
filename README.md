# quantum_artist

## Pertinent Files:

* artist.py

Reads in the data - either dynamically-generated from a fake backend, or the prerecorded data from a real backend.

Opens a gui window and draws the quantum art.

* artist1.py

Same concept, different art style. Uses fake backend data.

* four_bit_quantum_rng.py

Simulates our circuit on a fake backend (simulated quantum hardware). The simulation is designed to actual quantum computation, including the presence of noise (occasions when two entangled particles are measured as having un-entangled states).

`four_bit_quantum_rng` runs a large number of experiments and then outputs the measurements.

* graphics.py

Package we took from the internet. This file should be in the same directory as the programs running it.

* pseudo_rng.py

Pseudo RNG for 2 entangled qubits

* real_data.py

Resultant data of running our circuit 1000 times on a real quantum computer
