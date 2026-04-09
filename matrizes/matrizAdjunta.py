import numpy as np
from matrizTransposta import transposta
from cofator import cofator
from numpy.random import default_rng

def adjunta(matriz):
    matrizAdjunta = np.zeros(shape=matriz.shape)
    for linha in range(matriz.shape[0]):
        for coluna in range(matriz.shape[1]):
            matrizAdjunta[linha][coluna] = cofator(matriz, linha, coluna)

    return transposta(matrizAdjunta)

# matriz = default_rng().integers(10, size=(3, 3))
# print("\n-----------------------------------\nMatriz: \n")
# print(matriz, f"\n\nDimensão: {matriz.shape}")

# matrizAdjunta = adjunta(matriz)
# print("\n-----------------------------------\nMatriz Adjunta: \n")
# print(matrizAdjunta, f"\n\nDimensão: {matrizAdjunta.shape}")
