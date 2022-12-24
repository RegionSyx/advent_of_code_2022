from dataclasses import dataclass
from typing import List, Callable, Tuple, Union


@dataclass
class Monkey:
    items: List[int]
    operation: Tuple[str, int] = ("", 0)
    test: Tuple[int, int, int] = (0, 0, 0)


def _parse_monkeys(_input: str) -> List[Monkey]:
    monkeys: List[Monkey] = []
    for monkey in _input.split("\n\n"):
        lines = monkey.splitlines()
        m = Monkey([])
        for l in lines:
            match l.split():
                case ["Starting", "items:", *items]:
                    m.items = [int(x.strip()) for x in "".join(items).split(",")]
                case ["Operation:", "new", "=", "old", "*", "old"]:
                    m.operation = ("**", 2)
                case ["Operation:", "new", "=", "old", op, num]:
                    m.operation = (op, int(num))
                case ["Test:", "divisible", "by", num]:
                    m.test = (int(num), m.test[1], m.test[2])
                case ["If", "true:", "throw", "to", "monkey", num]:
                    m.test = (m.test[0], int(num), m.test[2])
                case ["If", "false:", "throw", "to", "monkey", num]:
                    m.test = (m.test[0], m.test[1], int(num))

        monkeys.append(m)

    return monkeys


def solution1(monkeys):
    inspections = {i: 0 for i in range(len(monkeys))}

    for round in range(20):
        for i, monkey in enumerate(monkeys):
            for _ in range(len(monkey.items)):
                inspections[i] += 1
                item = monkey.items.pop(0)

                match monkey.operation:
                    case ("+", num):
                        item += num
                    case ("*", num):
                        item *= num
                    case ("**", num):
                        item = item**num

                item = item // 3

                if (item % monkey.test[0]) == 0:
                    next_monkey = monkey.test[1]
                else:
                    next_monkey = monkey.test[2]

                monkeys[next_monkey].items.append(item)

    [first, second] = sorted(inspections.values())[-2:]
    return first * second


def solution2(monkeys):
    inspections = {i: 0 for i in range(len(monkeys))}

    base = 1
    for monkey in monkeys:
        base *= monkey.test[0]

    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            for _ in range(len(monkey.items)):
                inspections[i] += 1
                item = monkey.items.pop(0)

                match monkey.operation:
                    case ("+", num):
                        item += num
                    case ("*", num):
                        item *= num
                    case ("**", num):
                        item = item**num

                if (item % monkey.test[0]) == 0:
                    next_monkey = monkey.test[1]
                else:
                    next_monkey = monkey.test[2]

                item = item % base
                monkeys[next_monkey].items.append(item)

    [first, second] = sorted(inspections.values())[-2:]
    return first * second


def test_example1():
    with open("./day11/example.txt") as f:
        assert solution1(_parse_monkeys(f.read())) == 10605


def test_example2():
    with open("./day11/example.txt") as f:
        assert solution2(_parse_monkeys(f.read())) == 2713310158


if __name__ == "__main__":
    with open("./day11/input.txt") as f:
        print(solution1(_parse_monkeys(f.read())))
    with open("./day11/input.txt") as f:
        print(solution2(_parse_monkeys(f.read())))
