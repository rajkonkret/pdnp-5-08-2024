# instrukcje warunkowe
# instrukcje sterownia przepływem programu
# w zależnosci od warunku wykona jedną lub drugą instrukcje (blok instrukcji)
# warunek musi zwracac bool
# if
odp = True
print(bool(odp))  # True
odp = False
if odp:  # odp == True
    # blok wykonywany po if, gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
print(bool(odp))  # True
if odp:
    print("Radek")  # Radek

if odp == "Radek":
    print("Nadal Radek")  # Nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym przypadku
    print("To nie jest Tomek")  # To nie jest Tomek

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:  # do 9999
#     podatek = 0
# elif zarobki < 30000:  # od 10000 do 29999
#     podatek = 0.2
# elif zarobki < 100000:  # od 30000 do 99999
#     podatek = 0.4
# else:  # od 100000
#     podatek = 0.9
# # kolejność warunków ma znaczenie
# # pierwszy spełniony oznacza wyjscie z drzewka warunków
#
# print(f"Podatek wynosi {podatek * zarobki}")
# # dodać podatek 0.2 dla przedziału 10000 do 29999

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f'Rabat wynosi {rabacik}')  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # ternary operator
print(f'Rabat wynosi {rabat}')  # Rabat wynosi 25

# zasymulejmy system zbierania logów
# zmienne będą przechowywyać dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla console: Stało się coś strasznego
# dla email: System email
# jak system bedzie email, sprawwdamy typ błedu error, medium, inny
# nalezy do listy wpisac opis błedu który przyszedł
alert_system = 'email'
error = 'error'
lista_b = []
if alert_system == 'console':
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == "error":
        lista_b.append("Błąd krytyczny")
    elif error == 'medium':
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Inny system")

print(lista_b)
# System email
# ['Błąd krytyczny']

# napisac test z....
# zadac pytanie
# pobrac odpowiedz
# porównac odpowiedz do wzorca
# wyswietlic wynik
punkty = 0
odp = input("Podaj datę Chrztu Polski")  # zwraca str
if odp == '966':  # porównuje z wartościa typu str
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Błąd")
print(punkty)
