import re
import math
from collections import namedtuple

tilePattern = re.compile(r'Tile (\d+):')

T = namedtuple("TState", "id orientation")
C = namedtuple('Categories', 'corners edges inner')

nr_transforms = 16

monster = '''\
                  #
#    ##    ##    ###
 #  #  #  #  #  #'''


def construct_monster_pattern() -> []:
    "Get index of # for monster"
    pattern = []
    for line in monster.splitlines():
        pattern.append([])
        for i, c in enumerate(line):
            if c == "#":
                pattern[-1].append(i)
    return pattern


def count_monsters(img: [str], monster: [str]) -> int:
    "Count monster. Don't care about overlap."
    monster_length = max([max(line) for line in monster]) + 1
    monster_height = len(monster)
    monster_count = 0
    for i in range(len(img[0]) - monster_height):
        for j in range(len(img) - monster_length):
            is_monster = True
            for m_i, monster_hashes in enumerate(monster):
                for m_j in monster_hashes:
                    if img[i + m_i][j + m_j] != "#":
                        is_monster = False
                        break
                if not is_monster:
                    break
            if is_monster:
                monster_count += 1

    return monster_count


def three_rotations(edges: [str]) -> [str]:
    "Rotate 4 edges by 90, 180, 270 degrees."
    out = []
    out.append(edges[3][::-1])  # left to top, reverse
    out.append(edges[0])  # top to right
    out.append(edges[1][::-1])  # right to bottom, reverse
    out.append(edges[2])  # bottom to left
    out.append(out[3][::-1])  # left to top, reverse
    out.append(out[0])  # top to right
    out.append(out[1][::-1])  # right to bottom, reverse
    out.append(out[2])  # bottom to left
    out.append(out[7][::-1])  # left to top, reverse
    out.append(out[4])  # top to right
    out.append(out[5][::-1])  # right to bottom, reverse
    out.append(out[6])  # bottom to left
    return out


def transform_image(img: [str], orientation: int) -> [str]:
    def rotate90(img: [str]) -> [str]:
        dim = len(img[0])
        out = []
        for i in range(dim):
            row = []
            for j in range(dim - 1, -1, -1):
                row += img[j][i]
            out.append("".join(row))
        return out

    def swap_vertical(img: [str]) -> [str]:
        out = []
        for row in img:
            out.append(row[::-1])
        return out

    def swap_horizontal(img: [str]) -> [str]:
        return img[::-1]

    mirror, rotate = divmod(orientation, 4)
    if mirror == 1:
        img = swap_vertical(img)
    elif mirror == 2:
        img = swap_horizontal(img)
    elif mirror == 3:
        img = swap_vertical(img)
        img = swap_horizontal(img)
    for i in range(rotate):
        img = rotate90(img)
    return img


def count_hashes(img: [str]) -> int:
    count = 0
    for line in img:
        count += line.count("#")
    return count


class Tile:

    def __init__(self, id: int, pattern: [str]):
        self.id = id
        self.pattern = pattern
        self.nr_unique_sides = 0
        self._edges = []  # top, right, bottom, left
        self._edgepatterns = None  # Set of all edgepattens
        self.calc_edges()

    def calc_edges(self):
        top = self.pattern[0]
        right = "".join([line[-1] for line in self.pattern])
        bottom = self.pattern[-1]
        left = "".join([line[0] for line in self.pattern])
        self._edges.append(top)
        self._edges.append(right)
        self._edges.append(bottom)
        self._edges.append(left)
        self._edges.extend(three_rotations(self._edges[-4:]))
        # Flip across vertical line
        self._edges.append(top[::-1])
        self._edges.append(left)
        self._edges.append(bottom[::-1])
        self._edges.append(right)
        self._edges.extend(three_rotations(self._edges[-4:]))
        # Flip across horizontal line
        self._edges.append(bottom)
        self._edges.append(right[::-1])
        self._edges.append(top)
        self._edges.append(left[::-1])
        self._edges.extend(three_rotations(self._edges[-4:]))
        # Flip both
        self._edges.append(bottom[::-1])
        self._edges.append(left[::-1])
        self._edges.append(top[::-1])
        self._edges.append(right[::-1])
        self._edges.extend(three_rotations(self._edges[-4:]))
        # Set of all edge_patterns
        self._edgepatterns = set(self._edges)

    def edge(self, nr: int, orientation: int) -> int:
        "Get edge nr for one of 16 orientations"
        edge = self._edges[4 * orientation + nr]
        return edge

    def has_matching_edge(self, edge: int) -> bool:
        return edge in self._edgepatterns

    def transformed_image(self, orientation) -> str:
        "Get array of rows with transformed image."
        img = self.pattern

        img = transform_image(img, orientation)
        assert img[0] == self.edge(0, orientation)
        assert "".join(row[-1] for row in img) == self.edge(1, orientation)
        assert img[-1] == self.edge(2, orientation)
        assert "".join(row[0] for row in img) == self.edge(3, orientation)

        # Trim away the borders
        out_img = img[1:-1]
        out_img = [row[1:-1] for row in out_img]
        return out_img


def can_place_tile(tile_id, orientation, i, j, partial_board, side_len,
                   tiles) -> bool:
    "Place and return success after checking neighbors to left and top."
    tile = tiles[tile_id]
    if i > 0:
        neighbor = partial_board[(i-1) * side_len + j]
        n_tile = tiles[neighbor.id]
        n_orientation = neighbor.orientation
        if tile.edge(0, orientation) != n_tile.edge(2, n_orientation):
            return False
    if j > 0:
        neighbor = partial_board[i * side_len + j - 1]
        n_tile = tiles[neighbor.id]
        n_orientation = neighbor.orientation
        if tile.edge(3, orientation) != n_tile.edge(1, n_orientation):
            return False
    return True


def may_match(tile_id, i, j, partial_board, side_len, tiles) -> bool:
    "Check if tile has matching edges compared to neighbors"
    tile = tiles[tile_id]
    if i > 0:
        neighbor = partial_board[(i-1) * side_len + j]
        n_tile = tiles[neighbor.id]
        neigbor_edge = n_tile.edge(2, neighbor.orientation)
        if not tile.has_matching_edge(neigbor_edge):
            return False
    if j > 0:
        neighbor = partial_board[i * side_len + j - 1]
        n_tile = tiles[neighbor.id]
        neigbor_edge = n_tile.edge(1, neighbor.orientation)
        if not tile.has_matching_edge(neigbor_edge):
            return False
    return True


def place_tiles(tiles: {}, cat_tiles: C, board_size:  int) -> [T]:
    side_len = int(math.sqrt(board_size))
    partial_board = []

    tile_id = cat_tiles.corners[0]
    new_cat_tiles = C(cat_tiles.corners[:], cat_tiles.edges[:],
                      cat_tiles.inner[:])
    new_cat_tiles.corners.remove(tile_id)
    for orientation in range(nr_transforms):
        partial_board = [T(tile_id, orientation)]
        board = place_more_tiles(tiles, new_cat_tiles,
                                 partial_board, side_len)
        if board is not None:
            return board
    return None


def place_more_tiles(tiles, cat_tiles, partial_board, side_len):
    def is_corner(i, j, side_len):
        return i in (0, side_len - 1) and j in (0, side_len - 1)

    def is_side(i, j, side_len):
        return i in (0, side_len - 1) or j in (0, side_len - 1)

    i, j = divmod(len(partial_board), side_len)
    if is_corner(i, j, side_len):
        tile_list = cat_tiles.corners
    elif is_side(i, j, side_len):
        tile_list = cat_tiles.edges
    else:
        tile_list = cat_tiles.inner
    for tile_id in tile_list:
        if not may_match(tile_id, i, j, partial_board, side_len, tiles):
            continue
        for orientation in range(nr_transforms):
            if can_place_tile(tile_id, orientation, i, j,
                              partial_board, side_len, tiles):
                new_partial_board = partial_board[:]
                new_partial_board.append(T(tile_id, orientation))
                if len(new_partial_board) == len(tiles):
                    return new_partial_board
                new_cat_tiles = C(cat_tiles.corners[:], cat_tiles.edges[:],
                                  cat_tiles.inner[:])
                if is_corner(i, j, side_len):
                    new_cat_tiles.corners.remove(tile_id)
                elif is_side(i, j, side_len):
                    new_cat_tiles.edges.remove(tile_id)
                else:
                    new_cat_tiles.inner.remove(tile_id)
                board = place_more_tiles(tiles, new_cat_tiles,
                                         new_partial_board, side_len)
                if board is not None:
                    return board
    return None


def read_tiles(data: str) -> {int: Tile}:
    lines = str.splitlines(data)
    nr = 0
    plines = []
    tiles = {}
    for line in lines:
        mobj = tilePattern.match(line)
        if mobj:
            nr = int(mobj.group(1))
        elif line == "":
            tile = Tile(nr, plines)
            plines = []
            tiles[nr] = tile
        else:
            plines.append(line)
    if len(plines) > 0:  # last tile
        tile = Tile(nr, plines)
        tiles[nr] = tile
    return tiles


def find_unique_sides(tiles: {str: Tile}) -> C:
    "Find tiles with two (corners) or one (edges) sides."
    idx_list = list(tiles.keys())
    categories = C([], [], [])
    for idx in idx_list:
        other_idx = idx_list[:]
        other_idx.remove(idx)
        tile = tiles[idx]
        nr_unique_sides = 0
        for i in range(4):
            side = tile.edge(i, 0)
            for idx2 in other_idx:
                tile2 = tiles[idx2]
                if tile2.has_matching_edge(side):
                    break
            else:
                nr_unique_sides += 1
        if nr_unique_sides == 2:
            categories.corners.append(idx)
        elif nr_unique_sides == 1:
            categories.edges.append(idx)
        else:
            categories.inner.append(idx)
    return categories


class Image:

    def __init__(self, data: [str]):
        self.img = data


def construct_image(board, tiles) -> [str]:
    board_side = int(math.sqrt(len(board)))
    nr_lines = 0

    out_lines = []
    for i, t in enumerate(board):
        tile = tiles[t.id]
        img = tile.transformed_image(t.orientation)

        if i % board_side == 0:
            nr_lines = len(img)
            new_lines = [""] * nr_lines
            out_lines.extend(new_lines)

        for j in range(nr_lines):
            out_lines[-nr_lines+j] += img[j]
    return out_lines


def main():
    data = open('tiles.txt').read()
    tiles = read_tiles(data)
    cat_tiles = find_unique_sides(tiles)
    prod = 1
    for c in cat_tiles.corners:
        prod *= c
    print(f"Corner product is {prod}")
    board_size = len(tiles)
    board = place_tiles(tiles, cat_tiles, board_size)
    # print(board)

    img = construct_image(board, tiles)
    nr_hashes = count_hashes(img)
    monster = construct_monster_pattern()
    for rot in range(nr_transforms):
        rot_img = transform_image(img, rot)
        nr_monsters = count_monsters(rot_img, monster)
        if nr_monsters > 0:
            break
    print(f"Found {nr_monsters} monsters")
    water_roughness = nr_hashes - nr_monsters * 15  # hash in monster
    print(f"Water roughness is {water_roughness}")


if __name__ == "__main__":
    main()
