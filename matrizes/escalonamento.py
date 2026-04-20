import numpy as np
import math
from numpy.random import default_rng

# mmc: math.lcm()

def gauss(matriz):
    for i in range(matriz.shape[0]):
        for j in range (i + 1, matriz.shape[0]):
            if (matriz[i][i] != 0) and (matriz[j][i] !=0):
                # mmc: fator multiplicativo para que as linhas tenham o mesmo valor na coluna "inicial"
                mmc = math.lcm(matriz[i][i], matriz[j][i])

                # multiplicação das linhas para subtração de valores de mesmo módulo
                linha = np.zeros(shape=(matriz.shape[1],), dtype="int64")
                if matriz[i][i] != mmc:
                    linha = matriz[i] * (mmc / matriz[i][i]).astype("int64")
                else: 
                    linha = matriz[i]

                if matriz[j][i] != mmc:
                    matriz[j] *= (mmc / matriz[j][i]).astype("int64")

                print(f"Linhas: {linha} | {matriz[j]}")
                
                # zera todos os elementos abaixo do pivô
                matriz[j] -= linha

            print("\n-----------------------------------\nMatriz atual: \n")
            print(matriz, f"\n\nDimensão: {matriz.shape}")
    
    # for i in range(matriz.shape[0]):
    #     if matriz[i][i] != 0:
    #         divisor = math.lcm()
    #         matriz[i] /= divisor
    return matriz

matriz = default_rng().integers(1, 10, size=(3, 3))
print("\n-----------------------------------\nMatriz 1: \n")
print(matriz, f"\n\nDimensão: {matriz.shape}")
matrizEscalonada = gauss(matriz)
print("\n-----------------------------------\nMatriz escalonada: \n")
print(matrizEscalonada, f"\n\nDimensão: {matrizEscalonada.shape}")

