# lista6CT-2020.pdf
# Exercício 4
# Escreva uma função que recebe duas Strings: frase e letras; a frase representa um conjunto de caracteres e letras alguns caracteres. 
# Sua função deverá substituir cada caracter c contido na frase pelo caracter * se este caracter c estiver presente em letras.

def substitui(frase, letras):
    resp = ""

    for c in frase:
       if c in letras:
           resp = resp + "*"
       else:
           resp = resp + c

    return resp

f = input("Digite uma frase: ")
l = input("Digite as letras que deseja subtituir por *: ")

teste = substitui(f, l)

print(teste)
