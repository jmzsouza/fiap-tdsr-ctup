# lista5CT-2020.pdf
# Exercício 1
# Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros positivos dele:
# o 1 e o próprio n.
# Escreva uma função que recebe um inteiro n e retorna o valor True se n é primo ou False se ele não for primo.

from Lista5Funcoes import *

numero = int(input("Digite um número: "))

if ehprimo(numero):
    print("É primo!")
else:
    print("Não é primo!")