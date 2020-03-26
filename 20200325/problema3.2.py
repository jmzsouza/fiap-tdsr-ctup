#Selecao.pdf
#Problema 3.2
#Escreva um algoritmo que recebe um número e imprime na tela a informação que ou o número é positivo ou é negativo ou é igual a zero.

num =   int(input("Digite um número: "))
if num > 0:
    print(str(num) + " é positivo")
elif num < 0:
    print(str(num) + " é negativo")
else:
    print(str(num) + " é zero")