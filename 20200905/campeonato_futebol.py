# Lista de Informacoes
# P - Pontos | J - Jogos | V - Vitórias | E - Empates | D - Derrotas | GP - Gols Pró | GC - Gols Contra  | SG - Saldo de Gols

# Lista de Clubes
# Indice | Informacao
#   0    | nome
#   1    | pontos
#   2    | jogos
#   3    | vitorias  
#   4    | empates
#   5    | derrotas
#   6    | gols prós
#   7    | gols contra
#   8    | saldo de gols


import random

listaDeInformacoes = ["P", "J", "V", "E", "D", "GP", "GC", "SG"]
    
# criar uma lista de clubes
def criaListaDeClubes(clubesParticipantes, listaDeInformacoes):

    listaDeClubes = []

    for i in range(len(clubesParticipantes)):
        clube = [clubesParticipantes[i]]
        clube = clube + [0]*len(listaDeInformacoes)
        listaDeClubes.append(clube)

    return listaDeClubes

# obter nome
def getNome(clube):
    return clube[0]

# obter pontos
def getPontos(clube):
    return clube[1]

# obter jogos
def getJogos(clube):
    return clube[2]

# obter vitórias
def getVitorias(clube):
    return clube[3]

# obter empates
def getEmpates(clube):
    return clube[4]

# obter derrotas
def getDerrotas(clube):
    return clube[5]

# obter gols pró
def getGolsPro(clube):
    return clube[6]

# obter gols contras
def getGolsContra(clube):
    return clube[7]

# obter saldo de gols
def getSaldoDeGols(clube):
    return clube[8]

# adcionar golsPro, golsContra e saldoDeGols
def addGols(clube, golsPro, golsContra):
    clube[6] = clube[6] + golsPro
    clube[7] = clube[7] + golsContra
    clube[8] = clube[6] - clube[7]

# adicionar pontos, jogos e vitoria
def addVitoria(clube):
    clube[1] = clube[1] + 3
    clube[2] = clube[2] + 1
    clube[3] = clube[3] + 1

# adicionar jogos e derrota
def addDerrota(clube):
    clube[2] = clube[2] + 1    
    clube[5] = clube[5] + 1

# adicionar pontos, jogos e empate
def addEmpate(clube):
    clube[1] = clube[1] + 1
    clube[2] = clube[2] + 1    
    clube[4] = clube[4] + 1

# criar partida
def criaPartida(mandante, visitante):
    golsMandante = random.randint(0, 10)
    golsVisitante = random.randint(0, 10)

    addGols(mandante, golsMandante, golsVisitante)
    addGols(visitante, golsVisitante, golsVisitante)  

    if golsMandante > golsVisitante:
        addVitoria(mandante)
        addDerrota(visitante)
    elif golsMandante < golsVisitante:
        addVitoria(visitante)
        addDerrota(mandante) 
    else:
        addEmpate(mandante)
        addEmpate(visitante)      

    return golsMandante, golsVisitante

# ordenar tabela
def ordenaTabela(listaDeClubes):

    porGolsPros = sorted(listaDeClubes, key=lambda golsPro: golsPro[6], reverse=True)
    porSaldoDeGols = sorted(porGolsPros, key=lambda saldoDeGols: saldoDeGols[8], reverse=True)
    porVitorias = sorted(porSaldoDeGols, key=lambda vitorias: vitorias[3], reverse=True)
    porPontos = sorted(porVitorias, key=lambda pontos: pontos[1], reverse=True)
    tabelaOrdenada = porPontos

    return tabelaOrdenada    

# formatar os nomes baseados no maior nome de clube
def formatarNomes(tabelaOrdenada):
    nomesFormatados = []
    maiorNome = ""

    # maior nome entre os clubes incluindo a descrição "CLASSIFICACAO"
    cabecalhoClubes = [["CLASSIFICACAO"]] + tabelaOrdenada
    for i in range(len(cabecalhoClubes) - 1):
        linhaAtual = cabecalhoClubes[i]
        proximaLinha = cabecalhoClubes[i + 1]
        if len(linhaAtual[0]) >= len(proximaLinha[0]) and len(linhaAtual[0]) > len(maiorNome):
            maiorNome = linhaAtual[0]
        elif len(proximaLinha[0]) > len(maiorNome):
            maiorNome = proximaLinha[0]      

    # indentar nomes dos clubes
    for i in range(len(cabecalhoClubes)):
        compara = cabecalhoClubes[i]
        nomeCompara = str(compara[0])
        diferencaQtdChar = len(maiorNome) - len(nomeCompara)
        for j in range(diferencaQtdChar):
            nomeCompara  = nomeCompara + "."
        nomesFormatados.append(nomeCompara)
    return nomesFormatados

# imprimir tabela
def imprimeTabela(tabelaOrdenada, nomesFormatados):

    print("\n---------------------------- CAMPEONATO DE FUTEBOL -----------------------")
    print(f"{nomesFormatados[0]}:\t{listaDeInformacoes[0]}\t{listaDeInformacoes[1]}\t{listaDeInformacoes[2]}\t{listaDeInformacoes[3]}\t{listaDeInformacoes[4]}\t{listaDeInformacoes[5]}\t{listaDeInformacoes[6]}\t{listaDeInformacoes[7]}")
    
    for i in range(len(tabelaOrdenada)):
        clube  = tabelaOrdenada[i]
        print(f"{nomesFormatados[i+1]}:\t{getPontos(clube)}\t{getJogos(clube)}\t{getVitorias(clube)}\t{getEmpates(clube)}\t{getDerrotas(clube)}\t{getGolsPro(clube)}\t{getGolsContra(clube)}\t{getSaldoDeGols(clube)}")
        i = i + 1
    print("----------------------------------------------------------------------------")

# imprimir rodada
def imprimirRodada(mandante, visitante):
    placar = criaPartida(mandante, visitante)
    print(f"{getNome(mandante)}:{placar[0]} X {placar[1]}:{getNome(visitante)}")

# turno e returno
def turnoReturno(listaDeClubes, turno):

    tamanhoDaLista = len(listaDeClubes)

    rodada = 0
    while rodada < tamanhoDaLista - 1:
        print("\n---------------------")
        print(f"{turno}º Turno - {rodada + 1}a Rodada:")
        print("---------------------")

        j = 0
        while j < tamanhoDaLista / 2:
            # ajustar o mandante e visitante
            if j % 2 == 1 or rodada % 2 == 1 and j == 0:
                mandante = listaDeClubes[tamanhoDaLista - j - 1]
                visitante = listaDeClubes[j]
                imprimirRodada(mandante, visitante)
            else:
                mandante = listaDeClubes[j] 
                visitante = listaDeClubes[tamanhoDaLista - j - 1]
                imprimirRodada(mandante, visitante)
            j = j + 1

        # manter o primeiro no lugar e girar os outros clubes no sentido horário 
        primeiro = [listaDeClubes.pop(0)]
        ultimo = [listaDeClubes.pop()]
        listaDeClubes = primeiro + ultimo + listaDeClubes
        rodada = rodada + 1
    
    return listaDeClubes

# determinar o campeão
def determinarCampeao(listaDeClubes):

    vencedor = listaDeClubes[0]
    vencedores = [vencedor]

    for i in range(1, len(listaDeClubes)):
        clube = listaDeClubes[i]

        if getPontos(vencedor) < getPontos(clube):
            vencedor = clube
            vencedores = []
            vencedores.append(clube)   
        elif getPontos(vencedor) == getPontos(clube):

            if getVitorias(vencedor) < getVitorias(clube):
                vencedor = clube
                vencedores = []
                vencedores.append(clube)
            elif getVitorias(vencedor) == getVitorias(clube):

                if getSaldoDeGols(vencedor) < getSaldoDeGols(clube):
                    vencedor = clube
                    vencedores = []
                    vencedores.append(clube)                     
                elif getSaldoDeGols(vencedor) == getSaldoDeGols(clube):

                    if getGolsPro(vencedor) < getGolsPro(clube):
                        vencedor = clube
                        vencedores = []
                        vencedores.append(clube)
                    elif getGolsPro(vencedor) == getGolsPro(clube):
                        vencedores.append(clube)
                        vencedor = random.choice(vencedores)

    return vencedor

# simular o campeonato
def simulaCampeonato(listaDeClubes, qtdTurnos):

    listaInvertida = []
    turno = 1
    while turno <= qtdTurnos:
        if turno == 1 or turno % 2 == 1:
            listaDeClubes = turnoReturno(listaDeClubes, turno)           
        else:
            for i in reversed(range(len(listaDeClubes))):     
                listaInvertida.append(listaDeClubes[i])        
            turnoReturno(listaInvertida, turno)
        turno = turno + 1
    
    imprimeTabela(ordenaTabela(listaDeClubes), formatarNomes(ordenaTabela(listaDeClubes)))
    clubeCampeao = getNome(determinarCampeao(ordenaTabela(listaDeClubes)))
    print("CLUBE CAMPEAO:", clubeCampeao)
    print("----------------------------------------------------------------------------")    


# Programa
print("\n---------------------------- CAMPEONATO DE FUTEBOL -----------------------")

qtdClubes = int(input("Quantidade de clubes: "))
qtdTurnos = int(input("Número de turnos: "))

clubesParticipantes = []

if qtdClubes % 2 == 0:
    for i in range(1, qtdClubes + 1):
        nomeClube = input("Informe o nome do {}º clube: ".format(i))
        clubesParticipantes.append(nomeClube)
else:
    print("Informe apenas a quantidade par de clubes!")

listaDeClubes = criaListaDeClubes(clubesParticipantes, listaDeInformacoes)
simulaCampeonato(listaDeClubes, qtdTurnos)