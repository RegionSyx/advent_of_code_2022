from dataclasses import dataclass
import re
import itertools
from typing import List

@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    def difference(self, a):
        return Vec2D(self.x - a.x, self.y - a.y)

    def dot(self, a):
        return self.x * a.x + self.y * a.y

def solution1(puzzle_input):
    puzzle_map_raw, instructions_raw = puzzle_input.split('\n\n')

    puzzle_map = {}
    for row, l in enumerate(puzzle_map_raw.splitlines(), start=1):
        for col, c in enumerate(l, start=1):
            if c != ' ':
                puzzle_map[Vec2D(col, row)] = c

    instructions = list(zip(
        list(map(int, re.split('R|L|U|D', instructions_raw))),
        list(re.sub('[0-9]+', '', instructions_raw)) + [None]
    ))
    print(instructions)

    current_pos = Vec2D(min(v.x for v in puzzle_map if v.y == 1), 1)
    current_dir = Vec2D(1, 0)

    for steps, turn in instructions:
        path: List[Vec2D] = []
        match current_dir:
            case 0:
                path = [v for v in puzzle_map if v.y == current_pos.y]
                path.sort(key=lambda v: v.x)
                index = path.index(current_pos)
                path = path[index:] + path[:index]
            case 1:
                path = [v for v in puzzle_map if v.x == current_pos.x]
                path.sort(key=lambda v: v.y)
                index = path.index(current_pos)
                path = path[index:] + path[:index]
            case 2:
                path = [v for v in puzzle_map if v.y == current_pos.y]
                path.sort(key=lambda v: -v.x)
                index = path.index(current_pos)
                path = path[index:] + path[:index]
            case 3:
                path = [v for v in puzzle_map if v.x == current_pos.x]
                path.sort(key=lambda v: -v.y)
                index = path.index(current_pos)
                path = path[index:] + path[:index]

        next_pos = list(itertools.takewhile(
            lambda x: x[0] < steps + 1 and puzzle_map[x[1]] != '#', 
            enumerate(itertools.cycle(path))
        ))
        print(list(next_pos))
        current_pos = list(next_pos)[-1][1]

        puzzle_map[current_pos] = '*'

        if turn == 'R':
            current_dir = (current_dir + 1) % 4
        if turn == 'L':
            current_dir = (current_dir - 1) % 4


    for row in range(20):
        line = ""
        for col in range(20):
            line += puzzle_map.get(Vec2D(col, row), ' ')
        print(line)

    return current_pos.y * 1000 + current_pos.x * 4 + current_dir


with open('./day22/input.txt') as f:
    print(solution1(f.read()))