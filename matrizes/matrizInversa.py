import numpy as np
from matrizAdjunta import adjunta
from determinante import detLaplace
from multiplicacaoMatrizes import multMatrizes
from numpy.random import default_rng

def inversa(matriz):
    return adjunta(matriz) / detLaplace(matriz)

# matriz = default_rng().integers(10, size=(3, 3))
matriz = np.array([[1, 2, 3],
                   [2, 5, 3],
                   [1, 0, 8]])
print("\n-----------------------------------\nMatriz: \n")
print(matriz, f"\n\nDimensão: {matriz.shape}")
matrizInversa = inversa(matriz)

matrizAdjunta = adjunta(matriz)
print("\n-----------------------------------\nMatriz Adjunta: \n")
print(matrizAdjunta, f"\n\nDimensão: {matrizAdjunta.shape}")

determinanteMatriz = detLaplace(matriz)
print(f"\n-----------------------------------\nDeterminante = {determinanteMatriz}")

print("\n-----------------------------------\nMatriz Inversa: \n")
print(matrizInversa, f"\n\nDimensão: {matrizInversa.shape}")


print("\n-----------------------------------\nConferindo (matriz original x matriz inversa): \n")
identidade = multMatrizes(matriz, matrizInversa)
print(identidade, f"\n\nDimensão: {identidade.shape}")