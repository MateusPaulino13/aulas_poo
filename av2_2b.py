# dobro
# def dobro_numero(num):
#     return num * 2

# num = int(input("Digite um número: "))
# print(dobro_numero(num))

# soma da lista
def soma_lista(lista):
    return f"A soma dos valores é de: {sum(lista)}"

list = []
for i in range(5):
    numero = int(input("Digite um número: "))
    list.append(numero)
print(soma_lista(list))

# maior número da lista
# def maior_numero(lista):
#     return max(lista)


# print(maior_numero(lista))

# desafio
# def somaImposto(taxaImposto, custo):
#     imposto = taxaImposto / 100
#     taxa = custo * imposto

#     return custo + taxa

# valorProduto = float(input("Digite o valor do produto: "))
# taxa = float(input("Digite a taxa do imposto: "))

# print(somaImposto(taxa, valorProduto))