# lista4CT2020.pdf
# Exercício 12
# Se Fn é o n-ésimo número da sequência de Fibonacci, podemos calculá-la através da seguinte fórmula de recorrência:
# 1º termno F1= 1  - Fórmula: Fn = Fn - 1 + Fn - 2


sequencia = int(input("Qual n-ésimo número da sequência de Fibonacci deseja saber? "))

seqRecebida = sequencia
contador = 1

if sequencia > 0:

    penultimo = 0
    ultimo = 1
    numFibonnacci = str(ultimo)

    while sequencia > 1:

        resultado = ultimo + penultimo
        penultimo = ultimo
        ultimo = resultado
        sequencia = sequencia - 1
        numFibonnacci = numFibonnacci + ", " + str(resultado)

else:
    print("Informe apenas um número inteiro positivo!")

print("F{} = {}".format(seqRecebida, numFibonnacci))