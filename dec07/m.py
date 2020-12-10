
import re

from collections import namedtuple

Rule = namedtuple('Rule', ['bag', 'subs'])
Sub = namedtuple('Sub', ['nr', 'bag'])


def parse_rule(rule_line: str) -> Rule:
    mobj = re.match(r"(\w+ \w+) bags contain", rule_line)
    if mobj is None:
        raise ValueError("No initial color")
    bag = mobj.group(1)
    rest_of_line = rule_line[len(mobj.group(0)):]
    subs = []
    for mobj in re.finditer(r" (\d+) (\w+ \w+) bags?[,.]", rest_of_line):
        subs.append(Sub(int(mobj.group(1)), mobj.group(2)))
    return Rule(bag, subs)


def find_containers(bag: str, rules: []) -> []:
    outers = set()
    cores = [bag]
    while True:
        try:
            core = cores.pop()
        except IndexError:
            break
        for rule in rules:
            if rule.bag in outers:
                continue
            for sub in rule.subs:
                if sub.bag == core:
                    cores.append(rule.bag)
        if core != bag:
            outers.add(core)
    return outers


def count_subs(bag: str, rules: dict) -> int:
    count = 1
    subs = rules[bag]
    for sub in subs:
        count += count_subs(sub.bag, rules) * sub.nr
    return count


def main():
    with open('rules.txt') as ifh:
        lines = ifh.read().splitlines()
        rules = [parse_rule(raw_rule) for raw_rule in lines]
        containers = find_containers('shiny gold', rules)
        rulesdict = dict(rules)
        count = count_subs('shiny gold', rulesdict)
        count -= 1  # Don't count top bag
        print(len(containers))
        print(count)


if __name__ == "__main__":
    main()
