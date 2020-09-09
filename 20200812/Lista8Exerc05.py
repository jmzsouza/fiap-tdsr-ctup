# lista8CT-2020.pdf
# Exercício 5
# Faça uma função em Python que recebe uma lista de números reais 
# e retorna True se a lista está ordenada em ordem crescente ou False se ela não está.

def estaOrdenado(lista):

    i = 0
    while i + 1 < len(lista):
        if lista[i] > lista[i + 1]:
            return False
        i = i + 1
    return True

listaTeste = [3, 5, 7, 9, 11]
resultado = estaOrdenado(listaTeste)
print(resultado)







