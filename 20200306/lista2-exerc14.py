#lista2CT2020.pdf
#Exercício 14
#As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento: à vista ou em 10 vezes.
#Sua tarefa é desenvolver um programa/algoritmo onde o usuário informa (digita) o valor total à vista e o valor de cada parcela. 
#Seu programa imprime o desconto em percentual dado pela prefeitura para pagamento à vista.

valor = input('Qual o valor total à vista do IPTU? ')
vista = float(valor)

valor = input('Qual o valor de cada parcela do IPTU? ')
parcela = float(valor)

percentual = 100 - (vista * 100 / (10 * parcela))

print('O percentual de desconto do IPTU foi de',percentual,'%')
