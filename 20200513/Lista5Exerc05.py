# lista5CT-2020.pdf
# Exercício 5
# Construa uma função encaixa que dados dois inteiros positivos a e b verifica se b corresponde aos últimos dígitos de a.

from Lista5Funcoes import *

a = int(input("A: "))
b = int(input("B: "))

if encaixa(a, b):
    print("Encaixa")
else:
    print("Não encaixa")