from src.console_utils import filter_badwords, filter_badwords_adjacent_words
from src.filters import remove_repeats, remove_endings
import unittest


class TestSum(unittest.TestCase):

    def test_remove_repeats(self):
        self.assertEqual("kurwa", remove_repeats("kurrrwwwaaa"))

    def test_removingEnding_whenWordIsNoun_thenReturnsWordCore(self):
        self.assertEqual("kurwa", remove_endings("kurwę"))

    def test_removingEnding_whenWordIsAdjective_thenReturnsWordCore(self):
        self.assertEqual("jebać", remove_endings("jebana"))

    def test_removingEnding_whenWordIsAdverb_thenReturnsWordCore(self):
        self.assertEqual("chujowy", remove_endings("chujowa"))
