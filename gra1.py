import random
def game():
    opcii = ["kamien" , "nozyczki" , "papier"]
    while True:
       print("Hej! Zaczynamy gre Kamien,nozyczki,papier.")
       uzer = input("Zrob swoj wybor (kamien,nozyczki,papier): ").lower()
       if uzer not in opcii:
            print("zle upisane, prosze wpisac poprawnie!")
            continue
       computer = random.choice(opcii)
       print("ja mam :" ,{computer})
       if uzer == computer:
            print("Remis")
       elif ( uzer =="kamien" and computer=="nozyczki") or (uzer=="nozyczki" and computer=="papier") or (uzer=="papier"
                                                                                                and computer=="kamien"):
               print("Wygrales! Gratuluie!")
       else:
           print("Tym razem wygrała ja! ")
       wybur = input( "\n Sprobujemy jeszcze raz? (Tak/nie)").lower()
       if wybur !="tak":
            print("Dziekuie za gre! Czesc!")
            break
game()