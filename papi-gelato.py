aantalBollen = 0
aantalHoorntjes = 0
aantalBakjes = 0
blGeld = 0
bkGeld = 0
hrGeld = 0
def ijshouder(soort):
    if soort == "a":
        soort = "hoorntje"
        global aantalHoorntjes
        aantalHoorntjes += 1
        return soort
    elif soort == "b":
        soort = "bakje"
        global aantalBakjes
        aantalBakjes += 1
        return soort

def stap3(soort, bollen):
    antwoord = input("Hier is uw " + soort + " met " + bollen + " bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()
    if antwoord == "y":
        stap1()
    elif antwoord == "n":
        bonnetje()
        print("Bedankt en tot ziens!")
        exit()
    else:
        print("Sorry dat snap ik niet...")
        stap3(soort, bollen)


def stap2(bollen):
    soort = input("Wilt u deze " + bollen + " bolletje(s) in A) een hoorntje of B) een bakje? ").lower()
    if soort == "a" or soort == "b":
        soort = ijshouder(soort)
        stap3(soort, bollen)
    else:
        print("Sorry dat snap ik niet...")
        stap2(bollen)


def stap1():
    bollen = input("Hoeveel bolletjes wilt u? ")
    if bollen.isdigit() == False:
        print("Sorry dat snap ik niet...")
        stap1()
    else:
        bollen1 = int(bollen)
        global aantalBollen
        aantalBollen += bollen1
    if bollen1 <= 3 and bollen1 > 0:
        smaak(bollen1)
        stap2(bollen)
    elif bollen1 <=8:
        smaak(bollen1)
        print("Dan krijgt u van mij een bakje met " + bollen + " bolletjes.")
        soort = "bakje"
        global aantalBakjes
        aantalBakjes += 1
        stap3(soort, bollen)
    elif bollen1 > 8:
        print("Sorry, zulke grote bakken hebben we niet.")
        stap1()
    else:
        print("Sorry dat snap ik niet...")
        stap1()

def smaak(bollen):
    x = 0
    while x < bollen:
        x += 1
        check = input("Welke smaak wilt u voor bolletje nummer " + str(x) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").lower()
        if check != "a" and check != "c" and check != "m" and check != "v":
            x -= 1
            print("Sorry dat snap ik niet...")

def bolGeld(bollen):
    bolBetaal = round((float(bollen) * 1.10),2)
    global blGeld 
    blGeld = bolBetaal
    return "€" + str(bolBetaal)

def bakGeld(bakjes):
    bakBetaal = round((float(bakjes) * 0.75),2)
    global bkGeld
    bkGeld = bakBetaal
    return "€" + str(bakBetaal)

def hoornGeld(hoorntjeS):
    hoornBetaal = round((float(hoorntjeS) * 1.25),2)
    global hrGeld
    hrGeld = hoornBetaal
    return "€" + str(hoornBetaal)



def bonnetje():
        print('---------["Papi Gelato"]---------')
        print("")
        print("Bolletjes     " + str(aantalBollen) + " x €1.10   = " + bolGeld(aantalBollen))
        if aantalHoorntjes > 0 and aantalBakjes > 0:
            print("Horrentje     " + str(aantalHoorntjes) + " x €1.25   = " + hoornGeld(aantalHoorntjes))
            print("Bakje         " + str(aantalBakjes) + " x €0.75   = " + bakGeld(aantalBakjes))
        elif aantalBakjes > 0:
            print("Bakje         " + str(aantalBakjes) + " x €0.75   = " + bakGeld(aantalBakjes))
        elif aantalHoorntjes > 0:
            print("Horrentje     " + str(aantalHoorntjes) + " x €1.25   = " + hoornGeld(aantalHoorntjes))
        print('                          -------- +')
        print('Totaal                    = €' + str((hrGeld + bkGeld + blGeld)))

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
stap1()