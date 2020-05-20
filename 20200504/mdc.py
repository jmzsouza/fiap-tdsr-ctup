# TrabalhoComputationalThinking-2020.pdf
# Exercício 3
# Dados dois números inteiro positivos a e b, escreva um algoritmo que encontra o menor número inteiro
# que é múltiplo do número a e do número b. Neste exercício, você deverá validar as informações de entrada, ou seja,
# a e b devem ser número positivos. Faça, no papel, dois testes de mesa do seu algoritmo.
# Bata uma foto ou escaneie o teste de mesa feito no papel e anexe ao seu trabalho.

# Versão Simplificada

a = int(input("Digite a: "))
b = int(input("Digite b: "))
div = a

while a % div != 0 or b % div != 0:
    div = div - 1    

print(div)