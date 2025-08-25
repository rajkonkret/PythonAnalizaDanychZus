# kolekcja - przechowuje wiele elementów, róznego typu na raz

# lista  - zachowuje kolejnośc przy dodawaniu elementów
lista = []  # pusta lista
lista_pusta = list()  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>
lista_pusta.append("Piotr")  # dodanie elementów do listy
lista_pusta.append("Agnieszka")  # dodanie elementów do listy
lista_pusta.append("Radek")
lista_pusta.append("Zenek")
print(lista_pusta)  # ['Piotr', 'Agnieszka', 'Radek', 'Zenek']
print(type(lista))  # <class 'list'>
print(type(lista_pusta))  # <class 'list'>
lista_pusta.sort()  # zmienia oryginał
print(lista_pusta)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek']

# lista_pusta.append(345)
# print(lista_pusta)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek', 345]
# lista_pusta.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'

# indeksy od 0
# wstawienie w konkretne miejsce
lista_pusta.insert(1, "Magda")
print(lista_pusta)  # ['Agnieszka', 'Magda', 'Piotr', 'Radek', 'Zenek']

print(lista_pusta[0])  # Agnieszka
# print(lista_pusta[23]) # IndexError: list index out of range
print(lista_pusta[-1])  # ostatni element, Zenek
# długosc listy
print(lista_pusta[len(lista_pusta) - 1])  # Zenek

# slicowanie - fragment listy
# ['Agnieszka', 'Magda', 'Piotr', 'Radek', 'Zenek']
print(lista_pusta[0:2])  # ['Agnieszka', 'Magda'], z prawej zbior otwarty
print(lista_pusta[:2])  # ['Agnieszka', 'Magda']
print(lista_pusta[1:])  # ['Magda', 'Piotr', 'Radek', 'Zenek'], z ostatnim włącznie
print(lista_pusta[1:-1])  # ['Magda', 'Piotr', 'Radek'], ostatni niewłącznie
print(lista_pusta[0:4:2])  # start:stop:krok, ['Agnieszka', 'Piotr']
print(lista_pusta[::-1])  # ['Zenek', 'Radek', 'Piotr', 'Magda', 'Agnieszka']

print(lista_pusta[45:90])  # []

lista_pusta.remove("Magda")
print(lista_pusta)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek']

osoby = ['Tomek', 'Ewa', "Adam"]
osoby.extend(lista_pusta)
print(osoby)  # ['Tomek', 'Ewa', 'Adam', 'Agnieszka', 'Piotr', 'Radek', 'Zenek']

a = 1
b = 2
a = b
print(a)  # 2
b = 3
print(a)  # 2

nowa_lista = lista_pusta  # kopia referencji (adres w pamięci)
lista_copy = lista_pusta.copy()  # kopia listy
print(lista_pusta)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek']
print(nowa_lista)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek']
lista_pusta.clear()  # usuniecie elementów z listy
print(lista_pusta)
print(nowa_lista)
print(lista_copy)  # ['Agnieszka', 'Piotr', 'Radek', 'Zenek']

print(id(lista_pusta))  # 2623352881024
print(id(nowa_lista))  # 2623352881024
print(id(lista_copy))  # 2623350143040

# krotka (tupla) - niemutowalna lista
# pozwala lepiej zarządać pamięcią
krotka = (23, 34, 56, "Radek")
print(krotka)  # (23, 34, 56, 'Radek')
krotka1 = "radek", "tomek", "zenek"
print(krotka1)  # ('radek', 'tomek', 'zenek')

krotka2 = ("Radek",)
print(type(krotka2))  # <class 'tuple'>

krotka3 = "Radek",
print(type(krotka3))  # <class 'tuple'>

print(len(krotka))  # długosc krotki, 4 elemnty
# rozpakowanie krotki
# (23, 34, 56, 'Radek')
a, b, *c = (23, 34, 56, 'Radek')  # * - pozostałe elementy
print(a, b, c)  # 23 34 [56, 'Radek']
a, *b, c = (23, 34, 56, 'Radek')
print(a, b, c)  # 23 [34, 56] Radek

# krotka[1] = 4  # TypeError: 'tuple' object does not support item assignment

# słownik: dane typu klucz-wartosć
# {"name":"John"}
# odpowiednik jsona
oceny = {"Tomek": 4,
         "Radek": 5,
         "Agata": 5,
         "Zenek": 3,
         }

print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 5, 'Zenek': 3}
print(type(oceny))  # <class 'dict'>
print(oceny["Tomek"])  # 4
# print(oceny["tomek"]) # KeyError: 'tomek'
print(oceny.get("Tomek"))
print(oceny.get("tomek"))  # None

print(oceny.keys())
print(oceny.values())
print(oceny.items())
# dict_keys(['Tomek', 'Radek', 'Agata', 'Zenek'])
# dict_values([4, 5, 5, 3])
# dict_items([('Tomek', 4), ('Radek', 5), ('Agata', 5), ('Zenek', 3)])

oceny['Agata'] = 6
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 6, 'Zenek': 3}
lista_oceny = [3, 4, 5, 6, 5, 5]
oceny["Tomek"] = lista_oceny
print(oceny)
# {'Tomek': [3, 4, 5, 6, 5, 5], 'Radek': 5, 'Agata': 6, 'Zenek': 3}
print(oceny["Tomek"][1])  # 4

dictionary = {}
dict_pusty = dict()
print(dictionary)
print(dict_pusty)
# {}
# {}
print(type(dict_pusty))
print(type(dictionary))
# <class 'dict'>
# <class 'dict'>

# zbiór - set()
# przechowuje unikalne wartości
# nie zachowuje kolejnosci przy dodawania elemntów
# nie posiada indeksu
lista = [45, 55, 66, 77, 45, 55]
zbior1 = set(lista)
print(zbior1)  # {66, 77, 45, 55}

zbior1.add(100)
zbior1.add(102)
zbior1.add(105)
zbior1.add(77)
zbior1.add(55)
print(zbior1)  # {66, 100, 102, 105, 77, 45, 55}

zbior2 = {45, 55, 166, 177}

print(zbior1.difference(zbior2))  # {66, 100, 102, 105, 77}
print(zbior2.difference(zbior1))  # {177, 166}

print(zbior1.intersection(zbior2))  # {45, 55}

pusty_zbior = set()
print(pusty_zbior)
print(type(pusty_zbior))
# set()
# <class 'set'>

lista_ze_zbioru = list(zbior1)
print(lista_ze_zbioru)  # [66, 100, 102, 105, 77, 45, 55]

matrix = [[3, 4, 5], [6, 7], [8, 9, 0]]
print(matrix)  # [[3, 4, 5], [6, 7], [8, 9, 0]]
print(matrix[0][0])  # 3
matrix = [[3, 4, 5], [6, 7, [8, 9, 0]]]
print(matrix[1][2][2])  # 0
