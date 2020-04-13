# lista3CT2020.pdf
# Exercício 8
# Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a tabela a seguir:
# Categoria: Infantil ----> Idade: 5 a 7
# Categoria: Juvenil -----> Idade: 8 a 10
# Categoria: Adolescente -> Idade: 11 a 15
# Categoria: Adulto ------> Idade: 16 a 30
# Categoria: Senior ------> Idade: acima de 30

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 7:
    categoria = "Infantil"
elif idade >= 8 and idade <= 10:
    categoria = "Juvenil"
elif idade >= 11 and idade <= 15:
    categoria = "Adolescente"
elif idade >= 16 and idade <= 30:
    categoria = "Adulto"
elif idade > 30:
    categoria = "Senior"
else:
    categoria = "Indefinida"

print("Para a idade " + str(idade) + " a categoria de nadador é: " + categoria + ".")