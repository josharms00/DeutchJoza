from qiskit import QuantumCircuit
import numpy
import matplotlib.pyplot as plt
from q_Helper import q_Helper
from qiskit.visualization import plot_histogram

qh = q_Helper()

circuit = QuantumCircuit(2, 2)

# balanced functions

# will always return the same as the input 
def identity(c):
	c.cx(1, 0)

	return c

# will retrun the negated version of the input
def negate(c):
	c.x(1)

	return identity(c)

# constant functions

# will always make the bit 0
def constant_0(c):
	return c

# will always make the bit 1
def constant_1(c):
	c.x(0)

	return c

# output bit
circuit.x(0)

# input bit
circuit.x(1)

# both bits need to start in a superposition
circuit.h(0)
circuit.h(1)

circuit = negate(circuit)

circuit.h(0)
circuit.h(1)

# if the function is constant then the meesurement will be |11> if balanced it will be |01>
circuit.measure([0, 1], [0, 1])

# circuit.draw(output='mpl')

result, counts = qh.do_job(circuit, 100)

plot_histogram([counts])

plt.show()