def mesDe30Dias(mes):
    mesDe30Dias = (mes == 4 or mes == 6 or mes == 9 or mes == 11)
    return mesDe30Dias


# -------------------------------------------------
def anoBissexto(ano):
    anoBissexto = True

    if ano % 4 != 0:
        anoBissexto = False

    elif ano % 100 == 0 and ano % 400 != 0:
        anoBissexto = False

    return anoBissexto


# -------------------------------------------------
def dataValida(dia, mes, ano):
    dataValida = True

    diaInvalido = (dia < 1 or dia > 31)
    mesInvalido = (mes < 1 or mes > 12)

    if diaInvalido or mesInvalido:
        dataValida = False

    if dia == 31 and mesDe30Dias(mes):
        dataValida = False

    if mes == 2 and dia > 28:
        if dia > 29:
            dataValida = False
        if not anoBissexto(ano):
            dataValida = False

    return dataValida


# -------------------------------------------------
def somarDiasData(dia, mes, ano, qtdDias):
    dia = dia + qtdDias

    while dia > 31:

        if not mesDe30Dias(mes) and mes != 2:
            result = somarDiasCalculo(dia, mes, 31)

        elif mesDe30Dias(mes):
            result = somarDiasCalculo(dia, mes, 30)

        elif mes == 2 and dia > 28:
            if dia >= 29:
                if anoBissexto(ano):
                    result = somarDiasCalculo(dia, mes, 29)
                else:
                    result = somarDiasCalculo(dia, mes, 28)

        dia = result[0]
        mes = result[1]

        if mes > 12:
            mes = 1
            ano = ano + 1

    return dia, mes, ano


# -------------------------------------------------
def somarDiasCalculo(dia, mes, diasNoMes):
    dia = dia - diasNoMes
    mes = mes + 1
    return dia, mes


# -------------------------------------------------
def subtrairDiasData(dia, mes, ano, qtdDias):
    if dia <= qtdDias:

        while dia - qtdDias < 1:

            if not mesDe30Dias(mes - 1) and (mes - 1) != 2:
                result = subtrairDiasCalculo(qtdDias, dia, mes, 31)

            elif mesDe30Dias(mes - 1):
                result = subtrairDiasCalculo(qtdDias, dia, mes, 30)

            elif (mes - 1) == 2:
                if anoBissexto(ano):
                    result = subtrairDiasCalculo(qtdDias, dia, mes, 29)
                else:
                    result = subtrairDiasCalculo(qtdDias, dia, mes, 28)

            qtdDias = result[0]
            dia = result[1]
            mes = result[2]

            if mes < 1:
                mes = 12
                ano = ano - 1

    else:
        dia = dia - qtdDias

    return dia, mes, ano


# -------------------------------------------------
def subtrairDiasCalculo(qtdDias, dia, mes, diasNoMes):
    qtdDias = qtdDias - diasNoMes
    dia = dia - qtdDias
    mes = mes - 1
    return qtdDias, dia, mes


# -------------------------------------------------
def qtdDiasEntreDatas(diaData1, mesData1, anoData1, diaData2, mesData2, anoData2):
    totalMeses = ((anoData2 - anoData1) + 1) * 12
    mes1 = 12 - ((12 - mesData1) + 1)
    mes2 = 12 - mesData2
    qtdMeses = totalMeses - mes1 - mes2

    qtdDias = 0
    while qtdMeses > 0:

        if not mesDe30Dias(mesData1) and mesData1 != 2:
            result = somarDiasEntreDatas(qtdDias, diaData1, mesData1, diaData2, 31)
        elif mesDe30Dias(mesData1):
            result = somarDiasEntreDatas(qtdDias, diaData1, mesData1, diaData2, 30)

        elif mesData1 == 2:
            if anoBissexto(anoData1):
                result = somarDiasEntreDatas(qtdDias, diaData1, mesData1, diaData2, 29)
            else:
                result = somarDiasEntreDatas(qtdDias, diaData1, mesData1, diaData2, 28)

        qtdDias = result[0]
        diaData1 = result[1]
        mesData1 = result[2]
        abaterDias = result[3]

        qtdMeses = qtdMeses - 1

        if mesData1 > 12:
            mesData1 = 1
            anoData1 = anoData1 + 1

    if anoData1 == anoData2:
        qtdDias = qtdDias - abaterDias

    return qtdDias


# -------------------------------------------------
def somarDiasEntreDatas(qtdDias, diaData1, mesData1, diaData2, diasNoMes):
    qtdDias = qtdDias + (diasNoMes - diaData1)
    mesData1 = mesData1 + 1
    diaData1 = 0
    abaterDias = diasNoMes - diaData2

    return qtdDias, diaData1, mesData1, abaterDias
