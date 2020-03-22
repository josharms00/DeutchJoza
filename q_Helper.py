from qiskit import(execute, Aer) 
import matplotlib.pyplot as plt
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor 
from qiskit.tools.visualization import plot_bloch_multivector 
from qiskit.visualization import plot_histogram

# class to set up and run quantum circuits
class q_Helper(object):

	# initialize the provider and load account
	def __init__(self, first=False):
		if first:
			IBMQ.save_account(open("token.txt", "r").read())
		else:
			IBMQ.load_account()

		self.provider = IBMQ.get_provider("ibm-q")

	# does all the work for executing a job for a circuit
	# returns the results along with the counts
	def do_job(self, circuit, shots, backend="ibmq_qasm_simulator", local_sim=False):
		if local_sim:
			self.provider = Aer.get_backend("qasm_simulator")
		else:
			self.backend = self.provider.get_backend(backend)

		self.job = execute(circuit, backend=self.backend, shots=shots)

		self.result = self.job.result()

		return self.result, self.result.get_counts()

	# returns the backend with the least amount of queued jobs
	# can also filter the ones that have less than a specific 
	# amount of qubits
	def least_queued(self, qubits=0):

		least_back = self.provider.get_backend("ibmq_16_melbourne")
		prev_back = least_back

		for backend in self.provider.backends():
			try:
				# check jobs and amount of qubits 
				if prev_back.status().pending_jobs > backend.status().pending_jobs and len(backend.properties().qubits) >= qubits:
					least_back = backend

				prev_back = backend
			except:
				continue
				
		return least_back