class Solidos:
    def __init__(self, pi=3.14):
        self.pi = pi

    def area_triangulo(base, altura):
        area = (base * altura) / 2
        return area

    def area_quadrado(lado):
        area = (lado**2)
        return area
    
    def area_retangulo(base, altura):
        area = base * altura
        return area

    def area_circulo(raio):
        area = self.pi * (raio**2)
        return area

    def area_losango(Dmaior, Dmenor):
        area = (Dmaior * Dmenor) / 2
        return area

    def area_pentagono():
        area = 0
        return area

    def area_hexagono():
        area = 0
        return area

    def area_heptagono():
        area = 0
        return area

    def area_octogono():
        area = 0
        return area

    def volume_esfera(raio):
        vol = (4/3) * self.pi * (raio**3)
        return vol
    
    def volume_cilindrp(ac, altura):
        vol = ac * altura
        return vol

    def volume_cone(raio, altura):
        vol = (1/3) * self.pi * (raio**2) * altura
        return vol

    def volume_prisma(ab, altura):
        vol = ab * altura
        return vol
        