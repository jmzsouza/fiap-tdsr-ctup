# lista3CT2020.pdf
# Exercício 9
# No exercício da calculadora, visto em sala de aula, temos um problema com a operação de divisão.
# Sua tarefa será exibir uma mensagem informando que é impossível fazer uma divisão por 0.
# Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer tal operação.

numA = float(input("Digite um número: "))
op = input("Operador (+-*/): ")
numB = float(input("Digite outro número: "))

soma = (op == "+")
subtracao = (op == "-")
multiplicacao = (op == "*")
divisao = (op == "/")

if soma:
    resultado = numA + numB
elif subtracao:
    resultado = numA - numB
elif multiplicacao:
    resultado = numA * numB
else:
    if divisao and numB == 0:
        resultado = "Impossível realizar a divisão por 0."
    else:
        resultado = numA / numB

print("Resposta:", resultado)