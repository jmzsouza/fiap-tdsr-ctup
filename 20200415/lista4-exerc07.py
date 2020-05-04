# lista4CT2020.pdf
# Exercício 7
# A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = (5 / 9) * (F − 32).
# Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
# graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.

fahrenheit = 50
print("Fahrenheit | Celsius")
while fahrenheit <= 100:
    celsius = (5 / 9) * (fahrenheit - 32)
    print("    {}     |    {:.2f}   ".format(fahrenheit, celsius))
    fahrenheit += 1
