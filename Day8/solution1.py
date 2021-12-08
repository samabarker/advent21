#Convert inlet txt file into a list of strings
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        separator_location = item.index('|')
        modified_list.append(item[separator_location+2:len(item)-1])
    return modified_list


number_lengths = [2, 4, 3, 7] # for 1,4,7,8
counter = 0

input_list = get_input('input.txt')
input_list_list = []
for item in input_list:
    input_list_list.append(item.split())

for item in input_list_list:
    for i in item:
        if len(i) in number_lengths:
            counter += 1

print(counter)
