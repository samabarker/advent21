import itertools

#Function to import the input and format into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        new_item = item.split('-')
        new_item[1] = new_item[1][:len(new_item[1])-1]
        modified_list.append(new_item)
    return modified_list

def get_caves(list_of_moves):
    caves = ['start']
    for item in(list_of_moves):
        if item[0] == 'end' and item[1].isupper():
            continue
        elif item[1] == 'end' and item[0].isupper():
            continue
        if item[0] != 'start' and item[0] != 'end' and (item[0] not in caves or item[0].isupper()):
            caves.append(item[0])
        if item[1] != 'start' and item[1] != 'end' and (item[1] not in caves or item[1].isupper()) :
            caves.append(item[1])
    caves.append('end')
    return(caves)

def get_first_nodes(list_of_moves):
    first_nodes = []
    for item in list_of_moves:
        if item[0] == 'start':
            first_nodes.append(item[1])
        if item[1] == 'start':
            first_nodes.append(item[0])
    return(first_nodes)

def get_last_nodes(list_of_moves):
    last_nodes = []
    for item in list_of_moves:
        if item[0] == 'end':
            last_nodes.append(item[1])
        if item[1] == 'end':
            last_nodes.append(item[0])
    return(last_nodes)

a = get_input('input.txt')
b = get_caves(a)
c = get_first_nodes(a)
d = get_last_nodes(a)

final_list = []
counter1 = 0

for i in range(1, len(b)+1):
    for item in (itertools.permutations(b,i)):
        if item[0] == 'start' and item[len(item)-1] == 'end' and item[1] in c and item[len(item)-2] in d:
            if ([item[0],item[1]] in a or [item[1],item[0]] in a) and ([item[len(item)-2],item[len(item)-1]] in a or [item[len(item)-1],item[len(item)-2]] in a) and item not in final_list:
                final_list.append(item)


for item in final_list:
    counter = 0
    for i in range(1,len(item)-1):
        if [item[i], item[i+1]] in a or [item[i+1], item[i]] in a:
            counter += 1
    if counter == len(item) - 2:
        counter1 += 1

print(counter1)