# CPF-Binario.pdf
# Escreva um algoritmo que recebe um número na base decimal para a base binária

numeroDecimal = int(input("Digite numero decimal: "))

resto = numeroDecimal % 2
numeroDecimal = numeroDecimal // 2
inverter = 0

while numeroDecimal != 0:
    resto = numeroDecimal % 2
    numeroDecimal = numeroDecimal // 2
    inverter = inverter * 10 + resto

print(int(inverter))
