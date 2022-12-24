import pytest


@pytest.mark.parametrize(
    "example,result",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_example1(example, result):
    output = solution(example, 4)
    assert output == result


@pytest.mark.parametrize(
    "example,result",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_example2(example, result):
    output = solution(example, 14)
    assert output == result


def solution(signal, marker_length):
    for i in range(len(signal)):
        chars = signal[i : i + marker_length]

        if len(set(chars)) == len(chars):
            return i + marker_length


if __name__ == "__main__":
    with open("./day06/input.txt") as f:
        print(solution(f.read(), 4))

    with open("./day06/input.txt") as f:
        print(solution(f.read(), 14))
