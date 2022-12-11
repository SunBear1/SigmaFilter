from filters import remove_spaces, remove_repeats, charswap_filter, remove_endings, censor_word, \
    letter_combinations_filter, remove_special_characters
from source_dicts import SourceDictionaries
import morfeusz2

morf = morfeusz2.Morfeusz()

"""
Module containing functions with filtering algorithms
"""


def filter_badwords(input_text: list) -> list:
    text = input_text.copy()

    for input_word in text:
        no_repeats = remove_repeats(word=input_word)
        for i_word in letter_combinations_filter(word=no_repeats):
            for j_word in charswap_filter(word=i_word):
                no_special_chars = remove_special_characters(word=j_word)
                no_endings = remove_endings(analyzer=morf, word=no_special_chars)
                if no_endings in SourceDictionaries.RAW_BAD_WORDS and input_word in text:
                    text = censor_word(input_text=text, index=text.index(input_word), word_length=len(no_endings))
    return text


def filter_badwords_adjacent_words(input_text: list) -> list:
    text = input_text.copy()
    i = 0
    while True:
        if i + 1 >= len(text):
            break
        no_spaces = remove_spaces(first_word=text[i], second_word=text[i + 1])
        no_repeats = remove_repeats(word=no_spaces)
        for i_word in letter_combinations_filter(word=no_repeats):
            for j_word in charswap_filter(word=i_word):
                no_special_chars = remove_special_characters(word=j_word)
                no_endings = remove_endings(analyzer=morf, word=no_special_chars)
                if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                    text = censor_word(input_text=text, is_adjacent=True, index=i, word_length=len(no_endings))
        i += 1
    return text
