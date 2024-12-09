def parse(l):
    i = []
    for idx, n in enumerate(int (x) for x in l):
        value = [str(idx // 2)] * n if idx % 2 == 0 else '.' * n
        i.extend(list(value))
    return i


def next_l(inputs, l):
    try:
        return inputs.index('.', l)
    except ValueError:
        return -1


def next_r(inputs, r):
    for i in range(r, -1, -1):
        if inputs[i] != '.':
            return i
    return -1


def compact(inputs):
    cnt = len(inputs)
    r = cnt - 1
    l = 0
    while True:
        if l >= cnt or l >= r:
            break

        l = next_l(inputs, l)
        r = next_r(inputs, r)

        if l >= 0 and r >= 0 and l < r:
            inputs[l], inputs[r] = inputs[r], inputs[l]


def next_l2(inputs, l, len, max_l):
    l1 = next_l(inputs, l)

    if l1 == -1 or l1 > max_l:
        return -1, -1

    i = 1
    while i < len and inputs[l1 + i] == '.':
        i = i + 1

    if i == len:
        return l1, l1 + i - 1

    return next_l2(inputs, l1 + i, len, max_l)


def next_r2(inputs, r):
    r2 = next_r(inputs, r)
    if r2 == -1:
        return -1, -1

    n = inputs[r2]
    r1 = r2
    while r1 >= 0 and inputs[r1 - 1] == n:
        r1 = r1 - 1

    return r1, r2


def compact2(inputs):
    cnt = len(inputs)
    r1, r2 = cnt, cnt
    l = 0
    while True:
        r1, r2 = next_r2(inputs, r1 - 1)
        if r1 == -1:
            break

        size = r2 - r1 + 1
        l1, l2 = next_l2(inputs, 0, size, r1)

        if l1 >= 0 and r1 >= 0 and l1 < r1:
            inputs[l1 : l2 + 1], inputs[r1 : r2 + 1] = inputs[r1 : r2 + 1], inputs[l1 : l2 + 1]


def checksum(inputs):
    return sum([ idx * int(x) for idx, x in enumerate(inputs) if x != '.'])


def solve_one(l):
    inputs = parse(l)
    compact(inputs)
    print(checksum(inputs))


def solve_two(l):
    inputs = parse(l)
    compact2(inputs)
    print(checksum(inputs))


with open('input.txt') as f:
    l = f.read()
    solve_one(l)
    solve_two(l)
