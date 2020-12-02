import unittest

from collections import namedtuple

import m

TestCase = namedtuple("TestCase", "name input want")


class TestDec2(unittest.TestCase):

    def test_check_password(self):
        cases = [
            TestCase("valid pwd", {"min": 1, "max": 3, "char": "a", "pwd": "abcde"}, True),
            TestCase("non-valid pwd", {"min": 1, "max": 3, "char": "b", "pwd": "cdefg"}, False)
        ]
        for c in cases:
            d = c.input
            result = m.check_password(d["min"], d["max"], d["char"], d["pwd"])
            self.assertEqual(result, c.want, c.name)

    def test_parse_line(self):
        cases = [
            TestCase("first_line", "1-3 a: abcde", {"min": 1, "max": 3, "char": "a", "pwd": "abcde"}),
        ]
        for c in cases:
            result = m.parse_line(c.input)
            self.assertEqual(result, c.want, c.name)

    def test_check_password2(self):
        cases = [
            TestCase("case 1", {"min": 1, "max": 3, "char": "a", "pwd": "abcde"}, True),
            TestCase("case 2", {"min": 1, "max": 3, "char": "b", "pwd": "cdefg"}, False),
            TestCase("case 3", {"min": 2, "max": 9, "char": "c", "pwd": "ccccccccc"}, False)
        ]
        for c in cases:
            d = c.input
            result = m.check_password2(d["min"], d["max"], d["char"], d["pwd"])
            self.assertEqual(result, c.want, c.name)

if __name__ == '__main__':
    unittest.main()
