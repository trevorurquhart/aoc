def mark_grid(grid, coord, next_coord):
    x1, y1 = [int(a) for a in coord.split(",")]
    x2, y2 = [int(a) for a in next_coord.split(",")]

    mark(grid, x1, x2, y1, True)
    mark(grid, y1, y2, x1, False)


def mark(grid, x1, x2, y1, is_x):
    x_step = 1 if x2 > x1 else -1
    x_off = 0 if x1 == x2 else x2 - x1 + x_step
    for x in range(x1, x1 + x_off, x_step):
        if is_x:
            grid.add((x, y1))
        else:
            grid.add((y1, x))


def drop(current_posn, grid, sand_posns, max_depth, stop_before_max):
    if stop_before_max and current_posn[1] == max_depth - 1:
        return current_posn

    if current_posn[1] > max_depth:
        return None

    drop_one = (current_posn[0], current_posn[1] + 1)
    if drop_one not in grid and drop_one not in sand_posns:
        return drop(drop_one, grid, sand_posns, max_depth, stop_before_max)

    drop_one_left = (current_posn[0] - 1, current_posn[1] + 1)
    if drop_one_left not in grid and drop_one_left not in sand_posns:
        return drop(drop_one_left, grid, sand_posns, max_depth, stop_before_max)

    drop_one_right = (current_posn[0] + 1, current_posn[1] + 1)
    if drop_one_right not in grid and drop_one_right not in sand_posns:
        return drop(drop_one_right, grid, sand_posns, max_depth, stop_before_max)

    return current_posn


def drop_sand(grid, criteria, max_depth, stop_before_max=False):
    sand_posns = set()
    sand = (500, 0)
    while criteria(resting_spot := drop(sand, grid, sand_posns, max_depth, stop_before_max)):
        sand_posns.add(resting_spot)
        sand = (500, 0)
    return sand_posns


def solve_one(grid):
    max_depth = max([x[1] for x in grid])
    posns = drop_sand(grid, lambda x: x is not None, max_depth)
    print(len(posns))


def solve_two(grid):
    max_depth = max([x[1] for x in grid]) + 2
    posns = drop_sand(grid, lambda x: x != (500, 0), max_depth, True)
    print(len(posns) + 1)


def parse_grid(lines):
    grid = set()
    for coord_set in [l.strip().split(' -> ') for l in lines]:
        for idx, coord in enumerate(coord_set):
            if idx + 1 < len(coord_set):
                mark_grid(grid, coord, coord_set[idx + 1])
    return grid


with open('question_data.txt') as q:
    grid = parse_grid(q.readlines())
    solve_one(grid)
    solve_two(grid)
    # solve_two()
