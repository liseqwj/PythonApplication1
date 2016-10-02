count = 0 # zmienna globalna

def show_count():
    print("count = ", count)

def set_count(c): #zmienna lokalna
    global count #aby pokazac do czego ma sie odnosic zmienna c w tej funkcji, trzeba dodac global

    count = c 
