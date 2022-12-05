def test_example1():
    with open("./day05/example.txt") as f:
        example = f.readlines()

    output = solution1(example)

    assert output == 'CMZ'

def test_example2():
    with open("./day05/example.txt") as f:
        example = f.readlines()

    output = solution2(example)

    assert output == 'MCD'

def solution1(lines):
    stack = dict()
    starting_line = 0
    for l in lines:
        if l.strip() == "":
            break

        starting_line += 1
        
        for i, p in enumerate(range(1, len(l), 4)):
            if l[p] != ' ':
                if i+1 not in stack:
                    stack[i+1] = [l[p]]
                else:
                    stack[i+1].insert(0, l[p])

    for s in stack:
        stack[s].pop(0)
    

    for l in lines[starting_line+1:]:
        [_, num, _, _from, _, to] = l.split()
        num, _from, to = int(num), int(_from), int(to)

        for x in range(num):
            stack[to].append(stack[_from].pop())

    result = ""
    for i in range(1, len(stack)+1):
        result += stack[i][-1]

    return result

def solution2(lines):
    stack = dict()
    starting_line = 0
    for l in lines:
        if l.strip() == "":
            break

        starting_line += 1
        
        for i, p in enumerate(range(1, len(l), 4)):
            if l[p] != ' ':
                if i+1 not in stack:
                    stack[i+1] = [l[p]]
                else:
                    stack[i+1].insert(0, l[p])

    for s in stack:
        stack[s].pop(0)
    

    for l in lines[starting_line+1:]:
        [_, num, _, _from, _, to] = l.split()
        num, _from, to = int(num), int(_from), int(to)

        stack[to].extend(stack[_from][-1 * num:])
        del stack[_from][-1 * num:]

    print(stack)
    result = ""
    for i in range(1, len(stack)+1):
        result += stack[i][-1]

    return result

if __name__ == "__main__":
    with open("./day05/input.txt") as f:
        print(solution1(f.readlines()))

    with open("./day05/input.txt") as f:
        print(solution2(f.readlines()))