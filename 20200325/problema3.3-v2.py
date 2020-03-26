#Selecao.pdf
#Problema 3.3 - v.2
#Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações matemáticas(+,-,*,/))
#e calcula o valor da operação matemática, ou seja, se a entrada for 5, ∗ e 6 então seu programa deverá mostrar 30.

numA = float(input("Digite um número: "))
op = input("Operador (+-*/): ")
numB = float(input("Digite outro número: "))

if op == "+":
    resultado = numA + numB
elif op == "-":
    resultado = numA - numB
elif op == "*":
    resultado = numA * numB
elif op == "/":
    resultado = numA / numB
print("Resposta: ", resultado)