from itertools import cycle

rocks = cycle((
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
))


def next_rock(top):
    return [[x + 2, y + top + 4] for x, y in next(rocks)]


def move_horizontally(rock, move):
    for c in rock:
        c[0] += move


def drop_one(rock):
    for c in rock:
        c[1] -= 1


def resting(rock, grid):
    return any([(x, y - 1) in grid for x, y in rock])


def can_move(rock, move, grid, top):
    for x, y in rock:
        to_check = x + move
        if to_check < 0 or to_check >= 7 or (y <= top and (to_check, y) in grid):
            return False
    return True


def add_rock_to_grid(rock, grid):
    grid.extend(rock)


def printn(s):
    print(s, end='')


def print_grid(grid):
    print('\n\n')
    top = max([y for x, y in grid])
    for y in range(top, -1, -1):
        for x in range(0, 7):

            if y == 0:
                if x == 0:
                    printn("+")
                printn("-")
                if x == 6:
                    print("+")
            else:
                if x == 0:
                    printn("|")

                if (x, y) in grid:
                    printn("#")
                else:
                    printn(".")

                if x == 6:
                    print("|")


def trim(grid, top):
    return [(x, y) for x, y in grid if top - y > 100]


def solve_one(gust):
    top = 0
    no_of_rocks = 0
    grid = [(x, 0) for x in range(7)]

    while no_of_rocks < 2022:

        rock = next_rock(top)
        trim(grid, top)
        while True:
            g = next(gust)
            move = (1 if g == ">" else - 1)

            if can_move(rock, move, grid, top):
                move_horizontally(rock, move)

            if resting(rock, grid):
                break

            drop_one(rock)

        add_rock_to_grid(rock, grid)
        print_grid(grid)

        no_of_rocks += 1
        top = max([y for x, y in grid])

    print(top)


with open('test_data.txt') as q:
    data = q.read().strip()
    solve_one(cycle(list(data)))
