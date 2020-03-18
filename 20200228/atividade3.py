#Algoritmos1.pdf
#Atividade 3
#Dada uma sequencia de 10 números inteiros, encontre aquele que é o maior número da sequência.

sequencia = []

for contador in range(0,10):
	valor = input ("Digite um número: ")
    num = int(valor)
    sequencia.append(num)
    contador = contador + 1
next

print("Sequência: ", sequencia)
print("O maior número da sequência é: ", max(sequencia))