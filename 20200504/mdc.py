# TrabalhoComputationalThinking-2020.pdf
# Exercício 4
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o maior
# número inteiro que divide o número a e o número b.

# Versão Simplificada

a = int(input("Digite a: "))
b = int(input("Digite b: "))
div = a

while a % div != 0 or b % div != 0:
    div = div - 1    

print(div)