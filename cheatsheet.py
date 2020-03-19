import numpy
from qiskit import(QuantumCircuit, execute, Aer) # Aer handles the simulator
import matplotlib.pyplot as plt
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor # shows where the job is in the queue
from qiskit.visualization import plot_histogram

# only need to run one time
#IBMQ.save_account(open("token.txt", "r").read()) # get your account token from the saved file

IBMQ.load_account() # load user account

provider = IBMQ.get_provider("ibm-q") # choose quantum computer provider

circuit = QuantumCircuit(2, 2) # 2 quibits, 2 classical

circuit.x(0) # not gate on quibit 0: 00 => 10

circuit.cx(0, 1) # cnot gate first argument is control bit, second is input
				 # 10 => 11

circuit.h(0) # haddamard gate on qubit 0: 11 => (1/sqrt(2)|0> + 1/sqrt(2)|1>) X |1>. Where X is the tensor product

circuit.measure([0, 1], [0, 1]) # measure qubit states arguments are what classical bits
								# the qubits will map to. In this case qubit 0 == cbit 0

circuit.draw(output='mpl', filename='my_circuit.png') # this function will save the diagram of the circuit

# alternatively you can print out diagram to the console
# print(circuit) 

#backend = provider.get_backend("ibmq_16_melbourne") 	# choose which quantum computer to run the job on
backend = provider.get_backend("ibmq_qasm_simulator")	# can also use quantum simulator
#simulator = Aer.get_backend("qasm_simulator")			# run simulator locally

# queue the job up for that backend, shots is the amount of times to run the computation to 
# get more accurate results
job = execute(circuit, backend=backend, shots=100) 

result = job.result() # get results of measurement after the computation
counts = result.get_counts() # this returns the amount of times each state collapsed to when measured 

plot_histogram([counts]) # will plot distribution of results

plt.show() # display distribution plot