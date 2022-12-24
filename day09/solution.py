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
    head_pos = Vec2D(0, 0)
    tail_pos = Vec2D(0, 0)

    visited = set()

    for line in lines:
        direction, num = line.split(" ")
        for step_dir in direction * int(num):
            direction_vec = Vec2D(0, 0)
            match step_dir:
                case "U":
                    direction_vec = Vec2D(0, 1)
                case "D":
                    direction_vec = Vec2D(0, -1)
                case "L":
                    direction_vec = Vec2D(-1, 0)
                case "R":
                    direction_vec = Vec2D(1, 0)

            head_pos += direction_vec

            if (head_pos - tail_pos).magnitude() > 1:
                tail_pos += (head_pos - tail_pos).normalized()
            visited.add(tail_pos)

    return len(visited)


def solution2(lines):

    positions = [Vec2D(0, 0) for x in range(10)]

    visited = set()

    for line in lines:
        direction, num = line.split(" ")
        for step_dir in direction * int(num):
            direction_vec = Vec2D(0, 0)
            match step_dir:
                case "U":
                    direction_vec = Vec2D(0, 1)
                case "D":
                    direction_vec = Vec2D(0, -1)
                case "L":
                    direction_vec = Vec2D(-1, 0)
                case "R":
                    direction_vec = Vec2D(1, 0)

            positions[0] += direction_vec

            for i in range(len(positions) - 1):
                head_pos = positions[i]
                tail_pos = positions[i + 1]

                if (head_pos - tail_pos).magnitude() > 1:
                    positions[i + 1] += (head_pos - tail_pos).normalized()
            visited.add(positions[-1])

    return len(visited)


if __name__ == "__main__":
    with open("./day09/input.txt") as f:
        print(solution1(f.readlines()))

    with open("./day09/input.txt") as f:
        print(solution2(f.readlines()))
