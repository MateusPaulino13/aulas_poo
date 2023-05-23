# Problema 1
# def verifica_disponibilidade(bookCode, BookQnts):
#     if(BookQnts > 0):
#         return f"Código do livro: {bookCode}, Livro disponível para empréstimo"
#     else:
#         return "Livro indisponível para empréstimo"
    
# codigo = int(input("Digite o código do produto: "))
# quantidade = int(input("Digite a quantidade do produto: "))

# print(verifica_disponibilidade(codigo, quantidade))


# Problema 3
def calcula_desconto(valorProduto, desconto):
    return f"Valor com Desconto: R${valorProduto - ((desconto / 100) * valorProduto)}"

valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto: "))

print(calcula_desconto(valor, desconto))