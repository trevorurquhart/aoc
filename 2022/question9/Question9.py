def sign(x):
    return -1 if x < 0 else 1


class Knot:

    def __init__(self, left, right):
        self.x = left
        self.y = right
        self.unique_moves = set()

    def move(self, direction):
        match direction:
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x -= 1
            case 'R':
                self.x += 1

    def follow(self, knot):

        v_dist = knot.y - self.y
        h_dist = knot.x - self.x

        if abs(v_dist) == 2:
            self.y += v_dist // 2
            self.x += 0 if self.x == knot.x else sign(h_dist)
        elif abs(h_dist) == 2:
            self.x += h_dist // 2
            self.y += 0 if self.y == knot.y else sign(v_dist)

        self.unique_moves.add((self.x, self.y))


def solve(cmds, size):
    knots = [Knot(0, 0) for i in range(size)]
    for cmd in cmds:
        direction, distance = cmd.split(" ")
        for i in range(int(distance)):
            to_follow = None
            for knot in knots:
                if to_follow is None:
                    knot.move(direction)
                else:
                    knot.follow(to_follow)
                to_follow = knot

    print(len(knots[size - 1].unique_moves))


with open('question_data.txt') as q:
    lines = [cmd.strip() for cmd in q.readlines()]
    solve(lines, 2)
    solve(lines, 10)
