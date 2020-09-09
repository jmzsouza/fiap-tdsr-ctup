# lista8CT-2020.pdf
# Exercício 4
# Escreva um programa que pede para o usuário digitar um inteiro n. 
# Depois seu algoritmo pede para o usuário digitar uma sequência de n números reais. 
# Após a entrada dos dados, seu programa deverá imprimir os resultados das seguintes somas: 
# v[0] +v[n−1] , v[1] +v[n−2], v[2] + v[n − 3], ...; até que todos os valores informados tenham participado de alguma soma.

n = int(input("Digite n: "))
i = 0
v = []
while i < n:
    num = float(input("Número real: "))
    v.append(num)
    i = i + 1

i = 0
j = n - 1
while i <= j:
    print(v[i] + v[j])
    i = i + 1
    j = j - 1


