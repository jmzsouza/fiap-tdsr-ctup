#Algoritmos1.pdf
#Atividade 1
#Dada uma sequencia de números inteiros onde o  último termo dessa sequência é o número 0, calcule a  soma de todos os números da sequência.

valor = input ("Digite um número: ")
num = int(valor)

soma = 0

while (num != 0):
    soma = soma + num
	valor = input ("Digite um número: ")
    num = int(valor)
else:
	print("A soma é: ", soma)