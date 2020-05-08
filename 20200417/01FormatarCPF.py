# CPF-Binario.pdf
# Faça um programa que recebe um inteiro representando os números de um CPF e imprime ele formatado.
# Por exemplo, se o número for 12345678910, seu programa deverá imprimir 123.456.789-10.

cpf = int(input("Digite os números de um cpf: "))

i = 11
while i >= 1:

    digitoCPF = cpf % 10
    cpf = cpf // 10

    if i == 11:
        cpfFormatado = str(digitoCPF)
    elif i == 10:
        cpfFormatado = "-" + str(digitoCPF) + cpfFormatado
    elif i % 3 == 0 and i <= 6:
        cpfFormatado = str(digitoCPF) + "." + cpfFormatado
    else:
        cpfFormatado = str(digitoCPF) + cpfFormatado
    i = i - 1

print("CPF Formatado: ", cpfFormatado)
