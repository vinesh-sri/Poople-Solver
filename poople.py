import requests
from bs4 import BeautifulSoup
# using requests because I don't understand datamuse



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
    urls_to_open = {
    "url_one" : f'https://api.datamuse.com/words?sp={start_letters[0]}{start_letters[1]}{start_letters[2]}*',
    "url_two" : f'https://api.datamuse.com/words?sp={start_letters[0]}{start_letters[1]}*{start_letters[3]}',
    "url_three" : f'https://api.datamuse.com/words?sp={start_letters[0]}*{start_letters[2]}{start_letters[3]}',
    "url_four" : f'https://api.datamuse.com/words?sp=*{start_letters[1]}{start_letters[2]}{start_letters[3]}'
    }
    words_json = []
    for name, url in urls_to_open.items():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            words_json.append(data)
        else:
            print(f"Failed to retrieve data from Datamuse API. Error code: {response.status_code}")
    filtered_words = [word_dict["word"]
        for unique_url_data in words_json
        for similar_words in unique_url_data
        for word_dict in similar_words
        if len(word_dict["word"]) == 4
    ]