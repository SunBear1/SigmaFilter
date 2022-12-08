"""
Main project module
"""
from console_utils import load_input_from_file, filter_badwords, filter_badwords_adjacent_words

INPUT_FILE_PATH = "../wejscie.txt"

if __name__ == '__main__':

    bad_input = True
    while bad_input:
        option = input("1) Wczytaj tekst z pliku\n2) Wczytaj tekst z konsoli\n")
        if option == "1":
            text_to_filter = load_input_from_file(path=INPUT_FILE_PATH)
            bad_input = False
        elif option == "2":
            text_to_filter = input("Wprowadź tekst:\n").split()
            bad_input = False

    for i in range(len(text_to_filter)):
        text_to_filter[i] = text_to_filter[i].lower()

    # Filter words without space filtering
    filter_badwords_results = filter_badwords(text=text_to_filter)
    print(filter_badwords_results)

    # Filter words with space filtering
    filter_badwords_adjacent_words_results = filter_badwords_adjacent_words(text=text_to_filter)
    print(filter_badwords_adjacent_words_results)
