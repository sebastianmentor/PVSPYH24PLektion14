**Uppgift: Utveckla en Avancerad Simulering av ett Transportsystem med OOP i Python**

Du ska skapa en omfattande simulering av ett transportsystem som inkluderar olika transportmedel, stationer, rutter och passagerare. Projektet ska använda avancerade objektorienterade programmeringsprinciper i Python, inklusive arv, polymorfism, abstrakta klasser och designmönster.

---

### **Kravspecifikation:**

#### **1. Klasser att implementera:**

- **Transportmedel (abstrakt klass)**
  - **Attribut:**
    - `id` (str)
    - `kapacitet` (int)
    - `hastighet` (float)
    - `position` (Position-objekt)
    - `passagerare` (lista över Passagerare-objekt)
  - **Metoder:**
    - `flytta(till_position)` - Flyttar transportmedlet till en ny position.
    - `lasta(passagerare)` - Lägger till passagerare om det finns plats.
    - `lasta_av(passagerare)` - Tar bort passagerare.
    - `uppdatera()` - Abstrakt metod för att uppdatera tillståndet.

- **Tåg (subklass av Transportmedel)**
  - **Attribut:**
    - `vagnar` (int)
  - **Metoder:**
    - `uppdatera()` - Implementerar uppdatering specifik för tåg.

- **Buss (subklass av Transportmedel)**
  - **Attribut:**
    - `linjenummer` (int)
  - **Metoder:**
    - `uppdatera()` - Implementerar uppdatering specifik för bussar.

- **Station**
  - **Attribut:**
    - `namn` (str)
    - `position` (Position-objekt)
    - `väntande_passagerare` (kö av Passagerare-objekt)
  - **Metoder:**
    - `anländ_transportmedel(transportmedel)` - Hanterar ankomst av transportmedel.
    - `avgå_transportmedel(transportmedel)` - Hanterar avgång av transportmedel.

- **Passagerare**
  - **Attribut:**
    - `id` (str)
    - `namn` (str)
    - `start_station` (Station-objekt)
    - `destination_station` (Station-objekt)
    - `ombord` (bool)
  - **Metoder:**
    - `vänta()` - Passageraren väntar på transportmedel.
    - `gå_ombord(transportmedel)` - Passageraren går ombord på transportmedel.
    - `gå_av()` - Passageraren går av vid destinationen.

- **Position**
  - **Attribut:**
    - `x` (float)
    - `y` (float)
  - **Metoder:**
    - `avstånd(till_position)` - Beräknar avståndet till en annan position.

- **Rutt**
  - **Attribut:**
    - `stationer` (lista över Station-objekt i ordning)
  - **Metoder:**
    - `nästa_station(current_station)` - Returnerar nästa station på rutten.

- **Transportsystem**
  - **Attribut:**
    - `transportmedel` (lista över Transportmedel-objekt)
    - `stationer` (lista över Station-objekt)
    - `passagerare` (lista över Passagerare-objekt)
    - `tid` (tidsobjekt eller räknare)
  - **Metoder:**
    - `starta_simulering()` - Startar simuleringen.
    - `uppdatera()` - Uppdaterar alla komponenter i systemet per tidssteg.
    - `visa_status()` - Visar aktuell status för systemet.

---

#### **2. Funktionalitet:**

- **Simulering av Transportmedel:**
  - Hantera rörelse av transportmedel längs sina rutter.
  - Hantera lastning och avlastning av passagerare vid stationer.
  - Simulera förseningar och hastighetsvariationer.

- **Passagerarhantering:**
  - Skapa passagerare med slumpmässiga start- och destinationsstationer.
  - Hantera passagerares väntetid och resor.

- **Stationshantering:**
  - Hantera köer av väntande passagerare.
  - Hantera ankomst och avgång av transportmedel.

- **Rutthantering:**
  - Definiera rutter med sekvenser av stationer.
  - Hantera flera rutter för olika transportmedel.

- **Simuleringskontroll:**
  - Möjlighet att pausa, stoppa och återställa simuleringen.
  - Justera simuleringshastigheten.

---

#### **3. Extra Utmaningar (Valfritt):**

- **Användning av Designmönster:**
  - Implementera designmönster som Observer, Strategy, Factory eller Singleton där det är lämpligt.

- **Multi-threading:**
  - Använd trådar för att simulera samtidiga aktiviteter av transportmedel och passagerare.

- **Grafiskt Gränssnitt eller Visualisering:**
  - Skapa en visuell representation av systemet med hjälp av bibliotek som Pygame eller Matplotlib.

- **Datahantering:**
  - Spara simuleringsdata till filer eller en databas för senare analys.

- **AI och Optimering:**
  - Implementera algoritmer för att optimera rutterna eller scheman för transportmedlen.
  - Simulera passagerarflöden baserat på tid på dagen eller andra parametrar.

---

#### **4. Testning:**

- **Enhetstester:**
  - Skriv omfattande tester för alla klasser och metoder.

- **Simuleringsscenarier:**
  - Skapa olika scenarier för att testa systemets beteende under olika förhållanden, t.ex. hög trafik, förseningar, etc.

- **Prestandaoptimering:**
  - Mät och optimera prestandan av simuleringen, särskilt om multi-threading används.

---

### **Instruktioner:**

- **Kodstruktur:**
  - Använd avancerade OOP-koncept som abstrakta klasser och gränssnitt.
  - Följ SOLID-principerna för objektorienterad design.
  - Följ PEP 8-stilguiden för Python-kodning.
  - Kommentera din kod och använd docstrings för att dokumentera klasser och metoder.

- **Dokumentation:**
  - Skapa en detaljerad README-fil som beskriver arkitekturen, designval och hur man kör simuleringen.
  - Om du implementerar designmönster, förklara var och varför de används.

---

### **Leverans:**

- Alla Python-filer med välstrukturerad och dokumenterad källkod.
- En README-fil med detaljerade instruktioner, beskrivningar och eventuella kända begränsningar.
- Testfiler och eventuella datafiler som krävs för att köra simuleringen.
- Om möjligt, inkludera en kort rapport eller presentation som beskriver din designprocess och lärdomar.

---

**Lycka till med denna utmanande uppgift!** Om du stöter på problem eller behöver diskutera designalternativ, tveka inte att be om hjälp.