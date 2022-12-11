import pytest
import morfeusz2

from filters import remove_repeats, remove_endings



@pytest.fixture
def analyzer():
    return morfeusz2.Morfeusz()


def test_remove_repeats():
    assert "kurwa" == remove_repeats("kurrrwwwaaa")


def test_removingEnding_whenWordIsNoun_thenReturnsWordCore(analyzer):
    assert "kurwa" == remove_endings(analyzer, "kurwę")


def test_removingEnding_whenWordIsAdjective_thenReturnsWordCore(analyzer):
    assert "jebać" == remove_endings(analyzer, "jebana")


def test_removingEnding_whenWordIsAdverb_thenReturnsWordCore(analyzer):
        assert "chujowy" == remove_endings(analyzer, "chujowa")
