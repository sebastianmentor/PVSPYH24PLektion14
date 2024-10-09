class Bok:
    def __init__(self, titel, författare, isbn):
        self.titel = titel
        self.författare = författare
        self.isbn = isbn
        self.tillgänglig = True 

    def __str__(self):
        return f"{self.titel}-{self.författare}-{self.isbn}"

    def visa_info(self):
        ...