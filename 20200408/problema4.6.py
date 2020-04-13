# Problema 4.6 Escreva um algoritmo que recebe um inteiro positivo num e imprime todos os divisores positivos de num.

num = int(input("Digite um inteiro positivo: "))
divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor = divisor + 1
