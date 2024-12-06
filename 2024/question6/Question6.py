import time


def walk(grid, y, x, dir, obstacle=(-1, -1)):

    steps = set()
    curr_y = y
    curr_x = x

    while True:
        ny, nx = next_move(dir, curr_y, curr_x)

        if not(in_grid(grid, ny, nx)):
            return steps, False

        if is_blocked(grid, ny, nx, obstacle):
            dir = rotate_right(dir)

        if not(is_blocked(grid, ny, nx, obstacle)):
            step = (ny, nx, dir)
            if step in steps:
                return steps, True
            steps.add(step)
            curr_y, curr_x = ny, nx


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
    steps, loop = walk(grid, y, x, "^")
    unique = set([(x, y) for x, y, d in steps])
    print(len(unique))
    return unique


def solve_two(grid, y, x, to_block):
    obs = []
    for obstacle in to_block:
        steps, loop = walk(grid, y, x, "^", obstacle)
        if loop:
            obs.append(obstacle)
    print(len(obs))


with open('input.txt') as f:
    entries = [l.strip() for l in f.readlines()]
    y, x = [(idx, line.find("^")) for idx, line in enumerate(entries) if '^' in line][0]
    grid = [list(l) for l in entries]
    path = solve_one(entries, y, x)
    start = time.time()
    solve_two(entries, y, x, path)
    end = time.time()
    print(f'Took: {end - start}s')
