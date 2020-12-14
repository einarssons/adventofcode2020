import unittest
from collections import namedtuple
from dec13 import m13

short_data = '''\
939
7,13,x,x,59,x,31,19'''

SequenceTestCase = namedtuple('Sequence', ['buses', 'timestamp'])


class TestDec13(unittest.TestCase):

    def test_get_time_and_buses(self):
        now, buses = m13.get_time_and_buses(short_data)
        self.assertEqual(now, 939, "time")
        self.assertEqual(buses, [7, 13, 59, 31, 19], "buses")

    def test_earliest_bus(self):
        now, buses = m13.get_time_and_buses(short_data)
        waiting_time, bus = m13.get_waiting_time_and_bus(now, buses)
        self.assertEqual((waiting_time, bus), (5, 59), "wait time + bus")

    def test_get_bus_with_pairs(self):
        self.assertEqual(m13.get_buses_w_pos('67,x,7'),
                         [m13.BusWithPos(67, 0), m13.BusWithPos(7, 2)])

    def test_magic_sequence(self):
        cases = [
            SequenceTestCase('7,13,x,x,59,x,31,19', 1068781),
            SequenceTestCase('67,7,59,61', 754018),
            SequenceTestCase('67,x,7,59,61', 779210),
            SequenceTestCase('67,7,x,59,61', 1261476),
            SequenceTestCase('1789,37,47,1889', 1202161486)
        ]
        for case in cases:
            bwp = m13.get_buses_w_pos(case.buses)
            timestamp = m13.find_sequence_start(bwp)
            self.assertEqual(timestamp, case.timestamp, case.buses)


if __name__ == "__main__":
    unittest.main()
