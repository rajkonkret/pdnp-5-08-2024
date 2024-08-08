# stworzyc funkcję kantor
# ma posiadać dwie funkcję wewnętrzne usd i eur
# w zależności od parametru ma zwracac wybraną funkcję (adres funkcji)
# możliwośc przekazania dowolnej kwoty do wymiany
def kantor(waluta):
    def usd(kwota=0):
        print(f"Wymieniam dolary {kwota}. Mam {kwota * 4.01} pln. ")

    def eur(kwota=0):
        print(f"Wymieniam euro {kwota}. Mam {kwota * 4.31} pln. ")

    # zwracamy adres funkcji, nie zwracamy wyniku działąnia funkcji
    if waluta == "eur":
        return eur
    else:
        return usd


# uruchomienie kantoru usd
kantor_usd = kantor("usd")
kantor_usd()  # Wymieniam dolary
kantor_usd(4567)  # Wymieniam dolary 4567. Mam 18313.67 pln.

# uruchomienie kantoru eur
kantor_eur = kantor("eur")
kantor_eur(5000)  # Wymieniam euro 5000. Mam 21549.999999999996 pln.
