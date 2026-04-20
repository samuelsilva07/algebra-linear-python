import numpy as np
from numpy.random import default_rng

def somaVetores(vetor1, vetor2):
    if (vetor1.shape[1] == vetor2.shape[1] == 0):
        soma = np.zeros(2)
        for i in range(vetor1.shape[0]):
            soma[i] += (vetor1[i] + vetor2[i])
        return soma.astype(float)
    print("Não é possível somar vetores de dimensões diferentes")

v1 = np.array([1, 3])
v2 = np.array([5, 2])
print(f"\n-----------------------------------\nVetor 1: {v1}")
print(f"\n-----------------------------------\nVetor 2: {v2}")
vetorSoma = somaVetores(v1, v2)
print(f"\n-----------------------------------\nSoma: {vetorSoma}")
# print(v1 + v2)