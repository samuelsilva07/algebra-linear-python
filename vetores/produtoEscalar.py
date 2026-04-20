import numpy as np
from numpy.random import default_rng

def produtoEscalar(vetor1, vetor2):
    produto = 0
    for i in range(vetor1.shape[0]):
        produto += (vetor1[i] * vetor2[i])
    return produto.astype(float)

v1 = np.array([1, 3])
v2 = np.array([5, 2])
print(f"\n-----------------------------------\nVetor 1: {v1}")
print(f"\n-----------------------------------\nVetor 2: {v2}")
vetorProduto = produtoEscalar(v1, v2)
print(f"\n-----------------------------------\nProduto escalar: {vetorProduto}")
# print(v1 + v2)