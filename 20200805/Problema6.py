# Lista.pdf
# Problema 6
# Crie uma função em Python que recebe uma lista contendo números inteiros e separa essa lista em duas outras listas.
# Uma contém os valores dos índices pares e a outra os valores dos índices ímpares da lista original.

def separa(lista):
    i = 0
    pares = []
    impares = []
    while i < len(lista):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        else:
            impares.append(lista[i])
        i = i + 1
    return [pares, impares]
    
listaTeste = [7, -34, 26, 1, 3, 5, 8, 0]
separados = separa(listaTeste)
print(separados[0])
print(separados[1])