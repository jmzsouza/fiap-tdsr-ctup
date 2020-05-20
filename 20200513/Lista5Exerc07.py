# lista5CT-2020.pdf
# Exercício 7
# Escreva uma função em Python que recebe três números inteiros positivos representando uma data (dia, mês e ano),
# sua função deverá retornar True se for uma data válida ou False, caso contrário.

from Lista5Funcoes import *

dia = int(input("Informe o número de um dia: "))
mes = int(input("Informe o número de um mês: "))
ano = int(input("Informe o número de um ano: "))

if dataValida(dia, mes, ano):
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nAno.......: " + str(ano) +
          "\nResposta..: Data Válida")
else:
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nAno.......: " + str(ano) +
          "\nResposta..: Data inválida")