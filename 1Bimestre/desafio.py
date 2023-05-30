import time as t

def isFloat(num):
  try:
    float(num)
    return True
  except:
    return False

contador = 0

print("Bem-Vindo à corrida de obstáculos!")

t.sleep(1)

resposta = input("Qual é a altura da proxima (em Metros)? ")

verificacao = isFloat(resposta)
resposta = float(resposta)

while(verificacao):
    t.sleep(1)
    

    if(float(resposta) <= 1.5):
        contador += 1
        print("Parabéns! Você pulou a barreira com sucesso")
        print("")

        resposta = input("Qual é a altura da proxima (em Metros)? ")
    
    if(float(resposta) > 1.5):
        print("Ops, Você não conseguiu pular da barreira! ")
        print("")

        resposta = input("Qual é a altura da proxima (em Metros)? ")
    
    if(resposta == type(str)):
        print("")
        print(f"Você pulou com sucesso {contador} barreiras")
        break