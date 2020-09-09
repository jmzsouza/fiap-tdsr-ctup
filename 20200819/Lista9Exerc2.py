# lista9CT-Projeto-2020.pdf
# Exercício 2
# Faça uma função em Python que recebe uma lista e mistura o conteúdo dela, ou seja, troca os elementos de posição de forma aleatória.

import random

def mistura(lista):
    i = 0
    while i < 100:
        x = random.randint(0, len(lista))
        y = random.randint(0, len(lista))
        lista[x], lista[y] = lista[y], lista[x]
        i = i + 1
