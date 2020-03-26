#Selecao.pdf
#Problema 3.3 - v.3
#Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações matemáticas(+,-,*,/))
#e calcula o valor da operação matemática, ou seja, se a entrada for 5, ∗ e 6 então seu programa deverá mostrar 30.
#Algumas vezes, para facilitar a leitura do código, usamos variáveis booleanas para representar as condições:
numA = float(input("Digite um número: "))
op = input("Operador (+-*/): ")
numB = float(input("Digite outro número: "))

soma = (op == "+")
subtracao = (op == "-")
multiplicacao = (op == "*")
divisao = (op == "/")

if soma:
    resultado = numA + numB
elif subtracao:
    resultado = numA - numB
elif multiplicacao:
    resultado = numA * numB
elif divisao:
    resultado = numA / numB

print("Resposta: {:.2f}".format(resultado))