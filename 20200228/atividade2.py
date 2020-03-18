#Algoritmos1.pdf
#Atividade 2
#Dados um preço de um produto e o percentual de desconto, calcule o novo preço do produto.

valor = input("Digite o preço de um produto: ")
preco = int(valor)
valor = input("Digite o percentual de desconto: ")
desconto = float(valor)

soma = preco - (preco * desconto / 100)

print("O novo preço é: ", soma)