from filters import remove_repeats, remove_endings
import unittest
import morfeusz2


class TestSum(unittest.TestCase):
    morf = morfeusz2.Morfeusz()

    def test_remove_repeats(self):
        self.assertEqual("kurwa", remove_repeats("kurrrwwwaaa"))

    def test_removingEnding_whenWordIsNoun_thenReturnsWordCore(self):
        self.assertEqual("kurwa", remove_endings(self.morf, "kurwę"))

    def test_removingEnding_whenWordIsAdjective_thenReturnsWordCore(self):
        self.assertEqual("jebać", remove_endings(self.morf, "jebana"))

    def test_removingEnding_whenWordIsAdverb_thenReturnsWordCore(self):
        self.assertEqual("chujowy", remove_endings(self.morf, "chujowa"))
