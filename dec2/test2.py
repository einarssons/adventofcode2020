import unittest

from collections import namedtuple

import m

TestCase = namedtuple("TestCase", "name input want")


class TestDec2(unittest.TestCase):

    def test_parse_line(self):
        cases = [
            TestCase("first_line", "1-3 a: abcde", {"min": 1, "max": 3, "char": "a", "pwd": "abcde"}),
        ]
        for c in cases:
            result = m.parse_line(c.input)
            self.assertEqual(result, c.want, c.name)


if __name__ == '__main__':
    unittest.main()