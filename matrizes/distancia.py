from math import sqrt

def distancia(matriz1, matriz2):
    if matriz1.shape != matriz2.shape:
        print("As matrizes não possuem as mesmas dimensões!")
        return None

    dimensao = matriz1.shape
    soma = 0
    for linha in range(dimensao[0]):
        for coluna in range(dimensao[1]):
            diferenca = matriz1[linha][coluna] - matriz2[linha][coluna]
            soma += (diferenca ** 2)

    return sqrt(soma)