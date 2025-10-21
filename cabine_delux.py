from cabine import Cabine

class Delux(Cabine):
    def __init__(self, codice, letti, ponte, prezzo, tipologia):
        super().__init__(codice, letti, ponte, prezzo)
        self.tipologia = tipologia
        self.incremento_prezzo()

    def __str__(self):
        return f'{super().__str__()} {self.tipologia}'
    def __repr__(self):
        return f'{super().__repr__()}, tipologia={self.tipologia}'

    def incremento_prezzo(self):
        self.prezzo = self.prezzo * 1.20
