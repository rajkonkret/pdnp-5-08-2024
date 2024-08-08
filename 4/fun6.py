# stworzyc funkcję obliczająćą średnią
def liczby(name=None, *cyfry):  # * przyjmuje dowolną ilość argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3, 4, 5, 6)
    count = len(cyfry)
    suma = 0
    # Istnieje komenda pythona sumująca elementy kolekcji sum()
    suma_p = sum(cyfry)
    print(suma_p)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count

    except Exception as e:
        print("Blad", e)
    else:
        print(f"Srednia dla ucznia {name} wynosi {avg}")
    finally:
        print("Wykonuje się zawsze")


liczby(1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# Srednia wynosi 3.5
liczby()
# ()
# Blad division by zero
# Wykonuje się zawsze
liczby(7, 3, 4, 5, 4)
# (7, 3, 4, 5, 4)
# Srednia wynosi 4.6
# Wykonuje się zawsze
# Radek, 4,5,6,5,6,4
liczby("Radek", 4, 5, 6, 5, 6, 4)
# (2, 3, 4, 5, 6)
# Srednia dla ucznia 1 wynosi 4.0
# Wykonuje się zawsze
# ()
# Blad division by zero
# Wykonuje się zawsze
# (3, 4, 5, 4)
# Srednia dla ucznia 7 wynosi 4.0
# Wykonuje się zawsze
# (4, 5, 6, 5, 6, 4)
# Srednia dla ucznia Radek wynosi 5.0
# Wykonuje się zawsze
# (4, 5, 6, 5, 6, 4)
# 30
# Srednia dla ucznia Radek wynosi 5.0
# Wykonuje się zawsze
