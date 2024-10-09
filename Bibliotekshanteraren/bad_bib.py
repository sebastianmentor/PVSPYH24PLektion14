def skapa_bibliotek(böcker=None, medlemmar=None, lånade_böcker=None):
    if böcker and medlemmar and lånade_böcker: # Vi har skickat in alla 3
        pass
    elif böcker and medlemmar: # vi har skickat in böcker och medlemmar
        lånade_böcker = []
    elif böcker and lånade_böcker: # vi har skickat in böcker och lånade_böcker
        medlemmar = []
    elif medlemmar and lånade_böcker: # vi har skickat in medelmmar och lånade_böcker
        böcker = []
    elif böcker: # vi har bara skickat in böcker
        medlemmar = []
        lånade_böcker = []
    elif medlemmar: # vi har bara skickat in medlemmar
        lånade_böcker = []
        böcker = []
    elif lånade_böcker: # vi har bara skickat in lånade_böcker
        böcker = []
        medlemmar = []
    else: # vi skicka inte in något när vi anropa skapa_bibliotek()
        böcker = []
        medlemmar = []
        lånade_böcker = []

    bib = {
        "böcker":böcker,
        "medlemmar":medlemmar,
        "lånade_böcker":lånade_böcker
    }

    return bib