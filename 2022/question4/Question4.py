def one_range_fully_contained(range_one, range_two):
    return range_one.issubset(range_two) or range_two.issubset(range_one)


def ranges_overlap(range_one, range_two):
    return range_one & range_two != set()


def as_range(elf_range):
    lower, upper = map(int, elf_range.split("-"))
    return set(range(lower, upper + 1))


def solve(lines, fn):
    total = 0
    for line in lines:
        range_one, range_two = [as_range(r) for r in line.split(",")]
        if fn(range_one, range_two):
            total += 1
    print(total)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines, one_range_fully_contained)
    solve(lines, ranges_overlap)
