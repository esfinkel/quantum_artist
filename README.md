# quantum_artist

By Elisabeth Finkel, Kshama Malavalli, and Gayathrini Premawardhana (all B.A. Cornell University, 2021)

## Usage

`pip install -r requirements.txt`

Run `artist.py`. Comment/uncomment `DATA_SOURCE` (at top of file) to select whether you want to use our pre-collected real quantum data (in `real_data.py`) or dynamically generate new data using a fake quantum backend (`in four_bit_quantum_rng.py`).

You can also generate new data from real quantum hardware yourself, if you want. In that case you must follow the instructions at https://qiskit.org/documentation/install.html to cache your qiskit access token, if you've never done so, and uncomment `provider =...` in `four_bit_quantum_rng.py`.

## Project Statement

The objective of the “random drawer” is to create art using the results from a quantum RNG. Because there will be noisy data that we will not be getting rid of, this data will also be used to draw (this part of the drawing will essentially be a visual representation of noise).

Implementation: Make a random number generator that returns 0’s and 1’s. Then use these random numbers to make decisions on where/how to draw lines and shapes on a python canvas. We’ll end up with abstract art!

Applications: Can help create works of abstract art, fantasy coastline maps that support story-telling, etc.

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
