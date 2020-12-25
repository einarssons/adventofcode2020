import unittest
from dec25 import m25


class Test25(unittest.TestCase):

    def testExample(self):
        public_keys = [5764801, 17807724]
        secret = m25.get_secret(public_keys)
        self.assertEqual(secret[0], secret[1])
        self.assertEqual(secret[0], 14897079)