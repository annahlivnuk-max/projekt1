def BMI():
    waga= float(input("wpisz wage w kg:"))
    wzrost= float(input("wpisz wzrost w m:"))
    wynik= waga/wzrost**2
    if wynik >25 :
        print("Wysokie BMI")
    elif wynik <18.5 :
        print("niskie BMI")
    else:
        print("norma")
    return wynik

BMI()