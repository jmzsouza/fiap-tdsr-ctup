import Imagem

matriz = Imagem.getMatrizImagemCinza("domino.png")
altura = len(matriz)
largura = len(matriz[0])
print("Altura: ", altura)
print("Largura: ", largura)

for i in range(altura):
    for j in range(largura):
        matriz[i][j] = matriz[i][j] + 100

Imagem.salvaImagemCinza("dominoClaro.png", matriz)        

