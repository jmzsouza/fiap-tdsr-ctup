# Listas.pdf
# Problema 2
# Já vimos como calcular a média aritmética de vários números. 
# Sua tarefa agora é escrever uma função que recebe umalista contendo número reais e retorna o maior número e o menor número da lista. 
# O retorno do seu método deverá ser na forma de tuplas.

def maiorMenor(conjunto):
    max = conjunto[0]
    min = conjunto[0]
    i = 1
    while i < len(conjunto):
        if conjunto[i] < min:
            min = conjunto[i]
        if conjunto[i] > max:
            max = conjunto[i]
        i = i + 1

    return (min, max)

lista = [3.2, -0.1, 8.9, 5.4, -3.1, 6.2, 10]
resultado = maiorMenor(lista)
print(resultado)