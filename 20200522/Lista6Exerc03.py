# lista6CT-2020.pdf
# Exercício 3
# Escreva uma função que recebe duas Strings: frase e letra; a frase representa um conjunto de caracteres e letra um único caracter. 
# Sua função deverá substituir toda ocorrência do caracter letra contido frase pelo caracter *. 
# Por exemplo, se frase for "Jabuticaba" e a letra for "a"então seu método deverá retornar "J*butic*b*". 
# Note que, sua função deverá funcionar independente da letra ser maiúscula ou minúscula, ou seja, toda letra "a"e "A"deve ser substituída. 
# Considere que não há caracteres acentuados nas palavras e não deve ser usado o método replace neste exercício.

def substitui(frase, letras):
    resp = ""

    for c in frase:
       if c in letras:
           resp = resp + "*"
       else:
           resp = resp + c
        
    resp = resp[0].upper() + resp[1:len(resp)]

    return resp

f = input("Digite uma frase: ").lower()
l = input("Digite uma letra que deseja subtituir por *: ").lower()

teste = substitui(f, l)

print(teste)