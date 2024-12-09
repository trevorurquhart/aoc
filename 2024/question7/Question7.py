import itertools

combos = {}
operations = ['+', '*', '||']


def get_ans(c, ops):
    ans = ops[0]
    for idx in range(len(ops) - 1):
        op = c[idx]
        operation = operations[op]
        value = ops[idx + 1]
        if '+' == operation:
            ans = ans + value

        if '*' == operation:
            ans = ans * value

        if '||' == operation:
            ans = int(str(ans) + str(value))

    return ans


def solve_line(l, no_ops):
    split = l.split(": ")
    ans = int(split[0])
    ops = [int(o) for o in split[1].split(' ')]
    combinations = get_combos(no_ops, len(ops) - 1)
    for c in combinations:
        calc = get_ans(c, ops)
        if calc == ans:
            return ans

    return 0

# def multiply(ans, ops, n):
#     for i in range(len(ops)):
#         for n in range(len(ans)):
#             ans.

def solve_one(lines):
    ans = sum([solve_line(l, 2) for l in lines])
    print(ans)


def solve_two(lines):
    ans = sum([solve_line(l, 3) for l in lines])
    print(ans)


def get_combos(o, n):
    if (o, n) not in combos.keys():
        combos[(o, n)] = list(itertools.product(range(o), repeat = n))
    return combos[(o, n)]


with open('input.txt') as f:
    lines = f.readlines()
    stripped = [l.strip() for l in lines]
    print(stripped)
    solve_one(stripped)
    solve_two(stripped)






