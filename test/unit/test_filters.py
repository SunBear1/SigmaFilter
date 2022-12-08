from src.console_utils import filter_badwords, filter_badwords_adjacent_words
from src.filters import remove_repeats, remove_endings


def test_remove_repeats():
    assert remove_repeats("kurrrwwwaaa") == "kurwa"


def test_removingEnding_whenWordIsNoun_thenReturnsWordCore():
    assert remove_endings("kurwę") == "kurwa"


def test_removingEnding_whenWordIsAdjective_thenReturnsWordCore():
    assert remove_endings("jebana") == "jebać"
