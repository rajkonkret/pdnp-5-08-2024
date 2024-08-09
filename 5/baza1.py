# bazy danych - przechowują zbiory danych
# relacyjne, nierelacyjne - sql, nosql
# relacyjne zwykle dane w tabelach
# nierelacyjne przechowują np.: całe obiekty (jsony)
# postgres, mysql, mssql, mariadb, oracle
# gadaja językiem sql
import sqlite3  # biblioteka baza danych sqlite

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza zostala podłączona")
except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza zostala podłączona
# Połączenie zostało zamknięte
