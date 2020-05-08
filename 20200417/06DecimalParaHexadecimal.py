# CPF-Binario.pdf
# Escreva um algoritmo que recebe um número na base decimal para a base hexadecimal

numeroDecimal = int(input("Digite um número decimal: "))

resto = numeroDecimal % 16
numeroDecimal = numeroDecimal // 16
inverter = 0

while numeroDecimal != 0:

    resto = numeroDecimal % 16
    numeroDecimal = numeroDecimal // 16

    if resto == 10:
        valor = 'A'
    elif resto == 11:
        valor = 'B'
    elif resto == 12:
        valor = 'C'
    elif resto == 13:
        valor = 'D'
    elif resto == 14:
        valor = 'E'
    elif resto == 15:
        valor = 'F'
    else:
        valor = str(resto)

    inverter = inverter * 10 + resto

print(inverter)
