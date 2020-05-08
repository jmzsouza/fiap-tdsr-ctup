# CPF-Binario.pdf
# Escreva um algoritmo que recebe um número na base hexadecimal para a base decimal

numeroHexa = input("Informe um número em hexadecimal: ")

soma = 0
potencia = 1
i = len(numeroHexa) - 1
valor = 0

while i >= 0:
    carac = numeroHexa[i]

    if carac == 'A':
        valor = 10
    elif carac == 'B':
        valor = 11
    elif carac == 'C':
        valor = 12
    elif carac == 'D':
        valor = 13
    elif carac == 'E':
        valor = 14
    elif carac == 'F':
        valor = 15
    else:
        valor = int(carac)

    soma = soma + valor * potencia
    potencia = potencia * 16
    i = i - 1

print(soma)
