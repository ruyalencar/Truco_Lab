class RegraTruco:

    FORCA_VALOR = {
        "4": 0,
        "5": 1,
        "6": 2,
        "7": 3,
        "Q": 4,
        "J": 5,
        "K": 6,
        "A": 7,
        "2": 8,
        "3": 9 
    }

    FORCA_NAIPE = {
        "♦": 0,
        "♠": 1,
        "♥": 2,
        "♣": 3
    }

    def __init__(self, manilha):
        self.manilha = manilha
    
    def comparar(self,carta1, carta2):
        if carta1.valor == self.manilha and carta2.valor == self.manilha:

            f1 = self.FORCA_NAIPE[carta1.naipe]
            f2 = self.FORCA_NAIPE[carta2.naipe]

            if f1 > f2:
                return 1
            elif f2 > f1:
                return 2
            else: 
                return 0


        f1 = self.FORCA_VALOR[carta1.valor]
        f2 = self.FORCA_VALOR[carta2.valor]

        if f1 > f2:
            return 1
        elif f2 > f1:
            return 2 
        else:
            return 0
        
        
        

    
    