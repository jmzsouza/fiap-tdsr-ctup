# lista6CT-2020.pdf
# Exercício 5
# Dados dois strings (um contendo uma frase e outro contendo uma palavra), determine o número de vezes que a palavra ocorre na frase. 
# Exemplo: Para a palavra ANA e a frase: ANA E MARIANA GOSTAM DE BANANA
# Temos que a palavra ocorre 4 vezes na frase. Escreva um programa que resolve o problema acima, 
# seu programa deverá receber as duas strings e retornar o número de ocorrências da palavra na frase.

def encontra(frase, palavra):
    i = 0
    ocorrencias = 0
    while i < len(frase):
        if frase[i:i+len(palavra)] == palavra:
            ocorrencias = ocorrencias + 1
        i = i + 1
    return ocorrencias

frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra que deseja localizar na frase: ").lower()

teste = encontra(frase, palavra)
print("Ocorrências:", teste)