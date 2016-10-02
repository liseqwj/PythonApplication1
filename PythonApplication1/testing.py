"""Retrieve and print words from a url
Usage:
    python testing.py url
"""
import sys
from urllib.request import urlopen


def fetch_words(url): 
    """Fetch a list of words from a URL
    
        Args:
            url: the url
        Returns:
            a list of strings.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words    


def print_items(items):          
    """Print items one per line.
       Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a url.
    """
    words = fetch_words(url)
    print_items(words)

      
if __name__ == "__main__":    
    main(sys.argv[1]) # the Oth arg is the module filename
    

   
#def square(x):
#    return x * x

#print(square(5))

#def even_or_odd(n):
#    if n % 2 == 0:
#        print("even")
#        return
#    print("odd")

