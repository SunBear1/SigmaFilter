"""
Main project module
"""
import yaml

from console_utils import run_filters

TEST_WORDS_FILEPATH = "../data/test_badwords.yaml"

# word_without_spaces = remove_spaces(word)
# word_without_repeats = remove_repeats(word_without_spaces)
# list_of_potentials_words = remove_special_chars(word_without_repeats)
# for word in list_of_potentials_words:
#     word_without_endings = remove_endings(word)
#     if word in bad_words:
#         MARK AS BAD


if __name__ == '__main__':
    user_input = input("Type word to check(skip if run words from test_badwords.yaml)\n")
    if user_input == "":
        with open(TEST_WORDS_FILEPATH, "r", encoding="utf8") as stream:
            badwords = yaml.safe_load(stream)["badwords"]
        for word in badwords:
            run_filters(word=word)
    else:
        run_filters(word=user_input)
