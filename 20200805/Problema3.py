# Listas.pdf
# Problema 3
# Escreva uma função que se reproduz o mesmo funcionamento do método count. 
# Sua função recebe como parâmetros uma lista, um valor e retorna a quantidade de ocorrências de valor na lista.

def contagem(lista, valor):
    ocorrencias = 0
    for info in lista:
        if info == valor:
            ocorrencias = ocorrencias + 1

    return ocorrencias

frutas = ["maça", "figo", "pêra", "figo", "caqui", "figo", "limão"]
resultado = contagem(frutas, "figo")
print(resultado)