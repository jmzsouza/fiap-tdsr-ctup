# lista3CT2020.pdf
# Exercício 14
# Agora, vamos acrescentar na verificação de data os casos de ano bissexto, ou seja, o ano que fevereiro tem 29 dias.
# Um ano é bissexto se:
# a) o ano for divisível por 4
# b) anos múltiplos de 100, não são bissextos
# c) quando o ano for divisível por 400 ele é bissexto
# d) as últimas regras prevalecem sobre as primeiras
# Para exemplificar um pouco essas regras, observe que 1900 não foi bissexto mas 2000 foi.

dia = int(input("Informe um dia: "))
mes = int(input("Informe um mês: "))
ano = int(input("Informe um ano: "))

dataValida = True
bissexto = "Não"

diaInvalido = (dia < 1 or dia > 31)
mesInvalido = (mes < 1 or mes > 12)

mesEde30Dias = (mes == 4 or mes == 6 or mes == 9 or mes == 11)

if diaInvalido or mesInvalido:
    dataValida = False

if dia == 31 and mesEde30Dias:
    dataValida = False

if mes == 2 and dia > 28:
    if dia > 29:
        dataValida = False
    elif ano % 4 != 0:  # se chegou aqui é dia 29
        dataValida = False
    elif ano % 100 == 0 and ano % 400 != 0:  # ano é multiplo de 4
        dataValida = False
    else:
        bissexto = "Sim"

if dataValida:
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nAno.......: " + str(ano) +
          "\nBissexto..: " + bissexto +
          "\nResposta..: Data Válida")
else:
    print("\nDia.......: " + str(dia) +
          "\nMês.......: " + str(mes) +
          "\nAno.......: " + str(ano) +
          "\nBissexto..: " + bissexto +
          "\nResposta..: Data inválida")
