from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-08-07
print(type(today))  # <class 'datetime.date'>
time = datetime.now()
print('Aktualny czas', time)  # Aktualny czas 2024-08-07 12:42:13.979285

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-08-08

print(time.time())  # 12:44:49.713699
print(today.day)  # 7 dzień
print(time.hour)  # 12 godzina

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 07/08/2024

formatted_time = datetime.now().strftime('%H:%M')
print(formatted_time)  # 12:50
print(type(formatted_time))  # <class 'str'>

# zamiana stringa z data na obiekt datatime
data_object = datetime.strptime("07/08/2024", "%d/%m/%Y")
print(data_object)  # 2024-08-07 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

# praca domowa, wyswietlic date jako 12h
