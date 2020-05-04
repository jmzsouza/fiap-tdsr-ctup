# lista4CT2020.pdf
# Exercício 2
# Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
# determinar a média das notas dessa turma. Considere que o usuário digite as informações corretamente.

quantidadeDeAlunos = int(input("Digite uma quantidade de alunos de uma turma: "))

contador = 1
somaDeNotas = 0

while contador <= quantidadeDeAlunos:
    notaDoAluno = float(input("Digite a nota do aluno " + str(contador) + ": "))
    while notaDoAluno < 0 or notaDoAluno > 10:
        notaDoAluno = float(input("Digite uma nota válida para o aluno " + str(contador) + ": "))
    somaDeNotas += notaDoAluno
    contador += 1

mediaDaTurma = somaDeNotas / quantidadeDeAlunos

print("A média das notas da turma é:", str(mediaDaTurma))