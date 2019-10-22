import random
import sys

quotes = sys.argv[1:]

def random_python_quote():
    for quote in quotes:
        rand_index = random.randint(0, len(quotes) - 1)
        
    return quotes[rand_index]

if __name__ == '__main__':
    #quote = random_python_quote()
    random.shuffle(quotes)
    a = ' '.join(quotes)
    print(a)