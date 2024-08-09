import matplotlib.pyplot as plt

# pip install matplotlib

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

plt.plot(x, y, color="red")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.show()
