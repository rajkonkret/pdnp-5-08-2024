user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # liczby zmiennoprzecinkowe -> float, używamy kropki
print(type(wersja))  # <class 'float'>
liczba = 123456789123  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# Przy tym sposobie wypisywania sprawdzane są typy danch
# print("Witaj %d, masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit - liczba
print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})  # Witaj Tomek, masz teraz 39 lat.
print("Witaj %(user)s, masz teraz %(age)d lat." % {"user": user, 'age': wiek})  # Witaj Tomek, masz teraz 39 lat.

print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, tekst sforamtowany

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4
# zaokrągla przy wyświetlaniu
print("Wynik = %.2f" % 3.876)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X nadal się nie zmieniło", x)  # X nadal się nie zmieniło 3.14

y = round(x)
print("y=", y)  # zaokrąglona
print(f"{x=}")
# y= 3
# x=3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4
# print(f"Używamy wersji pythona {wersja:.f}")  # ValueError: Format specifier missing precision

print(f'{user:>10}')  # "     Tomek"  wyrównanie do prawej - długość 10
print(f'{user:<20}')  # "Tomek               "  wyrównał do lewej
print(f'{user:^25}')  # "          Tomek          "

print(liczba)  # 123456789123
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,789,123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 123,456,789,123
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 123,456,789,123
# Nasza duża liczba 123 456 789 123
# Nasza duża liczba 123.456.789.123

liczba_2 = 123_456_789_123
# 15_000_000
# 15000000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 123456789123
