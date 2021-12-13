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
    caves = []
    for item in(list_of_moves):
        if item[0] != 'start' and item[0] != 'end' and item[0] not in caves:
            caves.append(item[0])
        if item[1] != 'start' and item[1] != 'end' and item[1] not in caves :
            caves.append(item[1])
    caves.append('end')
    return(caves)

def check_legal(cave_visits):
    if cave_visits[0] != 'start':
        return False
    for i in range(0, len(cave_visits)):
        for j in range(0, len(cave_visits)):
            if cave_visits[i] == cave_visits[j] and i != j and cave_visits[j].islower():
                return False
    counter = 0
    for i in range(0, len(cave_visits)-1):
        if [cave_visits[i], cave_visits[i+1]] in a or [cave_visits[i+1], cave_visits[i]] in a:
            counter += 1
    if counter == len(cave_visits) - 1:
        return True
    else:
        return False

def recur(caves, cave_visits):
    global valid_routes
    for i in range(0,len(caves)):
        cave_visits.append(caves[i])
        if check_legal(cave_visits):
            if cave_visits[len(cave_visits)-1] == "end":
                valid_routes.append(cave_visits)
            recur(caves, cave_visits)
        cave_visits.pop()


a = get_input('input.txt')
b = get_caves(a)
valid_routes = []
recur(b,['start'])
print(len(valid_routes))

