from dataclasses import dataclass
from tqdm import tqdm
import itertools


@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    def __add__(self, a):
        return Vec2D(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return Vec2D(self.x - a.x, self.y - a.y)

    def distance(self, a):
        return abs(self.x - a.x) + abs(self.y - a.y)


def solution1(lines):
    sensor_beacons = []

    scan = {}
    for l in lines:
        tokens = l.split(" ")
        sensor_beacons.append(
            (
                Vec2D(int(tokens[2][2:-1]), int(tokens[3][2:-1])),
                Vec2D(int(tokens[8][2:-1]), int(tokens[9][2:])),
            )
        )

    for sensor, beacon in tqdm(sensor_beacons):
        scan[sensor] = "S"
        scan[beacon] = "B"
        distance = sensor.distance(beacon)
        height = abs(sensor.y - 2000000)

        for x in range(sensor.x - distance + height, sensor.x + distance + 1 - height):
            y = 2000000
            if sensor.distance(Vec2D(x, y)) <= distance:
                if Vec2D(x, y) not in scan:
                    scan[Vec2D(x, y)] = "#"

    return sum(1 for p, v in scan.items() if p.y == 2000000 and v == "#")


def solution2(lines):
    sensor_beacons = []

    scan = {}
    for l in lines:
        tokens = l.split(" ")
        sensor_beacons.append(
            (
                Vec2D(int(tokens[2][2:-1]), int(tokens[3][2:-1])),
                Vec2D(int(tokens[8][2:-1]), int(tokens[9][2:])),
            )
        )

    sensor_dists = {}
    for sensor, beacon in tqdm(sensor_beacons):
        sensor_dists[sensor] = sensor.distance(beacon)

    candidates = list()
    for a, b in tqdm(itertools.combinations(sensor_dists.keys(), 2)):
        dist = a.distance(b)
        if (sensor_dists[a] + sensor_dists[b] + 2) == dist:
            candidates.append(a)
            candidates.append(b)

    cands_cands = []
    for c in candidates:
        my_cands = set()
        distance = sensor_dists[c]
        for x in range(c.x - distance - 1, c.x + distance + 2):
            my_cands.add(Vec2D(x, c.y + (distance - abs(x - c.x)) + 1))
            my_cands.add(Vec2D(x, c.y - (distance - abs(x - c.x)) - 1))
        cands_cands.append(my_cands)

    this_is_it = cands_cands[0] & cands_cands[1] & cands_cands[2] & cands_cands[3]

    assert len(this_is_it) == 1

    return list(this_is_it)[0].x * 4000000 + list(this_is_it)[0].y


def test_example1():
    with open("./day15/example.txt") as f:
        assert solution1(f.readlines()) == 26


if __name__ == "__main__":
    with open("./day15/input.txt") as f:
        print(solution2(f.readlines()))
