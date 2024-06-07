class Media:

    def __init__(self, titolo: str) -> None:
        self.titolo = titolo
        self.review = list()


    def set_title(self, title):
        self.titolo = title


    def get_title(self):
        return self.titolo


    def aggiungi_valutazione(self, voto:int):
        if 1 <= voto <= 5:
            self.review.append(voto)
            return "Il voto è stato aggiunto correttamente"
        else:
            return "Il voto deve essere un numero compreso tra 1 e 5"
    

    def get_media(self):
        self.media_voti: float = media_voti

        n = len(self.review)
        somma_voti = sum(self.review)
        if n > 0:
            media_voti: float = somma_voti / n
            return media_voti
        else:
            return None
        

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
        print("Voto medio: ", self.get_media())
        print("Giudizio: ", self.get_rate())
        print("Terribile: ", self.rate_percentage(1))
        print("Brutto: ", self.rate_percentage(2))
        print("Normale: ", self.rate_percentage(3))
        print("Bello: ", self.rate_percentage(4))
        print("Grandioso: ", self.rate_percentage(5))



class Film(Media):
    def __init__(self, titolo: str) -> None:
        super().__init__(titolo)

        self.regista: str = ""
        self.elenco_libri: list = []

    def set_director(self, regista):
        self.regista = regista

    def get_director(self):
        return self.regista
    


class Libro(Media):
    def __init__(self, titolo: str, autore:str) -> None:
        super().__init__(titolo)

        self.autore = autore
        self.elenco_film = list()

    def get_author(self):
        return self.autore
    

libro_1: Libro = Libro("Dieci piccoli indiani", "Agatha Christie")
film_1: Film = Film("Oppenheimer")

libro_1.aggiungi_valutazione(3)
libro_1.aggiungi_valutazione(4)
libro_1.aggiungi_valutazione(4)
libro_1.aggiungi_valutazione(5)
libro_1.aggiungi_valutazione(5)
libro_1.aggiungi_valutazione(5)
libro_1.aggiungi_valutazione(3)
libro_1.aggiungi_valutazione(5)
libro_1.aggiungi_valutazione(4)

libro_1.aggiungi_valutazione(7)

libro_1.recensione()