# lista9CT-Projeto-2020.pdf
# Exercício 3
# Desenvolva uma função em Python que permite o usuário escolher, dentre vários elementos, 
# qual ele gostaria de descartar (como se fosse um descarte de baralho), 
# ou seja, além de retornar o valor, sua função deverá eliminar aquele elemento. 
# Os elementos estão armazenados em uma lista e serão passados como parâmetros para sua função.

def descarta(lista):
    print(lista)
    pos = int(input("Informe uma posicao:"))
    return lista.pop(pos)

