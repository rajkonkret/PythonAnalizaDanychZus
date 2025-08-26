# while - pętla sterowana warunkiem

i = 0
while i < 3:
    print(i)
    i += 1
# 0
# 1
# 2

while True:
    print("Na jakim jesteś kursie? ")
    wybor = input()
    if wybor == 'java':
        break  # przerywa pętle
# Na jakim jesteś kursie?
# python
# Na jakim jesteś kursie?
# php
# Na jakim jesteś kursie?
# c++
# Na jakim jesteś kursie?
# sap
# Na jakim jesteś kursie?
# java

# for - petla iteracyjna
for liczba in range(3):  # 0,1,2
    print(liczba)
# 0
# 1
# 2

lista_liczby = [9, 99, 999]
nowa = []
for i in lista_liczby:
    nowa.append(i + 1)
    # print(nowa) # za kazdym przejsciem pętli
print(nowa)  # po zakończeniu pętli
# [10, 100, 1000]

# list comprehensions
nowa2 = [i + 1 for i in lista_liczby]
print(nowa2)  # [10, 100, 1000]

print(list(range(15)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(tuple(enumerate(nowa2)))
# ((0, 10), (1, 100), (2, 1000))

print(tuple(enumerate(nowa2, start=1)))
# ((1, 10), (2, 100), (3, 1000))

osoba = ["Radek", "Tomek", "Zenek", "Piotr"]
wiek = [44, 55, 23]

# Radek 44
# zip() - łączy kolekcje
for i in zip(osoba, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 23)

# mozemy rozpakowac krotkę juz w pętli
for o, w in zip(osoba, wiek):
    print(o, w)
# Radek 44
# Tomek 55
# Zenek 23
