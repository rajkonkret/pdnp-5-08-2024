tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# wszystko jest obiektem
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
