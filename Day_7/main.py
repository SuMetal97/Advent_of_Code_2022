
import time
class Node:
    def __init__(self,key):
        self.prev = None
        self.next = []
        self.key = key
        self.value = 0


def make_Tree(root):
    with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripped_line = (line.strip('\n').split())
            if stripped_line[0] == '$':
                if stripped_line[1] == 'cd':
                    if stripped_line[2] == '..':
                        root = root.prev
                    else:
                        for i in root.next:
                            if i.key == stripped_line[2]:
                                i.prev = root
                                root = i
                                break
                elif stripped_line[1] == 'ls':
                    continue
            elif stripped_line[0] == 'dir':
                (root.next).append(Node(stripped_line[1]))
                
            else:
                root.value += int(stripped_line[0])

def Calculate_dir(root):
    next_node_values = 0
    for i in root.next:
        next_node_values += Calculate_dir(i)
    root.value = next_node_values + root.value
    
    return root.value

def Search_Dict(root, Part_1_Total):
    Part_1_Total = 0
    for i in root.next:
        Part_1_Total += Search_Dict(i, Part_1_Total)
    if  root.value <= 100000:
        Part_1_Total += root.value
    return Part_1_Total

def check_smallest(root):
    check = []
    for i in root.next:
        check.append(check_smallest(i))
    
    check.append(root.value)
    check.sort()
    if len(check) == 0:
        return 0
    else:
        while check[0] == 0 or check[0] < 208861:
            check.pop(0)
            if len(check) == 0:
                return 0
    return check[0]


def main():
    Part_1_Total = 0
    Part_2_Total = 0
    
    root = Node('/')
    make_Tree(root)
    Calculate_dir(root)
    Part_1_Total = Search_Dict(root, Part_1_Total)
    Part_2_Total = check_smallest(root)
    print("=============================")
    print("Part 1: " + str(Part_1_Total))
    print("Part 2: " + str(Part_2_Total))
    print("=============================")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
