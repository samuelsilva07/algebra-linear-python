import numpy as np
from cofator import cofator
from numpy.random import default_rng

def det(matriz): # função baseada no método de Laplace
    if matriz.shape[0] == 1 and matriz.shape[0] == 1:
        return matriz[0][0]    
    
    soma = 0
    for linha in range(matriz.shape[0]):
        valor = matriz[linha][0]
        soma = soma + (valor * cofator(matriz, linha, 0))

    return soma

# matriz = default_rng().integers(10, size=(3, 3))
# print("\n-----------------------------------\nMatriz: \n")
# print(matriz, f"\n\nDimensão: {matriz.shape}")
# determinanteMatriz = det(matriz)
# print(f"\n-----------------------------------\nDeterminante = {determinanteMatriz}")