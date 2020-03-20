from qiskit import(QuantumCircuit, execute, Aer) 
import matplotlib.pyplot as plt
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor 
from qiskit.tools.visualization import plot_bloch_multivector 
from qiskit.visualization import plot_histogram

class q_Helper(object):

	def __init__(self, first=false):
		if first:
			IBMQ.save_account(open("token.txt", "r").read())
		else:
			IBMQ.load_account()

		self.provider = IBMQ.get_provider("ibm-q")

	def do_job(self, circuit, shots, backend="ibmq_qasm_simulator", local_sim=false):
		if local_sim:
			self.provider = Aer.get_backend("qasm_simulator")
		else:
			self.backend = self.provider.get_backend(backend)

		self.job = execute(circuit, backend=slef.backend, shots=shots)

		self.result = self.job.result()

		return self.result, self.result.get_counts()