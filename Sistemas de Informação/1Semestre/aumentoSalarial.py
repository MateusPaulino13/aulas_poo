salario = float(input("Digite seu salário atual: "))
nivel = input("Digite o seu nível conhecimento (Júnior, Pleno ou Sênior): ")

if(nivel == "Junior" or nivel == "junior" or nivel == "Júnior" or nivel == "júnior"):
    salario = salario * 1.1
    print(f"Seu salário com aumento é de R${salario:.2f} e você é júnior")
elif(nivel == "Pleno" or nivel == "pleno"):
    salario = salario * 1.2
    print(f"Seu salário com aumento é de R${salario:.2f} e você é Pleno")
elif(nivel == "Sênior" or nivel == "sênior" or nivel == "Senior" or nivel == "senior"):
    temFilho = input("Você possui filhos? Digite sim ou não: ")
    if(temFilho == "Sim" or temFilho == "sim"):
        salario = (salario * 1.3) + 500
        print(f"Seu salário com aumento é de R${salario:.2f} e você é Sênior")
    else:
        salario = salario * 1.3
        print(f"Seu salário com aumento é de R${salario:.2f} e você é Sênior")
else:
    print("Cargo desconhecido!")