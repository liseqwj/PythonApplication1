from urllib.request import urlopen
import sys

def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words    

def print_items(items):          
    for item in items:
        print(item) 

def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)

      
if __name__ == "__main__":
    main()
   


#def square(x):
#    return x * x

#print(square(5))

#def even_or_odd(n):
#    if n % 2 == 0:
#        print("even")
#        return
#    print("odd")
