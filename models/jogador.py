class Jogador:
        def __init__(self, nome):
            self.nome = nome                #Essa Classe tem a função de criar os jogadores e dar uma função basica
            self.mao = []                   #que é a função de receber uma carta e mostrar a mão

        def receber_carta(self, carta):
            if carta:
                self.mao.append(carta)

        def mostrar_mao(self):
            return f"{self.nome}: {self.mao}"
