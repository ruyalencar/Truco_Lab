from models.jogador import Jogador
from models.baralho import Baralho
from models.baralho import VALORES
from models.baralho import NAIPES






class Jogo:
    def __init__(self):
        nome1 = input("Jogador 1: ")
        nome2 = input("Jogador 2: ")
                                                    #Essa Classe tem como objetivo, deixar tudo mais organizado e de 
        self.jogador1 = Jogador(nome1)              #facil compreenção 
        self.jogador2 = Jogador(nome2)
        self.baralho = Baralho(VALORES, NAIPES)         #Aqui é o ponta pé inicial
        self.vira = None
        self.manilha = None
    
    def iniciar(self):
        self.baralho.embaralhar()
        self.distribuir_cartas()
        self.definir_vira()                         #Aqui ele pede para fazer a distribuição das cartas
        self.definir_manilha()

    def distribuir_cartas(self):
        for _ in range(3):
            self.jogador1.receber_carta(self.baralho.distribuir_carta())   #funtion para a entrega das cartas entre os 
            self.jogador2.receber_carta(self.baralho.distribuir_carta())    #jogadores

    def definir_vira(self):
        self.vira = self.baralho.distribuir_carta()   #Definir o vira

    def definir_manilha(self):
        valor_vira = self.vira[:-1]
        indice = self.baralho.valores.index(valor_vira)
        proximo_indice = (indice + 1) % len(self.baralho.valores)       #definir a manilha e criar um loop
        self.manilha = self.baralho.valores[proximo_indice]

    def mostrar_estado(self):
        print ("Vira: {}" .format(self.vira))
        print ("Manilha: {}" .format(self.manilha))
        print (self.jogador1.mostrar_mao())    #mostrar o resultado de tudo
        print (self.jogador2.mostrar_mao())
        print ("Cartas restantes: ", len(self.baralho.cartas))