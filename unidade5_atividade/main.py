from datetime import date
from bank_account_models import Conta, ContaPoupanca, ContaCorrente, CartaoNatal, CartaoSaoValentin, CartaoAniversario
from random import randint

usuario = input('Digite o seu nome: ')
cartao1 = CartaoSaoValentin(usuario)
cartao2 = CartaoNatal(usuario)
cartao3 = CartaoAniversario(usuario)
cartao1.show_mensage()
cartao2.show_mensage()
cartao3.show_mensage()