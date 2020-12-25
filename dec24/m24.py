class Floor:

    def __init__(self):
        self.black_tiles = set()  # tile is tuple, only include if turned

    def flip(self, path: str):
        pos = [0, 0]
        while len(path) > 0:
            odd = 1 if pos[1] & 1 == 1 else 0
            if path.startswith("e"):
                pos[0] += 1
                path = path[1:]
            elif path.startswith("w"):
                pos[0] -= 1
                path = path[1:]
            elif path.startswith("se"):
                pos[0] += 1 - odd
                pos[1] -= 1
                path = path[2:]
            elif path.startswith("ne"):
                pos[0] += 1 - odd
                pos[1] += 1
                path = path[2:]
            elif path.startswith("sw"):
                pos[0] -= odd
                pos[1] -= 1
                path = path[2:]
            elif path.startswith("nw"):
                pos[0] -= odd
                pos[1] += 1
                path = path[2:]
            else:
                raise ValueError("Bad input %s", path)
        tile = (pos[0], pos[1])
        if tile in self.black_tiles:
            self.black_tiles.remove(tile)  # Flip back
        else:
            self.black_tiles.add(tile)

    def new_day_pattern(self) -> set:
        "Complete new day pattern"
        new_black_tiles = set()
        for tile in self.black_tiles:
            if 1 <= self.nr_black_neighbors(tile) <= 2:
                new_black_tiles.add(tile)
            ngbrs = self.neighbors(tile)
            for ngbr in ngbrs:
                if ngbr not in self.black_tiles:
                    if self.nr_black_neighbors(ngbr) == 2:
                        new_black_tiles.add(ngbr)
        self.black_tiles = new_black_tiles

    def nr_black_tiles(self) -> int:
        return len(self.black_tiles)

    def neighbors(self, pos) -> []:
        ngbrs = []
        ngbrs.append((pos[0] + 1, pos[1]))  # e
        ngbrs.append((pos[0] - 1, pos[1]))  # w
        odd = 1 if pos[1] & 1 == 1 else 0
        ngbrs.append((pos[0] + 1 - odd, pos[1] - 1))  # se
        ngbrs.append((pos[0] + 1 - odd, pos[1] + 1))  # ne
        ngbrs.append((pos[0] - odd, pos[1] - 1))  # sw
        ngbrs.append((pos[0] - odd, pos[1] + 1))  # nw
        return ngbrs

    def nr_black_neighbors(self, pos) -> int:
        nr_ngbr = 0
        for ngbr in self.neighbors(pos):
            if ngbr in self.black_tiles:
                nr_ngbr += 1
        return nr_ngbr


def main():
    paths = open("tiles.txt").read().splitlines()
    floor = Floor()
    for path in paths:
        floor.flip(path)
    print(f"A: nr black tiles is {floor.nr_black_tiles()}")
    for _ in range(100):
        floor.new_day_pattern()
    print(f"B: nr black tiles is {floor.nr_black_tiles()}")


if __name__ == "__main__":
    main()
