**Uppgift: Utveckla ett 2D Plattformsäventyrsspel med OOP i Python**

Du ska skapa ett 2D plattformsspel som använder objektorienterad programmering i Python. Spelet ska inkludera en spelkaraktär, hinder, fiender, samlarobjekt och flera nivåer.

---

### **Kravspecifikation:**

#### **1. Klasser att implementera:**

- **Spelobjekt (abstrakt klass)**
  - **Attribut:**
    - `x` (float) - Horisontell position
    - `y` (float) - Vertikal position
    - `bredd` (int)
    - `höjd` (int)
  - **Metoder:**
    - `rita()` - Abstrakt metod för att rita objektet på skärmen.
    - `uppdatera()` - Abstrakt metod för att uppdatera objektets tillstånd.

- **Spelare (subklass av Spelobjekt)**
  - **Attribut:**
    - `hastighet_x` (float)
    - `hastighet_y` (float)
    - `hälsa` (int)
    - `poäng` (int)
  - **Metoder:**
    - `rör_vänster()`
    - `rör_höger()`
    - `hoppa()`
    - `kollidera_med(objekt)` - Hanterar kollision med andra objekt.
    - `uppdatera()`
    - `rita()`

- **Fiende (subklass av Spelobjekt)**
  - **Attribut:**
    - `hastighet` (float)
    - `riktning` (str) - "vänster" eller "höger"
  - **Metoder:**
    - `rör_på_sig()` - Bestämmer hur fienden rör sig.
    - `uppdatera()`
    - `rita()`

- **Hinder (subklass av Spelobjekt)**
  - **Metoder:**
    - `uppdatera()`
    - `rita()`

- **Samlarobjekt (subklass av Spelobjekt)**
  - **Attribut:**
    - `typ` (str) - T.ex. "mynt", "hälsa"
  - **Metoder:**
    - `samla(spelare)` - Hanterar när spelaren samlar objektet.
    - `uppdatera()`
    - `rita()`

- **Nivå**
  - **Attribut:**
    - `nummer` (int)
    - `bakgrund` (bild eller färg)
    - `spelare` (Spelare-objekt)
    - `fiender` (lista över Fiende-objekt)
    - `hinder` (lista över Hinder-objekt)
    - `samlarobjekt` (lista över Samlarobjekt)
  - **Metoder:**
    - `ladda_nivå()` - Laddar alla objekt för nivån.
    - `uppdatera()` - Uppdaterar alla objekt i nivån.
    - `rita()` - Ritar alla objekt på skärmen.

- **Spel**
  - **Attribut:**
    - `nivåer` (lista över Nivå-objekt)
    - `aktuell_nivå_index` (int)
    - `kör` (bool)
  - **Metoder:**
    - `starta_spelet()`
    - `avsluta_spelet()`
    - `uppdatera()`
    - `rita()`
    - `hantera_händelser()` - Hanterar användarinmatning.

---

### **2. Funktionalitet:**

- **Spelarens Rörelse:**
  - Spelaren ska kunna röra sig vänster och höger samt hoppa.
  - Implementera gravitation så att spelaren faller när den inte står på ett hinder.
  - Begränsa spelarens rörelse inom spelvärlden.

- **Kollisioner:**
  - Hantera kollisioner mellan spelaren och hinder, fiender och samlarobjekt.
  - När spelaren krockar med en fiende minskar hälsan.
  - När spelaren samlar ett samlarobjekt ökar poängen eller hälsan.
  - Hantera kollisioner mellan fiender och hinder för att ändra riktning.

- **Fiender:**
  - Fiender ska röra sig automatiskt, t.ex. patrullera mellan två punkter.
  - Implementera olika typer av fiender med unika beteenden.

- **Nivåhantering:**
  - Skapa minst tre nivåer med ökande svårighetsgrad.
  - När spelaren når slutet av en nivå ska nästa nivå laddas.
  - Om spelaren förlorar all hälsa ska spelet avslutas eller börja om från första nivån.

- **Användargränssnitt:**
  - Visa spelarens hälsa och poäng på skärmen.
  - Implementera en startmeny med alternativ som "Starta Spelet", "Instruktioner" och "Avsluta".
  - Skapa en spelöver-skärm som visar slutpoäng och ger möjlighet att spela igen.

---

### **3. Extra Utmaningar (Valfritt):**

- **Användning av Pygame:**
  - Använd Pygame-biblioteket för grafik, ljud och händelsehantering.

- **Avancerad Fiende-AI:**
  - Implementera fiender som följer efter spelaren eller avfyrar projektiler.
  - Lägg till boss-fiender med unika attacker.

- **Sparfunktion:**
  - Lägg till möjligheten att spara och ladda spelets tillstånd mellan spelsessioner.

- **Ljud och Musik:**
  - Lägg till ljudeffekter för hopp, kollisioner och samlande av objekt.
  - Lägg till bakgrundsmusik för olika nivåer eller händelser.

- **Anpassningsbar Spelare:**
  - Låt spelaren välja mellan olika karaktärer med unika egenskaper, t.ex. högre hopp eller snabbare rörelse.

- **Fysikmotor:**
  - Implementera en enkel fysikmotor för mer realistiska rörelser och kollisioner.

- **Nivåredigerare:**
  - Skapa ett verktyg som tillåter användaren att skapa egna nivåer.

---

### **4. Testning:**

- **Enhetstester:**
  - Skriv tester för klasser och metoder, särskilt för spelmekanik som rörelse och kollisioner.

- **Speltestning:**
  - Spela igenom spelet flera gånger för att hitta och åtgärda buggar.
  - Be andra personer testa spelet och ge feedback på spelbarhet och svårighetsgrad.

- **Prestandatestning:**
  - Optimera spelet för att köra smidigt, även med många objekt på skärmen.

---

### **Instruktioner:**

- **Kodstruktur:**
  - Använd korrekta OOP-principer som inkapsling, arv och polymorfism.
  - Organisera koden i moduler och paket för bättre läsbarhet och underhåll.
  - Kommentera koden och använd docstrings för att dokumentera klasser och metoder.

- **Dokumentation:**
  - Skapa en README-fil som förklarar:
    - Hur man installerar nödvändiga beroenden (t.ex. Pygame).
    - Hur man kör spelet.
    - Spelkontroller och mål.
    - Eventuella kända buggar eller begränsningar.

- **Grafiska Resurser:**
  - Använd egna eller fria grafiska resurser för spelkaraktärer, fiender och bakgrunder.
  - Ange källa och licens för eventuella tredjepartsresurser.

---

### **Leverans:**

- **Källkod:**
  - Alla Python-filer med koden, organiserade i lämpliga mappar.
  - Se till att koden körs utan fel på en standard Python-installation med nödvändiga bibliotek.

- **Resurser:**
  - Bilder, ljudfiler och andra resurser som krävs för att köra spelet.

- **Dokumentation:**
  - README-fil med instruktioner och beskrivningar.
  - Eventuella ytterligare dokument som förklarar designbeslut eller användarmanualer.

- **Exekverbar Fil (Valfritt):**
  - Om möjligt, inkludera en exekverbar fil eller installationsprogram för enkel distribution.

---

**Ha det så roligt med projektet och låt kreativiteten flöda!** Om du stöter på problem eller har frågor under utvecklingen, tveka inte att be om hjälp.