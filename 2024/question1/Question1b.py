def solve_two(list_one, list_two):
    multiplier = {x: list_two.count(x) for x in list(set(list_two))}
    print(sum([x * multiplier.get(x, 0) for x in list_one]))


def solve_one(list_one, list_two):
    sorted_list_one = sorted(list_one)
    sorted_list_two = sorted(list_two)
    x = sum([abs(sorted_list_one[n] - sorted_list_two[n]) for n in range(len(list_one))])
    print(x)


with open('input.txt') as f:
    lines = f.readlines()
    first_list = [int(s.strip().split('   ')[0]) for s in lines]
    second_list = [int(s.strip().split('   ')[1]) for s in lines]
    solve_one(first_list, second_list)
    solve_two(first_list, second_list)
