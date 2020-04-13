# Problema 4.4: Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.

nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida, digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida,  digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("A média vale {:.2f}".format(media))
