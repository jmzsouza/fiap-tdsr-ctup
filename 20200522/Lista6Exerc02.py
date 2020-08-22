# lista6CT-2020.pdf
# Exercício 2
# Crie uma função em Python que recebe uma String e retorna uma outra String com os mesmos caracteres só que em caixa alta. 

def intercala(palavra):
    resp = ""
    i = 0

    while i < len(palavra):
        resp = resp + palavra[i + 1] + " "
        i = i + 1

    return resp

t = intercala(input(""))
print(t)