# funkcja - wydzielony fragment kodu, można go wywołac wielokrotnie
# może przyjmować argumenty

# ta funkcja nie zwraca wyniku
# deklaracja funkcji
def witaj():
    print("Witaj!")


# wykonanie funkcji
witaj()  # Witaj!


# funkcja zwraca wynik
def ksero(tekst: str, ile: int):
    """
    Ta funkcja zwraca string pomnożony zadaną ilość razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwracamy wynik do miejsca wywołąnia funkcji


print(ksero("Radek", 5))  # RadekRadekRadekRadekRadek

print(ksero(5, 5))  # 55555
wynik = ksero("Radek", 5)
print(wynik)  # RadekRadekRadekRadekRadek


def ksero2(tekst: str, ile=1):  # parametr z wartością domyślną
    """
    Ta funkcja zwraca string pomnożony zadaną ilość razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile


print(ksero2("Radek"))  # Radek
print(ksero2("Radek", 5))  # RadekRadekRadekRadekRadek


def ksero3(tekst: str = "treść", ile=1):
    """
    Ta funkcja zwraca string pomnożony zadaną ilość razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile


print(ksero3())
print(ksero3("Radek", 3))  # pozycyjne argumenty
print(ksero3(tekst="Radek", ile=3))  # nazwane argumenty


# treść
# RadekRadekRadek
# RadekRadekRadek

def ile_razy(*ile, **co):
    print(ile)
    print(co)


# * argumenty pozycyjne
# ** argumenty nazwane, słownikowe
ile_razy(4, 5, 6)  # (4, 5, 6) -> ile
ile_razy(4, 5, 6, name="Radek", status="OK")  # (4, 5, 6) -> ile (4, 5, 6)


# {'name': 'Radek', 'status': 'OK'}

def multi(a, b):
    try:
        return a * b
    except TypeError:
        return "nieprawidłowe dane"
    except ValueError:
        return 0


print(multi(4, 4))  # 16
print(multi("4", 4))  # 4444
print(multi("4", None))  # nieprawidłowe dane


def multi2(a, b):
    try:
        return a * b
    except Exception as e:
        return "nieprawidłowe dane:", e.args


print(multi2(4, 4))  # 16
print(multi2("4", 4))  # 4444
print(multi2("4", None))
# ('nieprawidłowe dane:', ("can't multiply sequence by non-int of type 'NoneType'",))

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(e)  # division by zero
