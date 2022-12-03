def solve_one(lines):
    maxElf, current = 0, 0

    for line in lines:
        if line == '':
            maxElf = max(current, maxElf)
            current = 0
        else:
            current = current + int(line)

    print(maxElf)


def solve_two(lines):
    top_elves = [0] * 3
    current_elf = 0

    for line in lines:
        if line == '':
            if current_elf > (minElf := min(top_elves)):
                top_elves[top_elves.index(minElf)] = current_elf
            current_elf = 0
        else:
            current_elf += int(line)

    print(sum(top_elves))


with open('data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
