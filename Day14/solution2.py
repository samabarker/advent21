#Convert inlet txt file into a list of strings
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    modified_list2 = []
    for item in content_list:
        separator_location = item.index('-')
        modified_list.append(item[:separator_location-1])
        modified_list2.append(item[separator_location+3:len(item)-1])
    return (modified_list, modified_list2)


instructions = get_input('input.txt')[0]
insertor = get_input('input.txt')[1]
input_str = 'KKOSPHCNOCHHHSPOBKVF'
itterations = 40

#Split input str pairs into list
input_list = []
input_list_nums = []
for i in range(0, len(input_str) - 1):
    input_list.append(input_str[i] + input_str[i+1])
    input_list_nums.append(1)

#Get pair combinations after each itteration
for i in range(0,itterations):
    new_list = []
    new_list_nums = []
    for item in input_list:
        to_insert = insertor[instructions.index(item)]
        item1 = item[0] + to_insert
        item2 = to_insert + item[1]
        if item1 not in new_list:
            new_list.append(item1)
            new_list_nums.append(input_list_nums[input_list.index(item)])
        else:
            new_list_nums[new_list.index(item1)] += input_list_nums[input_list.index(item)]
        if item2 not in new_list:
            new_list.append(item2)
            new_list_nums.append(input_list_nums[input_list.index(item)])
        else:
            new_list_nums[new_list.index(item2)] += input_list_nums[input_list.index(item)]
    input_list = new_list
    input_list_nums = new_list_nums

#Count time used first and second
letters = []
times_used = []
times_used2 = []
for item in input_list:
    if item[0] not in letters:
        letters.append(item[0])
        times_used.append(input_list_nums[input_list.index(item)])
        times_used2.append(0)
    else:
        times_used[letters.index(item[0])] += input_list_nums[input_list.index(item)]

for item in input_list:
    times_used2[letters.index(item[1])] += input_list_nums[input_list.index(item)]
    
#Find maximum from two above
max_times_used = []
for i in range(0, len(letters)):
    max_times_used.append(max(times_used[i], times_used2[i]))

#Print answer
print(letters)
print(max_times_used)
print(max(max_times_used) - min(max_times_used))
