# 1
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# class Aluno(Pessoa):
#     def __init__(self, nome, matricula):
#         super().__init__(nome)
#         self.matricula = matricula

# aluno = Aluno("Mateus", 22999)

# print(f"Nome do aluno: {aluno.nome}")
# print(f"Matrícula do aluno: {aluno.matricula}")

# 2
# class Veiculo:
#     def mostrar_descricao(self):
#         return "Este é um veículo"

# class Carro(Veiculo):
#     def mostrar_descricao(self):
#         return "Este é um carro"

# # criando instâncias
# veiculo = Veiculo()
# print(veiculo.mostrar_descricao())

# carro = Carro()
# print(carro.mostrar_descricao())


# 3
class Forma:
    def __init__(self, cor):
        self.cor = cor

    def mostarCor(self):
        return self.cor
    
class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

circulo = Circulo("Amarelo", 1.5)
print(f"Cor : {circulo.cor}")
print(f"Raio : {circulo.raio}")