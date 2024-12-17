import re


def solve(lines, offset = 0):
    cnt = 0
    cost = 0
    for line in lines:
        axs = re.search("(Button [A-B]?|Prize): X(?:\+|\=)([0-9]+), Y(?:\+|\=)([0-9]+)", line)
        if axs:
            cnt = cnt + 1
            prefix = axs.group(1)
            if prefix == "Button A":
                ax = int(axs.group(2))
                ay = int(axs.group(3))
            elif prefix == "Button B":
                bx = int(axs.group(2))
                by = int(axs.group(3))
            elif prefix == "Prize":
                px = int(axs.group(2)) + offset
                py = int(axs.group(3)) + offset

            if cnt > 0 and cnt % 3 == 0:
                b = (px * ay - ax * py) / (bx * ay - ax * by)
                a = (px - bx * b) / ax

                if b % 1 == 0 and a % 1 == 0:
                    cost = cost + 3 * a + b

    print(cost)


with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    solve(lines)
    solve(lines, 10000000000000)