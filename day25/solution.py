import functools

decoder = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

encoder = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}


def add(a, b):
    a_vals = [decoder[x] for x in a]
    b_vals = [decoder[x] for x in b]

    length = max(len(a), len(b))

    result = []
    carryover = 0
    for i in range(1, length + 1):
        if i > len(a):
            s = b_vals[-i] + carryover
        elif i > len(b):
            s = a_vals[-i] + carryover
        else:
            s = (a_vals[-i]) + b_vals[-i] + carryover

        carryover = (s + 2) // 5
        s = ((s + 2) % 5) - 2
        result.insert(0, s)

    if carryover != 0:
        result.insert(0, carryover)

    return "".join([encoder[x] for x in result])


def solution1(lines):
    return functools.reduce(add, [x.strip() for x in lines])


def test_example1():
    assert add("1=", "1-") == "12"


def test_example2():
    assert add("1", "2-") == "20"


if __name__ == "__main__":
    print(solution1(open("./day25/input.txt").readlines()))
