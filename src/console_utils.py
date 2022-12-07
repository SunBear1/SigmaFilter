"""
Module containing console UI functions
"""
from src.filters import remove_spaces, remove_repeats, charswap_filter, remove_endings
from src.source_dicts import SourceDictionaries


def load_input_from_file(path: str) -> list:
    words = []
    with open(path, mode="r", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words


def filter_badwords(text: list) -> list:
    for input_word in text:
        no_repeats = remove_repeats(word=input_word)
        for word in charswap_filter(word=no_repeats):
            no_endings = remove_endings(word)
            if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                idx = text.index(input_word)
                text[idx] = input_word.replace(input_word, ("*" * len(input_word)))
    return text


def filter_badwords_adjacent_words(text: list) -> list:
    i = 0
    while True:
        if i + 1 >= len(text):
            break
        no_spaces = remove_spaces(first_word=text[i], second_word=text[i + 1])
        no_repeats = remove_repeats(word=no_spaces)
        for word in charswap_filter(word=no_repeats):
            no_endings = remove_endings(word)
            if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                text[i] = str(text[i] + text[i + 1])
                text[i] = text[i].replace(text[i], ("*" * len(text[i])))
                text.pop(i + 1)
        i += 1
        return text
