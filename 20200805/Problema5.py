# Lista.pdf
# Problema 5
# Crie uma função em Python que recebe uma lista contendo números inteiros 
# e aumente todos os valores da lista em uma unidade.

def aumenta(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] + 1
        i = i + 1

listaTeste = [1, 3, 6, 9, 12, 15, 18, 21]
aumenta(listaTeste)
print(listaTeste)