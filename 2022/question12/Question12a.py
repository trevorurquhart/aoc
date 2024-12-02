def node_value(c):
    return 1 if c == 'S' else 26 if c == 'E' else ord(c) - 96


class Node:

    def __init__(self, idx, character):
        self.path = []
        self.adjacent_nodes = []
        self.character = character
        self.value = node_value(character)
        self.idx = idx
        self.visited = False

    def find_adjacent_nodes(self, data, x):
        if self.idx % x > 0 and self.can_move(n := data[self.idx - 1]):  # left
            self.adjacent_nodes.append(n)
        if self.idx % x < x - 1 and self.can_move(n := data[self.idx + 1]):  # right
            self.adjacent_nodes.append(n)
        if self.idx >= x and self.can_move(n := data[self.idx - x]):  # up
            self.adjacent_nodes.append(n)
        if self.idx + x < len(data) - 1 and self.can_move(n := data[self.idx + x]):  # down
            self.adjacent_nodes.append(n)

    def can_move(self, node):
        return self.value + 1 >= node.value

    def find_bf_path(self):
        queue = [self]

        while queue:
            n = queue.pop(0)
            if n.character == 'E':
                return n.path

            if not n.visited:
                for a in n.adjacent_nodes:
                    if not a.visited:
                        copy_of_path = [l for l in n.path]
                        copy_of_path.append(n)
                        a.path = copy_of_path
                        queue.append(a)
                n.visited = True


def parse_nodes(data, xlen):
    nodes = [Node(idx, c) for idx, c in enumerate(data)]
    for idx, n in enumerate(nodes):
        n.find_adjacent_nodes(nodes, xlen)
    return nodes


def solve_one(graph):
    start = graph[0]
    path = start.find_bf_path()
    print([p.character for p in path])
    print(len(path))


with open('question_data.txt') as q:
    qn_data = q.read().strip()
    xlen = qn_data.index("\n")
    data = list(qn_data.replace("\n", ""))
    solve_one(parse_nodes(data, xlen))
