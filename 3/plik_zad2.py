import chardet

# pip install chardet
with open('test.log', 'r', encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# Dośdane

# rb - odczyt binarny
with open('test.log', 'rb') as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6623585739772819, 'language': 'Turkish'}
# Po zwiększeniu próbki (ilości polskich liter w pliku)
# odczyt kodowania poprawny
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie znaków:", encoding)  # Kodowanie znaków: utf-8
print("Trafność", confidence)  # Trafność 0.99
print(raw_data.decode(encoding=encoding))
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# Dośdane
# Dośąćźdane
