def ijshouder(soort):
    if soort == "a":
        soort = "hoorntje"
        return soort
    elif soort == "b":
        soort = "bakje"
        return soort

def stap3(soort, bollen):
    antwoord = input("Hier is uw " + soort + " met " + bollen + " bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()
    if antwoord == "y":
        stap1()
    elif antwoord == "n":
        print("Bedankt en tot ziens!")
        exit()
    else:
        print("Sorry dat snap ik niet...")
        stap3(soort, bollen)


def stap2(bollen):
    soort = input("Wilt u deze " + bollen + " bolletje(s) in A) een hoorntje of B) een bakje? ").lower()
    if soort == "a" or soort == "b":
        soort = ijshouder(soort)
        stap3(bollen, soort)
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
    if bollen1 <= 3:
        smaak(bollen1)
        stap2(bollen)
    elif bollen1 <=8:
        smaak(bollen1)
        print("Dan krijgt u van mij een bakje met " + bollen + " bolletjes.")
        soort = "bakje"
        stap3(soort, bollen)
    elif bollen1 > 8:
        print("Sorry, zulke grote bakken hebben we niet.")
        stap1()

def smaak(bollen):
    x = 0
    while x < bollen:
        x += 1
        check = input("Welke smaak wilt u voor bolletje nummer " + str(x) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").lower()
        if check != "a" and check != "c" and check != "m" and check != "v":
            x -= 1
            print("Sorry dat snap ik niet...")

print("Welkom bij Papi Gelato.")
stap1()