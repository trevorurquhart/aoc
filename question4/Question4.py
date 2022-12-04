def one_range_fully_contained(range_one, range_two):
    return (range_one - range_two) == set() or (range_two - range_one) == set()


def ranges_overlap(range_one, range_two):
    return range_one & range_two != set()


def as_range(elf_range):
    lower, upper = elf_range.split("-")
    return set(range(int(lower), int(upper) + 1))


def solve(lines, fn):
    total = 0
    for line in lines:
        range_one, range_two = line.split(",")
        if fn(as_range(range_one), as_range(range_two)):
            total += 1
    print(total)


def solve_one(lines):
    solve(lines, one_range_fully_contained)


def solve_two(lines):
    solve(lines, ranges_overlap)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
