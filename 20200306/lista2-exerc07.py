#lista2CT2020.pdf
#Exercício 7
#Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
#dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
#divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

valor = input('Digite um número: ')
numA = int(valor)

print('O digito da dezena do número digitado é: ', numA // 10)
print('O digito da unidade do número digitado é: ', numA % 10)

