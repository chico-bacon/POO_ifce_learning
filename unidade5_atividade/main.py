from datetime import date, datetime
from cliente_model import Cliente, CartaoNatal, CartaoSaoValentin, CartaoAniversario
from conta_model import Conta, ContaPoupanca, ContaCorrente, ContaEspecial
from random import randint

def criar_cliente():
    client = Cliente()
    print(client.__str__())

    return client

def criar_conta():
    account = Conta()
    print(account.__str__())

    return account

def cadastrar_cliente(cliente, id, rg, cpf, nome, nascimento):
    cliente.set_id(id)
    cliente.set_rg(rg)
    cliente.set_cpf(cpf)
    cliente.set_nome(nome)
    cliente.set_dataNasc(nascimento)

def cadastrar_conta(conta, agencia, cliente, abertura):
    conta.set_agencia(agencia)
    conta.set_cliente(cliente)
    conta.set_dataAbertura(abertura)

#Gerando um cliente
cliente1 = criar_cliente()

id = randint(1, 1000)
nome = input('Nome: ')
nascimento = input('Data de nascimento(ano-mes-dia): ')
rg = input('RG: ')
cpf = input('CPF: ')

cadastrar_cliente(cliente1, id, rg, cpf, nome, nascimento)

print('\033[32mcliente criado com sucesso!\033[m')

print(cliente1.__str__())

#Gerando uma conta
conta1 = criar_conta()

agencia = randint(1, 1000)
abertura = date.today()

cadastrar_conta(conta1, agencia, cliente1.__str__(), abertura)

print('\033[32mConta bancária criada com sucesso!\033[m')

print(conta1.__str__())

conta_especial = ContaEspecial(numero=1, agencia=101, cliente=cliente1, saldo=1000, limite=500, dataAbertura=str(datetime.now().strftime('%c')))
conta_poupanca = ContaPoupanca(numero=1, agencia=6, cliente=cliente1, saldo=100, dataAbertura=str(datetime.now().strftime('%c')))
conta_corrente = ContaCorrente(numero=1, agencia=6, cliente=cliente1, saldo=100, dataAbertura=str(datetime.now().strftime('%c')))
print(conta_especial.sacar(1300))  # deve funcionar
print(conta_especial.sacar(250))   # deve dar saldo negativo
print(conta_especial.consultar_saldo())
conta_especial.exibir_extrato()
conta_poupanca.exibir_extrato()
conta_corrente.exibir_extrato()

cartao1 = CartaoSaoValentin(cliente1)
cartao2 = CartaoNatal(cliente1)
cartao3 = CartaoAniversario(cliente1)
cartao1.show_mensage()
cartao2.show_mensage()
cartao3.show_mensage()