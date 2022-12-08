"""
Module containing console UI functions
"""
from filters import remove_spaces, remove_repeats, charswap_filter, remove_endings, censor_word, \
    letter_combinations_filter
from src.source_dicts import SourceDictionaries


def load_input_from_file(path: str) -> list:
    words = []
    with open(path, mode="r", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words


def filter_badwords(input_text: list) -> list:
    text = input_text.copy()
    for input_word in text:
        no_repeats = remove_repeats(word=input_word)
        for word in charswap_filter(word=no_repeats):
            no_endings = remove_endings(word)
            if no_endings in SourceDictionaries.RAW_BAD_WORDS and input_word in text:
                text = censor_word(input_text=text, index=text.index(input_word))
    return text


def filter_badwords_adjacent_words(input_text: list) -> list:
    text = input_text.copy()
    i = 0
    while True:
        if i + 1 >= len(text):
            break
        no_spaces = remove_spaces(first_word=text[i], second_word=text[i + 1])
        no_repeats = remove_repeats(word=no_spaces)
        for j_word in letter_combinations_filter(word=no_repeats):
            for i_word in charswap_filter(word=j_word):
                no_endings = remove_endings(i_word)
                if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                    text = censor_word(input_text=text, is_adjacent=True, index=i)
        i += 1
    return text
