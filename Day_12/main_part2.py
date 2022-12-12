import time
from collections import deque
start_time = time.time()
input = []

with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            stripline = list(stripline)
            input.append((stripline))
            
for r,i in enumerate(input):
    for c,spot in enumerate(i):
        if spot == "S":
            input[r][c] = "a"
        if spot == "E":
            end_row = r
            end_col = c
            input[r][c] = "z"

path = deque()
path.append((0,end_row, end_col))
locations_visited = {(end_row,end_col)}

while path:
    distance, row, column = path.popleft()

    for next_row, next_col in [(row+1, column), (row-1, +column),(row,column+1), (row,column-1) ]:

        if next_row >= (len(input)) or next_col >= len(input[0]) or next_col <0 or next_row <0 or (next_row, next_col) in locations_visited:
            continue

        if ord(input[next_row][next_col]) - ord(input[row][column]) <-1:
            continue

        if input[next_row][next_col] == "a":
            print(distance +1)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit(0)
        locations_visited.add((next_row, next_col))
        path.append((distance + 1, next_row,next_col))