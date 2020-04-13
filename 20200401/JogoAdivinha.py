import random

sorteado = random.randrange(1, 11)

num = 1
while num <= 3:
    chance = int(input("Divite um número entre 1 a 10 para tentar adivinhar o número sorteado: "))
    if chance < sorteado:
        print("O número é menor que o sorteado.")
        num = num + 1
    elif chance > sorteado:
        print("O número é maior que o sorteado.")
        num = num + 1
    else:
        print("você adivinhou")