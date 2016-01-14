from slike import slike
from random import shuffle


class Besede:
    def __init__(self, ime):
        self.ime_datoteke = ime
        self.besede = []
        self.stevec = 0
        with open(ime) as f:
            self.besede = f.read().split()
        shuffle(self.besede)

    def daj_besedo(self):
        self.stevec += 1
        return self.besede[(self.stevec - 1) % len(self.besede)]


class Hangman:
    def __init__(self, generator):
        self.generator = generator
        self.maks_napake = len(slike) - 2
        self.napake = 0
        self.poskusi = []
        self.kljuc = generator.daj_besedo()
        self.namig = ["_"] * len(self.kljuc)

    def resetiraj(self):
        self.kljuc = self.generator.daj_besedo()
        self.namig = ["_"] * len(self.kljuc)
        self.napake = 0
        self.poskusi = []

    def status(self):
        if "_" not in self.namig:
            return 1
        if self.napake >= self.maks_napake:
            return -1
        return 0

    def ugani(self, crke):
        ujemanje = 0
        for c in crke:
            if c in self.kljuc:
                for i in range(len(self.kljuc)):
                    if self.kljuc[i] == c:
                        self.namig[i] = c
                        ujemanje += 1
            else:
                self.poskusi.append(c)
                self.napake += 1
                if self.napake == self.maks_napake:
                    return -1
        return ujemanje

    def slika(self):
        if self.status() == 1:
            return slike[-1]
        return slike[self.napake]

    def namigni(self):
        return " ".join(self.namig)


if __name__ == "__main__":
    uganke = Besede("besede2.txt")
    igra = Hangman(uganke)
    while True:
        igra.resetiraj()
        while igra.status() == 0:
            print(igra.slika())
            print(", ".join(igra.poskusi))
            print(igra.namigni())
            igra.ugani(input("Ugibaj: "))

        print(igra.slika())
        print(igra.namigni())
        if igra.status() == 1:
            print("Cestitamo za zmago!")
        if igra.status() == -1:
            print("Oh, pa naslednjic. Beseda je bila '%s'" % igra.kljuc)

        nadaljuj = ""
        while nadaljuj.lower() not in ["da", "ne"]:
            nadaljuj = input("Zelis nadaljevati? (DA/NE)")
        if nadaljuj.lower() == "ne":
            break
