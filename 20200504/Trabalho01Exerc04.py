# TrabalhoComputationalThinking-2020.pdf
# Exercício 4
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o maior
# número inteiro que divide o número a e o número b.
# Faça, no papel, dois testes de mesa do seu algoritmo e envie como descrito no exercício anterior.

numA = int(input("Digite um número inteiro positivo A: "))
numB = int(input("Digite um número inteiro positivo B: "))

if numA > 0 and numB > 0:

    if numA > numB:
        maior = numA
        menor = numB
    else:
        maior = numB
        menor = numA

    resto = maior

    while resto != 0:
        resto = maior % menor
        maior = menor
        menor = resto

    print("O maior divisor comum entre ({}, {}) = {}".format(numA, numB, maior))

else:
    print("Informe apenas números maiores que 0!")