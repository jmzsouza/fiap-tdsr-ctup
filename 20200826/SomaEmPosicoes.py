def aumento(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] + valor

valor = 5
matriz = [[5, 3, 4], [-2, 9, 6], [8, 1, -7]]
aumento(matriz, valor)
for linha in matriz:
    print(linha)