# IMC
# import math
# def imc(peso, altura):
#     imc = peso / math.pow(altura, 2)
#     if (imc < 18.5):
#         return "Abaixo do peso normal"
#     elif (imc > 18.5 and imc < 25):
#         return "Peso normal"
#     elif (imc >= 25 and imc < 30):
#         return "Excesso de peso"
#     elif (imc >= 30 and imc < 35):
#         return "Obesidade classe I"
#     elif (imc >= 35 and imc < 40):
#         return "Obesidade classe II"
#     else:
#         return "Obesidade classe III"
    
# peso = float(input("Digite o peso em Kg: "))
# altura = float(input("Digite a altura em Metros: "))

# print(imc(peso, altura))

# Quadrado
import math
def quadrado(num):
    return math.pow(num, 2)

print(quadrado(750))