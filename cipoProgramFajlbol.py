from Cipo import Cipo



def peldanyokListaban():

    f = open("cipok.txt","r",encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    cipok = []
    f.close()
    index = 0
    while index < len(sorok):
        sorok = sorok[index].strip()
        sorok = sorok[index].split(",")
        peldany = Cipo(sorok[0], int(sorok[1]))
        cipok.append(peldany)




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