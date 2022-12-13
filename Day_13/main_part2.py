import time
start_time = time.time()

input = list(map(eval, open("input.txt").read().split()))

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
locations = [1,2]
for a in input:
    if compare(a, [[2]]) < 0:
        locations[0] += 1
        locations[1] += 1
    elif compare(a, [[6]]) < 0:
        locations[1] += 1

print("Total Part 2: " + str(locations[0] * locations[1]))
print("--- %s seconds ---" % (time.time() - start_time))