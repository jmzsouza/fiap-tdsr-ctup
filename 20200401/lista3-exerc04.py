#lista3CT2020.pdf
#Exercício 4
#Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma partida. 
#Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE.

valor = input("Digite o nome de um time: ")
timaA = valor
valor = input("Informe o número de gols: ")
golsA = valor
valor = input("Digite o nome de outro time: ")
timaB = valor
valor = input("Informe o número de gols: ")
golsB = valor

if golsA == golsB:
    print("Houve empate na partida.")
else:
    if golsA > golsB:
        print(timaA, "foi o vencedor.")
    else:
        print(timaB, "foi o vencedor.")
