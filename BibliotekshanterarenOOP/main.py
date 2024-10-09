from bibliotek import Bibliotek, Medlem, Bok

# Exempel på medlemsobjekt
medlem1 = Medlem("Anna Andersson", 101)
medlem2 = Medlem("Erik Svensson", 102)
medlem3 = Medlem("Daniel Banan", 103)
medlem4 = Medlem("Sebastian Öhman", 104)
medlem5 = Medlem("Kalle Anka", 105)
medlem6 = Medlem("Nils Hansson", 106)

lista_med_medlemmar = [medlem1, medlem2, medlem3, medlem4, medlem5,medlem6]
# Skapa några bokobjekt
bok1 = Bok("Mästaren och Margarita", "Michail Bulgakov", "9780143108276")
bok2 = Bok("Sagan om ringen", "J.R.R. Tolkien", "9780261103573")
bok3 = Bok("Bröderna Lejonhjärta", "Astrid Lindgren", "9789129655546")
bok4 = Bok("Harry Potter och de vises sten", "J.K. Rowling", "9780747532699")

lista_med_böcker = [bok1, bok2, bok3, bok4]

bib = Bibliotek()

for medlem in lista_med_medlemmar:
    bib.registrera_medlem(medlem)

for bok in lista_med_böcker:
    bib.lägg_till_bok(bok)

for bok in bib.hämta_tillgängliga_böcker():
    print(bok)
print("#"*30)
medlem1.låna_bok(bok2)

for bok in bib.hämta_tillgängliga_böcker():
    print(bok)
print("#"*30)
medlem1.lämna_tillbaka_bok(bok2)
for bok in bib.hämta_tillgängliga_böcker():
    print(bok)

print(bib.sök_bok_författare("J.R.R. Tolkien"))
print(bib.sök_bok_författare("KAlle anka"))

medlem3.låna_bok(bok1)
print(f"{bib.ta_bort_bok(bok1)=}")