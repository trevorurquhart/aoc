def is_safe(values):
    diffs = [values[x + 1] - values[x] for x in range(len(values) - 1)]
    ok_diffs = [x for x in diffs
                 if (all(n > 0 for n in diffs) or all(n < 0 for n in diffs)) and
                     (1 <= abs(x) <= 3)]
    return len(diffs) == len(ok_diffs)


def is_safe_dampened(line):
    values = [int(x) for x in line.split(' ')]
    combos = [values] + [values[:i] + values[i+1 :] for i in range(len(values))]
    return any(is_safe(combo) for combo in combos)


def solve_one(lines):
    print(sum([1 if is_safe([int(x) for x in line.split(' ')]) else 0 for line in lines]))


def solve_two(lines):
    print(sum([1 if is_safe_dampened(line) else 0 for line in lines]))


with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    solve_two(lines)
