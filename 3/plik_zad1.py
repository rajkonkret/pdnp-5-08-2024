# działania z plikami
# context manager
# with - context manager w pythonie
# open() - praca z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler - rura do pliku
    fh.write("Powitanie\n")  # zapis do pliku
    fh.write("Drugie\n")  # zapis do pliku
    fh.write("Kolejne\n")  # zapis do pliku

# "x" sprawdza czy plik istnieje
# gdy istnieje:
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', 'x', encoding='utf-8') as f:
#     f.write("Coś")

# "w" tworzy nowy plik
# jeśli istnieje zostanie skasowany (zawartość zniknie)
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Nadpisane\n")

# "a" dopisanie na końcu pliku
with open("test.log", "a", encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dodane\n")
    f.write("Dośdane\n")

with open("test.log", "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# encoding='utf-8' wymuszenie kodowania znaków utf-8
