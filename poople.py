import requests
from bs4 import BeautifulSoup


class Word:
    def __init__(self, word):
        self.word = word
        self.letters = list(word)
    def __str__(self):
        return self.word

def poople(start_word):
    end_words = ["prop", "boop","coop","goop","hoop", "loop", "plop", "pomp"]
    poop = Word("poop")
    start = Word(start_word)
    url = f'https://api.datamuse.com/words?ml={3}'