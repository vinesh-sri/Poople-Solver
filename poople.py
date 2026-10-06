import requests
from bs4 import BeautifulSoup
from datamuse import Datamuse
api = Datamuse()
# test = api.words(sl="john")
# print(test)



# Used for reusable code
class Word:
    def __init__(self, word):
        self.word = word
        self.letters = list(word)
    def __str__(self):
        return self.word

# Main function 
def poople(start_word):
    end_words = ["prop", "boop","coop","goop","hoop", "loop", "plop", "pomp"]
    poop = Word("poop")
    start = Word(start_word)
    start_letters = start.letters
    url_one = f'https://api.datamuse.com/words?sp={start_letters[0]}{start_letters[1]}{start_letters[2]}*'
    url_two = f'https://api.datamuse.com/words?sp={start_letters[0]}{start_letters[1]}*{start_letters[3]}'
    url_three = f'https://api.datamuse.com/words?sp={start_letters[0]}*{start_letters[2]}{start_letters[3]}'
    url_four = f'https://api.datamuse.com/words?sp=*{start_letters[1]}{start_letters[2]}{start_letters[3]}'