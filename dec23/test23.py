import unittest

from dec23 import m23

example = "389125467"


class Test23(unittest.TestCase):

    def test_play(self):
        cup_list = [int(c) for c in example]
        game = m23.GameB(cup_list)
        game.turn()
        #self.assertEqual(game.list, [3, 2, 8, 9, 1, 5, 4, 6, 7])
        for _ in range(9):
            game.turn()
        #self.assertEqual(game.list, [5, 8, 3, 7, 4, 1, 9, 2, 6], "Ten turns")
        self.assertEqual(game.get_labels(), "92658374")
        self.assertEqual(game.get_two_cups(), (9, 2), "two cups")
