import unittest

import m12

example = '''\
F10
N3
F7
R90
F11'''


class Test12(unittest.TestCase):

    def test_example(self):
        instructions = example.splitlines()
        ship = m12.Ship()
        for instr in instructions:
            ship.move(instr)
        self.assertEqual(ship.position, [17, -8], "Ship position")

    def test_waypoint(self):
        instructions = example.splitlines()
        ship = m12.ShipWithWaypoint()
        for instr in instructions:
            ship.move(instr)
        self.assertEqual(ship.position, [214, -72], "Ship with waypoint")


if __name__ == "__main__":
    unittest.main()
