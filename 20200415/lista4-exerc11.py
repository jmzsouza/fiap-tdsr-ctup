# lista4CT2020.pdf
# Exercício 11
# No problema de verificar se um número é primo ou não resolvemos contando o número de divisores.
# Também podemos pensar em resolver este problema encontrando um divisor diferente de 1.
# Se tal divisor for o próprio n, significa que n é primo, caso contrário, dizemos que ele não é primo.
# Pensando nessa ideia, escreva um algoritmo que verifica se n é primo ou não.

num = int(input("Digite um número inteiro positivo: "))

divisor = 1
contDivisor = 0

if num > 1:

    while divisor <= num:
        if num % divisor == 0 and divisor != 1:
            contDivisor = contDivisor + 1
        divisor = divisor + 1

    if (divisor - 1) == num and contDivisor == 1:
        print("O número {} é primo".format(num))

    else:
        print("O número {} não é primo".format(num))
else:
    print("O número {} não é primo".format(num))