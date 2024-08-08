# klasa - element programowania obiektowego
# klasa - szablon, przepis
# wskazuje minimum cech jakie ma posiadać obiekt
# obiekt (instancja) zbudowany wg przepisu
# definicja klasy  nie uruchamia klasy
# dopiero budowanie obiektu uruchamia elementy w klasie
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# pola (stan obiektu -> zmienne)
# metody (funkcje)

# Deklaracja klasy
# PEP8 zaleca nawy kals z dużej litery
# komentarz wielolinijkowy w kalsie (funkcji) jest traktowany jako dokumentacja
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt, który wywołuje
    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# tworzenie obiektu klasy
cz1 = Human()
# dokumentacja klasy
print(Human.__doc__)
#    Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

# pydoc -b - uruchomienie serwera z dokumentacją projektu
# pydoc -w kl1 - generowanie pliku html z dokumentacją

# sprawdźmy czy obiekt cz1 posiada pola imie, wiek, plec
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)

# nadanie wartości polom obiektu cz1
cz1.imie = "Anna"
cz1.wiek = 28

print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# k
# 28
# Anna

# stwórzcie obiekt innej plci
cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 29
cz2.plec = "m"
print("Plec", cz2.plec)
print("Wiek", cz2.wiek)
print("Imie", cz2.imie)
# Plec m
# Wiek 29
# Imie Radek
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
