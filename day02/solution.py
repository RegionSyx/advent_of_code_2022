def test_example():
    example = """A Y
B X
C Z
"""

    output = solution1(example)

    assert output == 15


def test_example2():
    example = """A Y
B X
C Z
"""

    output = solution2(example)

    assert output == 12


def _calc_score(a: str, b: str):
    match (a, b):
        case ("A", "X"):
            return 1 + 3
        case ("A", "Y"):
            return 2 + 6
        case ("A", "Z"):
            return 3 + 0
        case ("B", "X"):
            return 1 + 0
        case ("B", "Y"):
            return 2 + 3
        case ("B", "Z"):
            return 3 + 6
        case ("C", "X"):
            return 1 + 6
        case ("C", "Y"):
            return 2 + 0
        case ("C", "Z"):
            return 3 + 3

    return 0


def _choose_move(a: str, r: str):
    match (a, r):
        case ("A", "X"):
            return "Z"
        case ("A", "Y"):
            return "X"
        case ("A", "Z"):
            return "Y"
        case ("B", "X"):
            return "X"
        case ("B", "Y"):
            return "Y"
        case ("B", "Z"):
            return "Z"
        case ("C", "X"):
            return "Y"
        case ("C", "Y"):
            return "Z"
        case ("C", "Z"):
            return "X"

    return None


def solution1(guide: str):
    score = 0
    for line in guide.splitlines():
        if line:
            [A, B] = line.split(" ")
            score += _calc_score(A, B)
    return score


def solution2(guide: str):
    score = 0
    for line in guide.splitlines():
        if line:
            [A, B] = line.split(" ")
            R = _choose_move(A, B)
            score += _calc_score(A, R)

    return score


if __name__ == "__main__":
    with open("./day02/input.txt") as f:
        print(solution1(f.read()))

    with open("./day02/input.txt") as f:
        print(solution2(f.read()))
