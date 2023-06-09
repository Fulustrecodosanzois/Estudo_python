class Servico:
    def __init__(self, pedido=0):
        self.__pedido= pedido
        
    def novo_pedido(self):
        for perc in range(1,5):
            escolha= input("Qual seu pedido: ")
            self.__pedido+= 1
        print(f"Seu total do pedido é {self.__pedido}")
        
    def cancelar_pedido(self):
        for perc in range(1,5):
            escolha= input(f"Deseja cancelar o {perc}° pedido feito?\n sim ou não?  ")
            if escolha == "sim":
                self.__pedido-= 1
                
            elif escolha == "não":
                print("O pedido não foi cancelado")
    
    def exibir_pedido(self):
        return print(f"Seu número de pedidos agora é {self.__pedido}")