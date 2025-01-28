
from pojisteny import Pojisteny

class SpravaPojistenych:
    def __init__(self):
        self.pojisteni = []

    def pridat_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(novy_pojisteny)
        print(f"Pojištěný {jmeno} {prijmeni} byl úspěšně přidán.")

    def zobrazit_pojistene(self):
        if not self.pojisteni:
            print("Žádní pojištění nejsou evidováni.")
        else:
            print("Seznam pojištěných:")
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        nalezeni = [p for p in self.pojisteni if p.jmeno == jmeno and p.prijmeni == prijmeni]
        if nalezeni:
            print("Nalezený pojištěný:")
            for pojisteny in nalezeni:
                print(pojisteny)
        else:
            print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")