
import time
start_time = time.time()
input = list(map(str.splitlines, open("input.txt").read().strip().split("\n\n")))

def compare(a,b):
    if type(a) == int:
        if type(b) == int:
            return a-b
        else:
            return compare([a], b)
    else:
        if type(b) == int:
            return compare(a, [b])

    for top, bottom in zip(a,b):
        value = compare(top, bottom)
        if value:
            return value
    
    return len(a) - len(b)

Total_Part_1 = 0

for iterator, (a,b) in enumerate(input):
    if compare(eval(a),eval(b)) <0:
        Total_Part_1 += iterator + 1

print("Total Part 1: " + str(Total_Part_1))
print("--- %s seconds ---" % (time.time() - start_time))