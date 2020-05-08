# listaExtraRepeticaoCT-2020.pdf
# Exercício 1
# Vamos escrever um programa que consiste em um Jogo de Adivinhação.
# O jogo funciona do seguinte modo: sorteia-se um número inteiro aleatório entre 1 e 1000.
# Sua tarefa é tentar adivinhar o número sorteado através de "chutes".
# A cada chute o programa deverá informar se o número "sorteado" é maior, menor ou igual ao número "chutado".
# Quando o usuário acertar o número deverá ser impresso uma mensagem dizendo que ele acertou e a quantidade
# de chutes dados.

import random

sorteado = random.randint(1, 1001)
chute = int(input("Tentativa: "))
tentativas = 1

while chute != sorteado:
    if chute < sorteado:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
    chute = int(input("Tentativa: "))
    tentativas = tentativas + 1

print("Você acertou! {} chutes".format(tentativas))
