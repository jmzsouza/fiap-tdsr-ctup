#lista2CT2020.pdf
#Exercício 9
#Dados o preço de um produto e um percentual de desconto, 
#escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual. 
#E se, ao invés de um desconto, fosse um aumento. O que muda no seu algoritmo?

valor = input('Digite o valor de um produto: ')
produto = float(valor)

valor = input('Digite o valor de um percentual: ')
percentual = int(valor)

desconto = produto * (percentual / 100)
aumento = produto * (percentual / 100)

print('o produto terá o desconto de:', desconto,'e seu novo valor é:', produto - desconto)
print('o produto terá o aumento de:', aumento,'e seu novo valor é:', produto + aumento)

