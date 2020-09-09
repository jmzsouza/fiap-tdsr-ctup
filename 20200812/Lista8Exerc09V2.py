# lista8CT-2020.pdf
# Exercício 9
# Escreva uma função que recebe como parâmetro duas listas listaA e listaB de números reais.
# Ela deverá retornar uma terceira lista contendo todos os números da listaA que também estão na listaB.

def interseccao(listaA, listaB):
    resposta = []
    for elemento in listaA:
        if elemento in listaB:
            resposta.append(elemento)
    
    return resposta

listA = [1, 6, 4, 8, 3]
listB = [10, 8, 0, 3, 7]
print(interseccao(listA, listB))



