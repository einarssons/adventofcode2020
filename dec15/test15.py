import unittest
from dec15 import m15


class Test15(unittest.TestCase):

    def test_simple(self):
        start_vector = [0, 3, 6]
        magic_list = m15.MagicList(start_vector)
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (0, 4), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (3, 5), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (3, 6), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (1, 7), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (0, 8), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (4, 9), f"turn {turn}")
        nr, turn = magic_list.step()
        self.assertEqual((nr, turn), (0, 10), f"turn {turn}")

    def test_2020(self):
        cases = [([0, 3, 6], 436), ([1, 3, 2], 1)]
        for case in cases:
            magic_list = m15.MagicList(case[0])
            nr = magic_list.run_until_turn(2020)
            self.assertEqual(nr, case[1], case[0])
