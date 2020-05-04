# lista4CT2020.pdf
# Exercício 9
# Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de tempo em meses t,
# escreva um algoritmo que calcula o valor final em dinheiro se d ficar aplicado a taxa de juros j durante t meses.

montante = float(input("Informe um montante em dinheiro: R$ "))
jurosMensal = float(input("Informe uma taxa de juros mensal: "))
tempoEmMeses = int(input("Informe um perído de tempo em meses: "))

contaMeses = 1

while contaMeses <= tempoEmMeses:
    montante = montante + (montante * (jurosMensal / 100))
    contaMeses = contaMeses + 1

print("O valor final é: {:.2f}".format(montante))