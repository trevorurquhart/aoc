offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def word(grid, x, y, d_x, d_y, len):
    return ''.join([grid[y + n * d_y][x + n * d_x] for n in range(len)])


def search_for_xmas(grid, x, y):
    return sum([check_for_xmas(grid, x, y, d_x, d_y) for d_x, d_y in offsets])


def check_for_xmas(grid, x, y, d_x, d_y):
    w_len = 4
    x_inbounds = d_x == 0 or (d_x == 1 and x <= len(grid[0]) - w_len) or (d_x == -1 and x >= 3)
    y_inbounds = d_y == 0 or (d_y == 1 and y <= len(grid) - w_len) or (d_y == -1 and y >= 3)
    return 1 if x_inbounds and y_inbounds and 'XMAS' == word(grid, x, y, d_x, d_y, w_len) else 0


def search_for_x_mas(grid, x, y):
    x_inbounds = x <= len(grid[0]) - 3
    y_inbounds = y <= len(grid) - 3
    return 1 if x_inbounds \
                and y_inbounds \
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
