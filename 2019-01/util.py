def readNumbers(fileName):
    numbers = []
    with open(fileName) as ifh:
        for line in ifh:
            nr = int(line)
            numbers.append(nr)
    return numbers

