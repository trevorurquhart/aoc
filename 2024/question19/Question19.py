import functools


@functools.cache
def solve_pattern_all(remaining):

    if remaining == "":
        return 1

    cnt = 0
    for t in towels:
        if remaining.startswith(t):
            cnt += solve_pattern_all(remaining[len(t):])

    return cnt


@functools.cache
def solve_pattern_one(remaining):

    if remaining == "":
        return 1

    for t in towels:
        if remaining.startswith(t):
            if solve_pattern_one(remaining[len(t):]) == 1:
                return 1

    return 0


def solve_one():
    ans = 0
    for p in patterns:
        ans += solve_pattern_one(p)

    return ans

def solve_two():
    ans = 0
    for p in patterns:
        ans += solve_pattern_all(p)

    return ans


with open("input.txt") as f:
    towels = f.readline().strip().split(", ")
    patterns = [l.strip() for l in f.readlines()]
    print(solve_one())
    print(solve_two())

