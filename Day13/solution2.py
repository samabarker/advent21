#Function to import the input and format into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        new_item = item.split(',')
        new_item[0] = int(new_item[0])
        new_item[1] = new_item[1][:len(new_item[1])-1]
        new_item[1] = int(new_item[1])
        modified_list.append(new_item)
    return modified_list

initial_points = get_input('input.txt')
folds = [[655,0],[0,447],[327,0],[0,223],[163,0],[0,111],[81,0],[0,55],[40,0],[0,27],[0,13],[0,6]]

for fold in folds:
    if fold[0] == 0:
        for point in initial_points:
            if point[1] > fold[1]:
                point[1] = fold[1]- abs(fold[1] - point[1])
    if fold[1] == 0:
        for point in initial_points:
            if point[0] > fold[0]:
                point[0] = fold[0]- abs(fold[0] - point[0])
    
unique_points = []
for item in initial_points:
    if item not in unique_points:
        unique_points.append(item)

max_x = 0
max_y = 0
for item in unique_points:
    if item[0] > max_x:
        max_x = item[0]
    if item[1] > max_y:
        max_y = item[1]

grid = []
for i in range(0,max_y+1):
    grid.append([])
    for j in range(0, max_x+1):
        grid[i].append('.')

for point in unique_points:
    grid[point[1]][point[0]] = '#'

for item in grid:
    print(item)