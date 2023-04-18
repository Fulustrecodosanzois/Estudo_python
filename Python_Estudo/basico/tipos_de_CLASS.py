class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura): #xpressão obrigatória na construção de class
        # É declarado todas as variaveis que farão parte da função
        self.cor= cor
        self.altura= altura
        self.profundidade=profundidade
        self. largura=largura
        # o "self" significa dizer que a variavel pertence aquela class, como se falasse "eu (da class).cor" (eu=self)
    def passar_canal(self,botao):#Aqui são colocados os comandos que serão chamados para executar uma função a partir das variaveis self
        if botao== '+':
            print("aumentar canal")
        elif botao== '-':
            print('diminuir o canal')   
            
controleRemoto= ControleRemoto('azul', "10cm", '3cm', '2cm') 
#print(controleRemoto.cor)# segue o padrão de importação, "função+atributo da função"

controleRemoto.passar_canal('+')

controleRemoto2= ControleRemoto('verde', '20cm', '4cm', '8cm')
        
print(controleRemoto2.profundidade)