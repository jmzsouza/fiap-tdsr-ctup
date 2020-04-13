# Problema 4.1: Dados uma sequência de 5 números inteiros. Calcule a soma de todos os números da sequência.

soma = 0
contador = 0

while contador < 5:
    num = int(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1

print("O resultado é:", soma)
