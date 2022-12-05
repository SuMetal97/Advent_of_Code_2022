import time

stacks = [[],[],[],[],[],[],[],[],[]]
stacks_part2 =[]
movelist = []
temp = []
tempstack = []
stripline = ""
full_stack= []
internal = 0
external = 0
iterator = 0
start_time = time.time()
with open('input.txt', 'r') as file:
    stackfile = file.readlines()
    for i in stackfile[0:9]:
        stripline = i.strip('\n')
        stripline = stripline.replace("]",'')
        stripline = stripline.replace("[",'')
        full_stack.append(stripline.split(' '))

    for i in full_stack:
        external = 0
        for char in i:
            if char == '':
                if internal == 3:
                    internal = 0
                    if(i[iterator+1] == None):
                        continue
                    else:
                        external += 1
                else:
                    internal +=1
            else:
                internal = 0
                
                stacks[external].append(char)
                external += 1
            iterator +=1
        iterator = 0
    for i in stacks:
        i.pop()
        i= i.reverse()

    for i in stackfile[10:]:
        stripline = i.strip("\n")
        stripline = stripline.replace("from", ' ')
        stripline = stripline.replace("move", ' ')
        stripline = stripline.replace("to", ' ').split(' ')
        temp.clear()
        for move in stripline:
            if move == " " or move == '' or move == None:
                continue
            else:
                temp.append(move)
                internal +=1
        movelist.append(temp[:])

    for i in stacks:
        stacks_part2.append(i[:])

    for line in movelist:
        for i in range(0, int(line[0])):
            stacks[int(line[2])-1].append(stacks[int(line[1]) - 1].pop())
    
    for line in movelist:
        for i in range(0, int(line[0])):
            tempstack.append(stacks_part2[int(line[1]) - 1].pop())

        for i in range(0, int(line[0])):
            stacks_part2[int(line[2])-1].append(tempstack.pop())
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print("Part 1:")
    for i in stacks:
        print(i)
    
    print("\nPart 2:")
    for i in stacks_part2:
        print(i)