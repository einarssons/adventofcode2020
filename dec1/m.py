def expense(lst, wantsum):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == wantsum:
                return lst[i] * lst[j]


def expense3(lst, wantsum):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == wantsum:
                    return lst[i] * lst[j] * lst[k]


def main(file_name):
    with open(file_name) as ifh:
        input = []
        for line in ifh:
            number = int(line)
            input.append(number)
        print(expense(input, 2020))
        print(expense3(input, 2020))



if __name__ == "__main__":
    main("data.txt")