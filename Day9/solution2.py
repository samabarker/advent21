#Function to import the input and format into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[:(len(item)-1)])
    return modified_list


#Recursion function for checking points in a basin
def checker(all_data, point, inpt_list, diff = 1):
    if diff == 0:
        return inpt_list    
    if inpt_list == []:
        inpt_list.append(point)
    new_list = []
    for item in inpt_list:
        current_x = item[1]
        current_y = item[0]
        #One up
        if current_y > 0:
            if all_data[current_y - 1][current_x] != "9":
                new_list.append([current_y - 1, current_x])
        #One down
        if current_y < (len(all_data) - 1):
            if all_data[current_y + 1][current_x] != "9":
                new_list.append([current_y + 1, current_x])
        #One left
        if current_x > 0:
            if all_data[current_y][current_x - 1] != "9":
                new_list.append([current_y, current_x - 1])
        #One right
        if current_x < (len(all_data[0]) - 1):
            if all_data[current_y][current_x + 1] != "9":
                new_list.append([current_y, current_x + 1])
    counter = 0
    for item in new_list:
        if item not in inpt_list:
            inpt_list.append(item)
            counter += 1
    
    if checker(all_data, point, inpt_list, counter) == inpt_list:
        return inpt_list
    else:
        checker(all_data, point, inpt_list, counter)


#Call above import function with input file
input_list = get_input('input.txt')

#Define some variables
number_of_rows = len(input_list)
number_of_columns = len(input_list[0])
low_points = []
basin_numbers = []
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

#Create a list of zeros associated with each low point
for i in range(0, len(low_points)):
    basin_numbers.append(0)

#Call recursion function and add number of points in each basin to basin numbers list
for i in range(0, len(low_points)):
    basin_points = checker(input_list, low_points[i], [])
    basin_numbers[i] = len(basin_points)

#Report the answer
basin_numbers.sort(reverse = True)
print(basin_numbers)
print(basin_numbers[0] * basin_numbers[1] * basin_numbers[2])









