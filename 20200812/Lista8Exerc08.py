# lista8CT-2020.pdf
# Exercício 8
# Escreva uma função que recebe como parâmetro uma lista a de números inteiros 
# e retorna uma outra lista contendo somente os números pares de a.

def extraiPares(lista):
    
    resposta = []
    for elemento in lista:
        if elemento % 2 == 0:
            resposta.append(elemento)
    return resposta

listaTeste = [2, 3, 8, 5, -9, 6, 15, 17]
retorno = extraiPares(listaTeste)
print(retorno)





