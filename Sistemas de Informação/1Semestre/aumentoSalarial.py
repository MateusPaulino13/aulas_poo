salario = float(input("Digite seu salário atual: "))
nivel = input("Digite o seu nível conhecimento (Júnior, Pleno ou Sênior): ")

if(nivel == "Junior" or nivel == "junior" or nivel == "Júnior" or nivel == "júnior"):
    aumento = salario * 1.1
    print(f"Seu salário com aumento é de R${salario} e você é júnior")
elif(nivel == "Pleno" or nivel == "pleno"):
    aumento = salario * 1.2
    print(f"Seu salário com aumento é de R${salario} e você é Pleno")
elif(nivel == "Sênior" or nivel == "sênior" or nivel == "Senior" or nivel == "senior"):
    aumento = salario * 1.3
    print(f"Seu salário com aumento é de R${salario} e você é Sênior")