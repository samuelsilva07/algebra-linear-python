import numpy as np
# from numpy.random import default_rng

def cofator(matriz, linha, coluna):
    if matriz.shape[0] != matriz.shape[1]:
        print("Não é possível encontrar o cofator dessa matriz.\n")

    matriz = np.delete(matriz, linha, axis=0)
    matriz = np.delete(matriz, coluna, axis=1)

    sinal = pow(-1, exp=(linha + coluna))
    if (matriz.shape[0] == matriz.shape[1] == 1):
        return int(sinal * matriz[0][0])
    return int(sinal * round(np.linalg.det(matriz)))


# matriz = default_rng().integers(10, size=(3, 3))
# print("\n-----------------------------------\nMatriz: \n")
# print(matriz, f"\n\nDimensão: {matriz.shape}")
# for i in range(matriz.shape[0]):
#     for j in range(matriz.shape[1]):
#         print(f"\nC{i+1}{j+1} = {cofator(matriz, i, j)}")

