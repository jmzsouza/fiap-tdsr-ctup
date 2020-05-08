# TrabalhoComputationalThinking-2020.pdf
# Exercício 2
# O salário mensal de um professor, sem considerar os impostos, corresponde a soma dos seguintes valores:
# salário base, hora-atividade e descanso semanal remunerado (DSR). Para calcular o salário base multiplicamos
# o número de aulas semanais por 4,5 semanas e pelo valor hora-aula, o descanso semanal remunerado corresponde
# a 1/6 do salário base e a horaatividade corresponde a 5% da soma do salário base com o descanso semanal remunerado.
# Escreva um algoritmo que calcula e imprime o valor do salário base, o valor da hora-atividade, o valor do DSR
# e o valor do salário mensal. A entrada do algoritmo será o número de aulas semanais e valor hora-aula,
# não se preocupe com a validação de dados.

aulaSemanais = int(input("Informe o total de aulas lecionadas na semana: "))
horaAula = float(input("Informe o valor hora aula: "))

salarioBase = aulaSemanais * 4.5 * horaAula
dsr = salarioBase * (1 / 6)
horaAtividade = 0.05 * (salarioBase + dsr)
salarioMensal = salarioBase + horaAtividade + dsr

print("\nVALORES"
      "\nSalário Base....: {:.2f}"
      "\nDSR.............: {:.2f}"
      "\nHora-Atividade..: {:.2f}"
      "\nSalário Mensal..: {:.2f}".format(salarioBase, dsr, horaAtividade, salarioMensal))