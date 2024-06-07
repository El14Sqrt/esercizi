class Film:
    def __init__(self, titolo:str, durata:str) -> None:
        self.titolo=titolo
        self.durata=durata


class Sala:
    def __init__(self, numero:int, film:Film, posti:int, prenotazioni:int) -> None:
        self.numero=numero
        self.film=film
        self.posti=posti
        self.prenotazioni=prenotazioni

    def prenota_posti(self, posti, prenotazioni):
        pass

    def posti_disponibili(self, posti, prenotazioni):
        pass


class Cinema:
    def __init__(self, sala:Sala, film:Film) -> None:
        self.sala=sala
        self.film=film
        self.lista_sale = list()

    def aggiungi_sala(self, sala):
        if sala not in self.lista_sale:
            self.lista_sale.append(sala)

    def prenota_film(self, sala, film):
        pass
