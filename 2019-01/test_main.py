import unittest

from collections import namedtuple

from main import fuel

TestCase = namedtuple("TestCase", "name input want")

class TestFuel(unittest.TestCase):

    def testCases(self):
        cases = [
            TestCase("first", 10, 2)
        ]
        for c in cases:
            result = fuel(c.input)
            self.assertEqual(result, c.want, c.name)


if __name__ == '__main__':
    unittest.main()