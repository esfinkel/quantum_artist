import random, time

def two_qubit_rng(entries=1000, noise=0.025):
    random.seed(time.time())
    vals = []
    for _ in range(entries):
        entangled = (random.random() > noise)
        fst = int(random.random() > 0.5)
        snd = (fst if entangled else 1-fst)
        val = str(fst) + str(snd)
        vals.append(val)
    return vals

print(two_qubit_rng())