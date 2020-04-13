# lista3CT2020.pdf
# Exercício 11
# Escreva um algoritmo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# código: 1 -> condição de pagamento: A vista em dinheiro ou cheque, recebe 10% de desconto
# código: 2 -> condição de pagamento: A vista no cartão de crédito, recebe 5% de desconto
# código: 3 -> condição de pagamento: Em duas vezes, preço normal de etiqueta sem juros.
# código: 4 -> condição de pagamento: Em quatro vezes, preço normal de etiqueta mais juros de 7%

valorProduto = float(input("Digite o valor de um produto: "))
condicao = int(input("Digite o código da condição de pagamento desejada: "))

if condicao == 1:
    valorFinal = valorProduto - (valorProduto * 0.1)
elif condicao == 2:
    valorFinal = valorProduto - (valorProduto * 0.05)
elif condicao == 3:
    valorFinal = valorProduto
elif condicao == 4:
    valorFinal = valorProduto + (valorProduto * 0.07)
else:
    valorFinal = "Valor indefinido, pois a condição de pagamento é inválida."

print("\nValor do produto.......: " + str(valorProduto) +
      "\nCondição de pagamento..: " + str(condicao) +
      "\nValor final............: " + str(valorFinal))
