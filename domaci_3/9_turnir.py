import random

class Turnir:
    def __init__(self, naziv_turnira, broj_rundi):
        self._naziv_turnira = naziv_turnira
        self._lista_igraca = []
        self._broj_rundi = broj_rundi

    def get_naziv_turnira(self):
        return self._naziv_turnira

    def set_naziv_turnira(self, naziv_turnira):
        self._naziv_turnira = naziv_turnira

    def get_lista_igraca(self):
        return self._lista_igraca

    def set_lista_igraca(self, lista_igraca):
        self._lista_igraca = lista_igraca

    def get_broj_rundi(self):
        return self._broj_rundi

    def set_broj_rundi(self, broj_rundi):
        if 0 < broj_rundi < 10:
            self._broj_rundi = broj_rundi
        else:
            print("Invalid number of rounds! Number of rounds should be between 1 and 9.")

    def dodaj_igraca(self, ime_igraca, broj_bodova = 0):
        self._lista_igraca.append((ime_igraca, broj_bodova))

    def obrisi_igraca(self, ime_igraca):
        for igrac in self._lista_igraca:
            if igrac[0] == ime_igraca:
                self._lista_igraca.remove(igrac)
                print(f"Igrač {ime_igraca} je obrisan/a iz turnira.")
                return
        print(f"Igrač {ime_igraca} nije pronađen/a u turniru.")

    def prikazi_najboljeg_igraca(self):
        if not self._lista_igraca:
            print("Turnir nema igrača.")
            return

        najbolji_igrac = max(self._lista_igraca, key=lambda x: x[1])
        print(f"Najbolji igrač: {najbolji_igrac[0]} - Broj bodova: {najbolji_igrac[1]}")

    def pokreni_rundu(self):
        if len(self._lista_igraca) < 2:
            print("Nedovoljan broj igrača za pokretanje runde.")
            return

        igrac1, igrac2 = random.sample(self._lista_igraca, 2)
        print(f"Runda {self._broj_rundi + 1}: {igrac1[0]} vs {igrac2[0]}")

        pobjednik = igrac1 if random.random() < 0.6 else igrac2
        print(f"Pobjednik runde: {pobjednik[0]}")

        for i, igrac in enumerate(self._lista_igraca):
            if igrac == pobjednik:
                self._lista_igraca[i] = (igrac[0], igrac[1] + 1)

        self._broj_rundi += 1


# Example usage
turnir = Turnir("Turnir 1", 0)

turnir.dodaj_igraca("Ana")
turnir.dodaj_igraca("Ivana")
turnir.dodaj_igraca("Janko")
turnir.dodaj_igraca("Marko")
turnir.dodaj_igraca("Petar")

aktivni_igraci = [igrac[0] for igrac in turnir.get_lista_igraca()]

print(f"Aktivni igrači na turniru: {aktivni_igraci}")

turnir.obrisi_igraca(random.choice(aktivni_igraci))

for _ in range(turnir.get_broj_rundi(), 10):
    turnir.pokreni_rundu()

turnir.prikazi_najboljeg_igraca()
