"""
Main project module
"""
from console_utils import load_input_from_file
from src.filters import remove_spaces, remove_repeats, charswap_filter, remove_endings
from src.source_dicts import SourceDictionaries

INPUT_FILE_PATH = "../wejscie.txt"

if __name__ == '__main__':
    option = input("1) Wczytaj tekst z pliku\n2) Wczytaj tekst z konsoli\n")
    if option == "1":
        text_to_filter = load_input_from_file(path=INPUT_FILE_PATH)
    elif option == "2":
        text_to_filter = input("Wprowadź tekst:\n")
    else:
        option = input("Nieprawidłowa opcja\n1) Wczytaj tekst z pliku\n2) Wczytaj tekst z konsoli\n")

    for i in range(len(text_to_filter)):
        text_to_filter[i] = text_to_filter[i].lower()

    # Filter words without space filtering
    for input_word in text_to_filter:
        no_repeats = remove_repeats(word=input_word)
        for word in charswap_filter(word=no_repeats):
            no_endings = remove_endings(word)
            if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                idx = text_to_filter.index(input_word)
                text_to_filter[idx] = input_word.replace(input_word, ("*" * len(input_word)))

    print(text_to_filter)

    # Filter words with space filtering
    i = 0
    while True:
        if i + 1 >= len(text_to_filter):
            break
        no_spaces = remove_spaces(first_word=text_to_filter[i], second_word=text_to_filter[i + 1])
        no_repeats = remove_repeats(word=no_spaces)
        for word in charswap_filter(word=no_repeats):
            no_endings = remove_endings(word)
            if no_endings in SourceDictionaries.RAW_BAD_WORDS:
                text_to_filter[i] = str(text_to_filter[i] + text_to_filter[i + 1])
                text_to_filter[i] = text_to_filter[i].replace(text_to_filter[i], ("*" * len(text_to_filter[i])))
                text_to_filter.pop(i + 1)
        i += 1
    print(text_to_filter)
