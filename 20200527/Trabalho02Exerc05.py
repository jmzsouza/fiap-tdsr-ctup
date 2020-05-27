def stringInvertida(frase):
    resp = ""

    i = len(frase) - 1
    while i >= 0:
        resp = resp + frase[i]
        i = i - 1

    return resp


frase = input("Digite uma palavra/frase: ")
s = stringInvertida(frase)
print("Palavra/Frase invertida: {}".format(s))
