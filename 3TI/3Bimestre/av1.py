class Biblioteca:
    def __init__(self, name):
        self.name = name
        self.books = ["Joao e maria", "Biblía", "Pequeno principe","Como fazer amigos e influenciar pessoas","Amor teoricamente", "Do mil ao milhao","O Silencio vale ouro", "O principe","Segredos do Egito"]

    def mostrarLivros(self):

        print("||--Opções de livros--||")
        for i in self.books:
            print(i)
        print("||--------------------||")

    def disponibilidade(self, opcao):
        if opcao in self.books:
            print(f"Livro selecionado: {opcao}")
        else:
            print("Livro não encontrado")

print("||----Biblioteca Jojo's----||")

name = input("Digite seu nome: ")
biblioteca = Biblioteca(name)
biblioteca.mostrarLivros()
opcao = input("Qual livro deseja fazer o empréstimo: ")
biblioteca.disponibilidade(opcao)

# class feiraLivre():
#     def __init__(self, nome):
#         self.nome = nome
#         self.frutas = ["Banana", "Morango", "Uva", "Abacaxi", "Amora"]

#     def mostrarFrutas(self):
#         print("||--Opções de frutas--||")
#         for i in self.frutas:
#             print(i)
#         print("||--------------------||")

#     def selecaoFruta(self, fruta):
#         if(fruta in self.frutas):
#             print(f"Fruta selecionada: {fruta}")

# nome = input("Digite seu nome: ")
# feira = feiraLivre(nome)
# feira.mostrarFrutas()
# fruta = input("Qual a fruta para ser selecionada: ")
# feira.selecaoFruta(fruta)


# class agenciaViagens():
#     def __init__(self):
#         self.opcaoes = ["Praia", "Montanha", "Cidade"]

#     def mostrarOpcoes(self):
#         print("Opções de Viagens: ")
#         for i in self.opcaoes:
#             print(i)
    
#     def selecioneOpcao(self, opcao):
#         if(opcao in self.opcaoes):
#             print(f"Destino selecionado: {opcao}")
#         else: print("Destino não encontrado!")  

# agencia = agenciaViagens() 
# agencia.mostrarOpcoes()
# opcao = input("Digite uma opção de viagem: ")
# agencia.selecioneOpcao(opcao)

# class Agenda:
#     def __init__(self):
#         self.agenda = []
    
#     def adicionar_contato(self, nome, telefone):
#         self.agenda.append((nome, telefone))  # Adicionando uma tupla (nome, telefone)

#     def listar_contatos(self):
#         for contato in self.agenda:  # Iterar sobre os elementos da lista
#             nome, telefone = contato  # Desempacotar a tupla
#             print(f"Nome: {nome}, Telefone: {telefone}")

# agenda = Agenda()
# nome = input("Qual o seu nome: ")
# telefone = input("Qual o seu telefone: ")
# agenda.adicionar_contato(nome, telefone)
# agenda.listar_contatos()
