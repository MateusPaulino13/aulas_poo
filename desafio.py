# Desafio para a proxima aula
import time as t

contador = 0

print("Bem-Vindo à corrida de obstáculos!")

t.sleep(1)

resposta = float(input("Qual é a altura da proxima (em Metros)? "))

while(resposta <= 1.5):
    contador += 1
    t.sleep(1)

    print("Parabéns! Você pulou a barreira com sucesso")
    print("")

    resposta = float(input("Qual é a altura da proxima (em Metros)? "))
    
    if(resposta > 1.5):
        print("Ops, Você não conseguiu pular da barreira! ")

        resposta = float(input("Qual é a altura da proxima (em Metros)? "))
    if(type(resposta) != float):
        print(f"Você pulou com sucesso {contador} barreiras")
        break