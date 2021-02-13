# with thanks to Russell Huffman state of https://medium.com/qiskit/rothko-inspired-generative-quantum-art-6f34ca9d17cb
# for providing the code for this part of the project

# Importing standard Qiskit libraries and configuring account
from collections import defaultdict
from qiskit import QuantumCircuit, execute, Aer, IBMQ, QuantumRegister, ClassicalRegister
from qiskit.test.mock import FakeVigo
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()

##################################################

# paste qiskit code from website here
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.t(qreg_q[0])
circuit.s(qreg_q[1])
circuit.swap(qreg_q[1], qreg_q[2])

circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])

#################################################

# pick a device to run on
# backend = provider.get_backend('ibmq_qasm_simulator')
backend = FakeVigo()

# Execute the circuit on the backend
job = execute(circuit, backend, shots=1000, memory=True)

# Grab results from the job
result = job.result()

#get individual shots
outputArray = result.get_memory()

res = defaultdict(int)
for x in outputArray:
    res[x] += 1

# print(outputArray)
print(res)
