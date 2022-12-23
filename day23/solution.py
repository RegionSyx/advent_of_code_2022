from collections import defaultdict
from dataclasses import dataclass
import itertools

@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    def __add__(self, a):
        return Vec2D(self.x + a.x, self.y + a.y)
    
    def __sub__(self, a):
        return Vec2D(self.x - a.x, self.y - a.y)

def solution1(lines):
    elf_map = set()
    for row, l in enumerate(lines):
        for col, c in enumerate(l):
            if c == '#':
                elf_map.add(Vec2D(col, row))
    all_dirs = {Vec2D(x, y) for x, y in itertools.product((-1, 0, 1), (-1, 0, 1))} - {Vec2D(0, 0)}
    up_dirs = {Vec2D(x, -1) for x in (-1, 0, 1)}
    right_dirs = {Vec2D(1, y) for y in (-1, 0, 1)}
    down_dirs = {Vec2D(x, 1) for x in (-1, 0, 1)}
    left_dirs = {Vec2D(-1, y) for y in (-1, 0, 1)}
    north = Vec2D(0, -1)
    south = Vec2D(0, 1)
    east = Vec2D(1, 0)
    west = Vec2D(-1, 0)
    directions = [
            (up_dirs, north),
            (down_dirs, south),
            (left_dirs, west),
            (right_dirs, east),
            ]

    round = 0
    while True:
        round += 1
        old_elf_map = elf_map.copy()
        proposed = defaultdict(list)
        for elf in elf_map:
   
            if not ({elf + x for x in all_dirs} & elf_map):
                proposed[elf].append(elf)
            else:
                for dirs, dir in directions:
                    if not ({elf + x for x in dirs} & elf_map):
                        proposed[elf + dir].append(elf)
                        break


        for pos, elves in proposed.items():
            if len(elves) == 1:
                elf_map.remove(elves[0])
                elf_map.add(pos)


        directions.append(directions.pop(0))

        if old_elf_map == elf_map:
            break
   
    return round
    total = 0
    for x in range(bounds[0].x, bounds[1].x + 1):
        for y in range(bounds[0].y, bounds[1].y + 1):
            total += 0 if Vec2D(x, y) in elf_map else 1
    return total

if __name__ == '__main__':
    with open('./day23/input.txt') as f:
        print(solution1(f.readlines()))