import yaml
"""
Module containing all micro filers for word validation
"""

CHAR_SWAPS_FILEPATH = "../data/char_swaps.yaml"


def charswap_filter(word: str):
    def swap_words(s, x, y):
        return y.join(part.replace(y, x) for part in s.split(x))
            
    with open(CHAR_SWAPS_FILEPATH, "r", encoding="utf8") as stream:
        possible_swaps = yaml.safe_load(stream)["swaps_v2"]
    
    # filtering out capitalized letters     
    lowercase = word.lower()
    
    for letter, combinations in possible_swaps.items():
        for combination in combinations:
            if combination in lowercase:
                lowercase = swap_words(lowercase, combination, letter)

    print(lowercase)
                
def example_filer(word: str):
    if word == "kurva":
        return False
    return True

if __name__ == "__main__":
    charswap_filter("Koorwa")