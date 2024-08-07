import random

# do działąń na liczbach pseudolosowych

print(random.randint(1, 100))  # 49, int, 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # od 0 do 4
print(random.random())  # 0.5961498670796218 float od 0 do 0.99999
print(random.random() * 10)  # 4.280431178214598 float od 0 do 9.99999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # 67

lista_kula = list(range(1, 50))  # 1 do 49
# print(lista_kula)

# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))

# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)

print(random.choices(lista_kula, k=6))  # losuje z powtórzeniami [4, 39, 40, 13, 6, 4]
# losowanie bez powtórzeń, 6 ilosc liczb do wylosowania
print(random.sample(lista_kula, 6))
print(random.sample(lista_kula, k=6))
# [7, 33, 40, 22, 43, 5]
# [25, 27, 15, 20, 41, 33]
