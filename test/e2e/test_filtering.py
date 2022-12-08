import pytest

from src.console_utils import filter_badwords, filter_badwords_adjacent_words


@pytest.mark.parametrize("test_word, expected", [
    ("kurwa", 5),
    ("gówno", 5),
    ("jp", 2),
    ("milf", 4),
    ("wtf", 3),
    ("cyckoman", 8),
    ("chuj", 4),
    ("zjeb", 4),
    ("kutas", 5),
    ("suka", 4),
    ("pindol", 6),
    ("cipa", 4),
    ("jebanko", 7),
    ("pierdole", 8),
    ("zdzira", 6),
    ("zdz1r@", 6),
    ("zdz1r4", 6),
    ("zzdz1rr4", 6),
    ("zdziar", 6),
    ("zdzria", 6),
    ("dzz1r@", 6),
    ("zzddzziirraa", 6),
    ("c1pa", 4),
    ("c1111p4", 4),
    ("c1p4", 4),
    ("c11.p4", 4),
    ("kurw.a", 4),
    ("kur w a", 4),
    ("c1pa", 4),
    ("c1pa", 4),
    ("kurvv44", 5),
    ("g0wnÓ", 5),
    ("g0wnÓ", 5),
    ("jp", 2),
    ("pj", 2),
    ("j|°", 2),
    ("j]p", 2),
    ("jjjp", 2),
])
def test_single_words(test_word, expected):

    example_input = test_word.lower()

    filter_badwords_results = filter_badwords(input_text=[example_input])

    filter_badwords_adjacent_words_results = filter_badwords_adjacent_words(input_text=filter_badwords_results)

    assert filter_badwords_adjacent_words_results[0] == "*" * expected
