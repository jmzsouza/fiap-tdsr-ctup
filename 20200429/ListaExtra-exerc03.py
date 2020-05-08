# listaExtraRepeticaoCT-2020.pdf
# Exercício 3
# Dados um inteiro n e uma seqüência de n números inteiros, determinar o comprimento de
# um segmento crescente de comprimento máximo.
# Exemplos:
# Na seqüência 5, 10, 3, 2, 4, 7, 9, 8, 5 o comprimento do segmento crescente máximo é 4.
# Na seqüência 10, 8, 7, 5, 2 o comprimento de um segmento crescente máximo é 1.

n = int(input("Digite o tamanho da sequencia: "))

anterior = int(input("Informe um número: "))
comprimento = 1
maior = 1
contador = 1

while contador < n:
    atual = int(input("Informe um número: "))
    contador = contador + 1

    if anterior < atual:
        comprimento = comprimento + 1
    else:
        if comprimento > maior:
            maior = comprimento
        comprimento = 1
    anterior = atual

if comprimento > maior:
    maior = comprimento

print("A maior segmento crescente tem tamanho:", maior)