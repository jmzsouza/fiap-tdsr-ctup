# CPF-Binario.pdf
# Usando o algoritmo anterior, desenvolva um programa que verifica se um CPF é válido,
# seu programa recebe um long com 11 dígitos representando um CPF e verifica se ele é válido de acordo com a
# regra de formação apresentada.

cpf = int(input("Digite os números de um cpf: "))

cpfRecebido = cpf

cpf = cpf // 100
cpfSemVerificador = cpf

j = 2
soma = 0
digVerificador = 99
while j <= 11:
    digitoCPF = cpf % 10
    cpf = cpf // 10
    soma = soma + j * digitoCPF

    if digVerificador == 99 and j == 10:

        resto = soma % 11
        if resto < 2:
            digVerificador = 0
        else:
            digVerificador = 11 - resto

        cpf = cpfSemVerificador * 10 + digVerificador
        cpfSemVerificador = cpf
        j = 1
        soma = 0

    elif j == 11:

        resto = soma % 11
        if resto < 2:
            digVerificador = 0
        else:
            digVerificador = 11 - resto

        cpf = cpfSemVerificador * 10 + digVerificador

    j = j + 1

if cpf == cpfRecebido:
    print("O cpf {} é válido!".format(cpfRecebido))
else:
    print("O cpf {} é inválido!".format(cpfRecebido))
