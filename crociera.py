from cabine import Cabine
from passeggeri import Passeggeri
from cabine_animali import Animali
import csv


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.passeggeri = []
        self.cabine = []
        self.animali = []
        self.delux = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    if len(line) == 3:
                        codice = line[0]
                        nome = line[1]
                        cognome = line[2]
                        passeggero = Passeggeri(codice, nome, cognome)
                        self.passeggeri.append(passeggero)
                    elif len(line) == 4:
                        codice = line[0]
                        letti = line[1]
                        ponte =line[2]
                        prezzo = line[3]
                        cabina = Cabine(codice, letti, ponte, prezzo)
                        self.cabine.append(cabina)
                    elif len(line) == 5 and line[4].isdigit():
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        max_animali = line[4]
                        cabine_animali = Animali(codice, letti, ponte, prezzo, max_animali)
                        self.animali.append(cabine_animali)
                    else:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        tipologia = line[4]
                        cabine_delux = Delux(codice, letti, ponte, prezzo, tipologia)
                        self.delux.append(cabine_delux)
        except FileNotFoundError:
            return ("File not found")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina_trovata = None
        for cabina in self.cabine:
            if cabina.codice == codice_cabina:
                cabina_trovata = cabina
        if cabina_trovata is None:
            print("Cabina non trovato")
            return

        passegero_trovato = None
        for passegero in self.passeggeri:
            if passegero.codice == codice_passeggero:
                passegero_trovato = passegero
            if passegero_trovato is None:
                print("Passeggero non trovato")
                return

        if not cabina_trovata.disponibile:
            print("La cabina non è disponibile")
            return

        if passegero_trovato.cabina is not None:
            print("Il passeggero ha gia una cabina")
            return

        cabina_trvata.disponibile = False
        cabina_trovata.passeggero = passegero_trovato
        passegero_trovato.cabina = cabina_trovata


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        tutte_cabine = self.cabine + self.animali + self.delux
        return sorted(tutte_cabine)


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.passeggeri:
            if passeggero.cabina is not None:
                print(f'{passeggero.codice} {passeggero.nome} {passeggero.cognome} ha la cabina {passeggero.cabina}')
            else:
                print(f'{passeggero.codice} {passeggero.nome} {passeggero.cognome} non ha ancora una cabina assegnata')
        return


