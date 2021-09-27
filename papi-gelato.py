aantalBollen = 0
aantalHoorntjes = 0
aantalBakjes = 0
blGeld = 0
bkGeld = 0
hrGeld = 0
tpGeld = 0
slagroom = 0
sprinkels = 0
caramelBakje = 0
caramelHorentje = 0
aantalToppings = 0

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

def stap4(soort,bollen):
    toppings = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").lower()
    global aantalToppings
    if toppings == "a":
        stap3(soort, bollen)
    elif toppings == "b":
        global slagroom
        aantalToppings += 1
        slagroom += 1
    elif toppings == "c":
        global sprinkels
        aantalToppings += 1
        sprinkels += int(bollen)
    elif toppings == "d" and soort == "bakje":
        global caramelBakje
        aantalToppings += 1
        caramelBakje += 1
    elif toppings == "d" and soort == "hoorntje":
        global caramelHorentje
        aantalToppings += 1
        caramelHorentje += 1
    else:
        print("Sorry dat snap ik niet...")
        stap4(soort, bollen)

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
        stap4(soort, bollen)
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
        stap4(soort, bollen)
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
    return "€" + str(("{:.2f}".format(bolBetaal)))

def bakGeld(bakjes):
    bakBetaal = round((float(bakjes) * 0.75),2)
    global bkGeld
    bkGeld = bakBetaal
    return "€" + str(("{:.2f}".format(bakBetaal)))

def hoornGeld(hoorntjeS):
    hoornBetaal = round((float(hoorntjeS) * 1.25),2)
    global hrGeld
    hrGeld = hoornBetaal
    return "€" + str(("{:.2f}".format(hoornBetaal)))

def toppingGeld():
    global tpGeld
    tpGeld = round((slagroom * 0.50 + sprinkels * 0.30 + caramelHorentje * 0.60 + caramelBakje * 0.90), 2)
    return "€" + str(("{:.2f}".format(tpGeld)))

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
        if aantalToppings > 0:
            print("Topping       1 x " + toppingGeld() + "   = " + toppingGeld())
        print('                          -------- +')
        print('Totaal                    = €' + str(("{:.2f}".format((hrGeld + bkGeld + blGeld + tpGeld)))))

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
stap1()