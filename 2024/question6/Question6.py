import sys


def walk(steps, grid, y, x, dir, obstacle=(-1, -1)):

    step = (y, x, dir)

    if step in steps:
        return steps, True

    steps.add(step)

    while True:
        ny, nx = next_move(dir, y, x)
        if not(in_grid(grid, ny, nx)):
            return steps, False

        if not(is_blocked(grid, ny, nx, obstacle)):
            break

        if is_blocked(grid, ny, nx, obstacle):
            dir = rotate_right(dir)

    return walk(steps, grid, ny, nx, dir, obstacle)


def rotate_right(dir):
    match dir:
        case "^":
            return ">"
        case ">":
            return "v"
        case "<":
            return "^"
        case "v":
            return "<"


def next_move(dir, y, x):
    match dir:
        case "^":
            return y - 1, x
        case ">":
            return y, x + 1
        case "<":
            return y, x - 1
        case "v":
            return y + 1, x


def is_blocked(grid, y, x, obstacle):
    return grid[y][x] == "#" or (y, x) == obstacle


def in_grid(grid, y, x):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def solve_one(grid, y, x):
    steps, loop = walk(set(), grid, y, x, "^")
    print(len(set([(x, y) for x, y, d in steps])))


def solve_two(grid, y, x):
    obs = []
    for oy in range(len(grid)):
        for ox in range(len(grid[0])):
            obstacle = (oy, ox)
            steps, loop = walk(set(), grid, y, x, "^", obstacle)
            if loop:
                obs.append(obstacle)
    print(len(obs))


with open('input.txt') as f:
    sys.setrecursionlimit(10000)
    entries = [l.strip() for l in f.readlines()]
    y, x = [(idx, line.find("^")) for idx, line in enumerate(entries) if '^' in line][0]
    grid = [list(l) for l in entries]
    solve_one(entries, y, x)
    solve_two(entries, y, x)
