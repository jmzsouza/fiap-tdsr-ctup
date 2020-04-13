# Problema 4.3: Escreva um algoritmo que dados um número inteiro positivo n, imprime na tela todos os números de 1 a n.

n = int(input(" Digite a quantidade de números: "))

num = 1
while num <= n:
    print(num)
    num = num + 1

print(" Fim ")
