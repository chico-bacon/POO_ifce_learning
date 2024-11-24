class Usuario:
    def __init__(self, id=0, rg='', cpf='', nome='', dataNasc=''):
        self.id = id
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNasc = dataNasc

    def __str__(self):
        #return f'id: {self.id}\nnome: {self.nome}\ndata_de_nascimento: {self.data_nasc}'
        userInfo = str(self.id) + '\n'
        userInfo += self.rg + '\n'
        userInfo += self.cpf + '\n'
        userInfo += self.nome + '\n'
        userInfo += self.dataNasc + '\n'

        return userInfo

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

class Conta:
    def __init__(self, agencia=0, usuario='', dataAbertura=''):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura

    def __str__(self):
        accountInfo = str(self.agencia)
        accountInfo += self.usuario
        accountInfo += str(self.dataAbertura)

        return accountInfo

    def get_agencia(self):
        return self.agencia

    def set_agencia(self, agencia):
        self.agencia = agencia

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_dataAbertura(self):
        return self.dataAbertura

    def set_dataAbertura(self, dataAbertura):
        self.dataAbertura = dataAbertura
