from dataclasses import dataclass
from functools import reduce


@dataclass
class BusWithPos:
    bus: int
    pos: int


def get_time_and_buses(data: str) -> (int, []):
    lines = data.splitlines()
    now = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != "x"]
    return now, buses


def get_waiting_time_and_bus(now: int, buses: []) -> (int, int):
    min_wait_time = max(buses)
    best_bus = -1
    for bus in buses:
        wait_time = (bus - now % bus) % bus
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            best_bus = bus
    return min_wait_time, best_bus


def get_buses_w_pos(buses: str) -> [BusWithPos]:
    bwp = []
    for i, bus in enumerate(buses.split(',')):
        if bus != "x":
            bwp.append(BusWithPos(int(bus), i % int(bus)))
    return bwp


def gcd(a: int, b: int) -> int:
    "Greatest common divisor."
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def find_sequence_start0(buses_with_pos: [BusWithPos]) -> int:
    all_coprime = True
    for i, bwp in enumerate(buses_with_pos):
        for bwp2 in buses_with_pos[i+1:]:
            if gcd(bwp.bus, bwp2.bus) != 1:
                all_coprime = False
    if not all_coprime:
        raise ValueError("All are not coprime")
    print(buses_with_pos)
    max_bus = buses_with_pos[0]
    for bwp in buses_with_pos:
        if bwp.bus >= max_bus.bus:
            max_bus = bwp
    for n in range(100_000_000):
        seq_start = n * max_bus.bus - max_bus.pos
        for bwp in buses_with_pos:
            if (seq_start + bwp.pos) % bwp.bus != 0:
                break
        else:
            return seq_start
    raise ValueError("Did not find any start")
    return 0


def find_sequence_start(buses_with_pos: [BusWithPos]) -> int:
    all_coprime = True
    for i, bwp in enumerate(buses_with_pos):
        for bwp2 in buses_with_pos[i+1:]:
            if gcd(bwp.bus, bwp2.bus) != 1:
                all_coprime = False
    if not all_coprime:
        raise ValueError("All are not coprime")
    print(buses_with_pos)
    numbers = []
    remainders = []
    for bwp in buses_with_pos:
        numbers.append(bwp.bus)
        remainders.append((bwp.bus-bwp.pos) % bwp.bus)
    return chinese_remainder(numbers, remainders)


def chinese_remainder(numbers: [int], remainders: [int]) -> int:
    sum = 0
    prod = reduce(lambda a, b: a*b, numbers)
    for n_i, r_i in zip(numbers, remainders):
        p = prod // n_i
        sum += r_i * modular_inverse(p, n_i) * p
    return sum % prod


def modular_inverse(a: int, b: int) -> int:
    "Calculate the modular inverse a * ? = 1 mod b."
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    with open('input1.txt') as ifh:
        raw_data = ifh.read()
    now, buses = get_time_and_buses(raw_data)
    waiting_time, bus = get_waiting_time_and_bus(now, buses)
    prod = waiting_time * bus
    print(f"Bus {bus}, wait {waiting_time}, product {prod}")
    bwp = get_buses_w_pos(raw_data.splitlines()[1])
    timestamp = find_sequence_start(bwp)
    print(f'The magic timestamp is {timestamp}')


if __name__ == "__main__":
    main()
