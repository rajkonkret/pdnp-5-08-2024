# hermetyzacja
class Car:
    """
       Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole jest prywatne, nie moze byc zmienione poza klasą

    # enkapsulacja
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Jadę z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car = Car("Bentley", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# po oznaczeniu pola jako prywatne nie ma do niego dostępu
# print(car.__predkosc)  # 50
car.licznik()  # Jadę z szybkością 50 km/h
# car.__predkosc = 0
# car.__predkosc = 5
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Jadę z szybkością 50 km/h
# hermetyzacja - ustawienie pól jako prywatne, nie ma do nich dostępu poza klasa
# enkapsulacja - dla pol prywatnych dodanie metod do odczytu i zapisu stanu tych pól
