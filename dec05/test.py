import unittest
from collections import namedtuple

import m

TestCase = namedtuple("Case", ["code", "row", "column", "seat"])

class TestDec5(unittest.TestCase):

    def test_codes(self):
        cases = [
            TestCase("BFFFBBFRRR", 70, 7, 567),
            TestCase("FFFBBBFRRR", 14, 7, 119),
            TestCase("BBFFBBFRLL", 102, 4, 820)
        ]
        for c in cases:
            result = m.calc_seat(c.code)
            self.assertEqual(result["row"], c.row, c)
            self.assertEqual(result["column"], c.column, c)
            self.assertEqual(result["seat"], c.seat, c)


if __name__ == '__main__':
    unittest.main()
