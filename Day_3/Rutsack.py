import string
values = {}

for x, y in zip(range(1, 27), string.ascii_lowercase):
    values[y] = x
for x, y in zip(range(27,54), string.ascii_uppercase):
    values[y] = x
total_part1 = 0
total_part2 = 0
elf = []
tracker = 0
with open('input.txt', 'r') as file:
    for line in file:
        stripline = line.strip('\n')
        sack1 = stripline[0:len(stripline)//2]
        sack2 = stripline[(len(stripline)//2):len(stripline)]
        elf.append(stripline)
        for item in sack1:
            if item in sack2:
                total_part1 += values[item]
                break
        check = False
        if len(elf) == 3:
            for item1 in elf[0]:
                if check:
                    break
                for item2 in elf[1]:
                    if check:
                        break
                    for item3 in elf[2]:
                        if item1 == item2 == item3:
                            total_part2 += values[item1]
                            check = True
                            break
            tracker = 0
            elf.clear()

print("total part 1: " + str(total_part1))
print("total part 2: " + str(total_part2))

