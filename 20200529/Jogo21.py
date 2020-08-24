import Baralho
import random


def compra(baralho):
    pos = random.randint(0, 51)
    return baralho[pos]


def valor(carta):
    if carta[0] > 10:
        return 10
    else:
        return carta[0]


deck = Baralho.getBaralho()
suaPontuacao = 0
cpuPontuacao = 0

i = 1
while i <= 2:
    card = compra(deck)
    auxImg = Baralho.getImagem(card)
    print(auxImg)
    suaPontuacao = suaPontuacao + valor(card)
    i = i + 1

print("Sua pontuação: ", suaPontuacao)

i = 1
while i <= 2:
    card = compra(deck)
    cpuPontuacao = cpuPontuacao + valor(card)
    i = i + 1
    
resp = input("Você quer mais cartas (S/N)? ")
while resp == "S":
    card = compra(deck)
    auxImg = Baralho.getImagem(card)
    print(auxImg)
    suaPontuacao = suaPontuacao + valor(card)
    print("Sua pontuação: ", suaPontuacao)
    resp = input("Você quer mais cartas (S/N)? ")

while cpuPontuacao < 16:
    card = compra(deck)
    cpuPontuacao = cpuPontuacao + valor(card)

if cpuPontuacao > 21 and suaPontuacao > 21:
    print("Ambos perderam!")
elif cpuPontuacao > 21:
    print("Você ganhou!")
elif suaPontuacao > 21:
    print("CPU ganhou!")
elif cpuPontuacao > suaPontuacao:
    print("CPU ganhou!")
elif suaPontuacao > cpuPontuacao:
    print("Você ganhou!")
else:
    print("Empate!")

print("Sua pontuação: ", suaPontuacao)
print("CPU pontuação: ", cpuPontuacao)
