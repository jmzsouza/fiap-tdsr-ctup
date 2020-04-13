#lista3CT2020.pdf
#Exercício 2
#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se houve um empate.

valor = input("Digite um número: ")
numA = int(valor)
valor = input("Digite outro número: ")
numB = int(valor)

if numA == numB:
    print("Os numero são iguais.")
else:
    if numA > numB:
        print(numA, "é o maior.")
    else:
        print(numB, "é o maior.")
