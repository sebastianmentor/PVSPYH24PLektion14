def skapa_medlem(namn, medlems_id):
    """
    namn: str
    medlems_id: int
    """
    medlem = {
        "namn":namn,
        "id":medlems_id,
        "lån":[]
    }

    return medlem

def låna_bok(medlem, bok):
    medlem['lån'].append(bok)

def lämna_tillbaka_bok(medlem, bok):
    if bok in medlem['lån']:
        index = medlem['lån'].find(bok)
        return medlem['lån'].pop(index)
    
    return None

if __name__ == '__main__':
    medlem1 = skapa_medlem("Sebastian",5)
    print(medlem1)