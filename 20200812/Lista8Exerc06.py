# lista8CT-2020.pdf
# Exercício 6
# Escreva uma função em Python que recebe um inteiro x e uma lista de números inteiros ordenada em ordem crescente. 
# Sua função deverá inserir x na lista de forma que ela continue ordenada em ordem crescente. 
# Neste exercício você deve usar apenas o método insert da lista.

def insereOrdenado(x, lista):
    i = 0
    while i < len(lista) and x < lista[i]:
        lista.insert(i, x)
        i = i + 1

listaTeste = [3, 7, 13, 20, 23, 41, 36, 55]
insereOrdenado(29, listaTeste)
print(listaTeste)







