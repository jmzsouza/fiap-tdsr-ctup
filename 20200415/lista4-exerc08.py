# lista4CT2020.pdf
# Exercício 8
# Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
# positivos dele: o 1 e o próprio n. Escreva um algoritmo que recebe um inteiro n e verifica se n é primo ou não.

num = int(input("Digite um número inteiro positivo: "))

divisor = 1
contDivisor = 0

if num > 1:

    while divisor <= num:
        if num % divisor == 0:
            contDivisor = contDivisor + 1
        divisor = divisor + 1

    if contDivisor == 2:
        print("O número {} é primo".format(num))

    else:
        print("O número {} não é primo".format(num))
else:
    print("O número {} não é primo".format(num))
