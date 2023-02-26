import math
import numpy as np

class Grad:
    def __init__(self,redni,broj,x,y):
        self.redni=redni
        self.broj=broj
        self.x=x
        self.y=y

    def __str__(self):
        return str(self.broj)+"(" +str(self.x)+","+str(self.y)+")"

def ucitaj_fajl():
    svi_gradovi = np.array([])
    br = 0
    with open("data_tsp.txt") as fajl:
        for i in fajl.readlines():
            podaci = i.split(" ")
            svi_gradovi = np.append(svi_gradovi, Grad(br, int(podaci[0]), float(podaci[1]), float(podaci[2].replace("\n", ""))))
            br += 1

    matrica_gradova = np.zeros((len(svi_gradovi), len(svi_gradovi)))
    for i in range(len(svi_gradovi)):
        for j in range(len(svi_gradovi)):
            if i == j:
                matrica_gradova[i][j] = math.inf
                continue

            rastojanje = math.sqrt((svi_gradovi[i].x - svi_gradovi[j].x)**2 + (svi_gradovi[i].y - svi_gradovi[j].y)**2)
            matrica_gradova[i][j] = rastojanje

    return matrica_gradova, svi_gradovi