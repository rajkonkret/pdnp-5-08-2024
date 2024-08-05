tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# wszystko jest obiektem
# teksty są niemutowalne
""" Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()  # zapisanie do zmiennej wyniku funkcji upper() na obiekcie tekst
# . (kropka) użycie funkcji na obiekcie
# _ konwencja snake_case w nazwach zmiennych
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie - orginał nie jest zmieniany

# zmienic tekst na małe litery
tekst_lower = tekst.lower()
print(tekst_lower)
print(tekst.lower())
# witaj świecie
# witaj świecie

# Witaj Świecie
# 0123456789...
print(tekst.count("i"))  # 3
# indeksy numerowane są od zera
print(tekst.count("j", 0, 4))  # wynik 0 bo 0123, z prawej strony zbiór otwarty, ideks 4 nie jest brany

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"
print(tekst.removesuffix("Świecie").strip())  # "Witaj" strip() - usunie białe znaki np.: spacje końcowe i początkowe

print(tekst[4])  # wypisanie znaku o indeksie 4 -> "j"

# kodowanie znaków
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# \x wartość bajtu w postaci szesnastkowej
# \xc5 - dziesiętnie 197
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - fstring, tekst sformatowany
tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
#    Mam na imię Radek  -> 	Mam na imię {imie}
# i lubię pythona
# \t tabulator
# \n nowa linia
# \b backspace - usunięcie znaku

starszy = "Witaj %s!"  # %s - stringa
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", imie)  # Witaj Radek

# tekst wilolinijkowy
print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"
