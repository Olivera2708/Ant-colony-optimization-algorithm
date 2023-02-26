import gradovi
import mravi

if __name__ == "__main__":
    matrica_gradova, svi_gradovi = gradovi.ucitaj_fajl()

    ALFA = 1 #veca alfa - vise vrednujemo istrazivanje
    BETA = 12 #vece beta - vise vrednujemo eksploataciju
    STOPA_ISPARIVANJA = 0.1 #stopa isparivanja - smanjivanje vrednosti feromona iz starijih generacija
    BROJ_ITERACIJA = 100
    BROJ_MRAVA = 45
    najbolja = mravi.odredi_najbolju_putanju(BROJ_ITERACIJA, STOPA_ISPARIVANJA, matrica_gradova, svi_gradovi, BROJ_MRAVA, ALFA, BETA)
    print("Najbolja putanja je ", end="")
    for i in najbolja[0]:
        print(f"{i} -> ", end="")
    print(f"{najbolja[0][0]}\nRastojanje je {najbolja[1]}")