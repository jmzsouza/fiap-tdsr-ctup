#lista2CT2020.pdf
#Exercício 12
#O RM de um aluno da FIAP é composto por 5 dígitos. 
# Sua tarefa é escrever um algoritmo que recebe um RM e retorna a somatória de todos os dígitos do RM. 
# Por exemplo, suponha que o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.
#Dica: realize várias divisões e restos de divisões por 10.

valor = input('Digite o número do seu RM: ')
rm = int(valor)

dig1 = rm // 10 // 10 // 10 // 10 % 10
dig2 = rm // 10 // 10 // 10 % 10
dig3 = rm // 10 // 10 % 10
dig4 = rm // 10 % 10
dig5 = rm % 10

soma = dig1 + dig2 + dig3 + dig4 + dig5

print('A soma dos dígitos do seu RM é:',soma,'=',dig1,'+',dig2,'+',dig3,'+',dig4,'+',dig5,)
