# Laços de repetição
# While
i = 0

while i <= 10:
    print(f"Valor: {i}")
    i += 1

# for
names = ["Mateus", "Nycollas", "Ketlyn", "Ana", "Luiza", "Felipe"]

for i in names:
    print(i)

# exemplos
# for i in range(10):
#     print(i)


# for i in names:
#     if(i == "Ketlyn"):
#         continue
    
#     print(i)

# for i in range(2, 19, 2):
#     print(i)


# num = int(input("Digite um número para a tabuada: "))
# mult = int(input("Digite um número para multiplicar: "))

# for i in range(1, mult + 1):
#   result = num * i
#   print(f"{num} X {i} = {result}")


for i in range(1, 6, 1):
  num = int(input("Digite sua nota: "))
  soma += num



print(soma / 5)