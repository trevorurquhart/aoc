class Node:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.neighbours = []
        self.previous_visited = []


def find_nodes(n, idx, data, x):
    nodes = []
    n_value = node_value(n)

    if idx % x > 0 and can_move(data, idx - 1, n_value):  # left
        nodes.append(idx - 1)
    if idx % x < x - 1 and can_move(data, idx + 1, n_value):  # right
        nodes.append(idx + 1)
    if idx >= x and can_move(data, idx - x, n_value):  # up
        nodes.append(idx - x)
    if idx + x < len(data) - 1 and can_move(data, idx + x, n_value):  # down
        nodes.append(idx + x)

    return nodes


def can_move(data, idx, n_value):
    return n_value + 1 >= node_value(data[idx])


def node_value(c):
    return 1 if c == 'S' else 26 if c == 'E' else ord(c) - 96


def parse_graph(data, xlen):
    # graph = [[1 if c == 'S' else 26 if c == 'E' else ord(c) - 96 for c in list(line)] for line in data.split("\n")]
    nodes = []
    for idx, n in enumerate(data):
        nodes.append(find_nodes(n, idx, data, xlen))
    return nodes


def find_path(data, nodes, start):
    visited = [False] * len(data)
    previous = [None] * len(data)
    queue = [start]
    while queue:
        n = queue.pop(0)
        if data[n] == 'E':
            p = n
            path = [p]
            while previous[p] is not None:
                p = previous[p]
                path.append(p)

            return path

        if not visited[n]:
            next_nodes = nodes[n]
            for x in next_nodes:
                if not visited[x]:
                    previous[x] = n
            queue.extend(next_nodes)
            visited[n] = True
    return None


def solve_one(data, graph):
    start = data.index('S')
    path = find_path(data, graph, start)
    print(len(path) - 1)


def solve_two(data, graph):
    start_points = [i for i, x in enumerate(data) if x in ("a", "S")]
    paths = [find_path(data, graph, s) for s in start_points]
    print(min(len(p) - 1 for p in paths if p is not None))


with open('question_data.txt') as q:
    qn_data = q.read().strip()
    xlen = qn_data.index("\n")
    data = list(qn_data.replace("\n", ""))
    graph = parse_graph(data, xlen)

    solve_one(data, graph)
    solve_two(data, graph)
