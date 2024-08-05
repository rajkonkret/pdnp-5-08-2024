import sys

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu

print("Nazywam się Radek")
print('Nazywam się Radek')

# Nazywam się Radek
# Nazywam się Radek
# ctrl / - zakomentowanie wielu linijek
# print("Nazywam się Radek')
#   File "/Users/radoslawjaniak/PycharmProjects/pdnp-5-08-2024/1/pierwszy.py", line 10
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1 - oznacza, ze pojawił się bład
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie linii
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek

# type() - sprawdzenie typow danych
print(type("Radek"))  # <class 'str'> typ tekstowy
print(type("39"))  # <class 'str'>
print("39")  # 39
print("39" + "39")  # 3939 konkatenacja (łączenie tekstów)
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print(39 + 39)  # 78
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zamienia typów podczas operacji
print(int("39") + 39)  # 78 int() - zamiana (rzutowanie) na liczbę całkowitą
print("39" + str(39))  # 3939 str()  - zamiana na tekst

print("8" + "8" + "8")  # 888
print(8 * 8 * 8)  # 512

print(5 * "4")  # 44444

# zmienna - pudełko na dane
liczba = 39
print(liczba)  # 39
print(type(liczba))  # <class 'int'>
print("5" * liczba)  # 555555555555555555555555555555555555555

liczba = "39"
print(type(liczba))  # <class 'str'>

name = "Radek"
print(name + "Kowalski")  # RadekKowalski

name = 90
# print(name + 'Kowalski')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# to jest tylko podpowiedź (hint)
name: str = "Radek"
name = 90
print(name)  # 90

# nazwy zmiennych z małej litery
# snake_case
# zmienna powinna podpowiadać co zawiera

age = 56
print(age)
print(type(age))
