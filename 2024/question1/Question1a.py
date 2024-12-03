with open('input.txt') as f:
    lines = f.readlines()
    firstList = sorted([int(s.strip().split('   ')[0]) for s in lines])
    secondList = sorted([int(s.strip().split('   ')[1]) for s in lines])
    x = sum([abs(firstList[n] - secondList[n]) for n  in range(len(firstList))])
    print(x)