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
            start_row = r
            start_col = c
            input[r][c] = "a"
        if spot == "E":
            end_row = r
            end_col = c
            input[r][c] = "z"

path = deque()
path.append((0,start_row, start_col))
locations_visited = {(start_row,start_col)}

while path:
    distance, row, column = path.popleft()

    for next_row, next_col in [(row+1, column), (row-1, +column),(row,column+1), (row,column-1) ]:

        if next_row >= (len(input)) or next_col >= len(input[0]) or next_col <0 or next_row <0 or (next_row, next_col) in locations_visited:
            continue

        if ord(input[next_row][next_col]) - ord(input[row][column]) >1:
            continue

        if next_row == end_row and next_col == end_col:
            print(distance +1)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit(0)
        locations_visited.add((next_row, next_col))
        path.append((distance + 1, next_row,next_col))



