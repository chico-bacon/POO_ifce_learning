class Restaurante():
    def __init__(self, nome='', tipoCozinha='', dataAbertura='', endereco=''):
        self.nome = nome
        self.tipoCozinha = tipoCozinha
        self.dataAbertura = dataAbertura
        self.endereco = endereco

    def __str__(self):
        infoRestaurante = 'Nome: ' + self.nome + '\n'
        infoRestaurante += 'Cozinha : ' + self.tipoCozinha + '\n'
        infoRestaurante += 'Data de Abertura: ' + self.dataAbertura + '\n'
        infoRestaurante += 'Endereco: ' + self.endereco + '\n'

        return infoRestaurante

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipoCozinha(self):
        return self.tipoCozinha

    def set_tipoCozinha(self, tipoCozinha):
        self.tipoCozinha = tipoCozinha

    def get_dataAbertura(self):
        return self.dataAbertura

    def set_dataAbertura(self, dataAbertura):
        self.dataAbertura = dataAbertura

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

