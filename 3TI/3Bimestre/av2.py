import time

class Restaurante:
    def __init__(self):
        self.opcoes = ['Pizza', 'Hambúrguer', 'Massa', "Pudim", "Sushi"]
        self.pedidos_cliente = []

    def listar_cardapio(self):
        print("//----Opções----//")
        for opcao in self.opcoes:
            time.sleep(0.4)
            print(opcao)
    
    def fazer_pedido(self):
        pedidos = int(input("Quando pedidos gostaria de fazer? "))
        
        for i in range(pedidos):
            item = input("Escolha um das opções de nosso menu: ")

            if(item in self.opcoes):
                self.pedidos_cliente.append(item)
                print("Pedido feito com sucesso!")
            else:
                print("Opção não encontrada!")
            
    
    def listar_pedidos(self):
        print("//----Pedidos feitos----//")
        for pedido in self.pedidos_cliente:
            time.sleep(0.5)
            print(pedido)

restaurante = Restaurante()
restaurante.listar_cardapio()
restaurante.fazer_pedido()
restaurante.listar_pedidos()