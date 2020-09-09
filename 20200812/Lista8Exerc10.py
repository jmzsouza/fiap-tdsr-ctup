# lista8CT-2020.pdf
# Exercício 10
# Escreva um método chamado intercala que recebe como parâmetro duas listas a e b de números reais ordenadas em ordem crescente. 
# Seu método deverá retornar uma terceira lista contendo a união dos elementos de a e b ordenados em ordem crescente.

def intercala(listaA, listaB):

    resposta = []
    i = 0
    j = 0

    while i < len(listaA) and j < len(listaB):
        if listaA[i] < listaB[j]:
            resposta.append(listaA[i])
            i = i + 1
        else:
            resposta.append(listaB[j])
            j = j + 1

    while i < len(listaA):
        resposta.append(listaA[i])
        i = i + 1
        
    while j < len(listaB):
        resposta.append(listaB[j])
        j = j + 1

    return resposta

lA = [2, 5, 6]
lB = [1, 4, 7, 9]
resultado = intercala(lA, lB)
print(resultado)








