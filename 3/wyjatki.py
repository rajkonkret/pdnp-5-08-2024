# wyjątki
# błedy podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/pdnp-5-08-2024/3/wyjatki.py", line 1, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
number = 90
try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza w słowniku")  # rzucenie błędu
    wynik = number / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # tylko gdy nie ma błedu
    print("Wynik działania", wynik)
finally:  # wykonuje się zawsze
    print("Wykonuje się zawsze")

print("Dalsza częśc programu")
# Bład typu
# Wykonuje się zawsze
# Dalsza częśc programu

# try - except [else - finally]
