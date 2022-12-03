your_moves = {'X':1, 'Y':2, 'Z':3}
elf_moves = {'A':1, 'B':2, 'C':3}
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        elf = line[0]
        me = line[2]
        if elf == 'A':
                    if me == 'X':
                        total += your_moves[me] + 3
                    elif me ==  'Y':
                        total += your_moves[me] + 6
                    elif me == 'Z':
                        total += your_moves[me] + 0
        elif elf == 'B':
                    if me == 'X':
                        total += your_moves[me] + 0
                    elif me == 'Y':
                        total += your_moves[me] + 3
                    elif me == 'Z':
                        total += your_moves[me] + 6
        elif elf == 'C':
                    if me ==  'X':
                        total += your_moves[me] + 6
                    elif me == 'Y':
                        total += your_moves[me] + 0
                    elif me ==  'Z':
                        total += your_moves[me] + 3

print(total)



















