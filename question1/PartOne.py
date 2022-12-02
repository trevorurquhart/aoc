with open('data.txt') as f:
    maxCal = 0
    elf = 0

    for line in f:
        line = line.strip()
        if line == '':
            maxCal = max(elf, maxCal)
            elf = 0
        else:
            elf = elf + int(line)

    print(maxCal)
