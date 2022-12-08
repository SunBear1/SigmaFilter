from src.console_utils import filter_badwords, filter_badwords_adjacent_words
from src.filters import remove_repeats


def test_remove_repeats():
    assert remove_repeats("kurrrwwwaaa") == "kurwa"
