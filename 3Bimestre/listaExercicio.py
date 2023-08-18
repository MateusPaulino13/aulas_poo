# 1
# print("Seja bem-vindo agência aeria")
# name = input("Qual o seu nome: ")

# print("Opções de viajem: Montanhas, Praia, Cidade")
# opcao = input("Escolha uma das opções acima: ")

# print(f"Nome: {name}, destino de origem: {opcao}")


# 2

# class Biblioteca:
#     def __init__(self, name):
#         self.name = name

#     def mostrarLivros(self):
#         books = [
#             "Joao e maria", "Biblía", "Pequeno principe",
#             "Como fazer amigos e influenciar pessoas",
#             "Amor teoricamente", "Do mil ao milhao",
#             "O Silencio vale ouro", "O principe",
#             "Segredos do Egito"
#         ]

#         print("Opções de livros:")
#         for i in books:
#             print(i)

#     def disponibilidade(self, opcao):
#         books = [
#             "Joao e maria", "Biblía", "Pequeno principe",
#             "Como fazer amigos e influenciar pessoas",
#             "Amor teoricamente", "Do mil ao milhao",
#             "O Silencio vale ouro", "O principe",
#             "Segredos do Egito"
#         ]

#         if opcao in books:
#             print(f"Livro selecionado: {opcao}")
#         else:
#             print("Livro não encontrado")

# print("||----Biblioteca Silva's----||")

# name = input("Digite seu nome: ")
# biblioteca = Biblioteca(name)
# biblioteca.mostrarLivros()
# opcao = input("Qual livro deseja fazer o empréstimo: ")
# biblioteca.disponibilidade(opcao)


# 3
class feiraLivre():
    def __init__(self, nome):
        self.nome = nome