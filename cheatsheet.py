import numpy
import qiskit as q 
import matplotlib
from qiskit import IBMQ

# only need to run one time
#IBMQ.save_account(open("token.txt", "r").read()) # get your account token from the saved file

IBMQ.load_account() # load user account

provider = IBMQ.get_provider("ibm-q") # choose quantum computer provider

circuit = q.QuantumCircuit(2, 2) # 2 quibits, 2 classical

circuit.x(0) # not gate on quibit 0: 00 => 10

circuit.cx(0, 1) # cnot gate first argument is control bit, second is input
				 # 10 => 11

circuit.measure([0, 1], [0, 1]) # measure qubit states arguments are what classical bits
								# the qubits will map to. In this case qubit 0 == cbit 0

circuit.draw(output='mpl', filename='my_circuit.png') # this function will save the diagram of the circuit

print(circuit) # alternatively you can print out diagram to the console
