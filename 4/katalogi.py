import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path_2 = Path('ops_example/D')

# usunięcie katalogu, jeśli istnieje
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# utworzenie katalogu
base_path.mkdir()
path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir()  # FileNotFoundError: [Errno 2] No such file or directory: 'ops_example/A/B'
# parents=True - tworzenie pośrednich katalogów
path_b.mkdir(parents=True)
# katalog C utworzy się w zwykły sposób bo juz istnieje katalog A
path_c.mkdir()

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w') as stream:
        stream.write(f"Jakaś treść w pliku {filename}")

# move - przenosi pliki z katalogu B do katalogu D(usunie w katologu B)
shutil.move(path_b, path_d)
# scieżka do pliku ex1.txt
ex1 = path_d / 'ex1.txt'
# zmiana nazwy dla tego pliku
ex1.rename(ex1.parent / 'ex1_renamed.log')
