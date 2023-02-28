idade = int(input("Digite sua Idade: "))

if(idade <= 11):
    print("Criança")
elif(idade > 11 and idade <= 18):
    print("Adolescente")
elif(idade > 18 and idade <= 24):
    print("Jovem")
elif(idade > 24 and idade <= 40):
    print("Adulto")
elif(idade > 40 and idade <= 60):
    print("Meia Idade")
else:
    print("Idoso")