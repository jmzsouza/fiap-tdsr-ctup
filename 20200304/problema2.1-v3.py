#Algoritmos1.pdf
#Problema 2.1 - v.3 
#Dados uma sequência de 5 números inteiros. Calcule a soma de todos os números da sequência.

contador = 0
soma = 0

for contador in range(5):
	valor = input("Digite um número: ")
    num = int(valor)
    soma = soma + num
    contador = contador + 1
next

print("A soma da sequência é: ", soma)
