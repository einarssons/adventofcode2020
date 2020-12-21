import unittest
from dec20 import m20

example = '''\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''

image = '''\
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###'''


class Test20(unittest.TestCase):

    def test_read_tiles(self):
        tiles = m20.read_tiles(example)
        self.assertEqual(len(tiles), 9, "nr tiles")

    def test_place_tiles(self):
        tiles = m20.read_tiles(example)
        cat_tiles = m20.find_unique_sides(tiles)
        board_size = len(tiles)
        board = m20.place_tiles(tiles, cat_tiles, board_size)
        print(board)
        self.assertEqual(board[0].id * board[3-1].id *
                         board[-3].id * board[-1].id, 20899048083289)
        img = m20.construct_image(board, tiles)
        img = "\n".join(img)
        print(img)

    def test_find_unique(self):
        tiles = m20.read_tiles(example)
        cat = m20.find_unique_sides(tiles)
        self.assertEqual(len(cat.corners), 4, "corners")
        self.assertEqual(len(cat.edges), 4, "edges")
        self.assertEqual(len(cat.inner), 1, "edges")

    def test_output_image(self):
        "Check image output using builtin asserts"
        tiles = m20.read_tiles(example)
        a_tile = list(tiles.values())[0]
        for i in range(m20.nr_transforms):
            a_tile.transformed_image(i)

    def test_monster_count(self):
        img = image.splitlines()
        nr_hashes = m20.count_hashes(img)
        monster = m20.construct_monster_pattern()
        for rot in range(m20.nr_transforms):
            rot_img = m20.transform_image(img, rot)

            nr_monsters = m20.count_monsters(rot_img, monster)
            if nr_monsters > 0:
                break
        self.assertEqual(nr_monsters, 2, "Nr monsters")
        water_roughness = nr_hashes - nr_monsters * 15  # hash in monster
        self.assertEqual(water_roughness, 273, "roughness")
