words = "Have you ever walked through a room But it was more like the room passed around you Like there was a leash around your neck that pulled you through?".split()

print(words)
a = [len(word) for word in words]   #wykonuje funkcje LEN na kazdym elemencie listy i zwraca do LISTY a
print(a)                            #[expression(item) for item in iterable]

print("*********************************")

from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
print(f)


print("*********************************")

print("*********************************")
f = {len(str(factorial(x))) for x in range(20)} #zwraca SET a nie liste bo jest {}, pokazuje tylko unikalne wartosci funkcji 
print(f)                                        #factorial(x)


print("*********************************")
print("*********************************")

from pprint import pprint as funkielnowka

country_to_capital = {"UK":"London",
                      "Brazil":"Brasil",
                      "USA":"Washington",
                      "Poland":"Warsaw"}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}

print(capital_to_country)
funkielnowka(capital_to_country)

import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob("*.py")}   #expr (sciezka:rozmiar pliku) for plik in iterable(*.py w danym katalogu)

funkielnowka(file_sizes)

file_size = {os.path.relpath(p): os.path.getsize(p) for p in glob.glob("*.py")}
funkielnowka(file_size)

file_size = {os.path.normpath(p): os.path.getsize(p) for p in glob.glob("*.py")}
funkielnowka(file_size)