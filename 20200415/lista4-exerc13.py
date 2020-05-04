# lista4CT2020.pdf
# Exercício 13
# Dizemos que um número natural n é palíndromo se o 1º algarismo de n é igual ao seu último
# algarismo, o 2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente.
# Exemplos: 567765 e 32423 são palíndromos. 567675 não é palíndromo.

num = int(input("Digite um número: "))

numOriginal = num
resp = 0

while num != 0:
    d = num % 10
    num = num // 10
    resp = resp * 10 + d

if numOriginal == resp:
    print("O número {} é palídrome".format(numOriginal))
else:
    print("O número {} não é palídrome".format(numOriginal))
