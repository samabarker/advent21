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
folds = [[655,0]]

for fold in folds:
    if fold[0] == 0:
        for point in initial_points:
            if point[1] > fold[1]:
                point[1] = fold[1]- abs(fold[1] - point[1])
    if fold[1] == 0:
        for point in initial_points:
            if point[0] > fold[0]:
                point[0] = fold[0]- abs(fold[0] - point[0])
    
print(initial_points)
unique_points = []
for item in initial_points:
    if item not in unique_points:
        unique_points.append(item)

print(len(unique_points))