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
# class feiraLivre():
#     def __init__(self, nome):
#         self.nome = nome
#         self.frutas = ["Banana", "Morango", "Uva", "Abacaxi", "Amora"]

#     def mostrarFrutas(self):
#         for i in self.frutas:
#             print(i)

#     def selecaoFruta(self, fruta):
#         if(fruta in self.frutas):
#             print(f"Fruta escolhida: {fruta}")

# nome = input("Digite seu nome: ")
# feira = feiraLivre(nome)
# feira.mostrarFrutas()
# fruta = input("Qual a fruta para ser selecionada: ")
# feira.selecaoFruta(fruta)


# 4
class Agenda:
    def __init__(self):
        self.agenda = []
    
    def adicionar_contato(self, nome, telefone):
        self.agenda.append((nome, telefone))  # Adicionando uma tupla (nome, telefone)

    def listar_contatos(self):
        for contato in self.agenda:  # Iterar sobre os elementos da lista
            nome, telefone = contato  # Desempacotar a tupla
            print(f"Nome: {nome}, Telefone: {telefone}")

agenda = Agenda()
nome = input("Qual o seu nome: ")
telefone = input("Qual o seu telefone: ")
agenda.adicionar_contato(nome, telefone)
agenda.listar_contatos()
