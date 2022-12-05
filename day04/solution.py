def test_example1():
    with open("./day04/example.txt") as f:
        example = f.read()

    output = solution1(example)

    assert output == 2

def test_example2():
    with open("./day04/example.txt") as f:
        example = f.read()

    output = solution2(example)

    assert output == 4

def solution1(l: str):
    result = 0
    for line in l.splitlines():
        [first, second] = line.split(',')
        [first_start, first_end] = first.split('-')
        [second_start, second_end] = second.split('-')

        first_assignments = set(range(int(first_start), int(first_end) + 1))
        second_assignments = set(range(int(second_start), int(second_end) + 1))
        if first_assignments.issubset(second_assignments) or second_assignments.issubset(first_assignments):
            result += 1

    return result

def solution2(l: str):
    result = 0
    for line in l.splitlines():
        [first, second] = line.split(',')
        [first_start, first_end] = first.split('-')
        [second_start, second_end] = second.split('-')

        first_assignments = set(range(int(first_start), int(first_end) + 1))
        second_assignments = set(range(int(second_start), int(second_end) + 1))
        if first_assignments.intersection(second_assignments):
            result += 1

    return result


if __name__ == "__main__":
    with open("./day04/input.txt") as f:
        print(solution1(f.read()))

    with open("./day04/input.txt") as f:
        print(solution2(f.read()))