import unittest

from dec24 import m24

min_example = "nwwswee"

example = '''\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''


class Test24(unittest.TestCase):

    def test_min_example(self):
        fl = m24.Floor()
        fl.flip(min_example)
        self.assertEqual(fl.black_tiles, set([(0, 0)]))

    def test_example(self):
        fl = m24.Floor()
        instructions = example.splitlines()
        for instr in instructions:
            fl.flip(instr)
        self.assertEqual(fl.nr_black_tiles(), 10)

    def test_B(self):
        fl = m24.Floor()
        instructions = example.splitlines()
        for instr in instructions:
            fl.flip(instr)
        self.assertEqual(fl.nr_black_tiles(), 10)  # After day 0
        fl.new_day_pattern()
        self.assertEqual(fl.nr_black_tiles(), 15)  # After day 1 
        for _ in range(99):
            fl.new_day_pattern()
        self.assertEqual(fl.nr_black_tiles(), 2208, "Day 100")