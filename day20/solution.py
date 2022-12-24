from tqdm import tqdm


def move(output, num):
    index = next(i for i, v in enumerate(output) if v == num)
    if num[1] == 0:
        return output

    item = output.pop(index)
    if num[1] < 0 and index + num[1] == 0:
        output.insert(len(output), item)
    elif num[1] > 0 and (index + num[1]) == len(output):
        output.insert(0, item)
    else:
        output.insert((index + num[1]) % len(output), item)
    return output


def solution1(lines):
    nums = [(i, int(l)) for i, l in enumerate(lines)]

    output = nums.copy()

    for num in nums:
        move(output, num)

    out_values = [x[1] for x in output]
    return sum(
        out_values[(out_values.index(0) + x) % len(out_values)]
        for x in (1000, 2000, 3000)
    )


def solution2(lines):
    nums = [(i, int(l) * 811589153) for i, l in enumerate(lines)]

    output = nums.copy()

    for num in nums * 10:
        move(output, num)

    out_values = [x[1] for x in output]
    return sum(
        out_values[(out_values.index(0) + x) % len(out_values)]
        for x in (1000, 2000, 3000)
    )


def test_example1():
    assert move([1, 2, -3, 3, -2, 0, 4], 1) == [2, 1, -3, 3, -2, 0, 4]


def test_example2():
    assert move([2, 1, -3, 3, -2, 0, 4], 2) == [1, -3, 2, 3, -2, 0, 4]


def test_example3():
    assert move([1, -3, 2, 3, -2, 0, 4], -3) == [1, 2, 3, -2, -3, 0, 4]


def test_example4():
    assert move([1, 2, 3, -2, -3, 0, 4], 3) == [1, 2, -2, -3, 0, 3, 4]


def test_example5():
    assert move([1, 2, -2, -3, 0, 3, 4], -2) == [1, 2, -3, 0, 3, 4, -2]


def test_example6():
    assert move([1, 2, -3, 0, 3, 4, -2], 0) == [1, 2, -3, 0, 3, 4, -2]


def test_example7():
    assert move([1, 2, -3, 0, 3, 4, -2], 4) == [1, 2, -3, 4, 0, 3, -2]


def test_example8():
    assert move([1, 2, -3, 3, 0, 4, -2], 3) == [3, 1, 2, -3, 0, 4, -2]


def test_example9():
    assert move([1, 2, -3, 3, 0, 4, -2], -2) == [1, 2, -3, 3, -2, 0, 4]


def test_example10():
    assert move([4, -2, 5, 6, 7, 8, 9], -2) == [4, 5, 6, 7, 8, -2, 9]


def test_example11():
    assert move([4, 5, -2, 6, 7, 8, 9], -2) == [4, 5, 6, 7, 8, 9, -2]


def test_example12():
    assert move([4, 5, 6, 7, -2, 8, 9], -2) == [4, 5, -2, 6, 7, 8, 9]


def test_example13():
    assert move([4, 5, 6, 7, -2, 8, 0], 0) == [4, 5, 6, 7, -2, 8, 0]


if __name__ == "__main__":

    with open("./day20/input.txt") as f:
        print(solution2(f.readlines()))
