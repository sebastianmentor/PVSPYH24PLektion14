import medlem as M

def skapa_bibliotek():
    bib = {
        "böcker":[],
        "medlemmar":[],
        "lånade_böcker":[]
    }
    return bib

def skriv_ut_bibliotek(bib):
    for key, val in bib.items():
        print(f"{key}:")
        for item in val:
            print(f"\t{item}")

def lägg_till_sparade_böcker(bib, böcker):
    bib['böcker'] += böcker

def lägg_till_sparade_medlemmar(bib, medlemmar):
    bib['medlemmar'] += medlemmar

def lägg_till_sparade_lånade_böcker(bib, lånade_böcker):
    bib['lånade_böcker'] += lånade_böcker

def lägg_till_bok(bib, bok):
    bib['böcker'].append(bok)

def lägg_till_medlem(bib, medlem):
    bib['medlemmar'].append(medlem)

def hämta_medlem(bib, medlems_id):
    for medlem in bib['medlemmar']:
        if medlems_id == medlem['id']:
            return medlem
    
    return None

def hämta_bok(bib, isbn):
    for bok in bib['böcker']:
        if isbn == bok['isbn']:
            return bok
    
    return None    

def låna_ut_bok(bib, isbn, medlems_id):
    låntagare = hämta_medlem(bib, medlems_id)
    if not låntagare: return False

    lånebok = hämta_bok(bib, isbn)
    if not lånebok: return False

    M.låna_bok(låntagare, lånebok)

    bib['böcker'].remove(lånebok)
    lån = {'lånebok': lånebok, 'medlems_id':medlems_id}
    bib['lånade_böcker'].append(lån)

    return True

def hämta_lånad_bok(bib, isbn, medlems_id):
    for lånad_bok in bib['lånade_böcker']:
        if lånad_bok['medlems_id'] == medlems_id:
            if lånad_bok['lånebok']['isbn'] == isbn:
                return lånad_bok
            
    return None



def återlämna_bok(bib, isbn ,medlems_id):
    medlem = hämta_medlem()
    if not medlem: return False

    lånad_bok = hämta_lånad_bok(bib, isbn, medlems_id)
    if not lånad_bok: return False

    bok_från_medlem = M.lämna_tillbaka_bok(medlem, lånad_bok['lånebok'])
    if not bok_från_medlem: return False

    bib['lånade_böcker'].remove(lånad_bok)
    bib['böcker'].append(bok_från_medlem)


if __name__ == '__main__':
    bib1 = skapa_bibliotek(['bok1','bok2'], ['medlem1', 'medlem2'])
    bib2 = skapa_bibliotek(['bok1', 'bok2'])
    bib3 = skapa_bibliotek()