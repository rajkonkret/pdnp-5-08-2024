# funkcja wewnętrzna, zagniezdzona
# uzywane w dekoratorach
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # bez nawiasów, zwracamy referencje, adres fun2


xFun = fun1()  # To jest fun1
print(xFun)  # <function fun1.<locals>.fun2 at 0x104e0cea0>
print(type(xFun))  # <class 'function'>
# nazwa_funkcji nawiasy ()
xFun()  # To jest fun2
