import numpy as np
from math import sqrt

def norma1(vetor):
  return sum([abs(elemento) for elemento in vetor])

def normaEuclidiana(vetor):
  return sqrt(sum(elemento for elemento in vetor))

def normaInfinito(vetor):
  return max([abs(elemento) for elemento in vetor])

def normaP(vetor, p):
  return sum([abs(elemento) ** p for elemento in vetor]) ** (1 / p)

def normaInduzida(vetor, matriz):
    matriz_produto = np.linalg.matmul(matriz, vetor)
    produto_interno = np.dot(vetor.T, matriz_produto)
    return sqrt(produto_interno)