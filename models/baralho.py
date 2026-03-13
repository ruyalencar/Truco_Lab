from models.carta import Carta
import random


class Baralho:

    def __init__(self, valores, naipes):

        self.valores = valores
        self.naipes = naipes

        # cria todas as cartas
        self.cartas = [Carta(v, n) for n in naipes for v in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_carta(self):
        return self.cartas.pop() if self.cartas else None