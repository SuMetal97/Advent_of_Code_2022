text_list = []
temp_list = []
temp_list_2 = []
Number_processed = 0
Number_processed_2 = 0
with open('input.txt', 'r') as file:
    for i in file.readlines():
        for char in i:
            if(len(temp_list) == 4):
                temp_list.pop()
            temp_list.insert(0,char)
            Number_processed += 1

            if(len(set(temp_list)) == len(temp_list) and len(set(temp_list)) == 14):
                break
        #Comment this for loop out for part1, for part 2 comments do not matter
        for char_2 in i:
            if(len(temp_list_2) == 14):
                temp_list_2.pop()
            temp_list_2.insert(0,char_2)
            Number_processed_2 += 1
            if(len(set(temp_list_2)) == len(temp_list_2) and len(set(temp_list_2)) == 14):
                break
    print(temp_list)
    print(Number_processed)

    print(temp_list_2)
    print(Number_processed_2)
