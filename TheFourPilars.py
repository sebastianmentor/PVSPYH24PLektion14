# 1. Abstraction
# 2. Incapsulation
# 3. Inheritance 
# 4. Polymorfism

# Låt oss abstrahera en Affär!

class Affär:
    def __init__(self, namn, adress, nyckel):
        self.namn = namn
        self.adress = adress
        self._nyckel = nyckel
        self._dörr_öppen = False
        self._lager = []

    def gå_in_i_affären(self):
        if self._dörr_öppen:
            print("Dörrarna öppnar sig, varsågod och gå in!")
        else:
            print("Affären är stängd! Dörrana öppnas inte!")

    def öppna_affären(self, nyckel):
        if self._nyckel == nyckel:
            if self._dörr_öppen:
                print("Dörren är redan öppen! Går ej att låsa upp då!")
            else:
                self._dörr_öppen = True
                print("Dörrarna låses upp!")
        else:
            print("Oglitlig nyckel, går ej att öppna dörrarna då!")

    def stäng_affären(self, nyckel):
        ...
