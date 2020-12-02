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


if __name__ == '__main__':
    unittest.main()
