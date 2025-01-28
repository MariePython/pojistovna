


from pojisteny import Pojisteny
from sprava import SpravaPojistenych

if __name__ == "__main__":
    sprava = SpravaPojistenych()

    while True:
        print("\nSpráva pojištěných")
        print("1. Přidat pojištěného")
        print("2. Zobrazit všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Ukončit")

        volba = input("Vyberte možnost: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = int(input("Zadejte věk: "))
            telefon = input("Zadejte telefonní číslo: ")
            sprava.pridat_pojisteneho(jmeno, prijmeni, vek, telefon)
        elif volba == "2":
            sprava.zobrazit_pojistene()
        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            sprava.vyhledat_pojisteneho(jmeno, prijmeni)
        elif volba == "4":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")