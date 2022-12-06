import yaml
"""
Module containing all micro filers for word validation
"""

CHAR_SWAPS_FILEPATH = "../data/char_swaps.yaml"


def charswap_filter(word: str):
            
    with open(CHAR_SWAPS_FILEPATH, "r", encoding="utf8") as stream:
        yml_data = yaml.safe_load(stream)
    possible_swaps = yml_data["swaps"]
    ambiguities = yml_data["ambiguities"]
    
    lowercase = word.lower()
    for letter, combinations in possible_swaps.items():
        for combination in combinations:
            if combination in lowercase:
                lowercase = lowercase.replace(combination, letter)
    
    possible_profanities = []
    #ambiguity check. f.e '4' can mean both 'a' or 'h' according to Leet so 2 variations are created instead of 1.
    for combination, letters in ambiguities.items():
        for letter in letters:
            if combination in lowercase:
                possible_profanities.append(lowercase.replace(combination, letter))
    
    print(possible_profanities)

                
def example_filer(word: str):
    if word == "kurva":
        return False
    return True

if __name__ == "__main__":
    charswap_filter("Koorw4")