#Algoritmos1.pdf
#Atividade 4
#Considere a equação de segundo grau  x² + 3x − 10 = 0, encontre as raízes da equação.

a = 1.0
b = 3.0
c = -10.0

delta = (b ** 2.0) - 4 * a * c
raiz = float(delta) ** 0.5

x1 = (-b + raiz) / (2.0 * a)
x2 = (-b - raiz) / (2.0 * a)

print("O valor de delta: ", delta)
print("O valor de x1: ", x1)
print("O valor de x2: ", x2)