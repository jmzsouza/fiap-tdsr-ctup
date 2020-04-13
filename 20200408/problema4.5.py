# Problema 5.5: Escreva um programa que dado um inteiro n positivo
# calcula e imprime a soma de todos os números inteiros entre 1 e n.

n = int(input("Digite um inteiro positivo: "))

while n < 0:
    n = int(input("Erro ! Digite um inteiro positivo: "))

soma = 0
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

print("Valor da soma é: ", soma)
