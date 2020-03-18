#lista2CT2020.pdf
#Exercício 11
#Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual de aumento. 
#Você deverá escrever um algoritmo que recebe 2 números reais representando os salários antes e depois do aumento 
#e deverá calcular e exibir o percentual de aumento que João obteve.

valor = input('Qual o salário anterior de João? ')
anterior = float(valor)

valor = input('Qual o salário atual de João? ')
atual = float(valor)

aumento = (atual - anterior) * 100 / anterior

print('O aumento no salário foi de',aumento,'%')
