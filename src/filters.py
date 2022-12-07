from source_dicts import SourceDictionaries
from itertools import product
"""
Module containing all micro filers for word validation
"""

def charswap_filter(word: str) -> list:
            
    #STEP 1 - initial replacements with reference to Leet system. Capitalized letters do not matter in this filter
    for combination, letter in SourceDictionaries.POSSIBLE_SWAPS.items():
        if combination in word:
            word = word.replace(combination, letter)
    
    # 
    possible_profanities = list()
    possible_profanities.append(word)
    
    # STEP 2 - ambiguity check. f.e '4' can mean both 'a' or 'h' according to Leet so 2 variations are created instead of 1.
    for ambiguity, letters in SourceDictionaries.AMBIGUITIES.items():
        if ambiguity in word:
            for letter in letters:
                temp = list()
                for profanity in possible_profanities:
                    if ambiguity in profanity:
                        if profanity.count(ambiguity) > 1:
                            # Combinations of ambiguous letter replacements. F.e "iloi" -> ["lloi","llol","ilol"]
                            options = [(c,) if c != ambiguity else (ambiguity, letter) for c in profanity]
                            temp.extend([''.join(o) for o in product(*options)])
                        else: 
                            temp.append(profanity.replace(ambiguity, letter))
                possible_profanities.extend(temp)
    
    return possible_profanities


def example_filer(word: str):
    if word == "kurva":
        return False
    return True

if __name__ == "__main__":
    print(charswap_filter("plndol"))
