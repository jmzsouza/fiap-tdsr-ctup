# lista8CT-2020.pdf
# Exercício 2
# Escreva uma função que recebe como parâmetro um inteiro positivo n 
# e retorna uma lista preenchida com n números inteiros aleatórios entre 1 e 1000.

import random

def geraListaEleatoria(n):

    lista = []
    while n > 0:
        lista.append(random.randint(1, 1001))
        n = n - 1
    return lista

n = int(input("Digite uma quantidade de entrada de números: ")) 
listaRandomica = geraListaEleatoria(n)
print(listaRandomica)


