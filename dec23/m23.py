class Game:

    def __init__(self, cup_list: [int]):
        self.list = cup_list
        self.available_values = self.list[:]
        self.available_values.sort()
        self.current = self.list[0]

    def turn(self):
        curr_index = self.list.index(self.current)
        self._shift_left(curr_index)
        # Now we have current at position 0
        pickup = self.list[1:4]
        self.list = [self.list[0]] + self.list[4:]
        dest = self._find_destination(self.current, pickup)
        dst_idx = self.list.index(dest)
        self.list = self.list[:dst_idx+1] + pickup + self.list[dst_idx+1:]
        curr_idx = self.list.index(self.current)
        new_curr_idx = (curr_idx + 1) % len(self.list)
        self.current = self.list[new_curr_idx]

    def get_labels(self):
        one_idx = self.list.index(1)
        tmp_list = self.list[one_idx:] + self.list[:one_idx]
        return "".join([str(nr) for nr in tmp_list[1:]])

    def get_two_cups(self):
        one_idx = self.list.index(1)
        tmp_list = self.list[one_idx:] + self.list[:one_idx]
        return tmp_list[1:3]

    def _shift_left(self, nr_steps: int):
        self.list = self.list[nr_steps:] + self.list[:nr_steps]

    def _find_destination(self, current: int, pickup: [int]) -> int:
        dest = current
        while True:
            dest -= 1
            if dest not in self.available_values:
                dest = self.available_values[-1]
            if dest in pickup or dest == self.current:
                continue
            return dest


class GameB:
    def __init__(self, cup_list: [int]):
        self.next = {}
        for i in range(len(cup_list) - 1):
            self.next[cup_list[i]] = cup_list[i + 1]
        self.next[cup_list[len(cup_list)-1]] = cup_list[0]
        self.min_value = min(cup_list)
        self.max_value = max(cup_list)
        self.current = cup_list[0]

    def turn(self):
        pick = self._pickup(self.current)
        dest = self._find_destination(self.current, pick)
        # Put pick after dest
        next_after = self.next[dest]
        self.next[dest] = pick[0]
        self.next[pick[-1]] = next_after
        self.current = self.next[self.current]

    def _pickup(self, current):
        pick = []
        next = self.next[current]
        pick.append(next)
        next = self.next[next]
        pick.append(next)
        next = self.next[next]
        pick.append(next)
        self.next[current] = self.next[pick[-1]]  # Point to after pick
        return pick

    def _find_destination(self, current, pick):
        dest = current
        while True:
            dest -= 1
            if dest < self.min_value:
                dest = self.max_value
            if dest in pick or dest == self.current:
                continue
            return dest

    def get_labels(self):
        next = self.next[1]
        order = []
        for _ in range(8):
            order.append(next)
            next = self.next[next]
        return "".join([str(nr) for nr in order])

    def get_two_cups(self):
        cup1 = self.next[1]
        cup2 = self.next[cup1]
        return cup1, cup2


def main():
    import time
    cup_list = [int(c) for c in '476138259']
    game = Game(cup_list)
    for _ in range(100):
        game.turn()
    print(f"A: The labels are {game.get_labels()}")

    cup_list = [int(c) for c in '476138259']
    cup_list += range(len(cup_list), 1_000_001)
    game = GameB(cup_list)
    start = time.time()
    for _ in range(10_000_000):
        game.turn()
    print(f"Time gone is {time.time() - start:.1f}s")
    print(f"B: The two cups are {game.get_two_cups()}")


if __name__ == "__main__":
    main()
