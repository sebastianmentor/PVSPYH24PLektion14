class Medlem:
    def __init__(self, namn, medlems_id):
        self.namn = namn
        self._medlems_id = medlems_id
        self.lånade_böcker = []

    def get_id(self):
        return self._medlems_id

    def låna_bok(self, bok):
        if bok.tillgänglig:
            self.lånade_böcker.append(bok)
            bok.tillgänglig = False
            return True
        return False
        

    def lämna_tillbaka_bok(self, bok):
        if bok in self.lånade_böcker:
            bok.tillgänglig = True
            self.lånade_böcker.remove(bok)
            return True
        return False
        
    def visa_lånade_böcker(self):
        for bok in self.lånade_böcker:
            print(bok)