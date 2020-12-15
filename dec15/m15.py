class MagicList():

    def __init__(self, start_list: [int]):
        self.pos = 0
        self.prev_nr = {}
        self.last_nr = start_list[0]
        for nr in start_list[1:]:
            self.prev_nr[self.last_nr] = self.pos
            self.last_nr = nr
            self.pos += 1

    def add_nr(self, nr: int):
        self.prev_nr[self.last_nr] = self.pos
        self.last_nr = nr
        self.pos += 1

    def step(self) -> (int, int):
        new_nr = 0
        if self.last_nr in self.prev_nr:
            new_nr = self.pos - self.prev_nr[self.last_nr]
        self.add_nr(new_nr)
        return (new_nr, self.pos+1)

    def run_until_turn(self, stop_turn: int) -> int:
        while True:
            nr, turn = self.step()
            if turn == stop_turn:
                return nr


def main():
    start_list = [0, 8, 15, 2, 12, 1, 4]
    magic_list = MagicList(start_list)
    nr = magic_list.run_until_turn(2020)
    print(f"Answer A 2020: {nr}")

    magic_list = MagicList(start_list)
    nr = magic_list.run_until_turn(30000000)
    print(f"Answer B 30000000: {nr}")


if __name__ == "__main__":
    main()
