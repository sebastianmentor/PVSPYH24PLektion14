from medlem import Medlem
from bok import Bok

class Bibliotek:
    def __init__(self):
        self._böcker = []
        self._medlemmar = []

    def registrera_medlem(self, medlem):
        if isinstance(medlem, Medlem) and not medlem in self._medlemmar:
            self._medlemmar.append(medlem)
            return True

        return False
    
    def ta_bort_medlem(self, medlem):
        if medlem in self._medlemmar:
            if medlem.lånade_böcker == []:
                self._medlemmar.remove(medlem)
                return True
                
            return False

        return False

    def lägg_till_bok(self, bok):
        if isinstance(bok, Bok) and not bok in self._böcker:
            self._böcker.append(bok)
            return True

        return False

    def ta_bort_bok(self, bok):
        if bok in self._böcker and bok.tillgänglig:
            self._böcker.remove(bok)
            return True
                
        return False


    def sök_bok_titel(self, titel):
        for bok in self._böcker:
            if bok.titel == titel:
                return True
        return False

    def sök_bok_författare(self, författare):
        for bok in self._böcker:
            if bok.författare == författare:
                return True
        return False

    def hämta_tillgängliga_böcker(self):
        lista_med_tillgängliga_böcker = []
        for bok in self._böcker:
            if bok.tillgänglig:
                lista_med_tillgängliga_böcker.append(bok)

        return lista_med_tillgängliga_böcker
        

