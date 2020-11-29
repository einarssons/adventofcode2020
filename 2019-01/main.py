from util import readNumbers

def fuel(mass):
    return mass//3 -2

def main():
    numbers = readNumbers("data.txt")
    sum = 0
    for mass in numbers:
        sum += fuel(mass)
    print(sum)


if __name__ == "__main__":
    main()