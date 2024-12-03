with open('input.txt') as f:
    lines = f.readlines()
    firstList = [int(s.strip().split('   ')[0]) for s in lines]
    secondList = [int(s.strip().split('   ')[1]) for s in lines]
    multiplier = {x: secondList.count(x) for x in list(set(secondList))}
    print(sum([x * multiplier.get(x, 0) for x in firstList]))