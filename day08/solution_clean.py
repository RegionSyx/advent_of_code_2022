def solution1(lines):
    tree_map = [list(map(int, l.strip())) for l in lines]

    def _is_tree_visible(trees):
        return len([t for t in trees[1:] if t >= trees[0]]) == 0

    return sum(
        [
            1
            if any(
                [
                    _is_tree_visible(tree_map[y][x::-1]),  # left
                    _is_tree_visible(tree_map[y][x::1]),  # right
                    _is_tree_visible([t[x] for t in tree_map[y::-1]]),  # up
                    _is_tree_visible([t[x] for t in tree_map[y::1]]),  # down
                ]
            )
            else 0
            for y in range(len(tree_map))
            for x in range(len(tree_map[y]))
        ]
    )


def solution2(lines):
    tree_map = [list(map(int, l.strip())) for l in lines]

    def _scenic_score(trees):
        return next(
            (i for i, x in enumerate(trees[1:], start=1) if x >= trees[0]),
            len(trees) - 1,
        )

    return max(
        [
            (
                _scenic_score(tree_map[y][x::-1])
                * _scenic_score(tree_map[y][x::1])  # left
                * _scenic_score([t[x] for t in tree_map[y::-1]])  # right
                * _scenic_score([t[x] for t in tree_map[y::1]])  # up  # down
            )
            for y in range(len(tree_map))
            for x in range(len(tree_map[y]))
        ]
    )


if __name__ == "__main__":
    with open("./day08/input.txt") as f:
        print(solution1(f.readlines()))
    with open("./day08/input.txt") as f:
        print(solution2(f.readlines()))
