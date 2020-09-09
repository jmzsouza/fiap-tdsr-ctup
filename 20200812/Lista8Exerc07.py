# lista8CT-2020.pdf
# Exercício 7
# Escreva uma função que recebe como parâmetro uma lista de números reais e um real x.
# Sua função deverá contar e retornar a quantidade de elementos que são maiores ou iguais a x.

def compara(x, lista):

    i = 0
    qtd = 0
    for i in range(len(lista)):
        if lista[i] >= x:
            qtd = qtd + 1

    return qtd

x = 5
conjunto = [0, 2, 5, 8, 18, 3, 5, 4, 7, 13, 5]
resposta = compara(10, conjunto)
print(resposta)


