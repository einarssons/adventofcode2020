class Seating:
    def __init__(self, layout: str):
        self.seats = [list(line) for line in layout.splitlines()]
        self.width = len(self.seats[0])
        self.height = len(self.seats)

    def nr_neigbors(self, row: int, col: int) -> int:
        count = 0
        for i in range(max(row - 1, 0), min(row+2, self.height)):
            for j in range(max(col-1, 0), min(col+2, self.width)):
                if i == row and j == col:
                    continue
                if self.seats[i][j] == "#":
                    count += 1
        return count

    def update(self):
        new_seats = [['']*self.width for row in self.seats]
        for i in range(self.height):
            for j in range(self.width):
                if self.seats[i][j] == "L":
                    if self.nr_neigbors(i, j) == 0:
                        new_seats[i][j] = "#"
                elif self.seats[i][j] == "#":
                    if self.nr_neigbors(i, j) >= 4:
                        new_seats[i][j] = "L"
                if new_seats[i][j] == '':
                    new_seats[i][j] = self.seats[i][j]
        self.seats = new_seats

    def update_line(self):
        new_seats = [['']*self.width for row in self.seats]
        for i in range(self.height):
            for j in range(self.width):
                if self.seats[i][j] == "L":
                    if self.nr_line_neigbors(i, j) == 0:
                        new_seats[i][j] = "#"
                elif self.seats[i][j] == "#":
                    if self.nr_line_neigbors(i, j) >= 5:
                        new_seats[i][j] = "L"
                if new_seats[i][j] == '':
                    new_seats[i][j] = self.seats[i][j]
        self.seats = new_seats

    def pattern(self) -> str:
        rows = ["".join(row) for row in self.seats]
        return "\n".join(rows)

    def occupied(self) -> int:
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.seats[i][j] == "#":
                    count += 1
        return count

    def nr_line_neigbors(self, row: int, col: int) -> int:
        count = 0
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1],
                      [-1, 0], [-1, -1], [0, -1], [1, -1]]
        for d in directions:
            for n in range(1, max(self.width, self.height)):
                r, c = row + n * d[0], col + n * d[1]
                if min(r, c) < 0:
                    break
                if r >= self.height or c >= self.width:
                    break
                v = self.seats[r][c]
                if v == '#':
                    count += 1
                    break
                if v == 'L':
                    break
        return count


def main():
    with open('seats.txt') as ifh:
        seating = Seating(ifh.read())
        nr_iterations = 0
        last_pattern = seating.pattern()
        while nr_iterations < 10000:
            seating.update()
            nr_iterations += 1
            if seating.pattern() == last_pattern:
                print(f"Nr iterations {nr_iterations}")
                break
            last_pattern = seating.pattern()
            if nr_iterations > 100000:
                print("Nr iterations is too big\n")
                break
        print("Number occupied seats is %d\n" % seating.occupied())

    with open('seats.txt') as ifh:
        seating = Seating(ifh.read())
        nr_iterations = 0
        last_pattern = seating.pattern()
        while nr_iterations < 10000:
            seating.update_line()
            nr_iterations += 1
            if seating.pattern() == last_pattern:
                print(f"Nr line iterations {nr_iterations}")
                break
            last_pattern = seating.pattern()
            if nr_iterations > 100000:
                print("Nr line iterations is too big\n")
                break
        print("Number line occupied seats is %d\n" % seating.occupied())


if __name__ == "__main__":
    main()
