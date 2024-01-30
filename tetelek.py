import math


def osztok():
    lista =[]
    szam = int(input("Mondj egy szamot: "))
    for i in range(2, round(math.sqrt(szam))+1, 1):
        if szam % i == 0:
            lista.append(i)
    return lista


def kivalasztas():
    prim = False
    n = 9999
    while prim == False:
        n += 1
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    print(n)

def linearis_kereses():
    also = 42
    felso = 67
    i = also
    while i<= felso and (i % 10 != 0):
        i += 1
    van = i <= felso

    if van == True:
        print("van 0-ra végződő szam: ", i)
    else:
        print("nincs 0ra végződő szám")
