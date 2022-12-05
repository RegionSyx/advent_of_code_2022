def test_simple_case():
    calories = """1
    """

    assert solution1(calories) == (1, 1)


def test_multiple_case():
    calories = """1

    2
    3
    """

    assert solution1(calories) == (2, 5)


def test_complex_case():
    calories = """1

    2
    3

    12000

    3
    4
    5
    6
    67
    """

    assert solution1(calories) == (3, 12000)

def test_solution2_example():
    calories = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

    assert solution2(calories) == 45000


def solution1(calories: str):
    lines = calories.splitlines()
    max_calories = 0
    max_elf = 1
    current_elf = 1
    current_calories = 0

    for l in lines:
        if l.strip() == "":

            if current_calories > max_calories:
                max_elf = current_elf
                max_calories = current_calories
            
            current_calories = 0
            current_elf += 1
        else:
            cals = int(l.strip())
            current_calories += cals

    return max_elf, max_calories

def solution2(calories: str):
    lines = calories.splitlines()
    current_calories = 0

    elves_calories = []

    for l in lines:
        if l.strip() == "":
            elves_calories.append(current_calories)
            current_calories = 0
        else:
            cals = int(l.strip())
            current_calories += cals
    else:
        if current_calories > 0:
            elves_calories.append(current_calories)


    return sum(list(reversed(sorted(elves_calories)))[:3])

if __name__ == "__main__":
    with open("./day01/input.txt") as f:
        print(solution1(f.read()))

    with open("./day01/input.txt") as f:
        print(solution2(f.read()))