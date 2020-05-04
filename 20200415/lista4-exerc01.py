# lista4CT2020.pdf
# Exercício 1
# Dada uma sequência de números inteiros onde o último elemento é o 0,
# escreva um algoritmo que calcula a soma dos números pares da sequência.

num = int(input("Digite um número: "))

acumula = 0

while num != 0:
    if num % 2 == 0:
        acumula = acumula + num
    num = int(input("Digite um número: "))

print("A soma dos números pares é:", acumula)