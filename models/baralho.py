

import random

VALORES = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]   #Lista Para criar o nosso baralho
NAIPES = ["♦", "♠", "♥", "♣"]




class Baralho:
    def __init__(self, valores, naipes):
        self.valores = valores                      #Classe que cria o baralho juntando as duas variaveis e tem a 
        self.naipes = naipes                        #função de fazer toda a manipulação dele 
        self.cartas = [f"{v}{n}" for n in self.naipes for v in self.valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_carta(self):
        return self.cartas.pop() if self.cartas else None