def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[:(len(item)-1)])
    return modified_list

#Import data
data_list = get_input("input.txt")
#data_list = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

#Initialise some variables
x = 0
y = 0
aim = 0

#Loop through getting first item in str (letter) and last item in str (number) and do relevent mathematics
for item in data_list:
    move_amount = int(item[len(item) - 1])
    if item[0] == 'f':
        x += move_amount
        y += (move_amount * aim)
    elif item[0] == 'd':
        aim += move_amount
    elif item[0] == 'u':
        aim -= move_amount

print(x*y)
