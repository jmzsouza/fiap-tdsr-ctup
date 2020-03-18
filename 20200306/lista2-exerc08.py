#lista2CT2020.pdf
#Exercício 8
#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. 
#Escreva um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. 
#Seu algoritmo deverá ler o número de camisas, o número de calças e o número de pares de sapato.

valor = input('Quantas camisas você possui? ')
x = int(valor)

valor = input('Quantas calças você possui? ')
y = int(valor)

valor = input('Quantos pares de sapatos você possui? ')
z = int(valor)

print('Você pode se vestir', x * y * z,'maneiras diferentes.')

