from game.jogo import Jogo
from models.carta import Carta

# O local que inicia tudo! CONTROLLER!

if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()
    jogo.mostrar_estado()



