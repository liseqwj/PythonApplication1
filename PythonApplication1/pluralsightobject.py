#count = 0 # zmienna globalna

#def show_count():
#    print("count = ", count)

#def set_count(c): #zmienna lokalna
#    global count #aby pokazac do czego ma sie odnosic zmienna c w tej funkcji, trzeba dodac global

#    count = c 


################################collections

################# tuple
#t = ("Norway", 4,953, 3) #tuple zapisujemy przez ()
#print(t)

#p = 1,2,3,4,5,6 #mozemy tez stworzyc tuple bez()

#a = ((220, 284), (1184, 1210), (2620,2924), (5020,5654)) #do tupli mozna przypisac zagniezdzone wartosci i potem odczytywac ich zawartosc przez []
#print(a[2][1]) # szuka tuple[2] i pokazuje [1] element z tego tupla - czyli 3 tupla, 2 element khh

#h = (493) #to nie jest tupla, type(h) zwraca int
#h = (493,) # to jest tupla
#e = () #pusta tupla, type zwraca tuple

#def minmax(items):
#    return min(items), max(items)

#a = minmax([1,2,3,4,5,6,7,8,9,10])
#print(a)

#lower, upper = minmax([1,2,3,4,5,6,7,8,9]) #przypisujemy min i max bezposrednio do zmiennych lower i upper
#print(lower, upper)

#a = 'jelly'
#b = 'fish'

#a, b = b, a  #idiomatic Python swap, zamienia wartosc zmiennych. a raczej zmienia odwolania do obiektow ;]
#print(a + " " + b)

#a = tuple("Microsoft Windows 10")   #tworzy tuple z innych iterowalnych obiektow
#b = tuple([10,20,30,40,50])         #np z listy         
#print(a)
#print(b)

###################str
#colors = ";".join(["#1515", "#213135", "#65464", "#884"]) #join laczy stringi przy pomocy zdefiniowanego separatora
#print(colors)

##colors = "|||".join(["1515", "213135", "65464", "884"])
##print(colors)

#a = colors.split(";") #dziele dlugi string na slowa oddzielone separatorem
#print(a)

#a = "unforgivenable".partition("forgiven") #dziele string na prefix, separator, sufix, tworzac tuple

#print(a)
#print(type(a))

#departure, separator, arrival = "London:Essex".partition(":") #tworze trzy stringi na raz, odpowiadajace obiektom departure, separator, arrival
#print(departure, separator, arrival)
#print(type(departure))
#print(type(separator))
#print(type(arrival))

#origin, _, dest = "seattle-boston".partition('-') #underscore _ uzywamy jako dummy name dla separatora, wiele narzedzi rozpoznaje taki zapis
#print(origin)
#print(dest)

#print("the age of {0} is {1}".format("Wojtek", 30))

#print("the age of {0} is {1}. {0}`s birthday is on {2}".format("Wojtek", 30, "April the 8th"))

#print("the age of {name} is {age}. {name}`s birthday is on {date}".format(name = "Wojtek", age = 30, date = "April the 8th"))

#print("the age of {} is {}".format("Wojtek", 30))

#pos = (65.2, 23.1, 82.2) #tworzymy tuple
#print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=pos)) #odwolujemy sie do elementow tupli wstawiajac je do stringa

#import math
#print("Stale w bibliotece math: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)) #:.3f formatujemy typ zmiennoprzecinkowy float tak aby pokazywal 3 miejsca po przecinku

##################range

#a = range(5)
#print(a) # drukuje od 0 do 4, stop zawsze 1 mniej niz argument range

#s = [0,1,2,3,4,5,6]
#for i in range(len(s)):
#    print(s[i]) # taki kod zadziala, ale jest niepytoniczny
#print("to było nie pytoniczne")

#for v in s:
#    print(v)    #zawsze lepiej bezposrednio iterowac po iterowalnym obiekcie, np liscie

#t = [6,372,8862,14800,2096886]
#for p in enumerate(t):
#    #print(str(p) + str(type(p)))
#    print(p)
    

#funkcja wbudowana enumerate zwroci liste tupli w formacie index:wartosc
#(0, 6)
#(1, 372)
#(2, 8862)
#(3, 14800)
#(4, 2096886)

#for i, v in enumerate(t):
#    print("i = {}, v = {}".format(i, v)) # w ten elegancki sposob sformatuje tuple wychodzace z funkcji enumerate(t)

##i = 0, v = 6
##i = 1, v = 372
##i = 2, v = 8862
##i = 3, v = 14800
##i = 4, v = 2096886

#####list

#s = "show how to index into seq".split(" ")

##-6    -5     -4      -3      -2      -1
##show  how    to    split    into    seq
##0      1      2       3       4       5  
#print(s[0])
#print(s[5])
#print(s[-1])
#a = s[5] == s[-1] #True, bo mozna odwolywac sie do pozycji z listy od 0 do konca i od -1 do poczatku
#print(a)

##slicing obiektu
#print(s[0:3]) #startowa pozycja i koncowa
#print(s[1:-1]) #pokaze wszystko bez brzegow (skonczy na -2!)

#print(s[3:]) #od pozycji startowej [3] do konca obiektu
#print(s[:3])

#full_slice = s[:]
#a = full_slice is s
#b = full_slice == s
#print(a, b) #full_slice NIE jest tym samym obiektem co s, jest rowne co do wartosci

#u = s.copy()    #metoda kopiowania zawartosci listy do innego obieku
#print(u)

#v = list(s)     #inna metoda kopiowania zawartosci listy s. w ten sposob mozna tez stworzyc liste z innych obiektow

#a = "Litwo! moja. Ile cie trzeba cenic, ten tylko sie, kto cie stracil".split()
#a.insert(1, "Ojczyzno") #wstawia na pozycje [1] stringa
#print(a)

#b = a.index("cenic,")
#print(b)

#a.append("Dzis")
#print(a)

#a.reverse() #odwraca zawartosc listy
#print(a)

#c = [5,15,25,84,63131,18,33018,1,21315,47,313218,0]
#c.sort()    #sortuje liste az milo
#print(c)

##### dictionary

a = {1: [1,2,3,4], 2: ["Wojtek", "Kamcia", "tatko"], 3: ["random spam"]} #dictionary, klucz: wartosc. wartosc moze byc lista, stringiem itp. wartosci musza byc niemutowalne:
                                                                         #stringi, liczby i tuple
names_and_ages = [("Alice", 32), ("Bobek", 14), ("Wojtek", 30)]
d = dict(names_and_ages) #tworze nowy obiekt konwertujacy liste na slownik
print(d)

e = dict(Kamcia=22)
d.update(e)
print(d)

colors = dict(aquamarine="#gfafs", czerwony="asdas", zielony="0x2134", czarny="0xffff")

for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key])) #mozna iterowac po slowniku po KLUCZACH, odczytujac wartosc przez slownik[KLUCZ]


for value in colors.values():
    print(value)    #iteruje po wartosciach ze slownika

for key, value in colors.items():
    print("{key} value is {value}".format(key=key, value=value)) # slownik.item() wyrzuca pary klucz-wartosc bedace tuplami

symbols = dict(usd='\u0024', gbp='\u00a3', nzd='\u0024', krw='\u20a9')
a = 'nzd' in symbols #metoda IN oraz NOT IN dziala na slownikach
print(a)

z = dict(h=1, tc=2, xe = 54, un = 137)
print(z)

del z["un"]     #mozemy usuwac ze slownika klucz i przypisana do niego wartosc
print(z)

m = {"H":[1,2,3],
     "He":[3,4],
     "Li":[7,9,10],
     "Be":[10,11],
     "C":[11,12,13,14]}

print(m)
m["H"] += [4,5,6,7] #mozna dodawac do istniejacej wartosci dla danego klucza

print(m)

m["N"]=[15,16,17]   #mozna dodawac do istniejacego slownika, jest mutowalny
print(m)


from pprint import pprint as pp #preety print, taka biblioteka rozumiesz
pp(m)

###########set
#zbior unikalnych wartosci, MOZE SLUZYC DO SZYBKIEGO USUWANIA DUPLIKATOW
#ma metody algebry, porownywania zbiorow (zawiera sie w, nie zawiera, razem itp)
a = {1,2,3,4,5,6,777,7,7,7,7,7,8,8,8,9,10}
print(a)

a.add(0)
print(a)
a.remove(5)
print(a)
a = {1,2,3}
b = {2,3,4}
print(a.union(b))   #union laczy oba zbiory >>> 1,2,3,4
print(a.intersection(b))    #intersection pokazuje czesc wspolna >>> 2,3
print(a.difference(b))      #difference pokazuje tylko to w A czego nie ma w B >>> 1
print(a.symmetric_difference(b))    #pokazuje tylko to co nie jest wspolne dla obu zbiorow >>> 1 i 4

print(a.issubset(b))    #pokazuje czy wszystko z a jest w b >> FALSE bo w B nie ma 1

a = {1,2,3}
b = {1,2,3,4}
print(a.issubset(b))    #TRUE, bo w B jest wszystko z A. A jest podzbiorem B
print(a.issuperset(b))  #FALSE, bo w A nie ma wszystkiego z B. A nie jest supersetem dla B
print(b.issuperset(a))  #TRUE, bo A zawiera sie w calosci w B
print(a.isdisjoint(b))  #sprawdza, czy dwa zbiory nie maja zadnych elementow wspolnych >> FALSE

a = {0,-2,-3}
b = {1,2,3,4}
print(a.isdisjoint(b))  #TRUE, bo miedzy A i B nie ma elementow wspolnych > zbiory rozlaczne