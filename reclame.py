from algemene_functies import mijn_functie2

def aanbieding_1(smaak,prijs,korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs - (korting * prijs)} euro."
    return uitvoer
    
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    inkomsten_totaal = sum(inkomsten)
    return inkomsten_totaal

print(inkomsten_totaal([220,430,125,160,205,90,345]))
      
weekomzet = [220, 430, 125, 160, 205, 90, 345]
def inkomsten_totaal(inkomsten,btw):
    uitvoer = f"Het totaal van alle inkomsten van deze week is {sum(weekomzet)} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal(weekomzet, 0.09 * sum(weekomzet)))   

def laag_en_hoog(mijn_lijst):
    laag_en_hoog = max(mijn_lijst), min(mijn_lijst)
    return laag_en_hoog


def gemiddelde(mijn_lijst):
    gemiddelde = f"De gemiddelde inkomsten deze week zijn {sum(weekomzet) / len(weekomzet)} euro."
    return gemiddelde


def meervoudig(invoer_lijst):
    if len(invoer_lijst) <5 or len(invoer_lijst) > 10:
        return "Fout"
    else:
        return laag_en_hoog(invoer_lijst)
    
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    meervoudig(invoer_lijst_2)
    korte_lijst = [1,2]
    return korte_lijst

mijn_functie2(korte_lijst)
return combinatie


    
    





