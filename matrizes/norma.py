from math import sqrt 

def normaFrobenius(matriz):
  return sqrt(sum([elemento ** 2 for elemento in matriz.flat]))

def norma1(matriz):
  return max([coluna for coluna in matriz.T])

def normaInfinito(matriz):
  return max([linha for linha in matriz])
