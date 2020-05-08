# listaExtraRepeticaoCT-2020.pdf
# Exercício 2
# Dizemos que um inteiro positivo n é perfeito se for igual à soma de seus divisores positivos diferentes de n.
# Exemplo:
# 6 é perfeito, pois 1 + 2 + 3 = 6.
# Sua tarefa será a de escrever um algoritmo em Python que, dado um inteiro positivo n, verificar se n é perfeito.

n = int(input("Digite um número: "))

i = 1
soma = 0

while i < n:
    resto = n % i
    if resto == 0:
        soma = soma + i
    i = i + 1

if soma == n:
    print("O número é perfeito!")
else:
    print("O número não é perfeito!")
