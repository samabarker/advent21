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
    lowers = []
    lowers_counter = []
    for cave in cave_visits:
        if cave.islower():
            if cave in lowers:
                lowers_counter[lowers.index(cave)] += 1
            else:
                lowers.append(cave)
                lowers_counter.append(1)
    if 'start' in lowers and lowers_counter[lowers.index('start')] > 1:
        return False
    if 'end' in lowers and lowers_counter[lowers.index('end')] > 1:
        return False
    counter = 0
    for item in lowers_counter:
        if item > 1:
            counter += 1
    if counter > 1:
        return False
    for item in lowers_counter:
        if item > 2:
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


