# här ska all logik för att prata med användaren ske!!
import bibliotek as BIB
import bok as BOK
import medlem as MEDLEM


if __name__ == '__main__':
    bib = BIB.skapa_bibliotek()
    # Bok 1: Sci-fi roman
    bok1 = BOK.skapa_bok(
        titel="Stjärnornas resa",
        författare="Eva Lund",
        isbn="978-3-16-148410-0",
        beskrivning="En resa genom rymden där besättningen upptäcker okända planeter och livsformer.",
        tillgänglig=True
    )

    # Bok 2: Deckare
    bok2 = BOK.skapa_bok(
        titel="Mordet på tåget",
        författare="Johan Ekman",
        isbn="978-1-84-149932-1",
        beskrivning="Ett spännande mordmysterium ombord på ett lyxtåg som rör sig genom Europas hjärta.",
        tillgänglig=False
    )

    # Bok 3: Fantasy
    bok3 = BOK.skapa_bok(
        titel="Drakarnas rike",
        författare="Anna Norén",
        isbn="978-0-14-312779-6",
        beskrivning="I en värld där drakar härskar, måste en modig ung tjej finna sitt sanna öde.",
        tillgänglig=True
    )

    # Bok 4: Fakta
    bok4 = BOK.skapa_bok(
        titel="Robotikens framtid",
        författare="Sven Karlsson",
        isbn="978-0-465-06710-7",
        beskrivning="En insiktsfull analys av hur robotar och AI kommer att förändra vår framtid.",
        tillgänglig=True
    )

    # Bok 5: Barnbok
    bok5 = BOK.skapa_bok(
        titel="Äventyret med björnarna",
        författare="Lina Larsson",
        isbn="978-0-7475-3269-9",
        beskrivning="Två små björnar ger sig ut på en episk resa genom skogen för att hitta sin familj.",
        tillgänglig=False
    )
        # Medlem 1: Äventyraren
    medlem1 = MEDLEM.skapa_medlem(
        namn="Alice Bergström",
        medlems_id=1001
    )

    # Medlem 2: Detektivfantasten
    medlem2 = MEDLEM.skapa_medlem(
        namn="Erik Johansson",
        medlems_id=1002
    )

    # Medlem 3: Fantasyälskaren
    medlem3 = MEDLEM.skapa_medlem(
        namn="Linnea Sandström",
        medlems_id=1003
    )

    # Medlem 4: Robotikexperten
    medlem4 = MEDLEM.skapa_medlem(
        namn="Oskar Nilsson",
        medlems_id=1004
    )

    # Medlem 5: Barnboksläsaren
    medlem5 = MEDLEM.skapa_medlem(
        namn="Ella Lundqvist",
        medlems_id=1005
    )   

    BIB.lägg_till_sparade_böcker(bib, [bok1,bok2,bok3,bok4,bok5])
    BIB.lägg_till_sparade_medlemmar(bib, [medlem1,medlem2,medlem3,medlem4,medlem5])

    print("#"*30)
    # print(bib)
    BIB.skriv_ut_bibliotek(bib)
    print("#"*30)
    gick_bra = BIB.låna_ut_bok(bib, "978-0-7475-3269-9", 1003)
    # print(gick_bra)
    BIB.skriv_ut_bibliotek(bib)
    print("#"*30)
