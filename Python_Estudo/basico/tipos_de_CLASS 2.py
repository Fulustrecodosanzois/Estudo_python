class Cliente:
    def __init__(self,nome, email, plano):
        self.nome= nome
        self.email= email
        self.lista_planos= ['basic', 'premium']
        self.plano= plano
    if plano in self.lista_planos:
        self.plano=plano
    else:
        raise Exception('Plano Inválido')
    
def mudar_plano(self,novo_plano):
    if novo_plano in self.lista_palnos:
        self.plano=novo_plano
    else:
        print('Plano inválido')
def ver_filme(self,filme, plano_filme):
    if self.plano== palno_filme:
        print(f'Assistindo {filme}')
    elif self.plano=='premium':
        print(f'assistindo {filme}')
    elif self.plano== 'basic'and plano_filme=='premium':
        print('Faça upgrade para premium para ver esse filme')
    else:
        print('plano inválido')
        
cliente = Cliente('luc', 'gdgsgs@gmail.com', 'basic')
print(cliente.plano)