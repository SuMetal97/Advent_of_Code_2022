import time
start_time = time.time()
input = []
freq = []
freq_check = [20,60,100,140,180,220]
register = 1
clock = 0
Part_1_Total = 0
CRT_temp = []
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            temp = stripline.split()
            input.append(temp)



def compute_Frequency(clock, register, input):
    input.append(clock * register)
    return input

for i in input:
    if clock%40 == register or clock%40 == register -1 or clock%40 == register +1:
        CRT_temp.append('#')
    else:
        CRT_temp.append('.')
    if clock%40 == 39:
        print(''.join(CRT_temp))
        CRT_temp.clear()
    
    if i[0] == "noop":
        clock += 1
        for x in freq_check:
            if x == clock:
                freq = compute_Frequency(clock, register, freq)
    if i[0] == "addx":
        
        clock += 1
        for x in freq_check:
            if x == clock:
                freq = compute_Frequency(clock, register, freq)

        if clock%40 == register or clock%40 == register -1 or clock%40 == register +1:
            CRT_temp.append('#')
        else:
            CRT_temp.append('.')
        if clock%40 == 39:
            print(''.join(CRT_temp))
            CRT_temp.clear()

        clock += 1
        for x in freq_check:
            if x == clock:
                freq = compute_Frequency(clock, register, freq)
        register += int(i[1])
        

for i in freq:
    Part_1_Total += i
print("==========================")
print("Total Part 1: " + str(Part_1_Total))
print("=========================")
print("--- %s seconds ---" % (time.time() - start_time))