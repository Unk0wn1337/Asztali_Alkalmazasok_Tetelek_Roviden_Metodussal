from Cipo import Cipo

peldany1 = Cipo("Nike", 42)
peldany2 = Cipo("Adidas", 41)
peldany3 = Cipo("Adidas", 45)

cipok = []
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)

for i in range(0, len(cipok), 1):
    nev: str = cipok[i].nev
    meret: int = cipok[i].meret
    print(f"{nev} ({meret})")


def meret_atlag():
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret

    atlag = ossz / len(cipok)
    print(round(atlag, 3))


meret_atlag()


def legnagyobbMeretuCipo():
    print("A legngyobb markaju cipo ",end="")
    legnagyobbHelye = 0
    for i in range(1, len(cipok),1):
        if cipok[i].meret > cipok[legnagyobbHelye].meret:
            legnagyobbHelye = i
    print(cipok[legnagyobbHelye].nev)


legnagyobbMeretuCipo()


def hanyDarabAdidasTermek():
    print("Hany darab adidas termek: ",end="")
    megszamlalas = 0
    for i in range(1, len(cipok), 1):
        if cipok[i].nev == "Adidas":
            megszamlalas+=1
    print(megszamlalas)

hanyDarabAdidasTermek()
def nagyobb_42_adidas():
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van nagyobb mint 42 adidas")
    else:
        print("Nincs nagyobb mint 42 adidas")


nagyobb_42_adidas()
