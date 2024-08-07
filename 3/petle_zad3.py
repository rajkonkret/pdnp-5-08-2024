# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat 1 !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # kończy bieżąćą pętlę (wychodzi całkowicie z pętli)

# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło, podaj ponownie")
#
# print("Hasło prawidłowe")
# Podaj hasłohaslo
# Błędne hasło, podaj ponowniestop
# Błędne hasło, podaj ponownienie znam hasla
# Błędne hasło, podaj ponowniejakie jest haslo?
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe

# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")  # str
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
# print(lista)
# print(lista_int)
# # ['3', '4', '5', '678'] - lista str
# # [3, 4, 5, 678]  - lista int

# usunięcie elementów z listy bez tracenia kolejności
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
