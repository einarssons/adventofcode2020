def calc_seat(code:str)->dict:
    row = 0
    for i, c in enumerate(code[:7]):
        if c == 'B':
            #row += 2 ** (6-i)
            row += 1 << (6-i)
    column = 0
    for i, c in enumerate(code[7:]):
        if c == 'R':
            #column += 2 ** (2-i)
            column += 1 << (2-i)
    seat = row * 8 + column
    return {'row':row, 'column':column, 'seat':seat}

def main():
    with open('seats.txt') as ifh:
        max_seat = 0
        seat_ids = []
        for line in ifh:
            line = line.strip()
            seat = calc_seat(line)
            seat_id = seat['seat']
            seat_ids.append(seat_id)
        seat_ids.sort()
        print(seat_ids[0], seat_ids[-1])
        all_seats = set(range(6, 952))
        all_boarding_passes = set(seat_ids)
        print(all_seats.difference(all_boarding_passes))

if __name__ == '__main__':
    main()