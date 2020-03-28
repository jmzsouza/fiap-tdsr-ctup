# Selecao.pdf
# Problema 3.5
# Escreva um algoritmo que recebe três números inteiros e imprime eles em ordem crescente.

numA = int(input("digite o 1º no : "))
numB = int(input("digite o 2º no : "))
numC = int(input("digite o 3º no : "))

if (numA <= numB) and (numB <= numC):
    print(numA, " ", numB, " ", numC)
elif (numA <= numC) and (numC <= numB):
    print(numA, " ", numC, " ", numB)
elif (numB <= numA) and (numA <= numC):
    print(numB, " ", numA, " ", numC)
elif (numB <= numC) and (numC <= numA):
    print(numB, " ", numC, " ", numA)
elif (numC <= numA) and (numA <= numB):
    print(numC, " ", numA, " ", numB)
else:
    print(numC, " ", numB, " ", numA)