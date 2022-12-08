from src.filters import remove_repeats


def test_remove_repeats():
    assert remove_repeats("kurrrwwwaaa") == "kurwa"
