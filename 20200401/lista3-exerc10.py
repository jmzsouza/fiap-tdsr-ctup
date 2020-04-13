# lista3CT2020.pdf
# Exercício 10
# Uma equação de 2º grau é da forma: ax² + bx + c = 0, onde a != 0.
# Escreva um algoritmo que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível.
# Use a seguinte fórmula para resolver a equação:

import math

valorA = int(input("Digite um valor para A: "))
valorB = int(input("Digite um valor para B: "))
valorC = int(input("Digite um valor para C: "))

delta = valorB ** 2 - 4 * valorA * valorC

if valorA != 0:
    if delta > 0:
        x1 = (- valorB + math.sqrt(delta)) / (2 * valorA)
        x2 = (- valorB - math.sqrt(delta)) / (2 * valorA)
        print("\nO valor de delta..: " + str(delta) +
              "\nO valor da raiz x1: " + str(x1) +
              "\nO valor da raiz x2: " + str(x2))
    else:
        print("Não é possível realizar o calculo, o valor de delta deve ser positivo.")
else:
    print("Não é possível realizar o calculo, o número A deve ser diferente de 0.")