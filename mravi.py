import numpy as np
import math

#inicijalizacjia matrice feromona, za svaku putanju jednaka sansa da krene njom
def inicijalizacija(matrica_gradova):
    matrica_feromona = np.ones(matrica_gradova.shape)
    matrica_feromona /= len(matrica_gradova)
    return matrica_feromona

#za izabrani grad gledamo gde je najbolje da ode, odredimo verovatnocu ka svakom gradu
def verovatnoca_izbora(matrica_feromona, grad, matrica_gradova, preostali_gradovi, alfa, beta):
    verovatnoca = np.zeros(len(preostali_gradovi))
    #za izbor iz prosledjenog grada
    suma = 0
    for i in range(len(preostali_gradovi)):
        if (preostali_gradovi[i].redni != grad): #grad je redni broj grada
            verovatnoca[i] = (1/matrica_feromona[grad][preostali_gradovi[i].redni])**alfa*(1/matrica_gradova[grad][preostali_gradovi[i].redni])**beta
            suma += verovatnoca[i]
        else:
            verovatnoca[i] = 0
    
    return verovatnoca / suma

#na osnovu verovatnoce na nasumican nacin bira putanju (vise se vreduje gde je verovatnoca veca)
def biranje_putanje(preostali_gradovi, grad, matrica_feromona, matrica_gradova, alfa, beta):
    verovatnoca = verovatnoca_izbora(matrica_feromona, grad, matrica_gradova, preostali_gradovi, alfa, beta)
    return np.random.choice(preostali_gradovi, p=verovatnoca)

#za putanju izracunati koliko je rastojanje
def ukupno_rastojanje(put, matrica_gradova):
    ukupno = 0
    prethodni = put[0].redni
    for i in range(1, len(put)):
        ukupno += matrica_gradova[prethodni][put[i].redni]
        prethodni = put[i].redni
    ukupno += matrica_gradova[prethodni][put[0].redni]
    return ukupno

#vraca sve mogucnosti putanja
def sve_mogucnosti(svi_gradovi, matrica_gradova, matrica_feromona, broj_mrava, alfa, beta):
    sve_putanje = []
    for _ in range(broj_mrava): #broj mrava
        put = putanja(svi_gradovi, matrica_feromona, matrica_gradova, alfa, beta)
        sve_putanje.append((put, ukupno_rastojanje(put, matrica_gradova)))
    return sve_putanje

#generise jednu putanju sa svim gradovima
def putanja(svi_gradovi, matrica_feromona, matrica_gradova, alfa, beta):
    put = [svi_gradovi[0]]
    preostali_gradovi = svi_gradovi
    preostali_gradovi = np.delete(preostali_gradovi, 0)
    for _ in range(len(svi_gradovi)-1):
        sledeci_grad = biranje_putanje(preostali_gradovi, put[-1].redni, matrica_feromona, matrica_gradova, alfa, beta)
        indeks = np.argwhere(preostali_gradovi == sledeci_grad)
        put.append(sledeci_grad)
        preostali_gradovi = np.delete(preostali_gradovi, indeks)
    return put

def azuriraj_feromona(sve_putanje, matrica_feromona):
    for putanja, rastojanje in sve_putanje:
        prethodni = putanja[0]
        for grad in putanja[1:]:
            matrica_feromona[prethodni.redni][grad.redni] += 1/rastojanje
            matrica_feromona[grad.redni][prethodni.redni] += 1/rastojanje
            prethodni = grad
    return matrica_feromona

#glavna funkcija koja se poziva
def odredi_najbolju_putanju(n, stopa_isparivanja, matrica_gradova, svi_gradovi, broj_mrava, alfa, beta): #prosledimo broj iteracija, broj mrava
    najbolja = ("a", math.inf) #ovo je najgore
    matrica_feromona = inicijalizacija(matrica_gradova)

    for _ in range(n):
        sve_putanje = sve_mogucnosti(svi_gradovi, matrica_gradova, matrica_feromona, broj_mrava, alfa, beta)
        matrica_feromona = azuriraj_feromona(sve_putanje, matrica_feromona)
        najkraca = min(sve_putanje, key=lambda x: x[1])

        if (najbolja[1] > najkraca[1]):
            najbolja = najkraca
        matrica_feromona *= (1-stopa_isparivanja)
    
    return najbolja