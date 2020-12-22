import unittest
from dec22 import m22

example = '''\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

loop_ex = '''\
Player 1:
43
19

Player 2:
2
29
14'''


class Test22(unittest.TestCase):

    def test_play(self):
        hands = m22.parse_hands(example)
        hands = m22.play_game(hands)
        self.assertEqual(len(hands[0]), 0)
        self.assertEqual(hands[1], [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(m22.score(hands[1]), 306)

    def test_loop(self):
        hands = m22.parse_hands(loop_ex)
        winner = m22.recursive_game(hands)
        self.assertEqual(winner, 0)
