with open('data.txt') as f:
    maxCal = 0
    topElves = [0] * 3
    currElfCal = 0

    for line in f:
        line = line.strip()
        if line == '':
            if currElfCal > (minElf := min(topElves)):
                topElves[topElves.index(minElf)] = currElfCal
            currElfCal = 0
        else:
            currElfCal += int(line)
    print(sum(topElves))
