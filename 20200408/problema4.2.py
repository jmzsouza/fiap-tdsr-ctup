# Problema 4.2: Dado um número inteiro positivo n, escreva um algoritmo que imprime a tabuada de n até o valor 10.

num = int(input("Digite um número: "))

i = 1
while i <= 10:
    print("{} x {} = {}".format(num, i, (num * i)))
    i = i + 1
