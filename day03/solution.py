def test_example1():
    with open("./day03/example.txt") as f:
        example = f.read()

    output = solution1(example)

    assert output == 157

def test_example2():
    with open("./day03/example.txt") as f:
        example = f.read()

    output = solution2(example)

    assert output == 70

def solution1(contents: str):
    common_items = []
    for rucksack in contents.splitlines():
        N = len(rucksack)
        first_half, second_half = rucksack[:N//2], rucksack[N//2:]

        common_items.extend(list(set(first_half).intersection(set(second_half))))

    total = 0
    for item in common_items:
        ordinal = ord(item)
        if ordinal >= ord('a'):
            total += ordinal - ord('a') + 1
        else:
            total += ordinal - ord('A') + 1 + 26

    return total


def solution2(contents: str):
    items = []
    lines = contents.splitlines()
    for rucksacks in [lines[i:i+3] for i in range(0, len(lines), 3)]:
        common_items = set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2]))
        items.append(list(common_items)[0])

    total = 0
    for item in items:
        ordinal = ord(item)
        if ordinal >= ord('a'):
            total += ordinal - ord('a') + 1
        else:
            total += ordinal - ord('A') + 1 + 26

    return total


if __name__ == "__main__":
    with open("./day03/input.txt") as f:
        print(solution1(f.read()))

    with open("./day03/input.txt") as f:
        print(solution2(f.read()))