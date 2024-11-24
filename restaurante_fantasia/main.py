from datetime import date
from random import choice
from restaurant_models import Restaurante

cozinhas = ['Fastfood', 'Italiana', 'Portuguesa', 'Mineira', 'Baina', 'Cearence', 'Paulista', 'Espanhola', 'Argentina', 'Chinesa', 'Japonesa', 'Francesa', 'Caseira']

def abrirRestaurante(restaurante, nome, tipo, abertura, endereco):
    restaurante.set_nome(nome)
    restaurante.set_tipoCozinha(tipo)
    restaurante.set_dataAbertura(abertura)
    restaurante.set_endereco(endereco)

def descreverRestaurante(restaurante):
    return restaurante.__str__()

cat_restaurants = []

for i in range(0, 6):
    rest = Restaurante()
    print(descreverRestaurante(rest))

    print(f'------Restaurante {i+1}------')
    nome = input('Nome: ')
    tipo = choice(cozinhas)
    print(f'Tipo de Cozinha: {tipo}')
    abertura = str(date.today())
    print(f'Data de abertura: {abertura}')
    endereco = input('Endereco: ')

    abrirRestaurante(restaurante=rest, nome=nome, tipo=tipo, abertura=abertura, endereco=endereco)
    cat_restaurants.append(rest)

print('Listando Restaurantes!\n')
for j in cat_restaurants:
    print(descreverRestaurante(j))
