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
#list_to_use = test_list

#Work out new list - sum of three consecutive items in the list_to_use
new_list = []
for i in range(0,len(list_to_use)-2):
    new_list.append(list_to_use[i] + list_to_use[i+1] + list_to_use[i+2])

#Set list_to_use to new_list so can reuse code from previous solution
list_to_use = new_list

#Count each time there is an increase between two consecutive values
counter = 0
for i in range(1,len(list_to_use)):
    if list_to_use[i-1] < list_to_use[i]:
        counter += 1

#Print result
print(counter)