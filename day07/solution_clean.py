from dataclasses import dataclass
from typing import List, Optional, Set, Union


def test_example1():
    with open('./day07/example.txt') as f:
        assert solution1(f.readlines()) == 95437


def test_example2():
    with open('./day07/example.txt') as f:
        assert solution2(f.readlines()) == 24933642


def create_file_tree(lines):
    cwd = []
    files = {}
    for line in lines:
        match line.split():
            case ['$', 'cd', '/']:
                cwd = []
            case ['$', 'cd', '..']:
                cwd.pop()
            case ['$', 'cd', name]:
                cwd.append(name)
            case ['$', 'ls']:
                ...
            case ['dir', name]:
                ...
            case [size, name]:
                files[(*cwd, name)] = int(size)

    return files


def _prefixes(lists):
    results = set()
    for l in lists:
        for i in range(len(l)):
            results.add(l[:i])
    return results


def solution1(lines):
    files = create_file_tree(lines)
    total = 0

    for p in _prefixes(files.keys()):
        size = sum(files[x] for x in files if len(x) >= len(p) and x[:len(p)] == p)

        if size <= 100_000:
            total += size

    return total


def solution2(lines):
    files = create_file_tree(lines)

    dir_sizes = []
    for p in _prefixes(files.keys()):
        size = sum(files[x] for x in files if len(x) >= len(p) and x[:len(p)] == p)
        dir_sizes.append(size)

    needed_space = 30000000 - (70000000 - sum(files.values()))
    return min([x for x in dir_sizes if x > needed_space])


if __name__ == '__main__':
    with open('./day07/input.txt') as f:
        print(solution1(f.readlines()))
    with open('./day07/input.txt') as f:
        print(solution2(f.readlines()))
