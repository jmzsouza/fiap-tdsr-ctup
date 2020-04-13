# lista3CT2020.pdf
# Exercício 7
#  A raiz quadrada é uma operação que apenas aceita números positivos.
#  Escreva um algoritmo que lê um número qualquer e retorna a raiz quadrada desse número se possível.
#  Use a função math.sqrt(<numero>) para calcular a raiz quadrada em Python. Note que, para usar essa função, você terá que importar o módulo math antes.

import math

num = float(input("Digite um número: "))

if num >= 0:
    raiz = math.sqrt(num)
    print("A raiz quadrada de: " + str(num) + " é: " + str(raiz))
else:
    print(num + " não é um número positivo")