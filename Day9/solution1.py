#Function to import the input and format into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[:(len(item)-1)])
    return modified_list

#Call above function with input file
input_list = get_input('input.txt')

#Define some variables
number_of_rows = len(input_list)
number_of_columns = len(input_list[0])
low_points = []
total = 0

#Run comparison with a few rules for edge point
for i in range(0, number_of_rows):
    for j in range(0, number_of_columns):
        current_number = input_list[i][j]
        current_comparitors = []
        if i > 0:
            current_comparitors.append(input_list[i-1][j])
        if i < (number_of_rows-1):
            current_comparitors.append(input_list[i+1][j])
        if j > 0:
            current_comparitors.append(input_list[i][j-1])
        if j < (number_of_columns-1):
            current_comparitors.append(input_list[i][j+1])
        
        counter = 0
        for item in current_comparitors:
            if current_number >= item:
                counter += 1
        if counter == 0:
            low_points.append([i,j])

#Add each low point up and print total
for item in low_points:
    total += int(input_list[item[0]][item[1]]) + 1

print(total)