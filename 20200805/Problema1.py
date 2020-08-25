# Listas.pdf
# Problema 1
# Considere uma turma de n alunos onde desejamos calcular a média das notas do N2020 
# e saber quantos alunos estão acima ou iguais a média e quantos alunos estão abaixo da média.
# Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos e cada uma das n notas. 
# Depois calcula e exibe a média da turma e as quantidades de alunos que estão abaixo da média ou que estão, pelo menos, na média da sala.

n = int(input("Digite a quantidade de alunos: "))

i = 0
soma = 0

notasAluno = []

while i < n:
    nota = float(input("Nota: "))
    soma = soma + nota
    i = i + 1
    notasAluno.append(nota)

media = soma / n
print("Média da turma: {}".format(media))

contaMenos = 0
for nota in notasAluno:
    if nota < media:
        contaMenos = contaMenos + 1

print("{} alunos abaixo da média".format(contaMenos))
print("{} alunos acima da média".format(n - contaMenos))

