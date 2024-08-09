# dziedziczenie
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator, dodaje funkcje do naszego elemntu
    # oznaczylismy metode jako abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # dziedziczy po klasie Ptak
    """
    Klasa opisująca kurę w pythonie
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiązkowo należy wywołać konstruktor klasy nadrzędnej czyli super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    # nadpisac
    def wydaj_odglos(self):
        print('ko ko ko ko ko ko')


class Orzel(Ptak):
    """
    Klasa Orzeł
    """

    def wydaj_odglos(self):
        print("kier kier kir")


# Po oznaczeniu klasy jako abstrakcyjna nie da się stworzyc obiektu tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

# kur2 = Kura("Kura domowa", 0)
# kur2.latam()
# Tu Kura domowa Lecę z szybkością 0
# po nadpisaniu metody latam() w klasie Kura
kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
kur2.wydaj_odglos()  # ko ko ko ko ko ko

or2 = Orzel("Orzeł Bielik", 55)
or2.wydaj_odglos()
or2.latam()
# kier kier kir
# Tu Orzeł Bielik Lecę z szybkością 55

# polimorfizm
# obiekty majaą wspołne cech dzięki dziedziczeniu z jedej klasy
# pozwala to uzyc tych obiektów jakby były takie same
lista = [kur2, or2]  # obiekty dwóch różnych klas, dziedziczą oba po Ptak
for i in lista:
    i.wydaj_odglos()
# ko ko ko ko ko ko
# kier kier kir
