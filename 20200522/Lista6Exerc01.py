# lista6CT-2020.pdf
# Exercício 1
# Crie uma função em Python que recebe uma String e retorna uma outra String com os mesmos caracteres só que em caixa alta. 

def caixaAlta(string):
    resp = ""
    i = 0

    while i < len(string):
        resp = resp + string[i].upper()
        i = i + 1

    return resp

resposta = caixaAlta(input("Digite uma palavra: "))
print(resposta)

