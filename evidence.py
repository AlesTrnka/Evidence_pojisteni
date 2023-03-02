import os
from klient import Klient

class Evidence:
    def __init__(self):
        self.seznam_klientu = []    # spustí průvodce programem
        pass

    def spustit_program(self):      # vybere operaci, kterou chce uživatel provést
        cislo_operace = None
        while True:
            os.system("cls")
            print("EVIDENCE POJIŠTĚNÍ")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            self.vypis_operaci()    # vypíše seznam operací, které je možné provést
            print()
            try:
                cislo_operace = int(input("Zvolte operaci, kterou chcete provést:\t"))
                if cislo_operace == 1:
                    os.system("cls")
                    self.pridej_klienta()   # přidání nového pojištěného
                elif cislo_operace == 2:
                    os.system("cls")
                    self.vypis_klienty()    # vypíše seznam přidaných pojištěných
                elif cislo_operace == 3:
                    os.system("cls")
                    self.vyhledej_klienta() # vyhledá pojištěného podle jména a příjmení
                elif cislo_operace == 4:
                    os.system("cls")
                    print("\nPřeji krásný den")
                    return False            #  ukončí program
                elif cislo_operace < 1 or cislo_operace > 4:        # reakce na zadání čísla mimo nabídku
                    print("\nNeplatné zadání. Číslo musí být v rozmezí 1-4.")
                    input("Pokračujte stiskem klávesy Enter...\n")
            except ValueError:              # reakce na zadání jiného znaku, než je číslo
                print("\nNeplatné zadání. Zadejte číslo v rozmezí 1-4.")
                input("Pokračujte stiskem klávesy Enter...\n")

    def vypis_operaci(self):    # vypíše seznam operací, které je možné provést
        operace = ["Přidat nového pojištěného", "Vypsat seznam pojištěných", "Vyhledat pojištěného", "Ukončit program"]
        for i in range(len(operace)):
            print(f"{i+1}  -  {operace[i]}")

    def pridej_klienta(self):   # přidání nového pojištěného
        print("PŘIDÁNÍ NOVÉHO POJIŠTĚNÉHO:")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
        while True:             # opakování zadávání v případě nepovolených znaků
            jmeno = input("Zadejte křestní jméno:\n")
            if jmeno.isalpha(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze písmena abecedy")
        while True:             # opakování zadávání v případě nepovolených znaků
            prijmeni = input("Zadejte příjmení:\n")
            if prijmeni.isalpha(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze písmena abecedy")
        while True:             # opakování zadávání v případě nepovolených znaků
            vek = input("Zadejte věk:\n")
            if vek.isdigit(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze celá čísla")
        while True:             # opakování zadávání v případě nepovolených znaků
            cislo = input("Zadejte telefonní číslo:\n")
            if cislo.isdigit(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze celá čísla")
        novy_klient = Klient(jmeno.capitalize(), prijmeni.capitalize(), vek, cislo)
        self.seznam_klientu.append(novy_klient)     # přidání zadaného pojištěného (instance) do seznamu
        print("\n")
        print("Údaje byly uloženy do databáze.\n")
        input("Pokračujte stiskem klávesy Enter...\n")

    def vypis_klienty(self):        # vypíše seznam přidaných pojištěných
        print("VÝPIS POJIŠTĚNÝCH")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
        print("\nJméno \ Příjmení \ Věk \ Telefon")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
        for i in range(len(self.seznam_klientu)):       # výpis klientů
            print(f"{self.seznam_klientu[i].jmeno}\t{self.seznam_klientu[i].prijmeni}\t\t{self.seznam_klientu[i].vek}\t{self.seznam_klientu[i].cislo}")
        input("\n\nPokračujte stiskem klávesy Enter\n")

    def vyhledej_klienta(self):     # Vyhledá klienta podle jména a příjmení
        print(f"VYHLEDÁNÍ POJIŠTĚNÉHO")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
        while True:                 # opakování zadávání v případě nepovolených znaků
            hledane_jmeno = input("Zadejte křestní jméno pojištěného, kterého chcete vyhledat:\n")
            if hledane_jmeno.isalpha(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze písmena abecedy")
        while True:                 # opakování zadávání v případě nepovolených znaků
            hledane_prijmeni = input("Zadejte příjmení pojištěného, kterého chcete vyhledat:\n")
            if hledane_prijmeni.isalpha(): break
            else: print("\nNeplatné zadání, je možné zadávat pouze písmena abecedy")
        os.system("cls")
        print(f"NALEZENÉ ZÁZNAMY:")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
        print(f"Pro zadané údaje '{hledane_jmeno} {hledane_prijmeni}' byly nalezeny tyto záznamy:\n")
        print("Jméno \ Příjmení \ Věk \ Telefon")
        print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
        for i in range(len(self.seznam_klientu)):       # vypíše pojištěného podle zadaných údajů
            if self.seznam_klientu[i].jmeno == hledane_jmeno.capitalize() and self.seznam_klientu[i].prijmeni == hledane_prijmeni.capitalize():
                print(f"{self.seznam_klientu[i].jmeno}\t{self.seznam_klientu[i].prijmeni}\t\t{self.seznam_klientu[i].vek}\t{self.seznam_klientu[i].cislo}")
            else:
                pass
        input("\n\nPokračujte stiskem klávesy Enter\n")
