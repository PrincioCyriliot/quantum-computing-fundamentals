from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

#Creation du circuit quantique avec 2 qubits et 2 bits classiques
circuit = QuantumCircuit(2, 2)

#Porte de Hadamard sur le qubit 0 (qubit de depart)
circuit.h(0)

#Porte CNOT entre le qubit 0(contrôle) et le qubit 1 (cible)
circuit.cx(0, 1)

#Mesure des 2 qubits
circuit.measure([0,1],[0, 1])

#Simulation de l'execution sur 1000 essais
simulator = AerSimulator()
temp = simulator.run(circuit, shots=1000)
result = temp.result()
counts = result.get_counts(circuit)

print("----Résultats de l'intrication (État de Bell)----")
print(counts)
#print(type(counts))