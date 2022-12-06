import string
import re


def load_stopwords():
    file1 = open("../data/polish.stopwords.txt", "r", encoding="utf8")
    lines = file1.readlines()
    return [line.strip() for line in lines]


class TextPreprocessor:

    polish_stopwords = load_stopwords()

    @staticmethod
    def __tokenize(_text):
        tokens = _text.split()
        return tokens

    @staticmethod
    def __remove_punctuation(_text):
        punctuation_free = "".join([i for i in _text if i not in string.punctuation])
        return punctuation_free

    @staticmethod
    def __remove_stopwords(_text):
        return [i for i in _text if i not in TextPreprocessor.polish_stopwords]

    @staticmethod
    def preprocess_text(_text):
        _text = TextPreprocessor.__remove_punctuation(_text)
        _text = _text.lower()
        _text = TextPreprocessor.__tokenize(_text)
        _text = TextPreprocessor.__remove_stopwords(_text)

        return _text
