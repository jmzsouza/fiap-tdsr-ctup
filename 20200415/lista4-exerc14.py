# lista4CT2020.pdf
# Exercício 14
# Uma das maneiras de evitar erros na digitação de números como conta corrente, CPF,
# boleto bancário é a utilização de um ou mais dígitos de controle. Um dos métodos de cálculo é a utilização do
# método módulo 10. Segue a descrição do algoritmo: Dado um número inteiro n devemos pegar cada dígito desse número
# começando pela casa das unidades e multiplicar, alternadamente, por 2 e por 1. Caso o resultado da multiplicação
# seja um  número maior ou igual a 10 devemos simplificar esse valor somando os dois dígitos. Após feitas as
# multiplicações e as simplificações devemos somar todos os valores e calcular o resto da divisão dessa soma por 10.
# Se o resto for 0 o dígito de controle é zero, caso contrário o dígito de controle será 10 menos o resto. Escreva um
# algoritmo que lê um número inteiro positivo e calcula o seu dígito de controle usando o método do módulo 10.

numero = int(input("Informe parte do boleto: "))

dcRecebido = numero % 10
numero = numero // 10

soma = 0
mult = 2

while numero != 0:
    digito = numero % 10
    valor = digito * 2
    valor = (valor // 10) + (valor % 10)
    soma = soma + valor
    numero = numero // 10
    if mult == 2:
        mult = 1
    else:
        mult = 2

resto = soma % 10
dcCalculado = 0
if resto > 0:
    dcCalculado = 10 - resto

if dcCalculado == dcRecebido:
    print("Essa parte do boleto foi validada!")
else:
    print("Erro nesta parte do boleto!")