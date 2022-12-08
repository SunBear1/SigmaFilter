"""
Main project module
"""
from console_utils import load_input_from_file, filter_badwords, filter_badwords_adjacent_words
import yaml
from src.console_utils import run_filters

INPUT_FILE_PATH = "../wejscie.txt"

if __name__ == '__main__':

    print("------------------------")
    print("------Sigma filter------")
    print("------------------------")
    print("© 2022 Autorzy:")
    print("Jeremi Ledwoń, Grzegorz Pozorski, Fryderyk Róg, Łukasz Niedźwiadek\n")
    print("Wprowadź tekst który chcesz ocenzurować")
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

    print("DEBUG", "Tekst przed filtrami", text_to_filter)
    # Filter words without space filtering
    filter_badwords_results = filter_badwords(input_text=text_to_filter)
    print("DEBUG", "filtr bez łączenia słów", filter_badwords_results)

    # Filter words with space filtering
    filter_badwords_adjacent_words_results = filter_badwords_adjacent_words(input_text=filter_badwords_results)
    print("DEBUG", "filtr z łączeniem słów", filter_badwords_adjacent_words_results)

    print("Ocenzurowany text:")
    result = ""
    for word in filter_badwords_adjacent_words_results:
        result += word + " "
    print(result)
