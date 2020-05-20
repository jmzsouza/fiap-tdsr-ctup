# TrabalhoComputationalThinking-2020.pdf
# Exercício 4
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o maior
# número inteiro que divide o número a e o número b.
# Faça, no papel, dois testes de mesa do seu algoritmo e envie como descrito no exercício anterior.

# Versão Simplificada

a = int(input("Informe a: "))
b = int(input("Informe b: "))

multiplo = b

while multiplo % a != 0 or multiplo % b != 0:
    multiplo = multiplo + 1

print(multiplo)

