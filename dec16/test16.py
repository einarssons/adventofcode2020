import unittest
from dec16 import m16


class Test16(unittest.TestCase):

    def test_valid(self):
        ticket = m16.TicketInfo('dec16/example.txt')
        self.assertEqual(len(ticket.rules), 3, "len of rules")
        invalids = ticket.get_all_invalid()
        self.assertEqual(invalids, [4, 55, 12])

    def test_column_match(self):
        ticket = m16.TicketInfo('dec16/example2.txt')
        self.assertEqual(len(ticket.rules), 3, "len of rules")
        invalids = ticket.get_all_invalid()
        self.assertEqual(invalids, [])
        uc0 = ticket.find_unique_column(ticket.rules[0])
        self.assertEqual(uc0, -1, "uc0")
        uc1 = ticket.find_unique_column(ticket.rules[1])
        self.assertEqual(uc1, -1, "uc1")
        uc2 = ticket.find_unique_column(ticket.rules[2])
        self.assertEqual(uc2, 2, "uc2")

    def test_all_column_match(self):
        ticket = m16.TicketInfo('dec16/example2.txt')
        self.assertEqual(len(ticket.rules), 3, "len of rules")
        ticket.get_all_invalid()
        ticket.match_all_columns()
        self.assertEqual(ticket.rules[0].pos, 1, ticket.rules[0].name)
        self.assertEqual(ticket.rules[1].pos, 0, ticket.rules[1].name)
        self.assertEqual(ticket.rules[2].pos, 2, ticket.rules[2].name)


if __name__ == "__main__":
    unittest.main()
