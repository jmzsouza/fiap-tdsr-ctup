# lista8CT-2020.pdf
# Exercício 12
# Dado uma lista de strings, escreva um algoritmo que conta o número de ocorrências da string na lista. Por exemplo:
# letras = [’a’, ’e’, ’b’, ’a’, ’c’, ’a’, ’b’, ’a’, ’e’]
# a: 4 vezes
# e: 2 vezes
# b: 2 vezes
# c: 1 vezes
# Dica, crie uma função para ajudar a resolver o problema.

def contagem(lista):
    contabilizado = []

    for i in range(len(lista)):
        if not lista[i] in contabilizado:
            qtd = lista.count(lista[i])
            print(lista[i], "aparece", qtd, "vezes")
            contabilizado.append(lista[i])

contagem(['a', 'b', 'e', 'a', 'c', 'a', 'b', 'e', 'd'])







