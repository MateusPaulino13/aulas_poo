# dobro
# def dobro_numero(num):
#     return num * 2

# num = int(input("Digite um número: "))
# print(dobro_numero(num))

# soma da lista
# def soma_lista(lista):
#     return sum(lista)

# list = (1, 7, 8, 3, 9)
# print(soma_lista(list))

# maior número da lista
# def maior_numero(lista):
#     return max(lista)

# lista = (1, 9, 5, 80, 54, 27)
# print(maior_numero(lista))

# desafio
def somaImposto(taxaImposto, custo):
    imposto = taxaImposto / 100
    taxa = custo * imposto

    return custo + taxa

valorProduto = float(input("Digite o valor do produto: "))
taxa = float(input("Digite a taxa do imposto: "))

print(somaImposto(taxa, valorProduto))