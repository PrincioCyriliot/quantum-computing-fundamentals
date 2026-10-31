from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# 1. Créer un circuit quantique avec 1 qubit et 1 bit classique
circuit = QuantumCircuit(1, 1)

# 2. Appliquer la porte de Hadamard (superposition)
circuit.h(0)

# 3. Mesurer le qubit
circuit.measure(0, 0)

# Afficher le schéma en mode texte dans la console
print("--- Schéma de ton circuit quantique ---")
print(circuit)

# Sauvegarder le schéma en image (circuit.png)
fig = circuit.draw(output='mpl')
fig.savefig('circuit.png', bbox_inches='tight')
plt.close(fig)
print("\n[INFO] L'image 'circuit.png' a été générée avec succès !")

# 4. Simuler l'exécution sur 1000 essais
simulator = AerSimulator()
job = simulator.run(circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\n--- Résultats de la simulation (sur 1000 essais) ---")
print("Combien de fois on a tiré 0 et combien de fois on a tiré 1 :", counts)