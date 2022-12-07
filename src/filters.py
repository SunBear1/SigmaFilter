"""
Module containing all micro filers for word validation
"""
from itertools import product

from source_dicts import SourceDictionaries


def charswap_filter(word: str) -> list:
    # STEP 1 - initial replacements with reference to Leet system. Capitalized letters do not matter in this filter
    lowercase = word.lower()

    for combination, letter in SourceDictionaries.POSSIBLE_SWAPS.items():
        if combination in lowercase:
            lowercase = lowercase.replace(combination, letter)

    possible_profanities = list()
    possible_profanities.append(lowercase)
    # STEP 2 - ambiguity check. f.e '4' can mean both 'a' or 'h' according to Leet so 2 variations are created instead of 1.
    for ambiguity, letters in SourceDictionaries.AMBIGUITIES.items():
        if ambiguity in lowercase:
            for letter in letters:
                temp = list()
                for profanity in possible_profanities:
                    if ambiguity in profanity:
                        if profanity.count(ambiguity) > 1:
                            options = [(c,) if c != ambiguity else (ambiguity, letter) for c in profanity]
                            temp = [''.join(o) for o in product(*options)]
                            temp = temp[1:]
                        else:
                            temp.append(profanity.replace(ambiguity, letter))
                possible_profanities.extend(temp)

    # STEP 3 - verifying if there is a profanity in possible_profanities list
    # for profanity in possible_profanities:
    #     if profanity in SourceDictionaries.RAW_BAD_WORDS:
    #         return False
    return possible_profanities


def remove_spaces(first_word: str, second_word: str) -> str:
    return first_word + second_word


def remove_repeats(word) -> str:
    return word


def remove_endings(word) -> str:
    return word
