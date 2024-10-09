**Uppgift: Utveckla ett Restaurangbeställningssystem med OOP i Python**

Du ska skapa ett restaurangbeställningssystem som använder objektorienterad programmering i Python. Systemet ska hantera menyer, beställningar och kundinformation.

---

### **Kravspecifikation:**

#### **1. Klasser att implementera:**

- **Maträtt**
  - **Attribut:**
    - `namn` (str)
    - `pris` (float)
    - `beskrivning` (str)
    - `tillgänglig` (bool)
  - **Metoder:**
    - `visa_info()` - Skriver ut information om maträtten.

- **Meny**
  - **Attribut:**
    - `maträtter` (lista över Maträtt-objekt)
  - **Metoder:**
    - `lägg_till_maträtt(maträtt)` - Lägger till en ny maträtt i menyn.
    - `ta_bort_maträtt(maträtt)` - Tar bort en maträtt från menyn.
    - `visa_meny()` - Visar alla tillgängliga maträtter.

- **Kund**
  - **Attribut:**
    - `namn` (str)
    - `telefonnummer` (str)
    - `beställningar` (lista över Beställning-objekt)
  - **Metoder:**
    - `gör_beställning(beställning)` - Lägger till en beställning till kundens historik.
    - `visa_beställningar()` - Visar alla kundens beställningar.

- **Beställning**
  - **Attribut:**
    - `beställnings_id` (int)
    - `kund` (Kund-objekt)
    - `maträtter` (lista över Maträtt-objekt)
    - `totalt_pris` (float)
    - `status` (str) - t.ex. "Mottagen", "Tillagas", "Klar", "Levererad"
  - **Metoder:**
    - `beräkna_totalt_pris()` - Beräknar det totala priset för beställningen.
    - `uppdatera_status(ny_status)` - Uppdaterar beställningens status.
    - `visa_beställning()` - Skriver ut detaljer om beställningen.

- **Restaurang**
  - **Attribut:**
    - `namn` (str)
    - `meny` (Meny-objekt)
    - `beställningar` (lista över Beställning-objekt)
    - `kunder` (lista över Kund-objekt)
  - **Metoder:**
    - `lägg_till_kund(kund)` - Lägger till en ny kund.
    - `ta_emot_beställning(beställning)` - Lägger till en ny beställning.
    - `visa_alla_beställningar()` - Visar alla beställningar i systemet.
    - `sök_beställning(beställnings_id)` - Söker efter en beställning via ID.

---

#### **2. Funktionalitet:**

- **Menyhantering:**
  - Lägga till och ta bort maträtter i menyn.
  - Visa alla tillgängliga maträtter med pris och beskrivning.

- **Beställningshantering:**
  - Kunder kan göra beställningar från menyn.
  - Systemet beräknar automatiskt det totala priset för en beställning.
  - Möjlighet att uppdatera status för beställningar.
  - Visa detaljer om specifika beställningar.

- **Kundhantering:**
  - Registrera nya kunder med namn och telefonnummer.
  - Visa en kunds beställningshistorik.

---

#### **3. Extra Utmaningar (Valfritt):**

- **Betalningshantering:**
  - Skapa en klass **Betalning** med attribut som `belopp`, `betalningsmetod` och `betalningsdatum`.
  - Koppla betalningar till beställningar och kunder.

- **Undantagshantering:**
  - Hantera fall där en maträtt som inte är tillgänglig försöker beställas.
  - Hantera ogiltiga inmatningar, såsom negativa priser eller tomma namn.

- **Arv och Polymorfism:**
  - Skapa en basklass **Person** som förälder till **Kund** och potentiellt **Anställd**-klasser.
  - **Anställd** kan ha underklasser som **Kock** och **Servitör**, med specifika roller och metoder.

- **Data Persistent:**
  - Spara data om menyer, kunder och beställningar till filer eller en databas för att bevara information mellan sessioner.

- **Grafiskt Gränssnitt:**
  - Implementera ett GUI med Tkinter eller PyQt för att förbättra användarinteraktionen.

---

#### **4. Testning:**

- Skapa en serie testfall för att säkerställa att alla metoder och klasser fungerar korrekt.
- Använd testdata för att simulera olika scenarier, såsom flera samtidiga beställningar eller ändringar i menyn.

---

### **Instruktioner:**

- **Kodstruktur:**
  - Använd korrekta OOP-principer som inkapsling, arv och polymorfism där det är lämpligt.
  - Följ PEP 8-stilguiden för Python-kodning.
  - Kommentera din kod för att förklara funktioner och komplexa delar.

- **Dokumentation:**
  - Skapa en README-fil som förklarar hur man installerar och kör programmet.
  - Beskriv de viktigaste funktionerna och hur användaren interagerar med systemet.

---

### **Leverans:**

- Alla Python-filer med källkoden.
- En README-fil med instruktioner och beskrivningar.
- Eventuella ytterligare filer, såsom testdata eller konfigurationsfiler.

---

**Lycka till med projektet!** Om du har några frågor eller behöver hjälp med specifika delar, tveka inte att be om hjälp.