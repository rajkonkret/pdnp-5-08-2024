class Human:
    """
    Klasa Human opisując człowieka
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):  # plec="k" nadajemy wartość domyślną
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        # lewa strona to pola obiektu
        # prawa to wartości nadane
        # self.imie1 = imie -> imie to to co przychodzi w argumentach metody
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # w wypiywaniu uzywamy pól z lewej strony czyli np.: self.wiek
    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # stworzyc metody wypisujące poszczegolne pola obiektu
    # wypisz_wiek()
    # wypisz_wzrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Dorota", 26, 170)
print(cz1.imie)
print(cz1.plec)
print(cz1.wzrost)
print(cz1.wiek)
# Dorota
# k
# 170
# 26
cz2 = Human("Radek", 50, 190, "m")
print(cz2.imie)
print(cz2.plec)
print(cz2.wzrost)
print(cz2.wiek)
# Radek
# m
# 190
# 50
cz1.powitanie()
cz2.powitanie()
# Nazywam się Dorota
# Nazywam się Radek
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
