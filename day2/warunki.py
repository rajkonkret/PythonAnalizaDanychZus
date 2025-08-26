# liczba = int(input("Podaj liczbę"))
# if liczba < 5:
#     print("Przegrałeś")
# elif liczba > 5:
#     print("Spróbuj ponownie")
# elif liczba == 5:
#     print("Wygrałeś")
# else:  # w innym przypadku
#     print("Nieznany błąd")

# od python 3.10

lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():  # strip() - czyszczenie biaych znaków
    case "python":
        print("Możesz zostać data scientist")
    case "php":
        print("Może zostać backend developerem")
    case "solidity":
        print("Możesz zostać blockchain developerem")
    case _:  # odpowiednik else
        print("Inny przypadek")
