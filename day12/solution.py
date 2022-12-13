from dataclasses import dataclass
from itertools import product
from typing import Dict

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


def solution(lines):
    topo_map = {}
    starting_pos = Vec2D(0, 0)
    ending_pos = Vec2D(0, 0)

    for row, l in enumerate(lines):
        for col, c in enumerate(l):
            if c == 'S':
                starting_pos = Vec2D(row, col)
                topo_map[Vec2D(row, col)] = ord('a')
            elif c == 'E':
                ending_pos = Vec2D(row, col)
                topo_map[Vec2D(row, col)] = ord('z')
            else:
                topo_map[Vec2D(row, col)] = ord(c)

    print(starting_pos, ending_pos)
    positions = set(topo_map.keys())

    steps = 0
    heads = {starting_pos}
    visited = {starting_pos}
    while ending_pos not in heads:
        steps += 1
        visited |= heads
        neighbors = (set(topo_map.keys()) - visited) & {pos + Vec2D(x, y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)] for pos in heads if (pos + Vec2D(x, y) in topo_map) and topo_map[pos + Vec2D(x, y)] <= topo_map[pos] + 1}
        heads = neighbors
    return steps

    def walk(pos: Vec2D, _map: Dict[Vec2D, int], steps: int):
        if pos == ending_pos:
            return steps

        current_height = _map[pos]

        new_map = _map.copy()
        del new_map[pos]

        neighbors = set(_map.keys()) & {pos + Vec2D(x, y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]}
        results = []
        for n in neighbors:
            if _map[n] <= current_height + 1:
                walk(n, new_map, steps + 1)
            del new_map[n]

        return min(results) if results else 999999999

    return walk(starting_pos, topo_map, 0)

def solution2(lines):
    topo_map = {}
    starting_positions = []
    ending_pos = Vec2D(0, 0)

    for row, l in enumerate(lines):
        for col, c in enumerate(l):
            if c == 'S':
                starting_positions.append(Vec2D(row, col))
                topo_map[Vec2D(row, col)] = ord('a')
            elif c == 'E':
                ending_pos = Vec2D(row, col)
                topo_map[Vec2D(row, col)] = ord('z')
            elif c == 'a':
                starting_positions.append(Vec2D(row, col))
                topo_map[Vec2D(row, col)] = ord('a')
            else:
                topo_map[Vec2D(row, col)] = ord(c)

    
    steps = 0
    heads = set(starting_positions)
    visited = set(starting_positions)
    while ending_pos not in heads:
        steps += 1
        visited |= heads
        neighbors = (set(topo_map.keys()) - visited) & {pos + Vec2D(x, y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)] for pos in heads if (pos + Vec2D(x, y) in topo_map) and topo_map[pos + Vec2D(x, y)] <= topo_map[pos] + 1}
        heads = neighbors
    return steps



def test_example1():
    example="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()

    assert solution(example) == 31

def test_example2():
    example="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()

    assert solution2(example) == 29

if __name__ == "__main__":
    with open('./day12/input.txt') as f:
        print(solution(f.readlines()))

    with open('./day12/input.txt') as f:
        print(solution2(f.readlines()))