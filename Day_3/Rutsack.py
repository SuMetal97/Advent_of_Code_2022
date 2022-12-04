import string
import time
start_time = time.time()
values = {}

for x, y in zip(range(1, 27), string.ascii_lowercase):
    values[y] = x
for x, y in zip(range(27,54), string.ascii_uppercase):
    values[y] = x
total_part1 = 0
total_part2 = 0
elf = []

with open('input.txt', 'r') as file:
    for line in file:
        stripline = line.strip('\n')
        sack1 = stripline[0:len(stripline)//2]
        sack2 = stripline[(len(stripline)//2):len(stripline)]
        sack1 = set(sack1)
        sack2 = set(sack2)
        elf.append(stripline)
        matching_char = list(sack1 & sack2)
        total_part1 += values[matching_char[0]]
        if len(elf) == 3:
            elf1 = set(elf[0])
            elf2 = set(elf[1])
            elf3 = set(elf[2])
            matching_char = list(elf1 & elf2 & elf3)

            total_part2 += values[matching_char[0]]
            elf.clear()

print("total part 1: " + str(total_part1))
print("total part 2: " + str(total_part2))
print("--- %s seconds ---" % (time.time() - start_time))
