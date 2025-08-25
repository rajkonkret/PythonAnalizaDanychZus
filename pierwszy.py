# PEP8
# snake_case
import sys

print()
print("Radek")
# ctrl -d - powielenie linii
print('Radek')

# Radek
# Radek
# ctrl / - zakomentowanie/odkomentowanie
# print("Radek')
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\pierwszy.py", line 11
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 11)
# ctrl - alt - l  - formatowanie

# typy danych
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, typ tekstowy

print("39" + "14")  # 3914, konkatenacja, łaczenie tekstów
print(39 + 14)  # 53, operacja matematyczna

# print("39" + 14) # TypeError: can only concatenate str (not "int") to str
# silne typownie - nie zmienia typów samodzielnie

print(type(39))  # liczba calkowita, <class 'int'>
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane

# snake_case

# typowanie dynamiczne, typ zmiennej wnioskowany na podstawie danych jakie zawiera
name = "Radek"
print(name)  # Radek, wypisanie zawartości zmiennej
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = 90
print(type(name))  # <class 'int'>
print(name)

age = 67
print(type(age))  # <class 'int'>

# mypy
# pip - instalator pakietów
#  pip install mypy
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject> mypy .\pierwszy.py
# pierwszy.py:46: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:51: error: Name "name" already defined on line 42  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject>

tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))  # <class 'str'>

# teksty sa niemutowalne
tekst.upper()  # nie podstawia zmian pod zmienna tekst
# """ Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
# text pool
print(tekst.upper())  # WITAJ ŚWIECIE, drukuje tekst z nowego miejsca pamięci
zmienna = tekst.upper()
print("Zmienna:", zmienna)
# Zmienna: WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

zmienna1 = "GROSS"
zmienna2 = "groß"

# == porównanie
print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # porównanie caseless, True

# != różne
print(1 != 8)  # rózne, True
# zmienne logiczne, boolean -> True, False

# rzutowanie - zamiana typów
print(int("39"))  # zamiana na int
print(str(39))  # zamiana str

print(int(True))  # 0
print(int(False))  # 1

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False

# None - nie wiem, stan nieokreslony, odpowidnik null
print(bool(None))  # False

temp = 36.6
print(type(temp))  # <class 'float'>
print(temp)  # 36.6
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024, max_10_exp=308,
#                min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

# bład zaokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal - ominięcie problemu zaokrąglenia, powolne, zajmują dużo miejsca

# f - string format
print(f"Nazywam się {name}. Dzien dobry")  # Nazywam się 90. Dzien dobry
print("Nazywam się {}.".format(name))  # Nazywam się 90

liczba = 3.900001
print(f"Wersja pythona: {liczba}")  # Wersja pythona: 3.900001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90

print(f"""tekst
    wielolinijkowy""")
# "tekst
#     wielolinijkowy"

"""Komentarz 
wielolinijkowy.
Komentarz dokumentacyjny"""
print(print.__doc__)

starszy = "Mam na imię %s"
print(starszy % name)  # Mam na imię 90

print("Wynik:", liczba)  # Wynik: 3.900001,  sep=' ', end='\n'
print("Wynik:", liczba, sep="....")  # Wynik:....3.900001 - zmieniony separator

print(100 / 3) # 33.333333333333336
print(100 // 3) # 33 - częśc całkowita z dzielenia
print(100 % 3) # modulo, reszta  z dzielenia, r=1
print(10 % 3) # 1 reszty 3 * 3 + 1 = 10
