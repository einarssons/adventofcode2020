
import unittest
import m11

seats = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


seats_round1 = '''\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''


seats_round2 = '''\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##'''

seats_line_1 = '''\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''

seats_line_2 = '''\
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#'''


class TestSeating(unittest.TestCase):

    def test_seating(self):
        start = seats
        seating = m11.Seating(start)
        seating.update()
        self.assertEqual(seating.pattern(), seats_round1, "After Step 1")
        seating.update()
        self.assertEqual(seating.pattern(), seats_round2, "After Step 2")
        nr_iterations = 2
        last_pattern = seating.pattern()
        while nr_iterations < 10000:
            seating.update()
            nr_iterations += 1
            if seating.pattern() == last_pattern:
                print(f"{nr_iterations} iterations\n")
                break
            last_pattern = seating.pattern()
        self.assertEqual(seating.occupied(), 37, "Occupied seats")

    def test_line_seating(self):
        seating = m11.Seating(seats)
        seating.update_line()
        self.assertEqual(seating.pattern(), seats_line_1, "seats_line_1")
        seating.update_line()
        self.assertEqual(seating.pattern(), seats_line_2, "seats_line_2")
        last_pattern = seating.pattern()
        nr_iterations = 2
        while nr_iterations < 10000:
            seating.update_line()
            nr_iterations += 1
            if seating.pattern() == last_pattern:
                print(f"{nr_iterations} iterations\n")
                break
            last_pattern = seating.pattern()
        self.assertEqual(seating.occupied(), 26, "Occupied seats")


if __name__ == "__main__":
    unittest.main()
