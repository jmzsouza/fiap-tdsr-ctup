def ehprimo(num):
    if num == 1:
        return False
    else:
        div = 2
        while num % div != 0:
            div = div + 1

        if num == div:
            return True
        else:
            return False


# -------------------------------------------------

def ehPerfeito(num):
    soma = 0
    div = 1
    while num > div:
        if num % div == 0:
            soma = soma + div
        div = div + 1

    if soma == num:
        return True
    else:
        return False


# -------------------------------------------------

def encaixa(a, b):
    potencia = 1
    while potencia <= b:
        potencia = potencia * 10

    resto = a % potencia
    if resto == b:
        return True
    else:
        return False


# -------------------------------------------------

def encaixou(a, b):
    encaixou = False
    while a >= b and not encaixou:
        if encaixa(a, b):
            encaixou = True
            return encaixou
        else:
            a = a // 10


# -------------------------------------------------

def dataValida(dia, mes, ano):
    dataValida = True

    diaInvalido = (dia < 1 or dia > 31)
    mesInvalido = (mes < 1 or mes > 12)

    mesEde30Dias = (mes == 4 or mes == 6 or mes == 9 or mes == 11)

    if diaInvalido or mesInvalido:
        dataValida = False

    if dia == 31 and mesEde30Dias:
        dataValida = False

    if mes == 2 and dia > 28:
        if dia > 29:
            dataValida = False
        elif ano % 4 != 0:  # se chegou aqui é dia 29
            dataValida = False
        elif ano % 100 == 0 and ano % 400 != 0:  # ano é multiplo de 4
            dataValida = False

    return dataValida

# -------------------------------------------------
