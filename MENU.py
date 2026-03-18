print("+==========+")
print("|1.BMI     |")
print("|2.Gra     |")
print("|3.Wyjsc   |")
print("+==========+")
odp= int(input("Podaj wybur (1,2,3):"))
if odp == 1:
    import bmi
elif odp == 2:
    import gra1
elif odp == 3:
    print("Pa!")
else :
    print("Nie ma takiej opcii!")