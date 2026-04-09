import numpy as np
from numpy.random import default_rng # gera arrays com valores aleatórios

def somaMatrizes(matriz1, matriz2):
    if (matriz1.shape == matriz2.shape):
        matrizSoma = np.zeros((linhas, colunas))
        for linha in matriz1.shape[0]:
            for coluna in matriz1.shape[1]:
                matrizSoma[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
        return matrizSoma.astype(np.int64)

linhas = int(input("Digite a quantidade de linhas das matrizes: "))
colunas = int(input("Digite a quantidade de colunas das matrizes: "))

# m1 = default_rng().integers(20, size=(linhas, colunas))
# m2 = default_rng().integers(20, size=(linhas, colunas))
# print("\n-----------------------------------\nMatriz 1: \n")
# print(m1)
# print("\n-----------------------------------\nMatriz 2: \n")
# print(m2)
# soma = somaMatrizes(m1, m2)
# print("\n-----------------------------------\nSoma: \n")
# # print(m1 + m2)
# print(soma)