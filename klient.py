class Klient:
    """ Třída pro vytvoření nových pojištěných (instancí) """
    
    def __init__(self, jmeno, prijmeni, vek, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo = cislo
    def __str__(self):
        return (f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.cislo}")