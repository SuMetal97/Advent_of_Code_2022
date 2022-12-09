import time
start_time = time.time()
head = [0,0]
tail = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
location_part1 = set()
location_part2 = set()

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
                
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            direction, amt = stripline.split()

            for i in range(int(amt)):
                #Set Head position "Easy Part"
                if direction == "U":
                    head[1] += 1
                elif direction == "D":
                    head[1] = head[1] - 1
                elif direction == "R":
                    head[0] += 1
                elif direction == "L":
                    head[0] = head[0] - 1
                else:
                    print("Error reading Direction!")
                    print(direction)

                #Set Tail tracking "Hard Part"
                tail[0][0], tail[0][1] =  calculate(head[0], head[1], tail[0][0], tail[0][1])
                tail[1][0], tail[1][1] =  calculate(tail[0][0], tail[0][1], tail[1][0], tail[1][1])
                tail[2][0], tail[2][1] =  calculate(tail[1][0], tail[1][1], tail[2][0], tail[2][1])
                tail[3][0], tail[3][1] =  calculate(tail[2][0], tail[2][1], tail[3][0], tail[3][1])
                tail[4][0], tail[4][1] =  calculate(tail[3][0], tail[3][1], tail[4][0], tail[4][1])
                tail[5][0], tail[5][1] =  calculate(tail[4][0], tail[4][1], tail[5][0], tail[5][1])
                tail[6][0], tail[6][1] =  calculate(tail[5][0], tail[5][1], tail[6][0], tail[6][1])
                tail[7][0], tail[7][1] =  calculate(tail[6][0], tail[6][1], tail[7][0], tail[7][1])
                tail[8][0], tail[8][1] =  calculate(tail[7][0], tail[7][1], tail[8][0], tail[8][1])
                
                location_part1.add(str(tail[0][0]) + str(tail[0][1]))
                location_part2.add(str(tail[8][0]) + str(tail[8][1]))
                
                
print("=========================")
print("--- %s seconds ---" % (time.time() - start_time))
print("Part_1_Solution :" + str(len(location_part1)))
print("Part_2_Solution :" + str(len(location_part2)))
print("=========================")
