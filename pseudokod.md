KLASS Cafe
    HA privat pängar
    HA privat DICTIONARY ingredienser
        DICTIONARY kaffebönor
            mängd
            pris
        DICTIONARY mjöl
            mängd
            pris
        DICTIONARY ägg
            mängd
            pris
        DICTIONARY socker
            mängd
            pris
        DICTIONARY bakpulver
            mängd
            pris
        DICTIONARY vispgrädde
            mängd
            pris
    METOD köp_ingredienser
        VÄLJ vilka och mängd av ingredienser
        OM man har tillräkligt med pengar
            ta bort den mängden pengar
            lägg till den mängden ingredienser
    METOD använd_ingredienser
        förlora en viss mängd ingredienser
    METOD get_ingredienser
        RETURN hur mycket det finns av en viss ingrediens
    METOD tjäna_pengar
        få mer pengar
    METOD spendera_pengar
        tappa pengar
    METOD get_pengar
        RETURN mängden pengar
    
KLASS Produkt
    HA namn
    HA mängd
    HA pris
    HA DICTIONARY recept
    METOD skapa_produkt
        OM det finns tillräkligt med ingredienser
            ta bort ingredienserna som används
            mängd blir mer

SUPERKLASS Person
    HA namn
    HA tålamod

SUBKLASS Normal
    HA 