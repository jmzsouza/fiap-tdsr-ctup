# lista3CT2020.pdf
# Exercício 6
# Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

numA = int(input("Digite um número: "))
numB = int(input("Digite outro número: "))

if numA % numB == 0:
    print(str(numA) + " é divisível por " + str(numB))
else:
    print(str(numA) + " não é divisível por " + str(numB))
