# lista8CT-2020.pdf
# Exercício 11
# Na Copa do Mundo do Brasil os quadrifinalistas foram, em ordem alfabética: 
# Alemanha, Argentina, Bélgica, Brasil, Colômbia, Costa Rica, França e Holanda. 
# Imaginando que não sabemos os resultados e nem os cruzamentos, 
# escreva um algoritmo que gere todos os possíveis campeões e vice-campeões dentre os oito times.

def imprimeSegundosColocados(primeiro, lista):
    for segundo in lista:
        if segundo != primeiro:
            print(primeiro, segundo)

def imprimeTudo(lista):
    for time in lista:
        imprimeSegundosColocados(time, lista)

times = ["Alemanha", "Argentina", "Belgica", "Brasil", "Colombia", "Costa Rica", "Franca", "Holanda"]
imprimeTudo(times)