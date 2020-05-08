# CPF-Binario.pdf
# Escreva um algoritmo que recebe um número na base binária para a base decimal

numeroBinario = int(input("Digite numero binario: "))

soma = 0
potenciaDois = 1

while numeroBinario != 0:
    resto = numeroBinario % 10
    numeroBinario = numeroBinario // 10
    soma = soma + resto * potDois
    potDois = potDois * 2

print("Valor em decimal:", soma)
