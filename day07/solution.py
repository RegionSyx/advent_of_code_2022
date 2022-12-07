from dataclasses import dataclass
from typing import List, Optional, Set, Union


def test_example1():
    with open('./day07/example.txt') as f:
        assert solution1(f.readlines()) == 95437


def test_example2():
    with open('./day07/example.txt') as f:
        assert solution2(f.readlines()) == 24933642



@dataclass(frozen=True)
class Dir:
    name: str
    parent: Optional['Dir']

@dataclass(frozen=True)
class File:
    name: str
    size: int
    parent: Dir


def create_file_tree(lines):
    root = Dir(name='/', parent=None)

    current_dir: List[Dir] = [root]

    dirs: Set[Dir] = set()
    files: Set[File] = set()

    current_line = 0
    while current_line < len(lines):
        parts = lines[current_line].strip().split(' ')
        match parts[1]:
            case 'cd':
                if parts[2] == '/':
                    current_dir = [root]
                elif parts[2] == '..':
                    current_dir = current_dir[:-1]
                else:
                    possible_dirs = [x for x in dirs if x.name == parts[2] and x.parent == current_dir[-1]]
                    if len(possible_dirs) != 1:
                        raise Exception("Multiple dirs found")
                    current_dir.append(possible_dirs[0])
                current_line += 1
            case 'ls':
                current_line += 1
                parts = lines[current_line].strip().split(' ')
                while current_line < len(lines) and parts[0] != '$':
                    
                    if parts[0] == 'dir':
                        dirs.add(Dir(name=parts[1], parent=current_dir[-1]))
                    else:
                        files.add(File(name=parts[1], size=int(parts[0]), parent=current_dir[-1]))
                    
                    current_line += 1

                    if current_line < len(lines):
                        parts = lines[current_line].strip().split(' ')
                    else:
                        break
                    

    return root, dirs, files


def solution1(lines):
    root, dirs, files = create_file_tree(lines)
    total = 0

    def _walk(node, dirs, files):
        nonlocal total
        size_of_files = sum([f.size for f in files if f.parent == node])
        size_of_dirs = sum([_walk(d, dirs, files) for d in dirs if d.parent == node])
        
        size = size_of_files + size_of_dirs
        if size <= 100_000:
            total += size
        return size
 
    _walk(root, dirs, files)

    return total


def solution2(lines):
    root, dirs, files = create_file_tree(lines)

    dir_sizes = []

    def _walk(node, dirs, files):
        nonlocal dir_sizes
        size_of_files = sum([f.size for f in files if f.parent == node])
        size_of_dirs = sum([_walk(d, dirs, files) for d in dirs if d.parent == node])
        
        size = size_of_files + size_of_dirs
        dir_sizes.append(size)
        return size
 
    _walk(root, dirs, files)

    used_space = sum([f.size for f in files])
    unused_space = 70000000 - used_space
    needed_space = 30000000 - unused_space

    return min([x for x in dir_sizes if x > needed_space])


if __name__ == '__main__':
    with open('./day07/input.txt') as f:
        print(solution1(f.readlines()))
    with open('./day07/input.txt') as f:
        print(solution2(f.readlines()))
 #   print(solution2(open('./day07/input.txt').read()))