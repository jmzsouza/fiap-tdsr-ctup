def montaPalavraTracejada(pal, letras):
    resp = ""

    for c in pal:
        if c in letras or c in letras.upper():
            resp = resp + c + " "
        else:
            if c == " ":
                resp = resp + " "
            else:
                resp = resp + "_ "
    return resp


maxErros = 6
erros = 0
letrasChut = ""

palavraOculta = "Coreia do Sul"
palavraX = montaPalavraTracejada(palavraOculta, letrasChut)
acertou = False

while erros < maxErros and not acertou:
    print(palavraX)
    print("Erros: {} de {}".format(erros, maxErros))
    print("Letras chutadas: ", letrasChut)
    letra = input("Letra: ").lower()

    letrasChut = letrasChut + letra
    if letra in palavraOculta or letra.upper() in palavraOculta:
        palavraX = montaPalavraTracejada(palavraOculta, letrasChut)
    else:
        erros = erros + 1

    if not "_" in palavraX:
        acertou = True

if acertou:
    print(palavraX)
    print("Parabéns você acertou!")
else:
    print("Você errou, pois excedeu o número de tentativas.")