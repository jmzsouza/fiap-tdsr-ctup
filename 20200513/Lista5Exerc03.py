# lista5CT-2020.pdf
# Exercício 3
# Usando a função que verifica se um número é perfeito ou não,
# escreva um algoritmo que mostra todos os números perfeitos no intervalo de 1 a 10000 (dez mil).

from Lista5Funcoes import *

num = 1
while num <= 10000:
    if ehPerfeito(num):
        print(num)
    num = num + 1
