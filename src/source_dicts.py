import yaml


class SourceDictionaries:
    with open("../data/badwords.yaml", "r", encoding="utf8") as stream:
        RAW_BAD_WORDS: list = yaml.safe_load(stream)["badwords"]
