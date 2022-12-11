import time
start_time = time.time()
Monkey_business = [0,0,0,0,0,0,0,0]
temp_input = []
input = []
item_temp = []
Modulus = 5*2*13*19*11*3*7*17 #23*19*13*17
#{Monkey, [items], [operation], divisable test number, if true, if false}
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            stripline = stripline.split()
            if stripline[0] == "Monkey" and len(temp_input) > 0:
                input.append(temp_input[:])
                temp_input.clear()
            if stripline[0] == "Monkey":
                temp_input.append(stripline[1].strip(":"))
            elif stripline[0] == "Starting":
                for i in range(2, len(stripline)):
                    item_temp.append(stripline[i].strip(","))
                temp_input.append(item_temp[:])
                item_temp.clear()
            elif stripline[0] == "Test:":
                temp_input.append(stripline[3])
            elif stripline[0] == "If":
                temp_input.append(stripline[5])
            elif stripline[0] == "Operation:":
                temp_input.append([stripline[3],stripline[4],stripline[5]])
input.append(temp_input)

def calculation(input1, operation, input2):
    if operation == "*":
        return int(input1) * int(input2)
    elif operation == "divisible":
        return int(input1)/int(input2)
    elif operation == "+":
        return int(input1)+int(input2)
    elif operation == "-":
        return int(input1)-int(input2)

def check_divisable(number):
    if number%1 == 0:
        return True
    else:
        return False

for iterations in range(10000):                                                     #20 for part 1, 10000 for part 2
    for monkey in input:
        for item in monkey[1]:
            if monkey[2][0] == "old":
                item1 = item
            else:
                item1 = monkey[2][0]
            if monkey[2][2] == "old":
                item2 = item
            else:
                item2 = monkey[2][2]            
            value = calculation(item1, monkey[2][1], item2)
            #value = value/3                                                         #For Part 1 only
            if(check_divisable(calculation(value,"divisible", monkey[3]))):
                value %= Modulus                                                    #For part 2 only
                input[int(monkey[4])][1].append(value)
            else:
                value %= Modulus                                                    #For part 2 only
                input[int(monkey[5])][1].append(value)
            Monkey_business[int(monkey[0])] +=1
                
        monkey[1].clear()

Monkey_business.sort()
Total_Part_1 = int(Monkey_business[7]) * int(Monkey_business[6])
print("=========================")
print("--- %s seconds ---" % (time.time() - start_time))
print("Part 1/2 Solution:" + str(Total_Part_1))
print("=========================")