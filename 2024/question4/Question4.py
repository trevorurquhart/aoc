offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def word(grid, x, y, dx, dy, len):
    return ''.join([grid[y + n * dy][x + n * dx] for n in range(len)])


def search_for_xmas(grid, x, y):
    return sum([check_for_xmas(grid, x, y, dx, dy) for dx, dy in offsets])


def check_for_xmas(grid, x, y, dx, dy):
    word_len = len('XMAS')
    x_ok = dx == 0 or (dx == 1 and x <= len(grid[0]) - word_len) or (dx == -1 and x >= 3)
    y_ok = dy == 0 or (dy == 1 and y <= len(grid) - word_len) or (dy == -1 and y >= 3)
    return 1 if x_ok and y_ok and 'XMAS' == word(grid, x, y, dx, dy, word_len) else 0


def search_for_x_mas(grid, x, y):
    x_ok = x <= len(grid[0]) - 3
    y_ok = y <= len(grid) - 3
    return 1 if x_ok \
                and y_ok \
                and word(grid, x, y, 1, 1, 3) in {'MAS', 'SAM'} \
                and word(grid, x + 2, y, -1, 1, 3) in {'MAS', 'SAM'} \
        else 0


def solve_one(grid):
    cnt = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cnt += search_for_xmas(grid, x, y)
    print(cnt)

def solve_two(grid):
    cnt = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cnt += search_for_x_mas(grid, x, y)
    print(cnt)


with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]
    solve_one(lines)
    solve_two(lines)
