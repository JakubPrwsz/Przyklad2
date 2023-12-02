'''
kalkulator prosty
'''
def main():
    a = int(input("podaj pierwszą liczbę "))

    b = int(input("podaj drugą liczbę "))

    print("1: dodawanie\n2: odejmowanie\n3: mnożenie\n4: dzielenie")

    dzialanie = input("podaj numer dzialania ktore chcesz wykonac: ")

    match dzialanie:
        case "1":
            print(a + b)
        case "2":
            print(a - b)
        case "3":
            print(a * b)
        case "4":
            print(a / b)


main()