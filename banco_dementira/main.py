from random import randint
from datetime import date
from bank_accounting_models import Usuario, Conta

def criar_usuario():
    user = Usuario()
    print(user.__str__())

    return user

def criar_conta():
    account = Conta()
    print(account.__str__())

    return account

def cadastrar_usuario(usuario, id, rg, cpf, nome, nascimento):
    usuario.set_id(id)
    usuario.set_rg(rg)
    usuario.set_cpf(cpf)
    usuario.set_nome(nome)
    usuario.set_dataNasc(nascimento)

def cadastrar_conta(conta, agencia, usuario, abertura):
    conta.set_agencia(agencia)
    conta.set_usuario(usuario)
    conta.set_dataAbertura(abertura)

#Gerando um usuario
usuario1 = criar_usuario()

id = randint(1, 1000)
nome = input('Nome: ')
nascimento = input('Data de nascimento(ano-mes-dia): ')
rg = input('RG: ')
cpf = input('CPF: ')

cadastrar_usuario(usuario1, id, rg, cpf, nome, nascimento)

print('\033[32mUsuario criado com sucesso!\033[m')

print(usuario1.__str__())

#Gerando uma conta
conta1 = criar_conta()

agencia = randint(1, 1000)
abertura = date.today()

cadastrar_conta(conta1, agencia, usuario1.__str__(), abertura)

print('\033[32mConta bancária criada com sucesso!\033[m')

print(conta1.__str__())