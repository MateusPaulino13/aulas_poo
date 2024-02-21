# positivo, negativo ou nulo
# num = float(input("Digite um número: "))

# if(num > 0):
#     print("O número escolhido é: POSITIVO")
# elif(num < 0):
#     print("O número escolhido é: NEGATIVO")
# elif(num == 0 or num is None):
#     print("O número escolhido é: ZERO ou NULO")


# 33 ou não
# for i in range(6):
#     num = int(input("Digite um número: "))

#     if(num == 33):
#         print("O número digitado é: 33")
#         break
    
#     if(num != 33):
#         print("O número digitado é diferente de: 33")
#         continue


# Jogo mágico
import random as rd

tentativas = 5
certo = rd.randint(0, 100)

print("||--Adivinhe o Número--||")
for i in range(tentativas + 1):

    num = int(input("Adivinhe o número: "))

    if(num == certo):
        print("||--Você Acertou--||")
        break
    else:
        print("||--Tente novamente--||")
    
print("Você Perdeu")
print(f"O número mágico era: {certo}")