from math import sqrt 

def normaFrobenius(matriz):
  soma = 0
  for elemento in matriz.flat:
    soma += elemento ** 2
  return sqrt(soma)

def norma1(matriz):
  soma_colunas = []
  for coluna in matriz.T:     # neste caso, utilizei a matriz transposta para acessar as colunas de modo mais fácil
    soma_colunas.append(sum(coluna))
  return max(soma_colunas)

def normaInfinito(matriz):
  soma_linhas = []
  for linha in matriz:
    soma_linhas.append(sum(linha))
  return max(soma_linhas)