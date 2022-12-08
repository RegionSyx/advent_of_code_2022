

def solution1(lines):
    tree_map = [list(map(int, l.strip())) for l in lines]
    print(tree_map)
    visible = set()

    for y, row in enumerate(tree_map):
        max_height = -1
        for x, col in enumerate(row):
            if col > max_height:
                visible.add((x, y))
                max_height = col

    for y, row in enumerate(tree_map):
        max_height = -1
        for x, col in enumerate(reversed(row)):
            if col > max_height:
                visible.add((len(row) - 1 - x, y))
                max_height = col

    for x in range(len(tree_map[0])):
        max_height = -1
        for y in range(len(tree_map)):
            if tree_map[y][x] > max_height:
                visible.add((x, y))
                max_height = tree_map[y][x]

    for x in range(len(tree_map[0])):
        max_height = -1
        for y in reversed(range(len(tree_map))):
            if tree_map[y][x] > max_height:
                visible.add((x, y))
                max_height = tree_map[y][x]

    return len(visible)


def _scenic_score(trees):
    score = 0
    max_height = trees[0]
    for tree in trees[1:]:
        score += 1
        if tree >= max_height:
            break

    return max(score, 1)

def solution2(lines):
    tree_map = [list(map(int, l.strip())) for l in lines]
    tree_scores = []

    for x in range(len(tree_map[0])):
        for y in range(len(tree_map)):
            score = (
                _scenic_score(list(reversed(tree_map[y][:x+1]))) * # left
                _scenic_score(tree_map[y][x:]) * # right
                _scenic_score([t[x] for t in list(reversed(tree_map[:y+1]))]) * # up
                _scenic_score([t[x] for t in tree_map[y:]]) # down
            )
            tree_scores.append(score)
    return  max(tree_scores)


if __name__ == "__main__":
    with open('./day08/input.txt') as f:
        print(solution1(f.readlines()))
    with open('./day08/input.txt') as f:
        print(solution2(f.readlines()))