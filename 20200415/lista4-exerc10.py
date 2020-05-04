# lista4CT2020.pdf
# Exercício 10
# Escreva um algoritmo que recebe um inteiro positivo n e calcula n! = 1 · 2 · 3 . . . ·(n − 1)· n.
# Por exemplo, se n = 6, então 6! = 1 · 2 · 3 · 4 · 5 · 6 = 720.

num = int(input("Digite um número a ser permutado: "))

soma = num

while num > 1:
    soma = soma * (num - 1)
    num = num - 1

print("O resultado é: ", soma)
