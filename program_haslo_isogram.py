while True:
   try:
        liczba=int(input("podaj liczbe calkowita: "))
        print(f"liczba {liczba} jest calkowita")
        print(abs(liczba))
        break
    except :
        print("Podaj liczbe calkowita,\n")


def sprawdz_haslo(haslo):
    punkty = 0
    ma_cyfre = False
    if len(haslo) >= 8:
        punkty += 1
    else:
        punkty = punkty

    for znak in haslo:
        if znak.isdigit():
            ma_cyfre = True

    if ma_cyfre: #ma_cyfre == True
         punkty+=1

    if haslo != haslo.lower():
        punkty+=1
    return punkty

haslo = input("Podaj hasło: ")


print(f"Twoja ocena to: {sprawdz_haslo(haslo)}")

def is_isogram(slowo):
    slowo = slowo.lower()
    return len(set(slowo)) == len(slowo)
slowo=input("podaj slowo:")
print(is_isogram(slowo))






def cyfry_na_slowa(tekst):
    slownik = {
        '0': 'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery',
        '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'
    }
    wynik = []
    for znak in tekst:
        wynik.append(slownik.get(znak, znak))
    return " ".join(wynik)
tekst=input("podaj liczbe: ")
print(cyfry_na_slowa(tekst))