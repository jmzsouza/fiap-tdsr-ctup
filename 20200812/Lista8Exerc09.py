# lista8CT-2020.pdf
# Exercício 9
# Escreva uma função que recebe como parâmetro duas listas listaA e listaB de números reais.
# Ela deverá retornar uma terceira lista contendo todos os números da listaA que também estão na listaB.

def busca(valor, lista):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return True
        i = i + 1

    return False

def interseccao(listaA, listaB):
    intersectado = []
    for elemento in listaA:
        if busca(elemento, listaB) == True:
            intersectado.append(elemento)

    return intersectado

listA = [1, 6, 4, 8, 3]
listB = [10, 8, 0, 3, 7]
print(interseccao(listA, listB))







