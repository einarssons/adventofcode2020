def read_groups(full_text: str) -> []:
    "Separate groups from newlines and join answers."
    lines = full_text.splitlines()
    groups = []
    group = []
    for line in lines:
        line = line.strip()
        if line != '':
            group += [line]
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups


def union_answers(group: list) -> int:
    answers = set()
    for person in group:
        person_answers = set(person)
        answers.update(person_answers)
    return len(answers)


def intersection_answers(group: list) -> int:
    answers = set(group[0])
    for person in group[1:]:
        person_answers = set(person)
        answers.intersection_update(person_answers)
    return len(answers)


def main():
    with open('answers.txt') as ifh:
        full_text = ifh.read()
    groups = read_groups(full_text)
    total_answers = 0
    for group in groups:
        total_answers += union_answers(group)
    total_answers2 = 0
    for group in groups:
        total_answers2 += intersection_answers(group)
    print(total_answers)
    print(f'answer 6b, {total_answers2}')


if __name__ == '__main__':
    main()
