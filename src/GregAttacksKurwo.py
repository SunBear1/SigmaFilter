import morfeusz2
from src.source_dicts import SourceDictionaries
from src.text_preprocessor import TextPreprocessor


def extract_lemma(_word):
    sep = ":"
    return _word.split(sep, 1)[0] if ":" in _word else _word


def is_classified_as_vulgarism(word_classes):
    for word_class in word_classes:
        if type(word_class) is list:
            if len(word_class) > 0:
                word_class = word_class[0]

        if word_class == "wulg.":
            return True

    return False


def find_vulgarisms(_badwords, _text):
    _found_badwords = []
    _words = TextPreprocessor.preprocess_text(_text)

    for word in _words:
        analysis = morf.analyse(word)

        for _, _, element in analysis:
            word_core = element[1]
            word_core = extract_lemma(word_core)

            if word_core in _badwords:
                _found_badwords.append(word)
                break

            if is_classified_as_vulgarism(element[2:]):
                _found_badwords.append(word)
                break

    return _found_badwords


if __name__ == "__main__":
    # demo
    morf = morfeusz2.Morfeusz()
    badwords = SourceDictionaries.RAW_BAD_WORDS
    text = "chuju, stówe mi wysisz kurwo (cipę -> niestety nie wykrywa kutas) (skurwysyn działa dzieki Morfeuszowi)!"

    found_badwords = find_vulgarisms(badwords, text)

    print(found_badwords)
