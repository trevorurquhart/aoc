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

    execute_move(dx, dy, grid, to_move)
    return robot[0] + dy, robot[1] + dx

def move2(robot, grid, m):

    to_move = [robot]
    y, x = robot
    if m == '<' or m == '>':
        dy = 0
        dx = -1 if m == '<' else 1
        while True:
            cx = x + dx
            next = grid[y][cx]

            if next == '#':
                return robot

            if next in ['[', ']']:
                to_move.append((y, cx))

            if next == '.':
                break

            x = cx

    if m == '^' or m == 'v':
        dx = 0
        dy = -1 if m == '^' else 1
        cy = y + dx
        next = grid[x][cy]

        if next in ['[', ']']:
            visited = set()
            to_visit = [next]
            while len(next) > 0:
                n = to_visit.pop()
                nbs = find_neighbours(grid, n)
                for n in nbs:
                    # if here

                    if n not in visited:
                        to_visit.append(n)




        y, x = cy, cx

    execute_move(dx, dy, grid, to_move)
    return robot[0] + dy, robot[1] + dx

def execute_move(dx, dy, grid, to_move):
    for n in reversed(to_move):
        ny, nx = n
        grid[ny][nx], grid[ny + dy][nx + dx] = grid[ny + dy][nx + dx], grid[ny][nx]


def move_through_grid_one(robot, grid, moves):
    r = robot
    for m in moves:
        r = move(r, grid, m)


def parse_grid_one(lines):
    grid = []
    for i, line in enumerate(lines):
        r_idx = line.find('@')
        if r_idx != -1:
            robot = i, r_idx
        grid.append(list(line))
    return grid, robot

# def push_box(grid):
def move_through_grid_two(robot, grid, moves):
    r = robot
    for m in moves:
        r = move2(r, grid, m)

def parse_grid_two(lines):
    grid = []
    outputs = {'#': ['#', '#'], 'O': ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
    for y, line in enumerate(lines):
        row = []
        for c in line:
            row.extend(outputs[c])
            if c == '@':
                robot = y, len(row) -2
        grid.append(row)

    return grid, robot

def sum_gps(grid):
    s = 0
    for y, l in enumerate(grid):
        s += sum([100 * y + x for x, v in enumerate(l) if v == 'O'])
    return s


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def solve_one(glines, moves):
    grid, robot = parse_grid_one(glines)
    move_through_grid_one(robot, grid, moves)
    print_grid(grid)
    ans = sum_gps(grid)
    print(ans)


def solve_two(lines, moves):
    grid, robot = parse_grid_two(lines)
    move_through_grid_two(robot, grid, moves)
    print_grid(grid)

with open("test_data2a.txt") as g, open("test_data2b.txt") as m:
    glines = [l.strip() for l in g.readlines()]
    moves = list(m.read().replace('\n', ''))
    # solve_one(glines, moves)
    solve_two(glines, m.read())
