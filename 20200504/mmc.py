# TrabalhoComputationalThinking-2020.pdf
# Exercício 3
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o menor número inteiro
# que é múltiplo do número a e do número b. Neste exercício, você deverá validar as informações de entrada, ou seja,
# a e b devem ser número positivos.

# Versão Simplificada

a = int(input("Informe a: "))
b = int(input("Informe b: "))

multiplo = b

while multiplo % a != 0 or multiplo % b != 0:
    multiplo = multiplo + 1

print(multiplo)

