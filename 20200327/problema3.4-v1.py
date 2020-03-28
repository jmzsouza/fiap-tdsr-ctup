# Selecao.pdf
# Problema 3.4 - v.1
# Escreva um algoritmo que lê o salário de um funcionário e
# mostra qual o percentual de desconto que será aplicado para sua contribuição ao INSS.
# Use a tabela abaixo para calcular o desconto:
# salário contribuição: até R$ 1.693,72 ----------------> alíquota/valor: 8%
# salário contribuição: de R$ 1.693,73 até R$ 2.822,90 -> alíquota/valor: 9%
# salário contribuição: de R$ 2.822,91 até R$ 5.645,80 -> alíquota/valor: 11%
# salário contribuição: acima de R$ 5.645,80 -----------> alíquota/valor: 11% sobre R$ 5.645,80
# Por exemplo, um trabalhador com salário de R$ 2.000,00 o percentual de desconto será de 9%.
# Quem ganha R$ 8.000,00 terá um desconto de 11% sobre o teto da aposentadoria.

salario = float(input("Digite o salário: "))

if salario >= 0 and salario <= 1693.72:
    contribuicao = salario * 0.08

if salario >= 1693.73 and salario <= 2822.90:
    contribuicao = salario * 0.09

if salario >= 2822.91 and salario <= 5645.80:
    contribuicao = salario * 0.11

if salario > 5645.80:
    contribuicao = 5645.80 * 0.11

print("O valor do INSS será de R$ {:.2f}".format(contribuicao))



