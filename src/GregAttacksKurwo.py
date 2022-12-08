import morfeusz2


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


def remove_endings(word):
    analysis = morf.analyse(word)

    word_core = ""
    try:
        word_core = analysis[0][2][1]
        if word_core == "":
            raise Exception
    except:
        print("enable to remove ending")

    return extract_lemma(word_core)


morf = morfeusz2.Morfeusz()
text = "chuju, stówe mi wysisz kurwo (cipę -> niestety nie wykrywa kutas) (skurwysyn działa dzieki Morfeuszowi)!"

for word in text.split():
    print(remove_endings(word))
