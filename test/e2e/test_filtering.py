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
    ("zzddzziirraa", 6),
    ("c1pa", 4),
    ("c1111p4", 4),
    ("c1p4", 4),
    ("c11.p4", 4),
    ("kurw.a", 5),
    ("kur.w)a", 5),
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
    ("sók4", 4),
    ("us.ka", 4),
    ("$.ók4", 4),
    ("wt.f", 3),
    ("vvtf", 3),
    ("wtph", 3),
    ("wt+f", 3),
    ("pier+dole", 8),
    (",p13rd0l3", 8),
    (",pierodle.", 8),
    (".p1ee+rdoel=", 8),
    ("jeabnko", 7),
    ("j3bank0", 7),
    ("jeb.anko", 7),
    ("jjeebb.aannkkoo", 7),
    ("cyck0m4n", 8),
    ("cy.<kóman", 8),
    ("(y(kóm4nnnnn", 8),
    ("cyckomaaaaи", 8),
    ("kuttsa", 5),
    ("=kuats.", 5),
    ("kuut@sss", 5),
    ("kuut4$", 5),
    ("kvtas", 5),
    ("q.t@s", 5),
    ("huj", 4),
    ("ch.oj", 4),
    ("cchojj", 4),
    ("<hjo", 4),
    ("chhoooy", 4),
    ("pindoi", 6),
    ("pllndl0", 6),
    ("pind?ol", 6),
    ("piiiiiiiiind0i", 6),
    ("€¥€k0m@n", 8),
    ("curva", 5),
    ("pindolę", 6),
    ("pindolowy", 6),
    ("pindolek", 6),
    ("pindolić", 6),
    ("pindolami", 6),
    ("pindolach", 6),
    ("chuje", 4),
    ("chujem", 4),
    ("chujach", 4),
    ("chujce", 4),
    ("chujów", 4),
    ("chujeczek", 4),
    ("chujami", 4),
])
def test_single_words(test_word, expected):
    example_input = test_word.lower()

    filter_badwords_results = filter_badwords(input_text=[example_input])

    filter_badwords_adjacent_words_results = filter_badwords_adjacent_words(input_text=filter_badwords_results)

    assert filter_badwords_adjacent_words_results[0] == "*" * expected
