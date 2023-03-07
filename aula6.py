# Problema: verificar se o número do usuário é negativo ou positivo
# number = float(input("Digite um número: "))

# if(number > 0.0):
#     print("O número digitado é positivo")
# elif(number < 0.0):
#     print("O número digitado é negativo")
# elif(number == 0.0):
#     print("O número digitado é igual a zero")


# Problema: Fazer uma calculadora de IMC
# peso = float(input("Digite seu peso em Kg: "))
# altura = float(input("Digite sua algura em Metros: "))
# imc = round(peso / (pow(altura, 2)), 2)

# if(imc < 18.5):
#     print("Seu peso está baixo")
# elif(imc >= 18.8 and imc < 24.9):
#     print("Seu peso está normal")
# elif(imc >= 25 and imc < 29.9):
#     print("Você está acima do peso")
# else:
#     print("Você está com obesidade")


# problema: encontrar o maior número
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if(a > b and b > c):
    print(f"Maior: {a}, Menor: {c}")
elif(a > c and c > b):
    print(f"Maior: {a}, Menor: {b}")
elif(b > a and a > c):
    print(f"Maior: {b}, Menor: {c}")
elif(c > a and a > b):
    print(f"Maior: {c}, Menor: {b}")
elif(c > b and b > a):
    print(f"Maior: {c}, Menor: {a}")
