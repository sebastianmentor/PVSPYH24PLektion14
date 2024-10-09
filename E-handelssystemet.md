**Uppgift: Utveckla ett E-handelssystem med OOP i Python**

Du ska skapa ett E-handelssystem som använder objektorienterad programmering i Python. Systemet ska hantera produkter, kunder, varukorgar och beställningar.

---

### **Kravspecifikation:**

#### **1. Klasser att implementera:**

- **Produkt**
  - **Attribut:**
    - `produkt_id` (int)
    - `namn` (str)
    - `pris` (float)
    - `beskrivning` (str)
    - `lager` (int)
  - **Metoder:**
    - `visa_info()` - Skriver ut information om produkten.
    - `justera_lager(antal)` - Justerar lagersaldot för produkten.

- **Kund**
  - **Attribut:**
    - `kund_id` (int)
    - `namn` (str)
    - `epost` (str)
    - `adress` (str)
    - `varukorg` (Varukorg-objekt)
    - `beställningar` (lista över Beställning-objekt)
  - **Metoder:**
    - `lägg_till_i_varukorg(produkt, antal)` - Lägger till en produkt i varukorgen.
    - `visa_varukorg()` - Visar innehållet i varukorgen.
    - `gör_beställning()` - Skapar en ny beställning baserat på varukorgen.
    - `visa_beställningar()` - Visar alla kundens beställningar.

- **Varukorg**
  - **Attribut:**
    - `produkter` (dictionary med Produkt-objekt som nycklar och antal som värden)
  - **Metoder:**
    - `lägg_till_produkt(produkt, antal)` - Lägger till en produkt till varukorgen.
    - `ta_bort_produkt(produkt)` - Tar bort en produkt från varukorgen.
    - `beräkna_totalt_pris()` - Beräknar det totala priset för alla produkter i varukorgen.
    - `visa_varukorg()` - Visar alla produkter och deras antal i varukorgen.

- **Beställning**
  - **Attribut:**
    - `beställnings_id` (int)
    - `kund` (Kund-objekt)
    - `produkter` (dictionary med Produkt-objekt som nycklar och antal som värden)
    - `totalt_pris` (float)
    - `datum` (datumobjekt)
    - `status` (str) - t.ex. "Behandlas", "Skickad", "Levererad"
  - **Metoder:**
    - `uppdatera_status(ny_status)` - Uppdaterar beställningens status.
    - `visa_beställning()` - Skriver ut detaljer om beställningen.

- **Butik**
  - **Attribut:**
    - `produkter` (lista över Produkt-objekt)
    - `kunder` (lista över Kund-objekt)
    - `beställningar` (lista över Beställning-objekt)
  - **Metoder:**
    - `lägg_till_produkt(produkt)` - Lägger till en ny produkt i butiken.
    - `ta_bort_produkt(produkt)` - Tar bort en produkt från butiken.
    - `registrera_kund(kund)` - Lägger till en ny kund.
    - `sök_produkt_namn(namn)` - Söker efter produkter baserat på namn.
    - `visa_alla_produkter()` - Visar alla produkter i butiken.
    - `visa_alla_beställningar()` - Visar alla beställningar som har gjorts.

---

#### **2. Funktionalitet:**

- **Produkt- och Lagerhantering:**
  - Lägga till och ta bort produkter i butiken.
  - Justera lagersaldo för produkter.
  - Visa alla tillgängliga produkter med pris och beskrivning.

- **Kundhantering:**
  - Registrera nya kunder med personliga uppgifter.
  - Kunder kan hantera sin varukorg och göra beställningar.
  - Visa kundens beställningshistorik.

- **Varukorgsfunktioner:**
  - Lägga till och ta bort produkter i varukorgen.
  - Visa innehållet i varukorgen och totalt pris.
  - Tömma varukorgen efter att en beställning har gjorts.

- **Beställningshantering:**
  - Skapa nya beställningar baserat på varukorgens innehåll.
  - Uppdatera status för beställningar.
  - Visa detaljer om specifika beställningar.

---

#### **3. Extra Utmaningar (Valfritt):**

- **Betalningssystem:**
  - Implementera en klass **Betalning** med attribut som `betalnings_id`, `belopp`, `betalningsmetod` och `betalningsdatum`.
  - Koppla betalningar till beställningar och kunder.

- **Undantagshantering:**
  - Hantera fall där en kund försöker beställa mer än vad som finns i lager.
  - Hantera ogiltiga inmatningar, såsom negativa antal eller priser.

- **Arv och Polymorfism:**
  - Skapa en basklass **Person** som förälder till **Kund** och potentiellt **Administratör**-klasser.
  - **Administratör** kan ha särskilda rättigheter, såsom att lägga till produkter och se alla beställningar.

- **Rabatt- och Kampanjsystem:**
  - Implementera ett system för rabatter, där vissa produkter kan ha rabatterade priser.
  - Skapa kampanjer som "Köp 3 betala för 2" eller procentuella rabatter vid köp över ett visst belopp.

- **Data Persistence:**
  - Spara data om produkter, kunder och beställningar till filer eller en databas för att bevara information mellan sessioner.

- **Grafiskt Gränssnitt:**
  - Skapa ett användarvänligt GUI med Tkinter eller PyQt för att förbättra interaktionen.

---

#### **4. Testning:**

- **Enhetstester:**
  - Skriv tester för varje klass och metod för att säkerställa att de fungerar korrekt.
  - Använd bibliotek som `unittest` eller `pytest`.

- **Simulering av Användarscenarier:**
  - Skapa testfall som simulerar en kund som bläddrar produkter, lägger till dem i varukorgen och gör en beställning.
  - Testa scenario där lagersaldot är lågt eller slutsålt.

- **Prestandatester:**
  - Om du implementerar data persistence, testa hur systemet presterar med en stor mängd data.

---

### **Instruktioner:**

- **Kodstruktur:**
  - Använd korrekta OOP-principer som inkapsling, arv och polymorfism där det är lämpligt.
  - Följ PEP 8-stilguiden för Python-kodning.
  - Kommentera din kod för att förklara funktioner och komplexa delar.

- **Dokumentation:**
  - Skapa en README-fil som förklarar hur man installerar och kör programmet.
  - Beskriv de viktigaste funktionerna och hur användaren interagerar med systemet.
  - Om du har implementerat extra funktioner, beskriv hur de fungerar.

---

### **Leverans:**

- Alla Python-filer med källkoden.
- En README-fil med instruktioner och beskrivningar.
- Eventuella ytterligare filer, såsom testdata, konfigurationsfiler eller databasfiler.

---

**Lycka till med projektet!** Om du har några frågor eller behöver hjälp med specifika delar, tveka inte att be om hjälp.