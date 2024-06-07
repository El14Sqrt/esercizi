class Media:

    def __init__(self) -> None:
        self.titolo = str
        self.review = list()


    def set_title(self, title):
        self.titolo = title


    def get_title(self):
        return self.titolo


    def aggiungi_valutazione(self, voto:int):
        if 1 <= voto <= 5:
            self.review.append(voto)
        else:
            return "Il voto deve essere un numero compreso tra 1 e 5"
    

    def get_media(self):
        self.media_voti: float = media_voti

        n = len(self.review)
        somma_voti = sum(self.review)
        media_voti: float = somma_voti / n
        return media_voti
    

    def get_rate(self):
        if 0 <= self.media_voti <= 1.5:
            return "TERRIBILE"
        elif 1.6 <= self.media_voti <= 2.5:
            return "BRUTTO"
        elif 2.6 <= self.media_voti <= 3.5:
            return "NORMALE"
        elif 3.6 <= self.media_voti <= 4.5:
            return "BELLO"
        elif 4.6 <= self.media_voti <= 5:
            return "GRANDIOSO"
        

    def rate_percentage(self, voto):
        percentage: float = self.review.count(voto) / len(self.review) * 100
        return percentage
    

    def recensione(self):
        print("Titolo: ", self.get_title())
        print("Voto medio: ", self.media_voti)
        print("Giudizio: ", self.get_rate())
        print("Terribile: ", self.rate_percentage(1))
        print("Terribile: ", self.rate_percentage(2))
        print("Terribile: ", self.rate_percentage(3))
        print("Terribile: ", self.rate_percentage(4))
        print("Terribile: ", self.rate_percentage(5))

class Film(Media):
    def __init__(self) -> None:
        super().__init__()
        self.elenco_libri = list()


class Libro(Media):
    def __init__(self) -> None:
        super().__init__()
        self.elenco_film = list()


