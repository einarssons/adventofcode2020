from dataclasses import dataclass
import re

rule_pattern = re.compile(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")
ticket_pattern = re.compile(r"[0-9,]+$")


class TicketInfo:

    def __init__(self, file_name: str):
        self.rules = []
        self.all_tickets = []  # my ticket is 0
        self.columns_mapped = set()
        self.nr_columns = 0
        self.read_data(file_name)

    def read_data(self, filename: str):
        with open(filename) as ifh:
            for line in ifh:
                line = line.strip()
                m = rule_pattern.match(line)
                if m:
                    name = m.group(1)
                    self.rules.append(Rule(name,
                                           (int(m.group(2)), int(m.group(3))),
                                           (int(m.group(4)), int(m.group(5))),
                                           -1))
                m = ticket_pattern.match(line)
                if m:
                    self.all_tickets.append(read_ticket(line))
            self.nr_columns = len(self.all_tickets[0])

    def get_all_invalid(self):
        invalid_indices = []
        all_invalid = []
        for i, ticket in enumerate(self.all_tickets):
            for nr in ticket:
                valid = False
                for rule in self.rules:
                    if rule.is_valid(nr):
                        valid = True
                        break
                if not valid:
                    all_invalid.append(nr)
                    invalid_indices.append(i)
        invalid_indices.reverse()
        print(f"There are {len(invalid_indices)} invalid tickets")
        for idx in invalid_indices:
            self.all_tickets.pop(idx)
        return all_invalid

    def free_columns(self) -> set():
        return set(range(self.nr_columns)).difference(self.columns_mapped)

    def find_unique_column(self, rule) -> int:
        possible_columns = set()
        free_columns = self.free_columns()
        for column in free_columns:
            for ticket in self.all_tickets:
                if not rule.is_valid(ticket[column]):
                    break
            else:
                possible_columns.add(column)
                if len(possible_columns) > 1:
                    return -1
        if len(possible_columns) == 0:
            raise ValueError(f"No column possible for {rule}")
        return possible_columns.pop()

    def match_all_columns(self):
        nr_loops = 0
        while len(self.free_columns()) > 0:
            for rule in self.rules:
                if rule.pos >= 0:
                    continue
                uc = self.find_unique_column(rule)
                if uc >= 0:
                    rule.pos = uc
                    self.columns_mapped.add(uc)
            nr_loops += 1
            if nr_loops % 100 == 0:
                print(f"Looped {nr_loops} times")


def read_ticket(line: str) -> [int]:
    return [int(x) for x in line.split(",")]


@dataclass
class Rule:
    name: str
    iv1: (int, int)
    iv2: (int, int)
    pos: int

    def is_valid(self, nr: int):
        return ((self.iv1[0] <= nr <= self.iv1[1]) or
                (self.iv2[0] <= nr <= self.iv2[1]))


def main():
    ti = TicketInfo("tickets.txt")
    invalid = ti.get_all_invalid()
    print(f"The sum is {sum(invalid)}")
    ti.match_all_columns()
    your_ticket = ti.all_tickets[0]
    prod = 1
    for rule in ti.rules:
        if rule.name.startswith('departure'):
            prod *= your_ticket[rule.pos]
    print(f"The departure product is {prod}")


if __name__ == "__main__":
    main()
