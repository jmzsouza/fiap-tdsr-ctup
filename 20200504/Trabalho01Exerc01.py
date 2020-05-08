# TrabalhoComputationalThinking-2020.pdf
# Exercício 1
# Um vendedor recebe um salário xo de R$ 500,00 reais mais comissões sobre suas vendas.
# Porém o percentual das comissões são diferentes de acordo com a classicação dos produtos.
# Veja a tabela abaixo indicando a categoria e os respectivos percentuais.
# categoria ---> descrição -------------> comissão (%)
# 1 -----------> camisetas e polos -----> 4,0
# 2 -----------> calças e camisas ------> 5,5
# 3 -----------> jaquetas e agasalhos --> 7,0
# 4 -----------> ternos e sobretudos ---> 8,5
# Sua tarefa será a de escrever um algoritmo que calcula o salário mensal do funcionário.
# Observe que faz parte do exercício você definir as informações que serão fornecidas pelo
# usuário para o cálculo do salário.

categoriaProduto = int(input("Informe a categoria do produto: "))
valorVendas = float(input("Informe o valor total de vendas da categoria: "))

salarioFixo = 500.0

if categoriaProduto == 1:
    comissao = valorVendas * 0.04
elif categoriaProduto == 2:
    comissao = valorVendas * 0.055
elif categoriaProduto == 3:
    comissao = valorVendas * 0.07
elif categoriaProduto == 4:
    comissao = valorVendas * 0.085
else:
    comissao = valorVendas * 0

salarioMensal = salarioFixo + comissao

print("O salário mensal do funcionário é: {:.2f}".format(salarioMensal))
