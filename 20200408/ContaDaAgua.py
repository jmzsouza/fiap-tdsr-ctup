# A Companhia Água Viva efetua a cobrança da água usando a seguinte tabela:

# faixas de consumo ------> valor por m³
# até 20m³ ---------------> R$ 2,00
# acima de 20 até 35m³ ---> R$ 3,50
# acima 35 até 50m³ ------> R$ 5,50
# acima de 50m³ ----------> R$ 7,00

# Devido a escassez de água que atinge a cidade, a Companhia decidiu premiar o consumidor que conseguir diminuir
# o consumo mensal em relação à média de consumo mensal do ano anterior.
# Além de menos m³ gastos, será concedido um desconto de 20% no valor da conta.
# Do mesmo modo, o consumidor cujo consumo mensal ultrapassar em mais de 10% a média de consumo do ano anterior, sofrerá
# uma multa de 30% no valor da conta. Sua tarefa é desenvolver um algoritmo que lê dois números reais, o primeiro
# número representa a média de consumo em m³ do ano anterior e o segundo representa o consumo em m³ do mês vigente.
# Após a leitura dos dados seu programa deverá mostrar o valor total da conta e o valor da multa ou desconto se houver.

mediaConsumoAnterior = float(input("Media do ano anterior: "))

consumoVigente = float(input("Consumo vigente: "))

valorUnitario = 0.0

if consumoVigente < 20:
    valorUnitario = 2.0
elif consumoVigente < 35:
    valorUnitario = 3.5
elif consumoVigente < 50:
    valorUnitario = 5.5
else:
    valorUnitario = 7.0

valorConta = consumoVigente * valorUnitario
valorFinal = valorConta

print("Valor da conta", valorConta)

if consumoVigente < mediaConsumoAnterior:
    desconto = valorConta * 0.2  # 20 % de desconto
    print("Desconto:", desconto)
    valorFinal = valorConta - desconto

elif consumoVigente > mediaConsumoAnterior * 1.1:  # equivale a 10% a mais
    multa = valorConta * 0.3  # 30% de acrescimo
    print("Multa:", multa)
    valorFinal = valorConta + multa

print("Valor final:", valorFinal)
