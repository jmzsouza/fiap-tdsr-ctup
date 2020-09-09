# lista8CT-2020.pdf
# Exercício 1
# Escreva um programa que cria uma lista de strings e preenche essa lista com 10 valores que
# serão digitados pelo usuário. Imprima a lista na tela.

i = 0
lista = []
while i < 10:
    valor = input("Digite um valor ou uma palavra: ")
    lista.append(valor)
    i = i + 1

for info in lista:
    print(lista)

