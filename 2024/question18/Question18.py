deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def v(p):
    y, x, s = p
    return grid[y][x] if 0 <= x < len(grid[0]) and 0 <= y < len(grid) else None


def setv(x, y, value):
    grid[y][x] = value


def drop(n, bytes):
    for b in range(0, n):
       drop_byte(bytes[b])


def drop_byte(b):
    x, y = b
    setv(x, y, '#')


def find_neighbours(p):
    py, px, ps = p
    return [p for p in [(py + dy, px + dx, ps + 1) for dy, dx in deltas] if v(p) == '.']


def walk():
    target = (len(grid) - 1, len(grid[0]) -1)
    visited = set()
    to_visit = [(0, 0, 0)]
    shortest_path = {}
    while len(to_visit) > 0:
        p = to_visit.pop(0)
        py, px, pp = p
        pcoord = (py, px)
        visited.add(pcoord)

        if pcoord not in shortest_path or shortest_path[pcoord] > pp:
            shortest_path[pcoord] = pp
        else:
            continue

        if (p[0], p[1]) == target:
            return p[2]

        for n in find_neighbours(p):
            ny, nx, nc = n
            if (ny, nx) not in visited:
                to_visit.append(n)

    return None


def solve_one():
    drop(12, bytes)
    path = walk()
    print(path)


def solve_two():
    for b in bytes:
        drop_byte(b)
        path = walk()
        if path is None:
            return b





with open("input.txt") as f:
    bytes = [(int(x), int(y)) for x, y in [l.strip().split(',') for l in f.readlines()]]
    grid = [['.' for x in range(0, 71)] for y in range(0, 71)]
    solve_one()
    print(solve_two())
