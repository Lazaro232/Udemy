import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def get_user_confirmation(word):
    user_answer = input(f'Did you mean {word[0]}? (y\\n): ')
    if user_answer.lower() == 'y':
        return True
    else:
        return False


def print_data(word):
    for meaning in data[word]:
        print(meaning)


def get_best_matches(word):
    closer_word = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
    if closer_word:
        user_answer = get_user_confirmation(closer_word)
        if user_answer:
            return print_data(closer_word[0])
        else:
            return print('Try again.')
    else:
        return "The word does not exist. Please double check it"


def translate(word):
    word = word.lower()
    if word in data:
        return print_data(word)
    else:
        return get_best_matches(word)


word = input('Enter word: ')

translate(word)
