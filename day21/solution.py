import graphlib
import operator
import itertools

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
    #   '==': operator.eq,
}


def solution1(lines, humn):
    monkeys = {}
    graph = {}
    for line in lines:
        match line.split():
            case [name, left, operator, right]:
                monkeys[name[:-1]] = (operator, left, right)
                graph[name[:-1]] = [left, right]
            case [name, num]:
                monkeys[name[:-1]] = int(num)
                graph[name[:-1]] = []

    results = {}
    for monkey in graphlib.TopologicalSorter(graph).static_order():
        match monkeys[monkey]:
            case (operator, left, right):
                results[monkey] = operations[operator](results[left], results[right])
            case num:
                results[monkey] = num

    return results["root"]


def solution2(lines):
    monkeys = {}
    graph = {}
    for line in lines:
        match line.split():
            case ["root:" as name, left, operator, right]:
                monkeys[name[:-1]] = ("==", left, right)
                graph[name[:-1]] = [left, right]
            case [name, left, operator, right]:
                monkeys[name[:-1]] = (operator, left, right)
                graph[name[:-1]] = [left, right]
            case [name, num]:
                monkeys[name[:-1]] = int(num)
                graph[name[:-1]] = []

    results = {}
    for monkey in graphlib.TopologicalSorter(graph).static_order():
        match monkeys[monkey]:
            case (operator, "humn", right):
                results[monkey] = (operator, "X", results[right])
            case (operator, left, "humn"):
                results[monkey] = (operator, results[left], "X")
            case (operator, left, right) if isinstance(
                results[left], int
            ) and isinstance(results[right], int):
                results[monkey] = operations[operator](results[left], results[right])
            case (operator, left, right):
                results[monkey] = (operator, results[left], results[right])
            case num if isinstance(num, int):
                results[monkey] = num
            case _:
                raise Exception(monkeys[monkey])

    def solve(operation, equality):
        match operation:
            case ("==", left, right) if isinstance(left, int):
                return solve(right, left)
            case ("==", left, right) if isinstance(right, int):
                return solve(left, right)
            case ("+", left, right) if isinstance(left, int):
                return solve(right, equality - left)
            case ("+", left, right) if isinstance(right, int):
                return solve(left, equality - right)
            case ("-", left, right) if isinstance(left, int):
                return solve(right, left - equality)
            case ("-", left, right) if isinstance(right, int):
                return solve(left, equality + right)
            case ("*", left, right) if isinstance(left, int):
                return solve(right, equality // left)
            case ("*", left, right) if isinstance(right, int):
                return solve(left, equality // right)
            case ("/", left, right) if isinstance(left, int):
                return solve(right, 1 // (equality * left))
            case ("/", left, right) if isinstance(right, int):
                return solve(left, equality * right)
            case "X":
                return equality
            case _:
                raise Exception(operation[0], equality)

    return solve(results["root"], True)


print(solution2(open("./day21/input.txt").readlines()))
