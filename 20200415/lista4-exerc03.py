# lista4CT2020.pdf
# Exercício 3
# Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5,
# (0 ≤ nota < 5, 0) e acima de 5, 0 (nota ≥ 5, 0).

quantidadeDeAlunos = int(input("Digite uma quantidade de alunos de uma turma: "))

contador = 1
somaDeNotas = 0
notaDeZeroACinco = 0
notaAcimaDeCinco = 0

while contador <= quantidadeDeAlunos:
    notaDoAluno = float(input("Digite a nota do aluno " + str(contador) + ": "))
    while notaDoAluno < 0 or notaDoAluno > 10:
        notaDoAluno = float(input("Digite uma nota válida para o aluno " + str(contador) + ": "))
    if 0 <= notaDoAluno < 5.0:
        notaDeZeroACinco += 1
    else:
        notaAcimaDeCinco += 1
    somaDeNotas += notaDoAluno
    contador += 1

mediaDaTurma = somaDeNotas / quantidadeDeAlunos

print("\nA média das notas da turma é..:", str(mediaDaTurma) +
      "\nAlunos com nota até 4.9.......:", str(notaDeZeroACinco) +
      "\nAluno com nota acima de 5.0...:", str(notaAcimaDeCinco))