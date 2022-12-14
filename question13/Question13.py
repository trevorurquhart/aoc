from enum import Enum
import functools


class RightOrder(Enum):
    YES = -1
    NO = 1
    CONTINUE = 0


def right_order(a, b):
    if isinstance(a, list) and not isinstance(b, list):
        return right_order(a, [b])

    if not isinstance(a, list) and isinstance(b, list):
        return right_order([a], b)

    if isinstance(a, list):
        for idx, i in enumerate(a):
            if idx > len(b) - 1:
                return RightOrder.NO

            r = right_order(i, b[idx])
            if r != RightOrder.CONTINUE:
                return r
        return RightOrder.YES if len(a) < len(b) else RightOrder.CONTINUE

    if a < b:
        return RightOrder.YES

    if a > b:
        return RightOrder.NO

    if a == b:
        return RightOrder.CONTINUE


def solve_one(lines):
    packet_pairs = [[eval(a) for a in l.split('\n')] for l in lines.split('\n\n')]
    ok_packets = []
    for idx, pp in enumerate(packet_pairs):
        if right_order(pp[0], pp[1]) == RightOrder.YES:
            ok_packets.append(idx + 1)
    print(sum(ok_packets))


def rocmp(a, b):
    return right_order(a, b).value


def solve_two(lines):
    to_sort = [eval(l.strip()) for l in lines if l.strip() != '']
    div1 = [[2]]
    div2 = [[6]]
    to_sort.append(div1)
    to_sort.append(div2)
    x = sorted(to_sort, key=functools.cmp_to_key(rocmp))
    print((x.index(div2) + 1) * (x.index(div1) + 1))


with open('question_data.txt') as q:
    i = q.read()
    solve_one(i)

with open('question_data.txt') as q:
    lines = q.readlines()
    solve_two(lines)
