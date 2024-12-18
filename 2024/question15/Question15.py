deltas = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}


def move(robot, grid, m):
    dy, dx = deltas[m]
    y, x = robot
    to_move = [robot]
    while True:
        cy, cx = y + dy, x + dx
        next = grid[cy][cx]
        if next == '#':
            return robot

        if next == 'O':
            to_move.append((cy, cx))

        if next == '.':
            break

        y, x = cy, cx

    for n in reversed(to_move):
        ny, nx = n
        grid[ny][nx], grid[ny + dy][nx + dx] = grid[ny + dy][nx + dx], grid[ny][nx]

    return robot[0] + dy, robot[1] + dx

def move_through_grid_one(robot, grid, moves):
    r = robot
    for m in moves:
        r = move(r, grid, m)


def parse_grid_one(lines):
    grid = []
    for i, g in enumerate(lines):
        line = g.strip()
        r_idx = line.find('@')
        if r_idx != -1:
            robot = i, r_idx
        grid.append(list(line))
    return grid, robot

def push_box(grid):


def parse_grid_two(lines):
    grid = []
    outputs = {'#': ['#', '#'], 'O': ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
    for y, line in enumerate(lines):
        row = []
        for c in line.strip():
            row.extend(outputs[c])
            if c == '@':
                robot = y, len(row) -2
        grid.append(row)

    return grid, robot

def sum_gps(grid):
    s = 0
    for y, l in enumerate(grid):
        s = s + sum([100 * y + x for x, v in enumerate(l) if v == 'O'])
    return s


def solve_one(glines, mlines):
    grid, robot = parse_grid_one(glines)
    moves = list(mlines.replace('\n', ''))
    move_through_grid_one(robot, grid, moves)
    print_grid(grid)
    ans = sum_gps(grid)
    print(ans)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def solve_two(glines, mlines):
    grid, robot = parse_grid_two(glines)
    moves = list(mlines.replace('\n', ''))
    print_grid(grid)

with open("test_data2a.txt") as g, open("test_data2b.txt") as m:
    glines = g.readlines()
    mlines = m.read()
    # solve_one(glines, mlines)
    solve_two(glines, mlines)
