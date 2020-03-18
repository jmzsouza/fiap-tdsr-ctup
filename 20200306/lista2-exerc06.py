#lista2CT2020.pdf
#Exercício 6
#Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.

valor = input('Digite o valor de raio para um círculo: ')
raio = float(valor)

pi = 3.141592
area = pi * (raio * raio)
perimetro = (2 * pi) * raio

print('O círculo tem a área: ', area, ' e o perimetro: ', perimetro)
