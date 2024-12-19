deltas = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
box_edges = ['[', ']']

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


def find_neighbours(grid, n, dy, visited):
    neighbours = []
    y, x = n
    ny = y + dy
    xy_value = grid[y][x]
    dx = -1 if xy_value == ']' else 1
    if (y, x + dx) not in visited:
        neighbours.append((y, x + dx))

    if (ny, x) not in visited:
        neighbours.append((ny, x))

    return neighbours

# def value_in_grid(grid)


def move2(robot, grid, dir):
    to_move = [robot]
    y, x = robot
    if dir == '<' or dir == '>':
        dy = 0
        dx = -1 if dir == '<' else 1
        while True:
            cx = x + dx
            next = grid[y][cx]

            if next == '#':
                return robot

            if next in box_edges:
                to_move.append((y, cx))

            if next == '.':
                break

            x = cx

    if dir == '^' or dir == 'v':
        dx = 0
        dy = -1 if dir == '^' else 1
        cy = y + dy
        next = grid[cy][x]

        if next == "#":
            return robot

        if next in box_edges:
            to_visit = [(cy, x)]
            while len(to_visit) > 0:
                pos = to_visit.pop(0)
                to_move.append(pos)
                nbs = find_neighbours(grid, pos, dy, to_move)
                for n in nbs:
                    ny, nx = n
                    n_value = grid[ny][nx]
                    if n_value == '.':
                        continue

                    if n_value == "#":
                        return robot

                    if n_value in ['[', ']'] and n not in to_move and n not in to_visit:
                        to_visit.append(n)

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


def calculate_gps(grid):
    ans = 0
    # 0 - 9 len 10
    ly = len(grid)
    hy = ly // 2
    lx = len(grid[0])
    hx = lx // 2
    for y in range(ly):
        for x in range(lx):
            if grid[y][x] == '[':
                ans += 100 * y + x
    return ans


def move_through_grid_two(robot, grid, moves):
    r = robot
    for m in moves:
        r = move2(r, grid, m)
    ans = calculate_gps(grid)
    print(ans)


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


with open("inputa.txt") as g, open("inputb.txt") as m:
    glines = [l.strip() for l in g.readlines()]
    moves = list(m.read().replace('\n', ''))
    # solve_one(glines, moves)
    solve_two(glines, moves)
