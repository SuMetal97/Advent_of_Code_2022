your_moves = {'X':1, 'Y':2, 'Z':3}
elf_moves = {'A':1, 'B':2, 'C':3}
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        elf = line[0]
        me = line[2]
        if elf == 'A':
                    if me == 'X':
                        total += elf_moves['C'] + 0
                    elif me ==  'Y':
                        total += elf_moves['A'] + 3
                    elif me == 'Z':
                        total += elf_moves['B'] + 6
        elif elf == 'B':
                    if me == 'X':
                        total += elf_moves['A'] + 0
                    elif me == 'Y':
                        total += elf_moves['B'] + 3
                    elif me == 'Z':
                        total += elf_moves['C'] + 6
        elif elf == 'C':
                    if me ==  'X':
                        total += elf_moves['B'] + 0
                    elif me == 'Y':
                        total += elf_moves['C'] + 3
                    elif me ==  'Z':
                        total += elf_moves['A'] + 6

print(total)



















