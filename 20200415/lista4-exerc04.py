# lista4CT2020.pdf
# Exercício 4
# Dados n um inteiro positivo e uma sequência de n números reais, escreva um algoritmo que
# conta e imprime a quantidade de números positivos e a quantidade de números negativos.

quantidade = int(input("Digite uma quantidade de números a ser digitados: "))

contador = 1
contadorPositivo = 0
contadorNegativo = 0

while contador <= quantidade:
    num = float(input("Digite um número: "))
    if num != 0:
        if num > 1:
            contadorPositivo += 1
        else:
            contadorNegativo += 1
    contador += 1

print("A quantidade de número positivos é:", str(contadorPositivo) +
      "\nA quantidade de números negativos é:", str(contadorNegativo))
