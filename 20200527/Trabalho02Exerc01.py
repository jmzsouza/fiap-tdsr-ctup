from Trabalho02Funcoes import *

dia = int(input("Informe o número de um dia: "))
mes = int(input("Informe o número de um mês: "))
ano = int(input("Informe o número de um ano: "))

if dataValida(dia, mes, ano):
    qtdDias = int(input("Informe a quantidade de dias: "))
    resp = somarDiasData(dia, mes, ano, qtdDias)
    print("{}/{}/{}".format(resp[0], resp[1], resp[2]))
else:
    print("Informe uma data valida!")

