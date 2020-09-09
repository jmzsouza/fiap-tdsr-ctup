# lista8CT-2020.pdf
# Exercício 3
# Escreva um algoritmo que pede para o usuário digitar 10 strings uma de cada vez. 
# Depois que o usuário digitar todas elas, seu programa deverá imprimir as strings na ordem inversa de leitura. 
# Por exemplo se as duas últimas strings foram, respectivamente, avestruz e onça; o programa imprime onça e depois avestruz.

listaStrings = []
i = 0
while i <= 10:
    string = input("Digite uma palavra: ")
    listaStrings.append(string)
    i = i + 1

i = len(listaStrings) - 1
while i >= 0:
    print(listaStrings[i])
    i = i + 1



