# lista5CT-2020.pdf
# Exercício 2
# Usando a função do exercício anterior,
# escreva um programa que imprime os 100 primeiros números ímpares começando do número 2.

from Lista5Funcoes import *

num = 2
contador = 0

while contador < 100:
    if ehprimo(num):
        print(num)
        contador = contador + 1
    num = num + 1