import string
import time
Full_Elf_Task = []
total_part_1 = 0
total_part_2 = 0
start_time = time.time()
with open('input.txt', 'r') as file:
    for line in file:
        stripline = line.strip('\n').split(',')
        elf1_tasks = stripline[0].split('-')
        elf2_tasks = stripline[1].split('-')
        elf1_tasks = set(range(int(elf1_tasks[0]), int(elf1_tasks[1]) +1))
        elf2_tasks = set(range(int(elf2_tasks[0]), int(elf2_tasks[1])+1))
        Full_Elf_Task.append((elf1_tasks, elf2_tasks))
        

for i,j in Full_Elf_Task:
    if (((i-j) == set()) or ((j-i) == set())):
        total_part_1 += 1
    if(i & j):
        total_part_2 += 1
print("--- %s seconds ---" % (time.time() - start_time))
print(total_part_1)
print(total_part_2)




