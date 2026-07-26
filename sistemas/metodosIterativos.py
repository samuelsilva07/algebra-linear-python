import numpy as np

def jacobi(sistema: np.ndarray, iteracoes: int):
    chute_inicial = np.zeros(sistema.shape[0])
    for _ in range(iteracoes):
        aproximacao = np.zeros(sistema.shape[0])
        for i in range(sistema.shape[0]):
            somatorio = 0
            for j in range(sistema.shape[1] - 1):
                if j != i:
                    somatorio += sistema[i][j] * chute_inicial[j]
            aproximacao[i] = (sistema[i][-1] - somatorio) / sistema[i][i]
        chute_inicial = aproximacao[::]

    return aproximacao

def gaussSeidel(sistema: np.ndarray, iteracoes: int):
    aproximacao = np.zeros(sistema.shape[0], dtype=float)
    for _ in range(iteracoes):
        for i in range(sistema.shape[0]):
            somatorio = 0
            for j in range(sistema.shape[1] - 1):
                if j != i:
                    somatorio += sistema[i][j] * aproximacao[j]
            aproximacao[i] = (sistema[i][-1] - somatorio) / sistema[i][i]

    return aproximacao

sistema = np.array([[10, 2, 1, 7],
           [1, 5, 1, 8],
           [2, 1, 6, 9]])

print(gaussSeidel(sistema, 20))

