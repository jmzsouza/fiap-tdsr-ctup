# TrabalhoComputationalThinking-2020.pdf
# Exercício 3
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o menor número inteiro
# que é múltiplo do número a e do número b. Neste exercício, você deverá validar as informações de entrada, ou seja,
# a e b devem ser número positivos. Faça, no papel, dois testes de mesa do seu algoritmo.
# Bata uma foto ou escaneie o teste de mesa feito no papel e anexe ao seu trabalho.

numA = int(input("Digite um número inteiro positivo A: "))
numB = int(input("Digite um número inteiro positivo B: "))

contA = 1
menorMultiplo = 0

if numA > 0 and numB > 0:

    if numA > numB:
        maior = numA
    else:
        maior = numB

    while contA <= maior and menorMultiplo == 0:
        multiploA = numA * contA
        contB = 1
        while contB <= maior and menorMultiplo == 0:
            multiploB = numB * contB
            if multiploA == multiploB:
                menorMultiplo = multiploB
            contB = contB + 1
        contA = contA + 1

else:
    print("Informe apenas números maiores que 0!")


print("O menor múltiplo comum entre ({}, {}) = {}! Porque? {} x {} = {} e {} x {} = {}."
      .format(numA, numB, menorMultiplo, numA, (contA - 1), multiploA, numB, (contB - 1), multiploB))



