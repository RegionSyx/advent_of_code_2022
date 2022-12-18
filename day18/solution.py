import itertools

def solution1(lines):
    cubes = [tuple(map(int, l.split(','))) for l in lines]

    bounds = [
        [
            min(t[0] for t in cubes),
            min(t[1] for t in cubes),
            min(t[2] for t in cubes),
        ],
        [
            max(t[0] for t in cubes),
            max(t[1] for t in cubes),
            max(t[2] for t in cubes),
        ],
    ]
    surface_area = 0
    for dim1, dim2, dim3 in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        for a in range(bounds[0][dim1], bounds[1][dim1] + 1):
            for b in range(bounds[0][dim2], bounds[1][dim2] + 1):
                line = sorted(t[dim3] for t in cubes if (a, b) == (t[dim1], t[dim2]))
                if not line:
                    continue
                prev_line = line[0]
                surface_area += 2
                for l in line[1:]:
                    if l > prev_line + 1:
                        surface_area += 2
                    prev_line = l

    return surface_area

def solution2(lines):
    cubes = [tuple(map(int, l.split(','))) for l in lines]

    bounds = [
        [
            min(t[0] for t in cubes),
            min(t[1] for t in cubes),
            min(t[2] for t in cubes),
        ],
        [
            max(t[0] for t in cubes),
            max(t[1] for t in cubes),
            max(t[2] for t in cubes),
        ],
    ]
    air_cubes = [(x, y, z) for x, y, z in 
                itertools.product(
                    range(bounds[0][0], bounds[1][0] + 1),
                    range(bounds[0][1], bounds[1][1] + 1),
                    range(bounds[0][2], bounds[1][2] + 1)
                ) if (x,y,z) not in cubes]
    
    surface_area = 0
    for dim1, dim2, dim3 in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        for a in range(bounds[0][dim1], bounds[1][dim1] + 1):
            for b in range(bounds[0][dim2], bounds[1][dim2] + 1):
                line = sorted(t[dim3] for t in cubes if (a, b) == (t[dim1], t[dim2]))
                if not line:
                    continue
                prev_line = line[0]
                surface_area += 2
                for l in line[1:]:
                    if l > prev_line + 1:
                        surface_area += 2
                    prev_line = l

    prev_air_cubes_len = len(air_cubes) + 1
    while prev_air_cubes_len != len(air_cubes):
        to_delete = set()
        prev_air_cubes_len = len(air_cubes)
        for ac in air_cubes:
            neighbors = [(x + ac[0], y + ac[1], z + ac[2]) for x, y, z in [
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]]
            if not len(set(neighbors) & (set(cubes) | set(air_cubes))) == 6:
                to_delete.add(ac)
        for x in to_delete:
            air_cubes.remove(x)


    air_surface_area = 0
    for dim1, dim2, dim3 in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        for a in range(bounds[0][dim1], bounds[1][dim1] + 1):
            for b in range(bounds[0][dim2], bounds[1][dim2] + 1):
                line = sorted(t[dim3] for t in air_cubes if (a, b) == (t[dim1], t[dim2]))
                if not line:
                    continue
                prev_line = line[0]
                air_surface_area += 2
                for l in line[1:]:
                    if l > prev_line + 1:
                        air_surface_area += 2
                    prev_line = l

    return surface_area - air_surface_area

if __name__ == '__main__':
    with open('./day18/input.txt') as f:
        print(solution2(f.readlines()))