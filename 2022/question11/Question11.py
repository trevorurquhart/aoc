import math


class Monkey:

    def __init__(self, items, operation, is_divisible_by, monkey1, monkey2):
        self.items = items
        self.op = operation
        self.is_divisible_by = is_divisible_by
        self.monkey1 = monkey1
        self.monkey2 = monkey2
        self.no_of_inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def throw(self, item, monkeys):
        target_monkey = self.monkey1 if item % self.is_divisible_by == 0 else self.monkey2
        monkeys[target_monkey].add_item(item)

    def inspect(self, monkeys, worry_fn):
        while self.items:
            self.no_of_inspections += 1
            item = worry_fn(self.op(self.items.pop(0)))
            self.throw(item, monkeys)


def parse_monkeys(data):
    monkeys = []
    for group in data.split("\n\n"):
        params = []
        for line in [l.strip() for l in group.split("\n")]:
            match line.split():
                case ["Starting", "items:", *items]:
                    params.append([int(item.replace(",", "")) for item in items])
                case ["Operation:", "new", "=", "old", "*", m]:
                    params.append((lambda x: x * x) if m == "old" else (lambda x, m=m: x * int(m)))
                case ["Operation:", "new", "=", "old", "+", a]:
                    params.append((lambda x: x + x) if a == "old" else (lambda x, a=a: x + int(a)))
                case ["Test:", "divisible", "by", s]:
                    params.append(int(s))
                case ["If", "true:", "throw", "to", "monkey", true_monkey]:
                    params.append(int(true_monkey))
                case ["If", "false:", "throw", "to", "monkey", false_monkey]:
                    params.append(int(false_monkey))
        monkeys.append(Monkey(*params))
    return monkeys


def solve(monkeys, rounds, worry_fn):
    for r in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys, worry_fn)
    ins = [m.no_of_inspections for m in monkeys]
    ins.sort()
    top, second = ins[-2:]
    print(top * second)


def solve_one(monkeys):
    solve(monkeys, 20, lambda x: x // 3)


def solve_two(monkeys):
    lcm = math.lcm(*[m.is_divisible_by for m in monkeys])
    solve(monkeys, 10000, lambda x: x % lcm)


with open('question_data.txt') as q:
    data = q.read()
    solve_one(parse_monkeys(data))
    solve_two(parse_monkeys(data))
