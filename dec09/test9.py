import unittest

import m9

test_numbers = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576\
'''.splitlines()


class Test8(unittest.TestCase):

    def test_find_first_bad_number(self):
        numbers = [int(nr) for nr in test_numbers]
        bad = m9.find_first_bad_number(numbers, 5)
        self.assertEqual(bad, 127)

    def test_find_holy_range(self):
        numbers = [int(nr) for nr in test_numbers]
        holy_range = m9.find_holy_range(numbers, 127)
        self.assertEqual(holy_range, [15, 25, 47, 40])
        self.assertEqual(max(holy_range) + min(holy_range), 62)

if __name__ == '__main__':
    unittest.main()
