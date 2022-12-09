import time
start_time = time.time()
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
tail2_x = 0
tail2_y = 0
tail3_x = 0
tail3_y = 0
tail4_x = 0
tail4_y = 0
tail5_x = 0
tail5_y = 0
tail6_x = 0
tail6_y = 0
tail7_x = 0
tail7_y = 0
tail8_x = 0
tail8_y = 0
tail9_x = 0
tail9_y = 0


def calculate(front_x, front_y, back_x, back_y):
    if (abs(front_x - back_x) > 1) or (abs(front_y - back_y) > 1):
        if front_x >  back_x and front_y > back_y:
            back_x +=1
            back_y +=1
        elif front_x <  back_x and front_y > back_y:
            back_x = back_x - 1
            back_y += 1
        elif front_x >  back_x and front_y < back_y:
            back_x += 1
            back_y = back_y -1
        elif front_x <  back_x and front_y < back_y:
            back_x = back_x - 1
            back_y = back_y - 1
        elif front_x == back_x and front_y > back_y:
            back_y += 1
        elif front_x == back_x and front_y < back_y:
            back_y = back_y -1
        elif front_x > back_x and front_y == back_y:
            back_x += 1
        elif front_x < back_x and front_y == back_y:
            back_x = back_x -1
        else:
            print("Error Moving TAIL!!!!")
            print(direction)
            print(amt)
    return back_x, back_y
                
location_part1 = set()
location_part2 = set() #For the dict, use str(X,y) positions for key, keeps track of Tail, head "X"(Dont Care)
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            direction, amt = stripline.split()

            for i in range(int(amt)):
                #Set Head position "Easy Part"
                if direction == "U":
                    head_y += 1
                elif direction == "D":
                    head_y = head_y - 1
                elif direction == "R":
                    head_x += 1
                elif direction == "L":
                    head_x = head_x - 1
                else:
                    print("Error reading Direction!")
                    print(direction)

                #Set Tail tracking "Hard Part"
                tail_x, tail_y =  calculate(head_x, head_y, tail_x, tail_y)
                tail2_x, tail2_y =  calculate(tail_x, tail_y, tail2_x, tail2_y)
                tail3_x, tail3_y =  calculate(tail2_x, tail2_y, tail3_x, tail3_y)
                tail4_x, tail4_y =  calculate(tail3_x, tail3_y, tail4_x, tail4_y)
                tail5_x, tail5_y =  calculate(tail4_x, tail4_y, tail5_x, tail5_y)
                tail6_x, tail6_y =  calculate(tail5_x, tail5_y, tail6_x, tail6_y)
                tail7_x, tail7_y =  calculate(tail6_x, tail6_y, tail7_x, tail7_y)
                tail8_x, tail8_y =  calculate(tail7_x, tail7_y, tail8_x, tail8_y)
                tail9_x, tail9_y =  calculate(tail8_x, tail8_y, tail9_x, tail9_y)
                
                location_part1.add(str(tail_x) + str(tail_y))
                location_part2.add(str(tail9_x) + str(tail9_y))
                
                
print("=========================")
print("--- %s seconds ---" % (time.time() - start_time))
print("Part_1_Solution :" + str(len(location_part1)))
print("Part_2_Solution :" + str(len(location_part2)))
print("=========================")
