from dataclasses import dataclass
from tqdm import tqdm

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


def rocks():
    while True:
        yield [Vec2D(x, y) for x, y in [(0, 0), (1, 0), (2, 0), (3, 0)]]
        yield [Vec2D(x, y) for x, y in [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]]
        yield [Vec2D(x, y) for x, y in [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]]
        yield [Vec2D(x, y) for x, y in [(0, 0), (0, 1), (0, 2), (0, 3)]]
        yield [Vec2D(x, y) for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]]
def jets(moves):
    while True:
        yield from list(moves)

        

def solution1(moves):
    moves = moves.strip()
    rocks_gen = rocks()
    jets_gen = jets(moves)
    current_rock = next(rocks_gen)
    current_pos = Vec2D(2, 3)
    fallen = set()
    stopped_rocks = 0

    while stopped_rocks < 2022:
   
        match next(jets_gen):
            case "<":
                if current_pos.x > 0:
                    if not fallen & set(current_pos + x for x in [y + Vec2D(-1, 0) for y in current_rock]):
                        current_pos += Vec2D(-1, 0)
            case ">":
                if current_pos.x + max(v.x for v in current_rock) < 6:
                    if not fallen & set(current_pos + x for x in [y + Vec2D(1, 0) for y in current_rock]):
                        current_pos += Vec2D(1, 0)

        if not fallen & set(current_pos + x for x in [y + Vec2D(0, -1) for y in current_rock]) and current_pos.y > 0:
            current_pos += Vec2D(0, -1)
        else:
            for r in current_rock:
                fallen.add(r + current_pos)
            current_rock = next(rocks_gen)
            current_pos = Vec2D(2, max(v.y for v in fallen) + 4)
            stopped_rocks += 1

    return max(v.y for v in fallen) + 1

#@profile
def solution2(moves, num):
    moves = moves.strip()
    rocks_gen = rocks()
    jets_gen = jets(moves)
    current_rock = next(rocks_gen)
    current_pos = Vec2D(2, 3)
    fallen = set()
    stopped_rocks = 0
    highest_stopped = 0
    floor = 0
    total_moves = 0
    with tqdm(total = num) as pbar:
        while stopped_rocks < num:
            
            match next(jets_gen):
                case "<":
                    if current_pos.x > 0:
                        if not fallen & set(current_pos + x for x in [y + Vec2D(-1, 0) for y in current_rock]):
                            current_pos += Vec2D(-1, 0)
                case ">":
                    if current_pos.x + max(v.x for v in current_rock) < 6:
                        if not fallen & set(current_pos + x for x in [y + Vec2D(1, 0) for y in current_rock]):
                            current_pos += Vec2D(1, 0)
            total_moves += 1
            if not fallen & set(current_pos + x for x in [y + Vec2D(0, -1) for y in current_rock]) and current_pos.y > 0:
                current_pos += Vec2D(0, -1)
            else:
                for r in current_rock:
                    fallen.add(r + current_pos)
                highest_stopped = max(v.y for v in fallen)
                current_rock = next(rocks_gen)
                current_pos = Vec2D(2, max(v.y for v in fallen) + 4)
                stopped_rocks += 1
                pbar.update(1)

                if total_moves % len(moves) == 0 and stopped_rocks % 5 == 0:
                    print(total_moves, stopped_rocks)
                    if len([v for v in fallen if v.y == highest_stopped]) == 7:
                        print(total_moves, stopped_rocks, highest_stopped)
                        
            if stopped_rocks % 100 == 0:
                for y in range(floor + 1, highest_stopped + 1):
                    if len([v for v in fallen if v.y == y]) == 7:
                        floor = y - 1
                for v in [v for v in fallen if v.y < floor]:
                    fallen.remove(v)

    return highest_stopped + 1


def test_example1():
    example = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

    assert solution1(example) == 3068


if __name__ == '__main__':
    #with open('./day17/input.txt') as f:
    #    print(solution1(f.read()))

    with open('./day17/input.txt') as f:
        print(solution2(f.read(), 1000000000000))