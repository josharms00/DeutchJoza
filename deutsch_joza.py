from qiskit import QuantumCircuit
import numpy
import matplotlib.pyplot as plt
from q_Helper import q_Helper
from qiskit.visualization import plot_histogram

qh = q_Helper()

circuit = QuantumCircuit(4, 2)

circuit.x(2)
#circuit.x(3)

def identity(c):
	c.cx(2, 0)
	c.cx(3, 1)

	return c

circuit = identity(circuit)

circuit.measure([0, 1], [0, 1])

# circuit.draw(output='mpl')

result, counts = qh.do_job(circuit, 100)

plot_histogram([counts])

plt.show()