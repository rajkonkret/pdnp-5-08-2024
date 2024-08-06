# od python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():  # strip() usuniecie poczatkowych i końcowych białych znaków(spacja)
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyślna, else
        print("Nie znam takiego języka")

print(lista)
