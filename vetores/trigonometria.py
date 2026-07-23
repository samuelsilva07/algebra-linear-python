from vetores.produtos import produtoInterno
from moduloVetor import modulo

def sen(vetor):
    return vetor[1] / modulo(vetor) # coordenada y

def cos(vetor):
    return vetor[0] / modulo(vetor) # coordenada x

def senAngulo(vetor1, vetor2):
    return produtoInterno(vetor1, vetor2) / (modulo(vetor1) * modulo(vetor2))

def cosAngulo(vetor1, vetor2):
    return modulo(produtoInterno(vetor1, vetor2)) / produtoInterno(modulo(vetor1) * modulo(vetor2))