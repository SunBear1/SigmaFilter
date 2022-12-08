from source_dicts import SourceDictionaries
from itertools import product, combinations

"""
Module containing all micro filers for word validation
"""


def charswap_filter(word: str) -> list:
    # STEP 1 - initial replacements with reference to Leet system. Capitalized letters do not matter in this filter
    for combination, letter in SourceDictionaries.POSSIBLE_SWAPS.items():
        if combination in word:
            word = word.replace(combination, letter)

    possible_profanities = [word]

    # STEP 2 - ambiguity check. f.e '4' can mean both 'a' or 'h' according to Leet so 2 variations are created instead of 1.
    for ambiguity, letters in SourceDictionaries.AMBIGUITIES.items():
        if ambiguity in word:
            for letter in letters:
                temp = list()
                for profanity in possible_profanities:
                    if profanity.count(ambiguity) > 1:
                        # Combinations of ambiguous letter replacements. F.e "iloi" -> ["lloi","llol","ilol"]
                        options = [(c,) if c != ambiguity else (ambiguity, letter) for c in profanity]
                        temp.extend([''.join(o) for o in product(*options)])
                    elif profanity.count(ambiguity) == 1:
                        temp.append(profanity.replace(ambiguity, letter))
                possible_profanities.extend(temp)

    return list(dict.fromkeys(possible_profanities))



def letter_combinations_filter(word) -> list:
    indices = [(i, i - 1) for i in range(1, len(word))]

    output = []
    for index_a, index_b in indices:
        new_word = list(word)
        new_word[index_a], new_word[index_b] = new_word[index_b], new_word[index_a]
        output.append("".join(new_word))

    return output


def remove_spaces(first_word: str, second_word: str) -> str:
    return first_word + second_word


def remove_repeats(word: str) -> str:
    chars = list(word)
    i = 0
    max_index = len(chars) - 2
    while i <= max_index:
        if chars[i] == chars[i + 1]:
            chars.pop(i)
            max_index -= 1
        else:
            i += 1
    return ''.join(chars)


def remove_endings(word) -> str:
    return word


def censor_word(input_text: list, index: int, is_adjacent: bool = False) -> list:
    text = input_text.copy()
    if is_adjacent:
        text[index] = str(text[index] + text[index + 1])
        text[index] = text[index].replace(text[index], ("*" * len(text[index])))
        text.pop(index + 1)
    else:
        text[index] = text[index].replace(text[index], ("*" * len(text[index])))
    return text