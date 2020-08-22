# lista6CT-2020.pdf
# Exercício 4
# Escreva uma função que recebe duas Strings: frase e letras; a frase representa um conjunto de caracteres e letras alguns caracteres. 
# Sua função deverá substituir cada caracter c contido na frase pelo caracter * se este caracter c estiver presente em letras.

def substitui(frase, letras):
    resp = ""
    i = 0

    while i < len(frase):
        if frase[0] in letras:
            resp = resp + "*"
        else:
            resp = resp + frase[i]
        i = i + 1

    return resp

f = input("Digite uma frase: ")
l = input("Digite as letras que deseja subtituir por *: ")

teste = substitui(f, l)

print(teste)
