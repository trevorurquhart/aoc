def priority(item):
    return ord(item) - (96 if item.islower() else 38)


def find_common_items(backpack):
    items = len(backpack) // 2
    return set(backpack[:items]).intersection(backpack[items:])


def find_badge(backpacks):
    return set.intersection(*[set(x) for x in backpacks])


def solve_one(lines):
    total = 0
    for line in lines:
        total += sum(map(priority, find_common_items(line)))
    print(total)


def solve_two(lines):
    total = 0
    group = []
    for line in lines:
        group.append(line)
        if len(group) == 3:
            total += priority(find_badge(group).pop())
            group.clear()

    print(total)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
