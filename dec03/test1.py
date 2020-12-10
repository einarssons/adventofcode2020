import unittest

from collections import namedtuple

import m

TestCase = namedtuple("TestCase", "name input want")
Input = namedtuple("Input", "forest nr_right nr_down")


example_forest = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
"""


class TestDec3(unittest.TestCase):

    def test_ride_toboggan(self):
        cases = [
            TestCase("small forest", Input(example_forest, 1, 1), 2),
            TestCase("small 3 1", Input(example_forest, 3, 1), 7),
            TestCase("small 5 1 ", Input(example_forest, 5, 1), 3),
            TestCase("small 7 1", Input(example_forest, 7, 1), 4),
            TestCase("small 1 2", Input(example_forest, 1, 2), 2),
        ]
        for c in cases:
            result = m.ride_toboggan(c.input.forest, c.input.nr_right,
                                     c.input.nr_down)
            self.assertEqual(result, c.want, c.name)


if __name__ == '__main__':
    unittest.main()
