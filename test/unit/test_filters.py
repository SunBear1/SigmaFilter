from src.console_utils import filter_badwords, filter_badwords_adjacent_words
from src.filters import remove_repeats, remove_special_characters


def test_remove_repeats():
    assert remove_repeats("kurrrwwwaaa") == "kurwa"


def test_remove_special_characters():
    assert remove_special_characters("ci.pa") == "cipa"
