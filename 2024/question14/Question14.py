import re

class Robot:

    def __init__(self, x, y, vx, vy, maxx, maxy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.maxx = maxx
        self.maxy = maxy

    def move(self):
        nx = self.x + self.vx
        if nx > self.maxx:
            nx = nx - self.maxx - 1
        elif nx < 0:
            nx = self.maxx + nx + 1
        self.x = nx

        ny = self.y + self.vy
        if ny > self.maxy:
            ny = ny - self.maxy - 1
        elif ny < 0:
            ny = self.maxy + ny + 1
        self.y = ny

    def quadrant(self, halfx, halfy):

        if 0 <= self.x < halfx and 0 <= self.y < halfy:
            return 0

        if halfx < self.x and 0 <= self.y < halfy:
            return 1

        if 0 <= self.x < halfx and halfy < self.y:
            return 2

        if halfx < self.x and halfy < self.y:
            return 3

        return None

    def mark_grid(self, l):
        l[self.y][self.x] = 'X'

    def position(self):
        return self.x, self.y


def parse(lines, maxx, maxy):
    robots = []
    for l in lines:
        # p=0,4 v=3,-3
        x, y, vx, vy = [int(x) for x in re.findall("-*[0-9]+", l)]
        robots.append(Robot(x, y, vx, vy, maxx, maxy))
    return robots

def solve_one(lines, moves, maxx, maxy):
    robots = parse(lines, maxx, maxy)
    move_robots(robots, moves)

    qcnt = [0, 0, 0, 0]
    for robot in robots:
        q = robot.quadrant(maxx // 2, maxy // 2)
        if q is not None:
            qcnt[q] = qcnt[q] + 1
    print(qcnt)
    ans = 1
    for q in qcnt:
        ans *= q
    print(ans)


def solve_two(lines, maxx, maxy):
    robots = parse(lines, maxx, maxy)

    moves = 0
    while True:
        l = [list('.' * (maxx + 1)) for y in range(maxy + 1)]

        for r in robots:
          r.mark_grid(l)

        candidate = False
        for c in l:
            if 'XXXXXXXX' in ''.join(c):
                candidate = True

        if candidate:
            print(f'Moves: {moves}')
            print_grid(l)
            print(moves)
            return moves

        move_robots(robots, 1)
        moves = moves + 1

def print_grid(g):
    for l in g:
        print(''.join(l))


def move_robots(robots, moves):
    for i in range(moves):
        for robot in robots:
            robot.move()


with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    solve_two(lines,100, 102)