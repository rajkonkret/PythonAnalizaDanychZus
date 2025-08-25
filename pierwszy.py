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