from Trabalho02Funcoes import *

diaData1 = int(input("Informe o número de um dia para data1: "))
mesData1 = int(input("Informe o número de um mês para data1: "))
anoData1 = int(input("Informe o número de um ano para data1: "))

diaData2 = int(input("Informe o número de um dia para data2: "))
mesData2 = int(input("Informe o número de um mês para data2: "))
anoData2 = int(input("Informe o número de um ano para data2: "))

if dataValida(diaData1, mesData1, anoData1) and dataValida(diaData2, mesData2, anoData2):
    resp = qtdDiasEntreDatas(diaData1, mesData1, anoData1, diaData2, mesData2, anoData2)
    print("Quantidade de dias entre as datas: {}".format(resp))
else:
    print("Digite apenas datas válidas!")
