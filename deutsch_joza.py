from qiskit import QuantumCircuit
import numpy
import matplotlib.pyplot as plt
from q_Helper import q_Helper
from qiskit.visualization import plot_histogram
import argparse

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

# will pick one based on user input
def choose_oracle_func(i, c):

	if i == 0: 
		return identity(c)
	elif i == 1: 
		return negate(c)
	elif i == 2:
		return constant_0(c)
	else:
		return constant_1(c)

def main():
	qh = q_Helper()

	legend = " 0: identity function \n 1: negation function \n 2: constant 0 function \n 3: constant 1 function \n exit: exit program"

	print(legend)

	inp = input("Please choose what function to test. \n")

	while(inp != "exit"):

		circuit = QuantumCircuit(2, 2)

		# output bit
		circuit.x(0)

		# input bit
		circuit.x(1)

		# both bits need to start in a superposition
		circuit.h(0)
		circuit.h(1)

		# choose what function to test
		circuit = choose_oracle_func(int(inp), circuit)

		circuit.h(0)
		circuit.h(1)

		# if the function is constant then the meesurement will be |11> if balanced it will be |01>
		circuit.measure([0, 1], [0, 1])

		# circuit.draw(output='mpl')

		result, counts = qh.do_job(circuit, 100)

		plot_histogram([counts])

		plt.show()

		print(legend)

		inp = input("Please choose what function to test next. \n")

if __name__ == '__main__':
    main()