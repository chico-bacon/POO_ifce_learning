from abc import ABC, abstractmethod 

class Usuario:
    def __init__(self, id=0, rg='', cpf='', nome='', dataNasc=''):
        self.id = id
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNasc = dataNasc

    def __str__(self):
        # return f'id: {self.id}\nnome: {self.nome}\ndata_de_nascimento: {self.data_nasc}'
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
    def __init__(self, numero=0, agencia=0, usuario='', data_abertura='', saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo

    def __str__(self):
        accountInfo = str(self.agencia)
        accountInfo += self.usuario
        accountInfo += str(self.data_abertura)
        accountInfo += str('R$ ' + self.saldo)

        return accountInfo

    # Funcoes de manipulacao de informacoes da conta
    def get_agencia(self):
        return self.agencia

    def set_agencia(self, agencia):
        self.agencia = agencia

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_dataAbertura(self):
        return self.data_abertura

    def set_dataAbertura(self, data_abertura=''):
        self.data_abertura = data_abertura

    # Funcoes de movimentacao da conta
    def consultarSaldo(self, saldo):
        return 'Seu saldo atual é de R$ {:.2f}'.format(saldo)

    def deposistar(self, valor):
        self.saldo += valor
        return '\033[32mDeposito de R$ {:.2f}, realizado com sucesso!\033[m'

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return '\033[32mSaque de R$ {:.2f} realizado com sucesso!\033[m'
        else:
            return '\033[31mSaque negado!\033[m'

    def transferir(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return '\033[32mTransferencia de R$ {:.2f} realizada com sucesso!'.format(valor)
        else:
            return '\033[31mTransferencia negada!\033[m' 


class ContaPoupanca(Conta):
    def __init__(self, numero=0, agencia=0, usuario='', dataAbertura='', saldo=0, rendimento=0):
        super(Conta, self).__init__(numero, agencia, usuario, dataAbertura, saldo)
        self.rendimento = rendimento

    def __str__(self):
        return super().__str__() + \
            str(self.rendimento)

    def get_rendimento(self):
        return self.rendimento

    def set_rendimento(self, rendimento):
        self.rendimento = rendimento

    def depositar(self):
        return
    
    def sacar(self):
        return
    
    def transferir(self):
        return


class ContaCorrente(Conta):
    def __init__(self, numero=0, usuario='', dataAbertura='', saldo=0, limite=0):
        super(Conta, self).__init__(numero, agencia, usuario, dataAbertura, saldo)
        self.limite = limite

class ContaEspecial(ContaCorrente):
    def __init__(self, numero=0, agencia=0, usuario='', dataAbertura='', saldo=0, limite=0):
        super(Conta, self).__init__(numero, agencia, usuario, dataAbertura, saldo)
        self.limite = limite

        def consultarSaldo(self):
            return 'Seu saldo atual é R$ {:.2f}'.format(self.saldo)

        def sacar(self, limite, saldo, valor):
            if valor <= saldo and valor <= limite:
                self.saldo -= valor
                return '\033[mSaque de R${:.2f} autorizado!'.format(valor)
            else:
                return '\033[mSaque negado\033[m'

        def transferir(self, limite, saldo, valor):
            if saldo >= valor and valor >= limite:
                self.saldo -= valor
                return '\033[32mTransferencia de R$ {:.2f} bem sucedida!\033[m'.format(valor)
            else:
                return '\033[31mNão foi possivel realizar transferencia\033[m'
            
        def depositar(self, saldo, valor):
            self.saldo += valor
            return f'Deposito de R${valor:.2f} efetuado com sucesso!'
            
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

    