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
