from abc import ABC, abstractmethod 
from datetime import datetime

class Conta:
    def __init__(self, numero=0, agencia=0, cliente='', data_abertura='', saldo=0, extrato=[]):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.data_abertura = data_abertura
        self.saldo = saldo
        self.extrato = extrato

    def __str__(self):
        return f'Conta: {self.numero}, Agência: {self.agencia}, Cliente: {self.cliente}, Abertura: {self.data_abertura}, Saldo: R${self.saldo:.2f}'

    # Funcoes de manipulacao de informacoes da conta
    def get_agencia(self):
        return self.agencia

    def set_agencia(self, agencia):
        self.agencia = agencia

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_dataAbertura(self):
        return self.data_abertura

    def set_dataAbertura(self, dataAbertura):
        self.data_abertura = dataAbertura

    def set_extrato(self, info):
        info += ' - ' + datetime.now().strftime('%c')
        self.extrato.append(info)

    # Funcoes de movimentacao da conta
    def consultar_saldo(self):
        return 'Seu saldo atual é de R$ {:.2f}'.format(self.saldo)

    def deposistar(self, valor):
        self.saldo += valor
        self.set_extrato(f'Deposito: R$ {valor:.2f}') 
        return f'\033[32mDeposito de R$ {valor:.2f}, realizado com sucesso!\033[m'

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.set_extrato(f'Saque: R$ {valor:.2f}')
            return '\033[32mSaque de R$ {:.2f} realizado com sucesso!\033[m'
        else:
            return '\033[31mSaque negado!\033[m'

    def transferir(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.set_extrato(f'Transferencia: R$ {valor:.2f}')
            return '\033[32mTransferencia de R$ {:.2f} realizada com sucesso!'.format(valor)
        else:
            return '\033[31mTransferencia negada!\033[m' 
    
    def exibir_extrato(self):
        print('Extrato da Conta Bancária')
        print('Data Abertura: ', self.get_dataAbertura())
        for item in self.extrato:
            print(item)

    

class ContaPoupanca(Conta):
    def __init__(self, numero=0, agencia=0, cliente='', dataAbertura='', saldo=0, rendimento=0, extrato=[]):
        super().__init__(numero, agencia, cliente, dataAbertura, saldo, extrato)
        self.rendimento = rendimento

    def __str__(self):
        return super().__str__() + \
            str(self.rendimento)
    
    def aplicar_rendimento(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        self.set_extrato(f'Rendimento de R$ {ganho:.2f}')
        return f'Rendimento de R$ {ganho:.2f} aplicado. Novo saldo: R$ {self.saldo:.2f}'

    def depositar(self, valor):
        self.saldo += valor
        self.set_extrato(f'Depósito de R$ {valor:.2f}')
        return 'Depósito realizado na poupança com sucesso!'
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.set_extrato(f'Saque de R$ {valor:.2f}')
            return 'Saque realizado na poupança com sucesso!'
        else:
            return 'Saldo insuficiente para essa operação!'
    
    def transferir(self, origem, destino, valor):
        if self.saldo >= valor:
            saldo -= valor
            self.set_extrato(f'Transferencia de R$ {valor:.2f} para {destino}')
            return f'Transferencia no valor de R$ {valor:.2f} realizada para {destino} realizada com sucesso!'
        else:
            return 'Saldo insuficiente para essa operação'

    def exibir_extrato(self):
        print('Extrato da Conta Poupanca')
        print('Data Abertura: ', self.get_dataAbertura())
        for item in self.extrato:
            print(item)

class ContaCorrente(Conta):
    def __init__(self, numero=0, agencia='', cliente='', dataAbertura='', saldo=0, limite=0, extrato=[]):
        super().__init__(numero, agencia, cliente, dataAbertura, saldo, extrato)
        self.limite = limite

    def __str__(self):
        return super().__str__() + \
            str(self.limite)
    
    def depositar(self, valor):
        self.saldo += valor
        self.set_extrato(f'Depósito de R$ {valor:.2f}')
        return 'Depósito realizado na conta corrente com sucesso!'
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.set_extrato(f'Saque de R$ {valor:.2f}')
            return 'Saque realizado na  com sucesso!'
        else:
            return 'Saldo insuficiente para essa operação!'
    
    def transferir(self, destino, valor):
        if self.saldo >= valor:
            saldo -= valor
            self.set_extrato(f'Rendimento de R$ {valor:.2f} para {destino}')
            return f'Transferencia no valor de R$ {valor:.2f} realizada para {destino} realizada com sucesso!'
        else:
            return 'Saldo insuficiente para essa operação'
    
    def exibir_extrato(self):
        print('Extrato da Conta Corrente')
        print('Data Abertura: ', self.get_dataAbertura())
        for item in self.extrato:
            print(item)

class ContaEspecial(ContaCorrente):
    def __init__(self, numero=0, agencia=0, cliente='', dataAbertura='', saldo=0, limite=0, extrato=[]):
        super().__init__(numero, agencia, cliente, dataAbertura, saldo, extrato)
        self.limite = limite

    def consultarSaldo(self):
        return 'Seu saldo atual é R$ {:.2f}'.format(self.saldo)

    def sacar(self, valor):
        if valor <= self.saldo and valor <= self.limite:
            self.saldo -= valor
            self.set_extrato(f'Saque de R$ {valor:.2f}')
            return '\033[mSaque de R${:.2f} autorizado!'.format(valor)
        else:
            return '\033[mSaque negado\033[m'

    def transferir(self, valor, destino):
        if self.saldo >= valor and  valor >= self.limite:
            self.saldo -= valor
            self.set_extrato(f'Transferencia de R$ {valor:.2f} para {destino}')
            return '\033[32mTransferencia de R$ {:.2f} para {} bem sucedida!\033[m'.format(valor, destino)
        else:
            return '\033[31mTransferencia negada!\033[m'
        
    def depositar(self, valor):
        self.saldo += valor
        self.set_extrato(f'Deposito de R$ {valor:.2f}')
        return f'Deposito de R${valor:.2f} efetuado com sucesso!'
    
    def exibir_extrato(self):
        print('Extrato da Conta Especial')
        print('Data Abertura: ', self.get_dataAbertura())
        for item in self.extrato:
            print(item)