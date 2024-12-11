import math
import functools


@functools.cache
def get_divisor(digits):
    return int(math.pow(10, digits // 2))


def solve_one(line, blinks):
    cnt = 0
    for c in line:
        cnt = cnt + blink_n(c, blinks)
    return cnt


@functools.cache
def blink_n(c, n):
    # print(f'c: {c}, n:{n}')
    result = blink(c)
    if n - 1 == 0:
        return len(result)

    return sum([blink_n(x, n - 1) for x in result])


@functools.cache
def blink(c):
    if c == 0:
        return [1]

    digits = int(math.log10(c))+1
    if digits % 2 == 0:
        divisor = get_divisor(digits)
        n1 = c // divisor
        n2 = c % divisor
        return [n1, n2]

    else:
        return [c * 2024]


with open("input.txt") as f:
    line = [int(x) for x in f.read().split(' ')]
    ans_one = solve_one(line, 75)
    print(ans_one)
