import unittest

from Poker.poker import check_pair, check_two_pair, check_flush, check_straight, check_full_house, check_four_of_a_kind, \
    check_three_of_a_kind


class PokerTest(unittest.TestCase):

    def test_pair(self):
        self.assertTrue(check_pair([0, 13, 14, 15, 16]))
        self.assertFalse(check_pair([0, 12, 42, 14, 11]))

    def test_two_pair(self):
        self.assertTrue(check_two_pair([0, 13, 12, 25, 4]))

    def test_three_of_a_kind(self):
        self.assertTrue(check_three_of_a_kind([0, 13, 26, 27, 51]))

    def test_four_of_a_kind(self):
        self.assertTrue(check_four_of_a_kind([0, 13, 26, 39, 51]))

    def test_flush(self):
        self.assertTrue(check_flush([0, 1, 2, 3, 4]))
        self.assertFalse(check_flush([0, 1, 2, 3, 14]))

    def test_full_house(self):
        self.assertTrue(check_full_house([0, 13, 26, 1, 14]))
        self.assertFalse(check_full_house([0, 13, 26, 1, 15]))

    def test_straight(self):
        self.assertTrue(check_straight([0, 1, 2, 3, 4]))
        self.assertTrue(check_straight([0, 10, 11, 12, 9]))
        self.assertFalse(check_straight([0, 1, 2, 3, 5]))
