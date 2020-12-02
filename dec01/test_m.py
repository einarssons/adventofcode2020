import unittest

from collections import namedtuple

import m

TestCase = namedtuple("TestCase", "name input want")

class TestFuel(unittest.TestCase):

    def test2Elements(self):
        cases = [
            TestCase("example", [1721, 979, 366, 299, 675, 1456], 514579)
        ]
        for c in cases:
            result = m.expense(c.input, 2020)
            self.assertEqual(result, c.want, c.name)

    def test3Elements(self):
        cases = [
            TestCase("example", [1721, 979, 366, 299, 675, 1456], 241861950)
        ]
        for c in cases:
            result = m.expense3(c.input, 2020)
            self.assertEqual(result, c.want, c.name)


if __name__ == '__main__':
    unittest.main()