def solution1(lines):
    X = 1
    cycle_values = [X]

    for line in lines:
        match line.split():
            case ["addx", num]:
                cycle_values.append(X)
                X += int(num)
                cycle_values.append(X)
            case ["noop"]:
                cycle_values.append(X)

    signals = [x[0] * x[1] for x in enumerate(cycle_values, start=1)]
    return sum(x for x in signals[19:220:40])


def solution2(lines):
    X = 1
    cycle_values = [X]

    for line in lines:
        match line.split():
            case ["addx", num]:
                cycle_values.append(X)
                X += int(num)
                cycle_values.append(X)
            case ["noop"]:
                cycle_values.append(X)

    output = ""
    for cycle, sprite_position in enumerate(cycle_values):
        if abs(sprite_position - cycle % 40) <= 1:
            output += "#"
        else:
            output += "."

        if cycle % 40 == 39:
            print(output)
            output = ""


if __name__ == "__main__":
    with open("./day10/input.txt") as f:
        print(solution1(f.readlines()))

    with open("./day10/input.txt") as f:
        print(solution2(f.readlines()))
