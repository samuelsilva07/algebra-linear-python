import numpy as np
from numpy.random import default_rng # gera arrays com valores aleatórios

def multMatrizes(matriz1, matriz2):
    if matriz1.shape[1] == matriz2.shape[0]:
        quantidadeProdutos = matriz1.shape[1] 
        linhasMatrizMult = matriz1.shape[0]
        colunasMatrizMult = matriz2.shape[1]
        matrizMult = np.zeros((linhasMatrizMult, colunasMatrizMult))

        for i in range(linhasMatrizMult):
            for j in range(colunasMatrizMult):
                for k in range(quantidadeProdutos):
                    matrizMult[i][j] += (matriz1[i][k] * matriz2[k][j])

        return matrizMult.astype(np.int64)
    return "Não é possivel multiplicar as matrizes."

# m1 = default_rng().integers(5, size=(5, 3))
# m2 = default_rng().integers(5, size=(3, 4))
# print("\n-----------------------------------\nMatriz 1: \n")
# print(m1, f"\n\nDimensão: {m1.shape}")
# print("\n-----------------------------------\nMatriz 2: \n")
# print(m2, f"\n\nDimensão: {m2.shape}")
# matrizMult = multMatrizes(m1, m2)
# print("\n-----------------------------------\nProduto: \n")
# print(matrizMult, f"\n\nDimensão: {matrizMult.shape}")