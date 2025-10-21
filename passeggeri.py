class Passeggeri:

    def __init__(self,codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = None

    def __str__(self):
        return f'{self.codice} {self.nome} {self.cognome}'
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(codice={self.codice}, nome={self.nome}, cognome={self.cognome})')
