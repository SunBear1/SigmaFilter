"""
Main project module
"""
import yaml

from src.console_utils import run_filters

TEST_WORDS_FILEPATH = "../data/test_badwords.yaml"

if __name__ == '__main__':
    user_input = input("Type word to check(skip if run words from test_badwords.yaml)\n")
    if user_input == "":
        with open(TEST_WORDS_FILEPATH, "r", encoding="utf8") as stream:
            badwords = yaml.safe_load(stream)["badwords"]
        for word in badwords:
            run_filters(word=word)
    else:
        run_filters(word=user_input)
