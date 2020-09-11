def criaTabuleiro():
    tab = []
    for i in range(3):
        tab.append([' '] * 3)
    return tab

def imprime(tab):
    for linha in tab:
        print(linha)

def joga(tab, jogador):
    print("Jogador", jogador)
    lin = int(input("Linha:"))
    col = int(input("Coluna:"))
    tab[lin][col] = jogador

def trocaJogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

def temEspaco(tab):
    return True

def haGanhador(tab):
    return False    

#criando um tabuleiro 
matriz = criaTabuleiro()
player = 'X'

while temEspaco(matriz) and not haGanhador(matriz):
    imprime(matriz)
    joga(matriz, player)
    player = trocaJogador(player)

if haGanhador(matriz):
    print(player, "venceu")
else:
    print("Deu empate!")    