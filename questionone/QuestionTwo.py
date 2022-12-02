with open('data.txt') as f:
    maxCal = 0
    elfs = [0] * 3
    currElfCal = 0

    for line in f:
        line = line.strip()
        if line == '':
            if currElfCal > (minElf := min(elfs)):
                elfs[elfs.index(minElf)] = currElfCal
            currElfCal = 0
        else:
            currElfCal += int(line)
    print(sum(elfs))
