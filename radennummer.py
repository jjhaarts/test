import random

def raad_het_nummer():
    te_raden_nummer = random.randint(1, 10)
    pogingen = 0

    print("Raad het nummer tussen 1 en 10.")

    while True:
        gok = int(input("Voer een gok in: "))
        pogingen += 1
        
        if gok == te_raden_nummer:
            print(f"Goed geraden! Het nummer was inderdaad {te_raden_nummer}. Je hebt het geraden in {pogingen} pogingen.")
            break
        elif gok < te_raden_nummer:
            print("Het te raden nummer is groter. Probeer opnieuw.")
        else:
            print("Het te raden nummer is kleiner. Probeer opnieuw.")

if __name__ == "__main__":
    raad_het_nummer()
