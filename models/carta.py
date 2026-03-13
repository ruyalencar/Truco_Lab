
class Carta:
    def __init__(self, Valores, Naipes):
        self.valores = Valores
        self.naipes = Naipes

    def __str__(self):
        return f"{self.valores}{self.naipes}"

    def __repr__(self):
        return f"{self.valores}{self.naipes}"

        # Aqui é aonde a classe Carta nunca as duas variaves e cria o nosso baralho 