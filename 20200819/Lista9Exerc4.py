# lista9CT-Projeto-2020.pdf
# Exercício 4
#  Considere duas cartas de Baralho X e Y de um jogo de Truco. Escreva a seguinte função abaixo:
# def compara(x, y):
# Sua função deverá retornar -1 se x > y, 0 se x = y ou 1 se x < y. 
# Lembrando que você deve seguir a comparação de cartas de um jogo de Truco sem considerar as "manilhas".

def valor(carta):
    if carta[0] == 3:
        return 20
    elif carta[0] == 2:
        return 18
    elif carta[0] == 1:
        return 16
    elif carta[0] == 12:
        return 11
    elif carta[0] == 11:
        return 12
    else:
        return carta[0]

def compara(x, y):
    if valor(x) > valor(y):
        return -1
    elif valor(x) < valor(y):
        return 1
    else:
        return 0

