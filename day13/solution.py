import ast
from functools import reduce, cmp_to_key


def compare(left, right):
    #import pdb; pdb.set_trace()
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            if compare(l, r) is None:
                continue
            else:
                return compare(l, r)
        else:
            if len(left) == len(right):
                return None
            else:
                return len(left) < len(right)

def solution1(i):
    pairs = i.split('\n\n')
    pairs = [[ast.literal_eval(p) for p in x.splitlines()] for x in pairs]

    return sum(i for i, r in enumerate(pairs, start=1) if compare(*r) == True)


def solution2(i):
    packets = [ast.literal_eval(x) for x in i.splitlines() if x != ''] + [[[2]], [[6]]]

    packets.sort(key=cmp_to_key(lambda a, b: -1 if compare(a, b) else 1))

    return reduce(lambda a, b: a * b, [i for i, x in enumerate(packets, start=1) if x == [[2]] or x == [[6]]], 1)

def test_example1():
    assert compare([1,1,3,1,1], [1,1,5,1,1]) == True

def test_example2():
    assert compare([[1],[2,3,4]], [[1],4]) == True

def test_example3():
    assert compare([9], [[8,7,6]]) == False

def test_example4():
    assert compare([[4,4],4,4], [[4,4],4,4,4]) == True 

def test_example5():
    assert compare([7,7,7,7], [7,7,7]) == False 

def test_example6():
    assert compare([], [3]) == True 

def test_example7():
    assert compare([[[]]], [[]]) == False 

def test_example8():
    assert compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]) == False 


def test_full1():
    example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    assert solution1(example) == 13

def test_full2():
    example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    assert solution2(example) == 140


if __name__ == '__main__':
    with open('./day13/input.txt') as f:
        print(solution1(f.read()))
    with open('./day13/input.txt') as f:
        print(solution2(f.read()))