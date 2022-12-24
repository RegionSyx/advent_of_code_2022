# Resources: ore, clay, obsidian, geode
import math


indexs = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def parse(lines):
    blueprints = {}
    for line in lines:
        tokens = line.split(" ")
        blueprints[int(tokens[1].strip(":"))] = {
            "ore": [int(tokens[6]), 0, 0, 0],
            "clay": [int(tokens[12]), 0, 0, 0],
            "obsidian": [int(tokens[18]), int(tokens[21]), 0, 0],
            "geode": [int(tokens[27]), 0, int(tokens[30]), 0],
        }
    return blueprints


def solution1(lines, max_minutes):
    blueprints = parse(lines)

    produces = {
        "ore": [1, 0, 0, 0],
        "clay": [0, 1, 0, 0],
        "obsidian": [0, 0, 1, 0],
        "geode": [0, 0, 0, 1],
    }

    def walk(resources, robots, to_buy, minutes, blueprint):
        # if to_buy:
        #     print(' ' * minutes, to_buy)
        if minutes > max_minutes:
            return resources[-1]

        new_resources = resources.copy()

        can_buy = all([a >= b for a, b in zip(new_resources, blueprint[to_buy])])
        # spend
        if can_buy:
            new_resources = [a - b for a, b in zip(new_resources, blueprint[to_buy])]

        # earn
        new_resources = [a + b for a, b in zip(new_resources, robots)]

        # ready
        if can_buy:
            new_robots = [a + b for a, b in zip(robots, produces[to_buy])]
            geodes = []
            # geodes.append(walk(resources, robots, None, minutes + 1, blueprint))
            for k, v in blueprint.items():
                can_buy = all(
                    [
                        (a > 0 and b > 0) or (b == 0)
                        for a, b in zip(new_robots, blueprint[k])
                    ]
                )
                if not can_buy:
                    continue

                should_buy = True
                match k:
                    case "ore":
                        should_buy = new_robots[indexs["ore"]] < max(
                            v[indexs["ore"]] for v in blueprint.values()
                        )
                    case "clay":
                        should_buy = (  # new_robots[indexs['ore']] >= blueprint['clay'][indexs['ore']] and \
                            new_robots[indexs["obsidian"]]
                            < blueprint["geode"][indexs["obsidian"]]
                            and new_robots[indexs["clay"]]
                            < blueprint["obsidian"][indexs["clay"]]
                        )
                    case "obsidian":
                        should_buy = (
                            new_robots[indexs["obsidian"]]
                            < blueprint["geode"][indexs["obsidian"]]
                        )
                    case "geode":
                        should_buy = True

                if not should_buy:
                    continue

                geodes.append(
                    walk(new_resources, new_robots, k, minutes + 1, blueprint)
                )

            return max(geodes) if geodes else new_resources[-1]
        else:
            return walk(new_resources, robots, to_buy, minutes + 1, blueprint)

    quality_levels = []
    for num, blueprint in reversed(blueprints.items()):
        # print(blueprint)
        resources = blueprint["ore"]
        robots = [0, 0, 0, 0]
        minutes = 0
        geodes = walk(resources, robots, "ore", minutes, blueprint)
        print(geodes)
        quality_levels.append(geodes)

    return quality_levels[0] * quality_levels[1] * quality_levels[2]


if __name__ == "__main__":
    with open("./day19/input.txt") as f:
        print(solution1(f.readlines()[:3], 32))
