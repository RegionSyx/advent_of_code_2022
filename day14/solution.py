from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    def __add__(self, a):
        return Vec2D(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return Vec2D(self.x - a.x, self.y - a.y)

    def magnitude(self):
        return max(abs(self.x), abs(self.y))

    def normalized(self):
        return Vec2D(min(max(self.x, -1), 1), min(max(self.y, -1), 1))


def solution1(lines):
    scan = {}
    starting_pos = Vec2D(500, 0)
    for l in lines:
        path = [Vec2D(*map(int, x.strip().split(","))) for x in l.split("->")]
        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1]

            if start.y == end.y:
                for x in range(min(start.x, end.x), max(end.x, start.x) + 1):
                    scan[Vec2D(x, start.y)] = "#"

            if start.x == end.x:
                for y in range(min(start.y, end.y), max(end.y, start.y) + 1):
                    scan[Vec2D(start.x, y)] = "#"

    scan[starting_pos] = "S"
    bounds = (
        min(v.x for v in scan.keys()),
        min(v.y for v in scan.keys()),
        max(v.x for v in scan.keys()),
        max(v.y for v in scan.keys()),
    )

    sand_counter = 1
    current_pos = starting_pos

    down = Vec2D(0, 1)
    downleft = Vec2D(-1, 1)
    downright = Vec2D(1, 1)
    while True:
        if current_pos.y > bounds[3]:
            break

        if scan.get(current_pos + down) is None:
            current_pos += down
            continue
        elif scan.get(current_pos + downleft) is None:
            current_pos += downleft
            continue
        elif scan.get(current_pos + downright) is None:
            current_pos += downright
            continue
        else:
            scan[current_pos] = "o"
            sand_counter += 1
            current_pos = starting_pos
            continue

    return sand_counter - 1


def solution2(lines):
    scan = {}
    starting_pos = Vec2D(500, 0)
    for l in lines:
        path = [Vec2D(*map(int, x.strip().split(","))) for x in l.split("->")]
        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1]

            if start.y == end.y:
                for x in range(min(start.x, end.x), max(end.x, start.x) + 1):
                    scan[Vec2D(x, start.y)] = "#"

            if start.x == end.x:
                for y in range(min(start.y, end.y), max(end.y, start.y) + 1):
                    scan[Vec2D(start.x, y)] = "#"

    scan[starting_pos] = "S"
    bounds = (
        min(v.x for v in scan.keys()),
        min(v.y for v in scan.keys()),
        max(v.x for v in scan.keys()),
        max(v.y for v in scan.keys()),
    )

    sand_counter = 1
    current_pos = starting_pos

    down = Vec2D(0, 1)
    downleft = Vec2D(-1, 1)
    downright = Vec2D(1, 1)
    while True:
        if current_pos.y >= bounds[3] + 1:
            scan[current_pos] = "o"
            sand_counter += 1
            current_pos = starting_pos
            continue

        if scan.get(current_pos + down) is None:
            current_pos += down
            continue
        elif scan.get(current_pos + downleft) is None:
            current_pos += downleft
            continue
        elif scan.get(current_pos + downright) is None:
            current_pos += downright
            continue
        elif current_pos == starting_pos:
            break
        else:
            scan[current_pos] = "o"
            sand_counter += 1
            current_pos = starting_pos
            continue

    return sand_counter


def test_example1():
    example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
    assert solution1(example.splitlines()) == 24


def test_example2():
    example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
    assert solution2(example.splitlines()) == 93


if __name__ == "__main__":
    with open("./day14/input.txt") as f:
        print(solution1(f.readlines()))
    with open("./day14/input.txt") as f:
        print(solution2(f.readlines()))
