#lista2CT2020.pdf
#Exercício 10
#Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
#Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
#seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.

valor = input('Qual a distância em metros percorrida por um velocista? ')
distancia = int(valor)

valor = input('Qual o tempo em segundos percorrido nesta distância? ')
segundos = float(valor)

mediaA = distancia / segundos
mediaB = (distancia / 1000) / (segundos / 3600)

print('O velocista tem a velocidade média de',mediaA,'m/s e',mediaB,'km/h')
