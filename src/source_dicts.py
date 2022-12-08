"""
Module loading all source dictionaries used inside filters.py
"""
import yaml


class SourceDictionaries:
    with open("../data/badwords.yaml", "r", encoding="utf8") as stream:
        RAW_BAD_WORDS: list = yaml.safe_load(stream)["badwords"]
    with open("../data/char_swaps.yaml", "r", encoding="utf8") as stream:
        yml_swap_data = yaml.safe_load(stream)
    with open("../data/special_chars.yaml", "r", encoding="utf8") as stream:
        yml_special_chars = yaml.safe_load(stream)

    SPECIAL_CHARACTERS: dict = yml_special_chars["special-chars"]
    AMBIGUITIES: dict = yml_swap_data["ambiguities"]
    raw_swaps: dict = yml_swap_data["swaps"]
    modified_swaps = {}
    for key, values in raw_swaps.items():
        for value in values:
            modified_swaps[value] = key
    sorted_swaps = dict(sorted(modified_swaps.items(), key=lambda item: len(item[0]), reverse=True))
    POSSIBLE_SWAPS: dict = sorted_swaps
