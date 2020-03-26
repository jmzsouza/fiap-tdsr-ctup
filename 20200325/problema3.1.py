#Selecao.pdf
#Problema 3.1
#Um número inteiro pode ser par ou ímpar. Escreva um algoritmo que recebe um números inteiro e imprime na tela a informação sobre sua paridade.

entrada = input("Digite um número inteiro: ")
num = int(entrada)
resto = num % 2
if resto == 0:
    print(num, " - é par")
else:
    print(num, " - é ímpar")