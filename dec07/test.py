import unittest
from collections import namedtuple

import m

test_rules = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.\
'''.splitlines()

parsed_rules = [
    m.Rule('light red', [(1, 'bright white'), (2, 'muted yellow')]),
    m.Rule('dark orange', [(3, 'bright white'), (4, 'muted yellow')]),
    m.Rule('bright white', [(1, 'shiny gold')]),
    m.Rule('muted yellow', [(2, 'shiny gold'), (9,  'faded blue')]),
    m.Rule('shiny gold', [(1, 'dark olive'), (2, 'vibrant plum')]),
    m.Rule('dark olive', [(3, 'faded blue'), (4, 'dotted black')]),
    m.Rule('vibrant plum', [(5, 'faded blue'), (6, 'dotted black')]),
    m.Rule('faded blue', []),
    m.Rule('dotted black', [])
]

test_rules2 = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.\
'''.splitlines()


TestCase = namedtuple("TestCase", ["text", "output"])


class TestDec7(unittest.TestCase):

    def test_parse_rules(self):
        for i, raw_rule in enumerate(test_rules):
            parsed_rule = m.parse_rule(raw_rule)
            self.assertEqual(parsed_rule, parsed_rules[i], raw_rule)

    def test_find_containers(self):
        rules = [m.parse_rule(raw_rule) for raw_rule in test_rules]
        containers = m.find_containers("shiny gold", rules)
        self.assertEqual(len(containers), 4, containers)

    def test_count_subs(self):
        rules = [m.parse_rule(raw_rule) for raw_rule in test_rules2]
        rulesdict = dict(rules)
        count = m.count_subs('shiny gold', rulesdict)
        count -= 1  # Don't count top bag
        self.assertEqual(count, 126)


if __name__ == '__main__':
    unittest.main()
