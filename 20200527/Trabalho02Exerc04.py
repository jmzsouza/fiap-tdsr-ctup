def contaVogais(frase):
    vogais = "aáàâãäeéèêëiíìîïoóòôõöuúùûü"
    i = 0
    contador = 0

    while i < len(frase):
        if frase[i] in vogais:
            contador = contador + 1
        i = i + 1
    return contador


frase = input("Digite uma frase: ").lower()
resp = contaVogais(frase)
print("Quantidade de vogais na frase: {}".format(resp))
