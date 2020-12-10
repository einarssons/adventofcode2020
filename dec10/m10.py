from dataclasses import dataclass


@dataclass
class Steps():
    step1: int
    step2: int
    step3: int


def sorted_jolts(adapters: [int]) -> [int]:
    jolts = adapters[:]
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    return jolts


def find_jolt_steps(adapters: [int]) -> Steps:
    "Find a chain and return nr steps of 1 and nr steps of 3"
    jolts = sorted_jolts(adapters)
    steps = Steps(0, 0, 0)
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i-1]
        if diff == 1:
            steps.step1 += 1
        elif diff == 2:
            steps.step2 += 1
        elif diff == 3:
            steps.step3 += 1
        else:
            raise ValueError('Wrong Difference')
    return steps


def find_sequences(adapters: [int]) -> [int]:
    'Find and return all sequences of ones longer than one'
    jolts = sorted_jolts(adapters)
    current_nr_ones = 0
    sequence_lengths = []
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i-1]
        if diff == 1:
            current_nr_ones += 1
        else:
            if current_nr_ones > 1:
                sequence_lengths.append(current_nr_ones)
            current_nr_ones = 0
    return sequence_lengths


def find_combinations(sequences: [int]) -> int:
    'Find total combinations of a sequence. Works up to 8'
    combinations = 1
    for n in sequences:
        combinations *= 2 ** (n-1) - max(((n - 3) * (n - 2)) // 2, 0)
    return combinations


def main():
    with open('jolts.txt') as ifh:
        adapters = [int(jolt) for jolt in ifh.read().splitlines()]
        steps = find_jolt_steps(adapters)
        sequences = find_sequences(adapters)
        combinations = find_combinations(sequences)
        print(steps)
        print("The product of steps1 and steps3 is %d\n" %
              (steps.step1 * steps.step3))
        print("The sequences of more than one steps of 1 are: %s\n" %
              sequences)
        print("The number of adapter combinations is %d\n" % combinations)


if __name__ == '__main__':
    main()
