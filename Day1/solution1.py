#Function to turn input file into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(int(item[:(len(item)-1)]))
    return modified_list

#Test list
test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

#Set current case
list_to_use = get_input("input.txt")

#Count each time there is an increase between two consecutive values
counter = 0
for i in range(1,len(list_to_use)):
    if list_to_use[i-1] < list_to_use[i]:
        counter += 1

#Print result
print(counter)