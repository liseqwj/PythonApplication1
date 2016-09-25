import random
from time import sleep

name = input("Podaj imie: \n")

print("Ej, {0}, mysle o pewnym numerze miedzy 1 a 20".format(name))


number = random.randint(1, 20)
guesses_made = 0
#print(number)

while guesses_made < 6:
        guesses_made += 1
        guess_number = int(input("No podaj jakas liczbe: \n"))
        if guess_number > number:
           print("Moja liczba jest mniejsza")
        if guess_number < number:
           print("Moja liczba jest wieksza")
        if guess_number == number:
            break

if guess_number == number:
    print("Brawo {0}! Zgadlas numer w {1} probach, gratki".format(name, guesses_made))
else:
    print("Wykorzystano wszystkie proby, tym razem sie nie udalo. Nie poddawaj sie {0}".format(name))

print("moja pierwsza gra w Pytongu, yeeeeah")

print("that`s all folks")


        


