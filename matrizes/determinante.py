import numpy as np
from cofator import cofator
from numpy.random import default_rng

def detSarrus(matriz):
    if matriz.shape[0] == 1 and matriz.shape[0] == 1:
        return matriz[0][0]  

    # diagonal positiva

    somaDiagonal1 = 0
    valorInicialColuna = 0

    while valorInicialColuna < matriz.shape[1]:
        coluna = valorInicialColuna
        produtoDiagonal = 1
        
        for linha in range(matriz.shape[0]):
            produtoDiagonal *= matriz[linha][coluna]
            coluna += 1

            if coluna == matriz.shape[1]:
                coluna = 0

        somaDiagonal1 += produtoDiagonal
        valorInicialColuna += 1

    # diagonal negativa
    
    somaDiagonal2 = 0
    valorInicialColuna = matriz.shape[1] - 1

    while valorInicialColuna >= 0:
        coluna = valorInicialColuna
        produtoDiagonal = 1
        
        for linha in range(matriz.shape[0]):
            produtoDiagonal *= matriz[linha][coluna]
            coluna -= 1

            if coluna < 0:
                coluna = matriz.shape[1] - 1

        somaDiagonal2 += produtoDiagonal
        valorInicialColuna -= 1
        
    print(f"Soma diagonal 1 = {somaDiagonal1}\nSoma diagonal 2 = {somaDiagonal2}\n")

    return somaDiagonal1 - somaDiagonal2
       
def detLaplace(matriz): # função baseada no método de Laplace
    if matriz.shape[0] == 1 and matriz.shape[0] == 1:
        return matriz[0][0]    
    
    soma = 0
    for linha in range(matriz.shape[0]):
        valor = matriz[linha][0]
        soma = soma + (valor * cofator(matriz, linha, 0))

    return soma

# matriz = default_rng().integers(1, 5, size=(3, 3))
# print("\n-----------------------------------\nMatriz: \n")
# print(matriz, f"\n\nDimensão: {matriz.shape}")
# determinanteMatriz = detSarrus(matriz)
# print(f"\n-----------------------------------\nDeterminante = {determinanteMatriz}")
