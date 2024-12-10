deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def next_0(grid, start):
    y, x = start
    while True:
        x = x + 1
        if x >= len(grid[0]):
            x = 0
            y = y + 1

        if y >= len(grid):
            return -1, -1

        if grid[y][x] == 0:
            return y, x


def neighbours(grid, y, x):
    n = []
    val = grid[y][x]
    for dy, dx in deltas:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == val + 1:
            n.append((ny, nx))
    return n


def count_trail_heads(grid, i):
    to_visit = [i]
    cnt = 0
    nines = set()
    while len(to_visit) > 0:
        y, x = to_visit.pop()
        if grid[y][x] == 9:
            nines.add((y, x))
            cnt = cnt + 1
        to_visit.extend(neighbours(grid, y, x))

    return cnt, len(nines)


def solve(grid):
    next0 = (0, -1)
    one_cnt = 0
    two_cnt = 0
    while True:
        next0 = next_0(grid, next0)
        if next0[0] == -1:
            break
        n, u = count_trail_heads(grid, next0)
        one_cnt = one_cnt + u
        two_cnt = two_cnt + n
    print(one_cnt)
    print(two_cnt)


with open("input.txt") as f:
    grid = [list(map(int, list(x))) for x in [y.strip() for y in f.readlines()]]
    solve(grid)