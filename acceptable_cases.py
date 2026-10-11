from bs4 import BeautifulSoup
import requests 
from time import time

def acceptable_words_auto():
    words_dictionary_url = 'https://poople.world/poople-word-list'
    response = requests.get(words_dictionary_url)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        words = [word.get_text() for word in soup.find_all('span', 'wl-word')]
        return words
    else:
        raise ConnectionError("Could not open link")


