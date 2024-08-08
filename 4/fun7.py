def connect(**opcje):  # ** argumenty słownikowe, dowolna ilośc argumentów nazwanych
    print(opcje)  # {'a': 8, 'b': 9}
    print(type(opcje))  # <class 'dict'>


connect(a=8, b=9)  # {'a': 8, 'b': 9}
connect(a=89)  # {'a': 89}


# ta funkcja przyjmuje dowolną ilość argumentów pozycyjnych
# oraz dowolną ilość argumentów nazwanych
def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6) {}
all_params(a=9, b=9, c=9, d=90)
# () {'a': 9, 'b': 9, 'c': 9, 'd': 90}
all_params(1, 2, 3, c=9, f=90)  # (1, 2, 3) {'c': 9, 'f': 90}
all_params()  # () {}
