import numpy as np
from math import lcm, gcd 
from numpy.random import default_rng

# mmc: lcm()
# mdc: gcd()

def gauss(matriz: np.ndarray):
    for i in range(matriz.shape[0]):
        for j in range (i + 1, matriz.shape[0]):
            if (matriz[i][i] != 0) and (matriz[j][i] != 0):
                # mmc: fator multiplicativo para que as linhas tenham o mesmo valor na coluna "inicial"
                mmc = lcm(matriz[i][i], matriz[j][i])

                # multiplicação das linhas para subtração de valores de mesmo módulo
                linha = np.zeros(shape=(matriz.shape[1],), dtype=np.int64)
                if matriz[i][i] != mmc:
                    linha = matriz[i] * (mmc / matriz[i][i]).astype(np.int64)
                else: 
                    linha = matriz[i]

                if matriz[j][i] != mmc:
                    matriz[j] *= (mmc / matriz[j][i]).astype(np.int64)
                # print(f"Linhas: {linha} | {matriz[j]}")
                
                # zera todos os elementos abaixo do pivô
                matriz[j] -= linha
                
                # print("\n-----------------------------------\nMatriz atual: \n")
                # print(matriz, f"\n\nDimensão: {matriz.shape}")
    
    # reduz as linhas para suas formas "irredutíveis"
    for i in range(matriz.shape[0]):
        if matriz[i][i] != 0:
            divisor = gcd(*matriz[i])
            matriz[i] = (matriz[i] / divisor).astype(np.int64)
            if (all(valor <= 0 for valor in matriz[i])):
                matriz[i] = abs(matriz[i])
        

    return matriz
    

matriz = default_rng().integers(10, size=(3, 3))
print("\n-----------------------------------\nMatriz 1: \n")
print(matriz, f"\n\nDimensão: {matriz.shape}")
matrizEscalonada = gauss(matriz)
print("\n-----------------------------------\nMatriz escalonada: \n")
print(matrizEscalonada, f"\n\nDimensão: {matrizEscalonada.shape}")

