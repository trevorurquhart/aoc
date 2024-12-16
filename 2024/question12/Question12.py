deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_neighbours(grid, point, visited):
    n = []
    y, x = point
    val = grid[y][x]
    for dy, dx in deltas:
        ny = y + dy
        nx = x + dx
        np = (ny, nx)
        if grid_value(grid, np) == val and np not in visited:
            visited.add(np)
            n.append(np)
    return n


def point_in_grid(grid, p):
    return 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])


def find_region(grid, p, visited):
    to_visit = [p]
    region = set()
    while len(to_visit) > 0:
        np = to_visit.pop()
        region.add(np)
        neighbours = find_neighbours(grid, np, visited)
        to_visit.extend(neighbours)
    return region


def grid_value(grid, p):
    if point_in_grid(grid, p):
        return grid[p[0]][p[1]]
    return None


def find_perimeter(region, grid):
    perim = []

    for p in region:
        p_value = grid_value(grid, p)
        for dy, dx in deltas:
            ny = p[0] + dy
            nx = p[1] + dx
            np = (ny, nx)
            if grid_value(grid, np) != p_value:
                perim.append(np)
    return perim


def solve_one(grid):
    visited = set()
    ans1 = 0
    ans2 = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            p = (y, x)
            if p not in visited:
                c = grid_value(grid, p)
                visited.add(p)
                region = find_region(grid, p, visited)
                perim = find_perimeter(region, grid)
                ans1 = ans1 + len(region) * len(perim)
                sides = find_sides2(grid, region, c)
                ans2 = ans2 + len(region) * sides
    return ans1, ans2


def remove_side(perim, p):
    if (p[0] - 1, p[1]) in perim or (p[0] + 1, p[1]) in perim:
        remove_in_dir(perim, p, 1, 0)
        remove_in_dir(perim, p, -1, 0)
        return

    if (p[0], p[1] - 1) in perim or (p[0], p[1] + 1) in perim:
        remove_in_dir(perim, p, 0, 1)
        remove_in_dir(perim, p, 0, -1)


def remove_in_dir(perim, point, dy, dx):
    p = point
    while True:
        p = (p[0] + dy, p[1] + dx)
        if p in perim:
            perim.remove(p)
        else:
            break


def find_sides(perim):
    cnt = 0
    while len(perim) > 0:
        point = perim.pop()
        remove_side(perim, point)
        cnt = cnt + 1
    return cnt


def find_sides2(grid, region, v):
    cnt = 0
    corners = [((1, 0), (0, 1), (1, 1)), ((1, 0), (0, -1), (1, -1)), ((-1, 0), (0, -1), (-1, -1)), ((-1, 0), (0, 1), (-1, 1))]
    for r in region:
        for c in corners:
            d1, d2, cr = c
            d1_value = grid_value(grid, (r[0] + d1[0], r[1] + d1[1]))
            d2_value = grid_value(grid, (r[0] + d2[0], r[1] + d2[1]))
            cr_value = grid_value(grid, (r[0] + cr[0], r[1] + cr[1]))
            if d1_value != v and d2_value != v:
                cnt = cnt + 1

            if d1_value == v and d2_value == v and cr_value != v:
                cnt = cnt + 1

    return cnt



with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    print(solve_one(grid))
    # print(solve_two(grid))