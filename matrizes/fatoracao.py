import numpy as np
from vetores.norma import normaEuclidiana
from vetores.produtos import produtoInterno

def fatoracaoQR(matriz):
    Q = np.zeros(shape=matriz.shape)
    R = np.zeros(shape=matriz.shape)
    for j in range(matriz.shape[0]):    # para cada coluna da matriz
        somatorio = np.zeros(matriz.shape[1]) # criação do vetor que representa a direção retirada da matriz

        for i in range(j):
            somatorio += produtoInterno(matriz[:,j], Q[:,i]) * Q[:,i]  # somatório representa a direção retirada de cada coluna da matriz, para que o vetor seja ortogonal
            R[i][j] = produtoInterno(matriz[:,j], Q[:,i])

        u = matriz[:,j] - somatorio   # o vetor u recebe a coluna j da matriz principal sem a direção retirada
        R[j][j] = normaEuclidiana(u)      # os elementos da diagonal principal de R recebem a norma do vetor u
        Q[:,j] = u / normaEuclidiana(u)  # normalização do vetor para adicioná-lo a matriz Q

    return Q, R