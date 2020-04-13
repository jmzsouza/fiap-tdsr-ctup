# lista3CT2020.pdf
# Exercício 13
# Desenvolva um algoritmo que informe se uma data é válida ou não.
# O algoritmo deverá ler 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido.
# Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

dia = int(input("Informe um dia: "))
mes = int(input("Informe um mês: "))

dataValida = True

diaInvalido = (dia < 1 or dia > 31)
mesInvalido = (mes < 1 or mes > 12)

mesEde30Dias = (mes == 4 or mes == 6 or mes == 9 or mes == 11)

if diaInvalido or mesInvalido:
    dataValida = False

if dia == 31 and mesEde30Dias:
    dataValida = False

if mes == 2 and dia > 28:
    dataValida = False

if dataValida:
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nResposta..: Data Válida")
else:
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nResposta..: Data inválida")