# Desafio 1

# velocidade = int(input("Digite a Velocidade do carro: "))
# multa = (velocidade - 80) * 5

# if(velocidade <= 100):
#     print("Você não foi multado")
# elif (velocidade > 150):
#     print(f"Você foi multado no valor de: R${multa}")


# Desafio 2

# num1 = int(input("Escreva o primeira número: "))
# num2 = int(input("Escreva o segundo número: "))
# num3 = int(input("Escreva o terceiro número: "))

# if(num1 > num2 and num3 < num2):
#     print(f"Maior: {num1} Menor: {num3}")
# elif(num2 > num1 and num3 < num1):
#     print(f"Maior: {num2} Menor: {num3}")
# elif(num3 > num2 and num1 < num2):
#     print(f"Maior: {num3} Menor: {num2}")


# Desafio 3

num1 = int(input("Escreva o primeira número: "))
num2 = int(input("Escreva o segundo número: "))
operacao = input("Escolha uma das operações matemáticas: ")

if(operacao == "multiplicação" or operacao == "Multiplicação" 
   or operacao == "Multiplicacaoo" or operacao == "multiplicacaoo"):
    resultado = num1 * num2
    print(f"O resultado de {num1} X {num2} = {resultado}")

elif(operacao == "divisão" or operacao == "Divisão" 
   or operacao == "Divisao" or operacao == "divisao"):
    resultado = num1 / num2
    print(f"O resultado de {num1} / {num2} = {resultado}")

elif(operacao == "Subtração" or operacao == "subtração" 
   or operacao == "Subtracao" or operacao == "subtracao"):
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} = {resultado}")

elif(operacao == "Soma" or operacao == "soma"):
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} = {resultado}")

elif(operacao == "Potência" or operacao == "potência"
    or operacao == "Potencia" or operacao == "potencia"):
    resultado = num1 ** num2
    print(f"O resultado de {num1} /\ {num2} = {resultado}")

elif(operacao == "Porcentagem" or operacao == "porcentagem"):
    resultado = (num1 / 100) * num2
    print(f"O resultado de {num1} porcento de {num2} = {resultado:.2f}")