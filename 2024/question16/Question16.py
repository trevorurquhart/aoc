deltas = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
rotate_left = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
rotate_right = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}


def v(grid, p):
    py, px = p
    return grid[py][px] if 0 <= py < len(grid) and 0 <= px <= len(grid[0]) else None


def find_neighbours(grid, point):
    n = []
    y, x, d, c, path = point
    for dir in [(d, 1), (rotate_left[d], 1001), (rotate_right[d], 1001)]:
        dy, dx = deltas[dir[0]]
        p = (y + dy, x + dx)
        if v(grid, p) in ['.', 'E']:
            n.append((p[0], p[1], dir[0], dir[1], path + [p]))
    return n


def solve(grid, S, E):
    best_cost = 1e9
    paths = []
    visited = {}

    sy, sx = S
    to_visit = [(sy, sx, 'E', 0, [sy, sx])]
    while len(to_visit) > 0:
        visiting = to_visit.pop()
        vy, vx, vdir, vcost, vpath = visiting
        if best_cost < vcost:
            continue

        if (vy, vx) == E:
            if vcost < best_cost:
                paths = []
                best_cost = vcost

            if vcost == best_cost:
                paths += vpath

        nbs = find_neighbours(grid, visiting)
        for n in nbs:
            ny, nx, dir, cost, path = n
            np = (ny, nx, dir)
            new_cost = vcost + cost
            if np not in visited or visited[np] >= new_cost:
                visited[np] = new_cost
                to_visit.append((ny, nx, dir, new_cost, path))

    print(best_cost)
    print(len(set(paths)) - 1)


with open("input.txt") as f:
    file = f.read()
    grid = [list(l.strip()) for l in file.split('\n')]
    S = divmod(file.replace('\n','').index('S'), len(grid[0]))
    E = divmod(file.replace('\n','').index('E'), len(grid[0]))
    solve(grid, S, E)
