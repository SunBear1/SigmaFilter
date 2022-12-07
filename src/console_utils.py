"""
Module containing console UI functions
"""


def load_input_from_file(path: str) -> list:
    words = []
    with open(path, mode="r", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words
