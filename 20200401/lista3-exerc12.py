# lista3CT2020.pdf
# Exercício 12
# Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de Computational Thinking,
# o número de aulas ministradas e o número de aulas assistidas por este aluno nesta disciplina.
# Calcule e mostre a média final deste aluno e diga se ele foi aprovado ou reprovado ou está de exame.
# Lembrando que a média do primeiro semestre tem peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentado mais de 70% das aulas.


mediaPrimeiroSemestre = float(input("Qual o valor na média semestral do 1º semestre? "))
mediaSegundoSemestre = float(input("Qual o valor na média semestral do 2º semestre? "))
aulasMinistradas = int(input("Qual o total de aulas ministradas? "))
aulasAssistidas = int(input("Qual o total de aulas assistidas/ "))

mediaFinal = mediaPrimeiroSemestre * 0.4 + mediaSegundoSemestre * 0.6
frequencia = aulasAssistidas * 100 / aulasMinistradas

if frequencia >= 70 and mediaFinal >= 6.0:
    situacao = "Aprovado"
elif frequencia >= 70 and 4.0 <= mediaFinal <= 5.9:
    situacao = "Exame"
elif frequencia >= 70 and 0 <= mediaFinal <= 3.9:
    situacao = "Reprovado"
else:
    situacao = "Reprovado"

print("\nFrequência na disciplina.: " + str(frequencia) +
      "\nMedia Final..............: " + str(mediaFinal) +
      "\nSituação.................:", situacao)
