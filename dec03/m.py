

def ride_toboggan(forest:str, nr_right:int, nr_down:int)->int:
    tree_rows = forest.splitlines()
    width = len(tree_rows[0])
    tree_crashes = 0
    for i, row_nr in enumerate(range(0, len(tree_rows), nr_down)):
        pos = (nr_right * i) % width
        if tree_rows[row_nr][pos] == "#":
            tree_crashes += 1
    return tree_crashes

tours = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
)

def main(file_name="forest.txt"):
    with open(file_name) as ifh:
        forest = ifh.read()
    n = 1
    for tour in tours:
        n *= ride_toboggan(forest, tour[0], tour[1])
    print(n)

if __name__ == '__main__':
    main('forest.txt')