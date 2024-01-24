from Cipo import Cipo



def peldanyokListaban():
    peldany1 = Cipo("Nike", 42)
    peldany2 = Cipo("Adidas", 41)
    peldany3 = Cipo("Adidas", 45)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok
def listaKiir(lista):
    for i in range(0, len(lista), 1):
        nev: str = lista[i].nev
        meret: int = lista[i].meret
        print(f"{nev} ({meret})")

#rövid verzió
#listaKiir(peldanyokListaban())

#Hosszú verzió:



def osszegzesTetele(cipok):
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret

    atlag = ossz / len(cipok)
    print(round(atlag, 3))



def maximumKivalasztas(cipok):
    print("A legngyobb markaju cipo ",end="")
    legnagyobbHelye = 0
    for i in range(1, len(cipok),1):
        if cipok[i].meret > cipok[legnagyobbHelye].meret:
            legnagyobbHelye = i
    print(cipok[legnagyobbHelye].nev)






def eldontesTetel(cipok):
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van nagyobb mint 42 adidas")
    else:
        print("Nincs nagyobb mint 42 adidas")




def megszamlalasTetel(cipok):
    print("Hany darab adidas termek: ",end="")
    megszamlalas = 0
    for i in range(1, len(cipok), 1):
        if cipok[i].nev == "Adidas":
            megszamlalas+=1
    print(megszamlalas)

cipokLista = peldanyokListaban()
listaKiir(cipokLista)

megszamlalasTetel(cipokLista)
eldontesTetel(cipokLista)
maximumKivalasztas(cipokLista)
osszegzesTetele(cipokLista)