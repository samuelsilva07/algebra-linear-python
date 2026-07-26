import numpy as np
from vetores.norma import normaEuclidiana
from vetores.produtos import produtoInterno
from sistemas.escalonamento import gauss

def fatoracaoQR(matriz: np.ndarray):
    Q = np.zeros(shape=matriz.shape)
    R = np.zeros(shape=matriz.shape)
    for j in range(matriz.shape[0]):    # para cada coluna da matriz
        somatorio = np.zeros(matriz.shape[1]) # criação do vetor que representa a direção retirada da matriz

        for i in range(j):
            R[i][j] = produtoInterno(matriz[:,j], Q[:,i])
            somatorio += R[i][j] * Q[:,i]  # somatório representa a direção retirada de cada coluna da matriz, para que o vetor seja ortogonal

        u = matriz[:,j] - somatorio   # o vetor u recebe a coluna j da matriz principal sem a direção retirada
        R[j][j] = normaEuclidiana(u)      # os elementos da diagonal principal de R recebem a norma do vetor u
        Q[:,j] = u / R[j][j]  # normalização do vetor para adicioná-lo a matriz Q

    return Q, R

def fatoracaoLU(matriz: np.ndarray):
    U = gauss(matriz)
    L = np.identity(n=matriz.shape[0])
    # for i in range(1, matriz.shape[0]):
    #     for j in range(i):

    return L, U

def fatoracaoLDU(matriz: np.ndarray):
    L, U = fatoracaoLU(matriz)
    D = np.eye(U)
    for i in range(matriz.shape[0]):
        U[i][i] = 1
    return L, D, U