from collections import defaultdict


def anti_node(point, coords, max_x, max_y):
    an = set()
    for coord in coords:
        add_node(an, point, coord, max_x, max_y)
    return an


def add_node(nodes, point1, point2, max_x, max_y):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    add(nodes, point1, dx, dy, max_x, max_y)
    add(nodes, point2, -dx, -dy, max_x, max_y)


def add(nodes, point, dx, dy, max_x, max_y):
    i = 0
    while True:
        p1 = (point[0] + dx * i, point[1] + dy * i)
        if in_grid(max_x, max_y, p1):
            nodes.add(p1)
        else:
            break
        i = i + 1


def in_grid(no_col, max_y, p1):
    return 0 <= p1[0] < no_col and 0 <= p1[1] < max_y


def find_anti_nodes(nodes, coord, no_col, max_y):
    antennas = coord.copy()
    while len(antennas) >= 2:
        point = antennas.pop()
        nodes.update(anti_node(point, antennas, no_col, max_y))
    return nodes


def solve_two(data, max_x, max_y):
    antennas = parse(data, max_x)
    nodes = set()
    for antenna, coord in antennas.items():
        find_anti_nodes(nodes, coord, max_x, max_y)
    print(nodes)
    print(len(nodes))


def parse(data, max_x):
    chars = defaultdict(list)
    for idx, c in enumerate(data):
        if not (c == '.'):
            chars[c].append(divmod(idx, max_x))
    return chars


with open('input.txt') as f:
    data = f.read()
    max_x = data.index('\n')
    stripped = data.replace('\n', '')
    max_y = len(stripped) // max_x

    solve_two(stripped, max_x, max_y)