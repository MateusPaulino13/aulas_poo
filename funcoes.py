# def mostrarNome(nome):
#     print(f"Seu nome é: {nome}")

# mostrarNome("Mateus")

# def Dobro(x):
#     return x * 2

# print(Dobro(10))

# def areaQuadrado(base, altura):
#     area = (altura * base) / 2
#     return area

# base = float(input("Digite o numero da base do triangulo: "))
# altura = float(input("Digite o numero da altura do triangulo: "))

# print(f"A área do triângulo é de: {areaQuadrado(base, altura)}m²")



# exercicios
# def boasVindas(nome):
#     print(f"Seja muito bem-vindo(a) : {nome}")

# n = input("Coloque seu nome: ")
# boasVindas(n)

import math as mt

def Elevar(base, expoente):
    return mt.pow(base, expoente)

b = float(input("Digite um número para a base: "))
e = float(input("Digite um número para o expoente: "))

print(f"O Resultado foi de: {Elevar(b,e)}")