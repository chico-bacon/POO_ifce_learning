from abc import ABC, abstractmethod 

class Cliente:
    def __init__(self, id=0, rg='', cpf='', nome='', dataNasc=''):
        self.id = id
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNasc = dataNasc

    def __str__(self):
        # return f'id: {self.id}\nnome: {self.nome}\ndata_de_nascimento: {self.data_nasc}'
        clientInfo = str(self.id) + '\n'
        clientInfo += self.rg + '\n'
        clientInfo += self.cpf + '\n'
        clientInfo += self.nome + '\n'
        clientInfo += self.dataNasc + '\n'

        return clientInfo

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_rg(self):
        return self.rg

    def set_rg(self, rg):
        self.rg = rg

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_dataNasc(self):
        return self.dataNasc

    def set_dataNasc(self, dataNasc):
        self.dataNasc = dataNasc

class CartaoWeb(ABC):
    def __init__(self, destinatario=''):
        self.destinatario = destinatario

    @abstractmethod
    def get_destinatario(self):
        return self.destinatario

    @abstractmethod
    def show_mensage(self):
        pass

class CartaoSaoValentin(CartaoWeb):
    def __init__(self, destinatario=''):
        super().__init__(destinatario)

    def get_destinatario(self):
        return self.destinatario
    
    def show_mensage(self):
        print(f'Feliz dia dos namorados, {self.destinatario}')

class CartaoNatal(CartaoWeb):
    def __init__(self, destinatario=''):
        super().__init__(destinatario)

    def get_destinatario(self):
        return self.destinatario
    
    def show_mensage(self):
        print(f'Feliz natal, {self.destinatario}')

class CartaoAniversario(CartaoWeb):
    def __init__(self, destinatario=''):
        super().__init__(destinatario)

    def get_destinatario(self):
        return self.destinatario
    
    def show_mensage(self):
        print(f'Feliz Aniversario, {self.destinatario}')
