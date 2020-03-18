#lista2CT2020.pdf
#Exercício 13
#Uma disciplina da faculdade possui 3 tipos de avaliações: NAC, AM e PS. 
#A média da disciplina é calculada de forma ponderada, onde a NAC tem peso 2, o AM peso 3 e a PS peso 5.
#Escreva um algoritmo que calcula a média da disciplina, 
#seu algoritmo deverá receber as três notas (NAC, AM e PS) e deverá imprimir o valor da média.
#MEDIA = (2 ∗ NAC + 3 ∗ AM + 5 ∗ P S)/10

valor = input('Qual o valor na nota NAC? ')
nac = float(valor)

valor = input('Qual o valor na nota AM? ')
am = float(valor)

valor = input('Qual o valor na nota PS? ')
ps = float(valor)

media = (2*nac+3*am+5*ps)/10

print('A média da disciplina é:',media)
