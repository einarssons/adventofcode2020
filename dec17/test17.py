import unittest

from dec17 import m17

example = '''\
.#.
..#
###'''


class Test17(unittest.TestCase):

    def test_example(self):
        grid = m17.Grid(example)
        self.assertEqual(len(grid.occ), 5, "Starting #")
        self.assertEqual(grid.bounding_box(),
                         m17.BoundingBox(0, 2, 0, 2, 0, 0), "Init bounding")

    def test_neigbor_count(self):
        grid = m17.Grid(example)
        self.assertEqual(grid.count_neighbors(m17.Box(1, 0, 0)), 3)

    def test_iterations(self):
        grid = m17.Grid(example)
        grid.iterate()
        self.assertEqual(len(grid.occ), 11)
        grid.iterate()
        self.assertEqual(len(grid.occ), 21)
        grid.iterate()
        grid.iterate()
        grid.iterate()
        grid.iterate()
        self.assertEqual(len(grid.occ), 112)

    def test_iterations4D(self):
        grid = m17.Grid4D(example)
        for _ in range(6):
            grid.iterate()
        self.assertEqual(len(grid.occ), 848)
