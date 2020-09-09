# lista8CT-2020.pdf
# Exercício 13
# Considere um corredor com mil portas, numeradas de 1 a 1000, que se encontram todas fechadas. 
# Por esse corredor passarão mil pessoas, que modicarão o estado das portas cujo número seja múltiplo do seu número de passagem: 
# a pessoa com o número 3 modicará o estado (fechará se estiverem abertas ou abrirá se estiverem fechadas) das portas nº 3, 6, 9, 12, ... 
# e a pessoa com o número 7 fará o mesmo às portas 7, 14, 21, etc. 
# Construa um programa que permita saber quantas são e quais são as portas abertas após a passagem da milésima pessoa. 
# Dica: use uma lista onde você armazena valores True ou False com 1001 posições para representar as portas. 
# Dica, crie uma função para ajudar a resolver o problema.

def passagem(pessoa, portas):

    i = 1

    while i < len(portas):
        if i % pessoa == 0:
            if portas[i] == True:
                portas[i] = False
            else:
                portas[i] = True
        i = i + 1

portas = [False] * 1001
for pessoa in range(1, 1001):
    passagem(pessoa, portas)

i = 1
while i < len(portas):
    if portas[i]:
        print("Porta aberta: ", i)
    i = i + 1







