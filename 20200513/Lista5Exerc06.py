# lista5CT-2020.pdf
# Exercício 6
# Usando a função do item anterior, faça um programa que lê dois inteiros positivos a e b e
# verifica se o menor deles é segmento do outro.

from Lista5Funcoes import *

a = int(input("A: "))
b = int(input("B: "))

if a > b and encaixou(a, b):
    print("b é segmento de a")
elif b > a and encaixou(b, a):
    print("a é segmento de b")
elif a == b and encaixou(a, b):
    print("um é seguimento do outro")
else:
    print("um não é seguimento do outro")
