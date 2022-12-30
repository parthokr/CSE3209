import nltk

nltk.download('gutenberg')
from nltk.corpus import gutenberg
from random import randint, choice
from string import punctuation, ascii_letters, digits


def main():
    txt = """
    Password strength:
    1. Weak
    2. Strong [Default]
    3. Exit
    """
    words = list(set(nltk.Text(gutenberg.words('austen-emma.txt'))))
    while True:
        print(txt)
        ch = input('Choice: ')
        if ch == '3':
            break
        elif ch == '1':
            n = randint(1, 2)
            selected_words = []
            for _ in range(n):
                selected_words.append(words[randint(0, len(words)-1)])
            print(''.join(selected_words))
        elif ch == '2':
            pool = ascii_letters + punctuation + digits
            l = randint(8, 25)
            pwd = ''
            for _ in range(l):
                pwd += choice(pool)
            print(pwd)

if __name__ == '__main__':
    main()
