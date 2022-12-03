with open('input.txt', 'r') as file:
    cal = 0
    starving_elves = []

    for line in file:
        if line == '\n':
            starving_elves.append(cal)
            cal = 0
        else:
            cal += int(line.strip('\n'))
####sort elves######
starving_elves.sort()
print(starving_elves[len(starving_elves) - 1])