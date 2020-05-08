# CPF-Binario.pdf
# Desenvolva um programa em Python que calcula os dígitos verificadores de um CPF.
# Seu programa recebe como entrada um inteiro de 9 dígitos.

cpf = int(input("Digite os primeiros 9 digitos do cpf: "))

cpfRecebido = cpf

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

        cpf = cpfRecebido * 10 + digVerificador
        cpfRecebido = cpf
        j = 1
        soma = 0

    elif j == 11:

        resto = soma % 11
        if resto < 2:
            digVerificador = 0
        else:
            digVerificador = 11 - resto

        cpf = cpfRecebido * 10 + digVerificador

    j = j + 1

print("CPF completo:", cpf)
