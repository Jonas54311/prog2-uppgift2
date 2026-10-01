KLASS Cafe
    HA privat pängar
    HA privat DICTIONARY ingredienser
        DICTIONARY kaffebönor
            mängd
            pris
        DICTIONARY mjöl
            mängd
            pris
        DICTIONARY socker
            mängd
            pris
        DICTIONARY ägg
            mängd
            pris
        DICTIONARY bakpulver
            mängd
            pris
        DICTIONARY vispgrädde
            mängd
            pris
    HA DICTIONARY produkter
        kaffe
            OBJEKT kaffe
        tårta
            OBJEKT tårta
        muffins
            OBJEKT muffins
        kaka
            OBJEKT kaka
    METOD köp_ingredienser
        VÄLJ vilka och mängd av ingredienser
        OM man har tillräkligt med pengar
            ta bort den mängden pengar
            lägg till den mängden ingredienser
    METOD sänk_ingredienser
        förlora en viss mängd ingredienser
    METOD get_ingredienser
        RETURN hur mycket det finns av en viss ingrediens
    METOD höj_pengar
        få mer pengar
    METOD get_pengar
        RETURN mängden pengar
    
KLASS Produkt
    HA namn
    HA privat mängd
    HA pris
    HA DICTIONARY recept
    METOD skapa_produkt
        TA IN den mängd av produkter som ska skapas
        OM det finns tillräkligt med ingredienser
            ta bort ingredienserna som används
            mängd blir mer
    METOD sänk_mängd
        OM mängden är mer än värdet det ska gå ned med
            mängden går ner med ett visst värde
    METOD get_mängd
        RETURNA mängd

SUPERKLASS Person
    HA namn
    HA privat tålamod
    METOD få_beställning
        kolla alla produkter i beställning
        OM man har tillräkligt av alla produkter för att bli klar med beställningen
            spelaren får pengar baserat på säljvärdet avv alla produkter och hur många man säljer
            spelaren förlorar mängd av produkter
            ta bort detta person objekt från personer listan
        ANNARS
            tappa tålamod
    METOD sänk_tålamod
        tappa en viss mängd tålamod
    METOD set_tålamod
        HE tålamod till ett visst värde
    METOD get_tålamod   
        RETURNA tålamod
    METOD bli_utsparkad
        ta bort detta person objekt från personer listan

SUBKLASS Normal_Person
    HA DICTIONARY beställning
        DICTIONARY kaffe
            mängd
            kaffe objektet
        DICTIONARY tårta
            mängd
            tårta objektet
        DICTIONARY kaka
            mängd
            kaka objekt
        DICTIONARY muffins
            mängd
            muffins objekt
    METOD välj_beställning
        REPEATA en random mängd gånger mellan 1 och 3
            en rändom produkts mängd i beställningen får + 1

SUBKLASS Hungrig_person
    HA DICTIONARY beställning
        DICTIONARY kaffe
            mängd
            kaffe objektet
        DICTIONARY tårta
            mängd
            tårta objektet
        DICTIONARY kaka
            mängd
            kaka objekt
        DICTIONARY muffins
            mängd
            muffins objektet
    METOD välj_beställning
        REPEATA en random mängd gånger mellan 3 och 6
            en rändom produkts mängd i beställningen får + 1

SUBKLASS Korkad_person
    HA DICTIONARY beställning (Inga av dom här kommer att gå att göra)
        DICTIONARY McHappy McMeal
            mängd
            McHappy objektet
        DICTIONARY Uuuuuuuuuuhhhh
            mängd
            Uuuuuuuuuuhhhh objektet
        DICTIONARY kycklingvingar, medium rare
            mängd
            kycklingvingar objektet
        DICTIONARY blinkersvätska
            mängd
            blinkersvätska objektet
    METOD välj_beställning
        REPEATA en random mängd gånger mellan 1 och 2
            en rändom produkts mängd i beställningen får + 1

SUBKLASS Kaffeberoende_person
    HA DICTIONARY beställning
        DICTIONARY kaffe
            mängd
            kaffe objektet
    METOD välj_beställning
        kaffe mängd blir en siffra mellan 3 och 6

SUBKLASS Marie_antoinette
    HA DICTIONARY beställning
        DICTIONARY tårts
            mängd
            tårta objektet
    METOD välj_beställning
        tårt mängd blir en siffra mellan 3 och 6

LISTA persontyper
    LISTA
        KLASSEN Normal
        vikt
    LISTA
        KLASSEN Hungrig
        vikt
    LISTA
        KLASSEN Korkad
        vikt
    LISTA
        KLASSEN Kaffeberoende
        vikt
    LISTA
        KLASSEN Marie_antoinette
        vikt

LISTA namn

LISTA nuvarande_personer
    tom

LOOPA tills pängar är mer än en trilljon
    OM längden av nuvarande_personer är mindre eller lika med 3 OCH en random siffra mellan 0 och 1 är mindre eller lika med 1 / längden av nuvarande personer + 1
        lägg till ett person objekt i listan med en random viktad person subklass och ett random namn från namn listan och random tålamod mellan 3 och 6
        använd det person objektets välj_beställning metod
    printa alla personer och deras beställningar och alla produkter, ingredienser och pengar som spelaren har
    spelaren får välja en sak att göra
        köpa nya ingredienser
            använd cafe objektets köp_ingredienser metod
        gör fler produkter
            spelaren väljer vilka och hur många hen ska baka av varje produkt
            änvänd produkt objekternas skapa_produkt metod med den mängden av produkter som ska skapas
        ge beställning
            spelaren väljer en person och den använder sin få_beställning metod
        sparka ut en person
            spelaren väljer en person och den använder sin bli_utsparkad metod
    alla personer i nuvarande_personder använder sänk_tålamod