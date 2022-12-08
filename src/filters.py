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
                        options = [
                            (c,) if c != ambiguity else (ambiguity, letter)
                            for c in profanity
                        ]
                        temp.extend(["".join(o) for o in product(*options)])
                    elif profanity.count(ambiguity) == 1:
                        temp.append(profanity.replace(ambiguity, letter))
                possible_profanities.extend(temp)

    return possible_profanities


def letter_combinations_filter(word) -> list:
    indices = [(i, i - 1) for i in range(1, len(word))]

    output = []
    for index_a, index_b in indices:
        new_word = list(word)
        new_word[index_a], new_word[index_b] = new_word[index_b], new_word[index_a]
        output.append("".join(new_word))

    return output


def example_filer(word: str):
    if word == "kurva":
        return False
    return True
