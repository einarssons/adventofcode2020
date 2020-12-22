
def parse_hands(data):
    hands = []
    for line in data.splitlines():
        if line.startswith('Player'):
            hand = []
            hands.append(hand)
        elif line == "":
            continue
        else:
            hand.append(int(line))
    return hands


def play_game(hands: []) -> []:
    while True:
        if min([len(hand) for hand in hands]) == 0:
            return hands
        if hands[0][0] > hands[1][0]:
            winner = 0
        else:
            winner = 1
        high = hands[winner].pop(0)
        hands[winner].append(high)
        low = hands[1-winner].pop(0)
        hands[winner].append(low)


def score(hand: [int]) -> int:
    nr = len(hand)
    sum = 0
    for i, h in enumerate(hand):
        sum += (nr-i) * h
    return sum


def signature(hands: []) -> str:
    both = [', '.join([str(h) for h in hand]) for hand in hands]
    return ' : '.join(both)


def recursive_game(hands: []) -> int:
    history = set()
    while True:
        if len(hands[1]) == 0:
            return 0
        if len(hands[0]) == 0:
            return 1
        hands_signature = signature(hands)
        if signature(hands) in history:
            return 0
        top = [hand.pop(0) for hand in hands]
        if top[0] > len(hands[0]) or top[1] > len(hands[1]):
            if top[0] > top[1]:
                winner = 0
            else:
                winner = 1
        else:
            winner = recursive_game([hands[0][:top[0]], hands[1][:top[1]]])
        hands[winner].append(top[winner])
        hands[winner].append(top[1-winner])
        history.add(hands_signature)


def main():
    data = open('hands.txt').read()
    hands = parse_hands(data)
    hands = play_game(hands)
    if len(hands[0]) == 0:
        print(f"Winning score A is {score(hands[1])}")
    else:
        print(f"Winning score A is {score(hands[0])}")
    hands = parse_hands(data)
    winner = recursive_game(hands)
    winning_hand = hands[winner]
    print(f"Winning score B is {score(winning_hand)}")


if __name__ == "__main__":
    main()

