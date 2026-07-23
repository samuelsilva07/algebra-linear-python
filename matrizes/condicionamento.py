from norma import normaFrobenius
from matrizInversa import inversa

def condicionamento(matriz):
    return normaFrobenius(matriz) * normaFrobenius(inversa(matriz))