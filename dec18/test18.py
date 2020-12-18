import unittest

from dec18 import m18

from collections import namedtuple

TestCase = namedtuple('TestCase', 'expr res')

TestCases = [
    TestCase('1 + 2 * 3 + 4 * 5 + 6', 71),
    TestCase('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)
]


class Test18(unittest.TestCase):

    def test_expr(self):
        for tc in TestCases:
            self.assertEqual(m18.evaluate(tc.expr), tc.res, tc.expr)


if __name__ == "__main__":
    unittest.main()
