# lista4CT2020.pdf
# Exercício 5
# Escreva um algoritmo que, dados um número inteiro positivo n,
# imprime na tela a contagem de todos os divisores positivos de n.

num = int(input("Digite um inteiro positivo: "))

contador = 0
divisor = 1

while divisor <= num:
    if num % divisor == 0:
        contador += 1
    divisor += 1

print("O número {} possui {} divisores.".format(num, contador))
