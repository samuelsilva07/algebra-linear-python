import math
import numpy as np

def modulo(vetor):
    soma = 0
    for valor in vetor:
        soma += pow(valor, 2)
    return math.sqrt(soma)
    
vetor = np.array([1, 3])
print(f"\n-----------------------------------\nVetor: {vetor}")
moduloVetor = modulo(vetor)
print(f"\n-----------------------------------\nProduto escalar: {moduloVetor}")