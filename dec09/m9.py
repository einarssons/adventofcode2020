def find_first_bad_number(numbers: [int], window: int) -> int:
    for i in range(window, len(numbers)):
        target = numbers[i]
        found = False
        for j in range(i-window, i):
            term1 = numbers[j]
            for k in range(j+1, i):
                term2 = numbers[k]
                if term1 + term2 == target:
                    found = True
                    break
            if found:
                break
        if not found:
            return target
    return -1


def find_holy_range(numbers: [int], target: int) -> list:
    for i in range(len(numbers)):
        sum = 0
        for j in range(i, len(numbers)):
            sum += numbers[j]
            if sum == target:
                return numbers[i:j+1]
            if sum > target:
                break
    return []


def main():
    with open('numbers.txt') as ifh:
        numbers = [int(nr) for nr in ifh.read().splitlines()]
        first_bad = find_first_bad_number(numbers, 25)
        holy_range = find_holy_range(numbers, first_bad)
        holy_sum = max(holy_range) + min(holy_range)
        print(f'first bad, {first_bad}')
        print(f'Le holy sum, {holy_sum}')


if __name__ == '__main__':
    main()
