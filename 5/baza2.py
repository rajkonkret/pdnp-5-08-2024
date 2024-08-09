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

    query = '''
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    c.execute(query)
    conn.commit()

    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek', 'radek@radek.pl', '10000');
    """
    # c.execute(insert)
    # conn.commit()

    update = """
    UPDATE developers SET salary=12000 WHERE id=1;
    """
    # c.execute(update)
    # conn.commit()

    select = """
    SELECT * FROM developers;
    """
    for row in c.execute(select):
        print(row)  # (1, 'Radek', 'radek@radek.pl', None, 12000.0)

except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza zostala podłączona
# Połączenie zostało zamknięte
