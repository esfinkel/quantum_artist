import random, time

def two_qubit_rng(entries=1000, noise=0.025):
    '''Generate `entries` outputs simulating the Bell Circuit.
    The two qubits have the same value `1-noise` percent of the time.'''
    # seed the RNG so you get different results every time
    random.seed(time.time())
    vals = []
    for _ in range(entries):
        # decide now if the two qubits will have the same value
        # (simulating entanglement). This happens with probability `1-noise`.
        entangled = (random.random() > noise)
        # The first qubit is 0 or 1 with equal probability
        fst = int(random.random() > 0.5)
        # The second is the same as the first if they're entangled, and
        # (for simplicity) the opposite otherwise
        snd = (fst if entangled else 1-fst)
        # record the result
        val = str(fst) + str(snd)
        vals.append(val)
    return vals

res = two_qubit_rng()

# confirm that '00' and '11' happen almost-but-not-quite equally frequently, and that an appropriate amount of noise is present
print(res.count('00'), res.count('11'), res.count('10'))