import requests
from bs4 import BeautifulSoup
from acceptable_cases import acceptable_words_auto
# using requests because I don't understand datamuse

# Used for reusable code
class Word:
    def __init__(self, word : str):
        self.word = word.lower()
        self.letters = list(word.lower())
    def __str__(self):
        return self.word
    def __repr__(self, word):
        return self.word

def n_off(word_you_want, word_to_check, off_by_n):
    if isinstance(word_you_want, Word) and isinstance(word_to_check, Word):
        discrepancies = 0
        for wyw_letters, wtc_letters in zip(word_you_want.letters, word_to_check.letters):
            if wyw_letters == wtc_letters:
                continue
            else:
                discrepancies += 1
        if discrepancies != off_by_n:
            return False
        else:
            return True
    else:
        return TypeError(f"bad operand type for n_off(): {type(word_you_want)} and {type(word_to_check)}")
     
# Main function 
def poople(start_word):
    dictionary_of_ok_words = acceptable_words_auto()
    dictionary_of_ok_words = list(map(lambda x: x.lower(), dictionary_of_ok_words))
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
    filtered_words = list(set([word
        for combo_words in words_json # combo_words : list
        for word_dictionary in combo_words # word_dictionary : dict
        if (len(word:= word_dictionary.get("word")) == 4) and (n_off(word, start_word, 1)) and (word in dictionary_of_ok_words) 
    ]))
    return filtered_words

print(poople("does"))



