# lista4CT2020.pdf
# Exercício 6
# Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que cada questão vale 1 ponto,
# escreva um algoritmo que lê a pontuação da prova obtida de cada um dos candidatos e calcula:
# a) a maior e a menor nota
# b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram
# de 21 a 50 e o percentual que acertou acima de 50 questões

nota = int(input("Digite a nota do candidato 1: "))

notaMaior = nota
notaMenor = nota

contador = 2

contadorAte20 = 0
contador20a50 = 0
contadorAcima50 = 0

while contador <= 20:
    nota = int(input("Digite a nota do candidato {}: ".format(contador)))
    if 0 < nota <= 70:
        if nota > notaMaior:
            notaMaior = nota
        if nota < notaMenor:
            notaMenor = nota

        if nota <= 20:
            contadorAte20 += 1
        elif nota <= 50:
            contador20a50 += 1
        else:
            contadorAcima50 += 1

        contador += 1

        percentualAte20 = (contadorAte20 / 20) * 100
        percentual20a50 = (contador20a50 / 20) * 100
        percentualAcima50 = (contadorAcima50 / 20) * 100

print("\nA maior nota é: ", str(notaMaior) +
      "\nA menor nota é: ", str(notaMenor) +
      "\nO percentual de candidatos que acertaram até 20 questões.......: {}%".format(percentualAte20) +
      "\nO percentual de candidatos que acertaram de 21 até 50 questões.: {}%".format(percentual20a50) +
      "\nO percentual de candidatos que acertaram acima de 50 questões..: {}%".format(percentualAcima50))
