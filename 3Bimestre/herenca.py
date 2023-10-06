# Herança
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def emitirSom(self):
        return "ALgum bem du loko"
    
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Cachorro")
        self.raca = raca
    
    def emitirSom(self):
        return "Au au"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, especie="Gato")
        self.cor = cor
    
    def emitirSom(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex", raca="Caramelo")

print(f"{dog.nome} é um {dog.raca}")
print(dog.emitirSom())

cat = Gato(nome="Juanylson", cor="Preto")

print(f"{cat.nome} é da cor {cat.cor}")
print(cat.emitirSom())