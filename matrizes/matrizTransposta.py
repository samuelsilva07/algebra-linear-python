import numpy as np
# from numpy.random import default_rng # gera arrays com valores aleatórios

def transposta(matriz):
    matrizTransposta = np.zeros((matriz.shape[1], matriz.shape[0]))
    for i in range(matriz.shape[1]):
        for j in range(matriz.shape[0]):
            matrizTransposta[i][j] = matriz[j][i]
    return matrizTransposta.astype(np.int64)

# matriz = default_rng().integers(5, size=(4, 3))
# print("\n-----------------------------------\nMatriz original: \n")
# print(matriz, f"\n\nDimensão: {matriz.shape}")
# matrizTransposta = transposta(matriz)
# print("\n-----------------------------------\nMatriz transposta: \n")
# print(matrizTransposta, f"\n\nDimensão: {matrizTransposta.shape}")

# m2 = m1.transpose()
# print("\n-----------------------------------\Matriz transposta: \n")
# print(m2, f"\n\nDimensão: {m2.shape}")