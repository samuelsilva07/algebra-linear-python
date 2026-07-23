import numpy as np
from math import sqrt

def norma1(vetor):
  modulo_valores = []
  for elemento in vetor:
    modulo_valores.append(abs(elemento))
  return sum(modulo_valores)

def normaEuclidiana(vetor):
  soma = 0
  for elemento in vetor:
    soma += elemento ** 2
  return sqrt(soma)

def normaInfinito(vetor):
  modulo_valores = []
  for elemento in vetor:
    modulo_valores.append(abs(elemento))
  return max(modulo_valores)

def normaP(vetor, p):
  soma = 0
  for elemento in vetor:
    soma += abs(elemento) ** p
  return soma ** (1 / p)

def normaInduzida(vetor, matriz):
    matriz_produto = np.linalg.matmul(matriz, vetor)
    produto_interno = np.dot(vetor.T, matriz_produto)
    return sqrt(produto_interno)