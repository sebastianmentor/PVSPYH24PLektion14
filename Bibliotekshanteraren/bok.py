# Hur kan vi representera en bok?


def skapa_bok(titel, författare, isbn, beskrivning, tillgänglig=True):
    bok  = {
        "titel":titel,
        "författare":författare,
        "isbn":isbn,
        "beskrivning":beskrivning
    }

    return bok

def hämta_info(bok):
    """Bok ska vara en dictionary med en:
    titel: str
    författare: str
    isbn: int
    tillgänglig: bool
    beskrivning: str
    """

    info = (
        f"Titel:{bok['titel']}\n"
        f"Författare:{bok['författare']}\n"
        f"ISBN:{bok['isbn']}\n"
        f"Beskrivning:{bok['beskrivning']}"
    )

    return info

def visa_info(bok):
    print(hämta_info(bok))



if __name__ == "__main__":
    harry_potter = skapa_bok("Harry Potter", "JK-rowling", "92929929229", "Harry trollar!")

    print(harry_potter)
    info = hämta_info(harry_potter)
    visa_info(harry_potter)