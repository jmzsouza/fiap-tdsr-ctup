# lista3CT2020.pdf
# Exercício 5
# A jornada de trabalho diária de um trabalhador é de 8 horas.
# Caso o trabalhador tenha trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra.
# O valor da hora-extra é o valor que ele recebe por hora acrescido de 50%.
# Supondo que ele trabalhe apenas nos dias úteis, escreva um algoritmo que recebe:
# a) o total de dias úteis de um mês
# b) o total de horas trabalhadas pelo trabalhador
# c) quanto o trabalhador recebe por hora
# Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário nal do trabalhador.

diasUteis = int(input("Digite o total de dias uteis de um mês: "))
horaTrabalhada = int(input("Digite o total de horas trabalhadas: "))
valorHora = float(input("Digite o valor de cada hora: "))

horaExtra = horaTrabalhada - diasUteis * 8
salarioBase = diasUteis * 8 * valorHora

if horaExtra <= 0:
    valorHoraExtra = horaExtra * valorHora
    salarioLiquido = horaTrabalhada * valorHora
else:
    valorHoraExtra = horaExtra * valorHora + horaExtra * valorHora * 0.5
    salarioLiquido = salarioBase + valorHoraExtra

print("\nDias úteis..................: " + str(diasUteis) +
      "\nJornada mensal exigida......: " + str(diasUteis * 8) +
      "\nValor Hora..................: " + str(valorHora) +
      "\nSalário base................: " + str(salarioBase) +
      "\nHoras trabalhadas...........: " + str(horaTrabalhada) +
      "\nTotal horas extras/devida...: " + str(horaExtra) +
      "\nValor horas extras/devida...: " + str(valorHoraExtra) +
      "\nSalário líquido.............: " + str(salarioLiquido))
