from collections import namedtuple
from dataclasses import dataclass

Box = namedtuple('Box', 'x y z')


@dataclass
class BoundingBox:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int


class Grid:

    def __init__(self, raw: str):
        self.occ = set()
        lines = raw.splitlines()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "#":
                    self.occ.add(Box(j, len(lines)-i-1, 0))

    def bounding_box(self):
        bb = None
        for occ in self.occ:
            if bb is None:
                bb = BoundingBox(occ.x, occ.x, occ.y, occ.y, occ.z, occ.z)
            if occ.x < bb.xmin:
                bb.xmin = occ.x
            if occ.x > bb.xmax:
                bb.xmax = occ.x
            if occ.y < bb.ymin:
                bb.ymin = occ.y
            if occ.y > bb.ymax:
                bb.ymax = occ.y
            if occ.z < bb.zmin:
                bb.zmin = occ.z
            if occ.z > bb.zmax:
                bb.zmax = occ.z
        return bb

    def count_neighbors(self, box: Box) -> int:
        neighbors = 0
        for x in range(box.x-1, box.x+2):
            for y in range(box.y-1, box.y+2):
                for z in range(box.z-1, box.z+2):
                    b = Box(x, y, z)
                    if b != box and b in self.occ:
                        neighbors += 1
        return neighbors

    def iterate(self):
        bb = self.bounding_box()
        next_occ = set()
        for x in range(bb.xmin-1, bb.xmax+2):
            for y in range(bb.ymin-1, bb.ymax+2):
                for z in range(bb.zmin-1, bb.zmax+2):
                    b = Box(x, y, z)
                    neighbors = self.count_neighbors(b)
                    if neighbors == 3:
                        next_occ.add(b)
                    elif b in self.occ and neighbors == 2:
                        next_occ.add(b)
        self.occ = next_occ


Box4D = namedtuple('Box4D', 'x y z w')


@dataclass
class BoundingBox4D:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int
    wmin: int
    wmax: int


class Grid4D:
    def __init__(self, raw: str):
        self.occ = set()
        lines = raw.splitlines()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "#":
                    self.occ.add(Box4D(j, len(lines)-i-1, 0, 0))

    def bounding_box(self):
        bb = None
        for occ in self.occ:
            if bb is None:
                bb = BoundingBox4D(occ.x, occ.x, occ.y, occ.y,
                                   occ.z, occ.z, occ.w, occ.w)
            if occ.x < bb.xmin:
                bb.xmin = occ.x
            if occ.x > bb.xmax:
                bb.xmax = occ.x
            if occ.y < bb.ymin:
                bb.ymin = occ.y
            if occ.y > bb.ymax:
                bb.ymax = occ.y
            if occ.z < bb.zmin:
                bb.zmin = occ.z
            if occ.z > bb.zmax:
                bb.zmax = occ.z
            if occ.w < bb.wmin:
                bb.wmin = occ.w
            if occ.w > bb.wmax:
                bb.wmax = occ.w
        return bb

    def count_neighbors(self, box: Box) -> int:
        neighbors = 0
        for x in range(box.x-1, box.x+2):
            for y in range(box.y-1, box.y+2):
                for z in range(box.z-1, box.z+2):
                    for w in range(box.w-1, box.w+2):
                        b = Box4D(x, y, z, w)
                        if b != box and b in self.occ:
                            neighbors += 1
        return neighbors

    def iterate(self):
        bb = self.bounding_box()
        next_occ = set()
        for x in range(bb.xmin-1, bb.xmax+2):
            for y in range(bb.ymin-1, bb.ymax+2):
                for z in range(bb.zmin-1, bb.zmax+2):
                    for w in range(bb.wmin-1, bb.wmax+2):
                        b = Box4D(x, y, z, w)
                        neighbors = self.count_neighbors(b)
                        if neighbors == 3:
                            next_occ.add(b)
                        elif b in self.occ and neighbors == 2:
                            next_occ.add(b)
        self.occ = next_occ


def main():
    start = open('start.txt').read()
    grid = Grid(start)
    for _ in range(6):
        grid.iterate()
    print(f"Nr active in 3D is {len(grid.occ)}")
    grid = Grid4D(start)
    for _ in range(6):
        grid.iterate()
    print(f"Nr active in 4D is {len(grid.occ)}")


if __name__ == "__main__":
    main()
