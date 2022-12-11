import time
start_time = time.time()
matrix = []
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            matrix.append([*stripline])
total_part_1 = 0
total_part_2 = 0
for rows in range(len(matrix)):
    for cols in range(len(matrix[rows])):
        point = matrix[rows][cols]
        if all(matrix[rows][x] < point for x in range(cols)) or all(matrix[rows][x] < point for x in range(cols+1, len(matrix[rows]))) or all(matrix[y][cols] < point for y in range(rows)) or all(matrix[y][cols] < point for y in range(rows+1, len(matrix))):
            total_part_1 +=1
for rows in range(len(matrix)):
    for cols in range(len(matrix[rows])):
        point = matrix[rows][cols]
        left=0
        right=0
        up=0
        down=0
        for i in range(cols-1, -1, -1):
            left += 1
            if matrix[rows][i] >= point:
                break 
        for i in range(cols +1, len(matrix[cols])):
            right += 1
            if matrix[rows][i] >= point:
                break 
        for i in range (rows-1, -1,-1):
            up += 1
            if matrix[i][cols] >= point:
                break
        for i in range(rows+1, len(matrix[rows])):
            down += 1
            if matrix[i][cols] >= point:
                break

        value = left*right*up*down
        total_part_2 = max(total_part_2,value)
print("==========================")
print("Total Part 1: " + str(total_part_1))
print("Total Part 2: " + str(total_part_2))
print("=========================")
print("--- %s seconds ---" % (time.time() - start_time))