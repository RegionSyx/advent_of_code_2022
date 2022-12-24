from dataclasses import dataclass
import re
import itertools
from typing import List, Any
from types import SimpleNamespace


@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    def __add__(self, a):
        return Vec2D(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return Vec2D(self.x - a.x, self.y - a.y)

    def dot(self, a):
        return self.x * a.x + self.y * a.y

    def cross(self, a):
        return self.x * a.y - self.y * a.x

    def rotate90(self):
        return Vec2D(-self.y, self.x)


DIRS = SimpleNamespace()
DIRS.UP = Vec2D(0, -1)
DIRS.DOWN = Vec2D(0, 1)
DIRS.RIGHT = Vec2D(1, 0)
DIRS.LEFT = Vec2D(-1, 0)


def solution1(puzzle_input):
    puzzle_map_raw, instructions_raw = puzzle_input.split("\n\n")

    puzzle_map = {}
    for row, l in enumerate(puzzle_map_raw.splitlines(), start=1):
        for col, c in enumerate(l, start=1):
            if c != " ":
                puzzle_map[Vec2D(col, row)] = c

    instructions = list(
        zip(
            list(map(int, re.split("R|L|U|D", instructions_raw))),
            list(re.sub("[0-9]+", "", instructions_raw)) + [None],
        )
    )

    current_pos = Vec2D(min(v.x for v in puzzle_map if v.y == 1), 1)
    current_dir = Vec2D(1, 0)

    for steps, turn in instructions:
        for _ in range(steps):
            puzzle_map[current_pos] = "*"

            next_pos = current_pos + current_dir
            if next_pos not in puzzle_map:
                path = [
                    v for v in puzzle_map if (v - current_pos).cross(current_dir) == 0
                ]
                path.sort(key=lambda v: (v - current_pos).dot(current_dir))
                next_pos = path[0]

            if puzzle_map.get(next_pos) == "#":
                continue

            current_pos = next_pos

        if turn == "R":
            current_dir = current_dir.rotate90()
        if turn == "L":
            for _ in range(3):
                current_dir = current_dir.rotate90()

    for row in range(20):
        line = ""
        for col in range(20):
            line += puzzle_map.get(Vec2D(col, row), " ")

    cardinalities = [Vec2D(1, 0), Vec2D(0, 1), Vec2D(-1, 0), Vec2D(0, -1)]
    return current_pos.y * 1000 + current_pos.x * 4 + cardinalities.index(current_dir)


def walk(current_pos, current_dir, puzzle_map):
    next_pos = current_pos + current_dir
    next_dir = current_dir
    if next_pos not in puzzle_map:
        size = 50
        face = ((current_pos.x - 1) // size, (current_pos.y - 1) // size)
        rel_x = (current_pos.x - 1) % size  # 0...size - 1
        rel_y = (current_pos.y - 1) % size  # 0...size - 1
        match (face, current_dir):
            case ((1, 1), DIRS.LEFT):
                next_dir = DIRS.DOWN
                next_pos = Vec2D(rel_y + 1, 0)
            case ((1, 0), DIRS.LEFT):
                next_dir = DIRS.RIGHT
                next_pos = Vec2D(0, 2 * size + (size - rel_y))
            case ((1, 0), DIRS.UP):
                next_dir = DIRS.RIGHT
                next_pos = Vec2D(0, 3 * size + 1 + rel_x)
            case ((1, 2), DIRS.DOWN):
                next_dir = DIRS.LEFT
                next_pos = Vec2D(0, 3 * size + 1 + rel_x)
            case ((2, 0), DIRS.RIGHT):
                next_dir = DIRS.LEFT
                next_pos = Vec2D(0, 2 * size + (size - rel_y))
            case ((1, 2), DIRS.RIGHT):
                next_dir = DIRS.LEFT
                next_pos = Vec2D(0, size - rel_y)
            case ((0, 3), DIRS.LEFT):
                next_dir = DIRS.DOWN
                next_pos = Vec2D(1 * size + rel_y + 1, 0)
            case ((2, 0), DIRS.DOWN):
                next_dir = DIRS.LEFT
                next_pos = Vec2D(0, 1 * size + rel_x + 1)
            case ((2, 0), DIRS.UP):
                next_dir = DIRS.UP
                next_pos = Vec2D(rel_x + 1, 0)
            case ((0, 2), DIRS.LEFT):
                next_dir = DIRS.RIGHT
                next_pos = Vec2D(0, size - rel_y)
            case ((0, 3), DIRS.RIGHT):
                next_dir = DIRS.UP
                next_pos = Vec2D(1 * size + rel_y + 1, 0)
            case ((0, 3), DIRS.DOWN):
                next_dir = DIRS.DOWN
                next_pos = Vec2D(2 * size + rel_x + 1, 1)
            case ((0, 2), DIRS.UP):
                next_dir = DIRS.RIGHT
                next_pos = Vec2D(0, 1 * size + 1 + rel_x)
            case ((1, 1), DIRS.RIGHT):
                next_dir = DIRS.UP
                next_pos = Vec2D(2 * size + rel_y + 1, 0)
            case _:
                raise Exception(f"Unhandled case {str(face)} {str(next_dir)}")
        path = [v for v in puzzle_map if (v - next_pos).cross(next_dir) == 0]
        path.sort(key=lambda v: (v - next_pos).dot(next_dir))
        next_pos = path[0]

    return next_pos, next_dir


def solution2(puzzle_input):
    puzzle_map_raw, instructions_raw = puzzle_input.split("\n\n")

    puzzle_map = {}
    for row, l in enumerate(puzzle_map_raw.splitlines(), start=1):
        for col, c in enumerate(l, start=1):
            if c != " ":
                puzzle_map[Vec2D(col, row)] = c

    instructions = list(
        zip(
            list(map(int, re.split("R|L|U|D", instructions_raw))),
            list(re.sub("[0-9]+", "", instructions_raw)) + [None],
        )
    )

    current_pos = Vec2D(min(v.x for v in puzzle_map if v.y == 1), 1)
    current_dir = Vec2D(1, 0)
    cardinalities = [Vec2D(1, 0), Vec2D(0, 1), Vec2D(-1, 0), Vec2D(0, -1)]
    arrows = [">", "V", "<", "^"]
    cases = {}

    for pos in puzzle_map:
        for dir in cardinalities:
            if ((pos.x - 1) % 50 == 0) and ((pos.y - 1) % 50 == 0):
                visited = set()
                current_pos, current_dir = pos, dir
                for _ in range(200):
                    visited.add(current_pos)
                    current_pos, current_dir = walk(
                        current_pos, current_dir, puzzle_map
                    )
                for row in range(200):
                    line = ""
                    for col in range(200):
                        line += (
                            puzzle_map.get(Vec2D(col, row), " ")
                            if Vec2D(col, row) not in visited
                            else "*"
                        )
                    print(line)
                assert len(visited) == 200, (pos, dir, len(visited))

    for steps, turn in instructions:
        for _ in range(steps):
            puzzle_map[current_pos] = arrows[cardinalities.index(current_dir)]

            next_pos, next_dir = walk(current_pos, current_dir, puzzle_map)
            if puzzle_map.get(next_pos) == "#":
                break

            current_pos = next_pos
            current_dir = next_dir

        if turn == "R":
            current_dir = current_dir.rotate90()
        if turn == "L":
            for _ in range(3):
                current_dir = current_dir.rotate90()

    for row in range(200):
        line = ""
        for col in range(200):
            line += puzzle_map.get(Vec2D(col, row), " ")
        print(line)

    for k, v in cases.items():
        print(k, *v)

    cardinalities = [Vec2D(1, 0), Vec2D(0, 1), Vec2D(-1, 0), Vec2D(0, -1)]
    return current_pos.y * 1000 + current_pos.x * 4 + cardinalities.index(current_dir)


def rotate_point(p, r):
    normalized = p - Vec2D(r, r)
    return Vec2D(normalized.y, normalized.x) + Vec2D(r // 2, r // 2)


with open("./day22/input.txt") as f:
    print(solution2(f.read()))
