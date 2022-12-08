from src.filters import remove_repeats, remove_special_characters


def test_remove_repeats():
    assert remove_repeats("kurrrwwwaaa") == "kurwa"


def test_remove_special_characters():
    assert remove_special_characters("ci.pa") == "cipa"
