#Find minimum unvisited node
def get_current_min_node(node_map):
    current_min = [0,0]
    for i in range(0, len(node_map)):
        for j in range(0, len(node_map[0])):
            if node_map[i][j][1] < node_map[current_min[0]][current_min[1]][1] and node_map[i][j][0] == 0:
                current_min = [i,j]
    return current_min

#Convert inlet txt file into a list of ints
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        this_line = []
        for i in range(0,len(item)-1):
            this_line.append(int(item[i]))
        modified_list.append(this_line)
    return modified_list 

#Import data as above
input_list = get_input('input.txt')

#Create route matrix. Set [0,0] node value to 0 and all others to 10000
route_graph = []
for i in range(0, len(input_list)):
    current_row = []
    for j in range(0,len(input_list[i])):
        current_row.append([0,10000])
    route_graph.append(current_row)
route_graph[0][0] = [0,0]

#Run Dijkstras algorithm
while True:
    current_min = get_current_min_node(route_graph)
    if current_min[0] > 0:
        to_add = input_list[current_min[0]-1][current_min[1]]
        if route_graph[current_min[0]][current_min[1]][1] + to_add < route_graph[current_min[0]-1][current_min[1]][1] and route_graph[current_min[0]-1][current_min[1]][0] == 0:
            route_graph[current_min[0]-1][current_min[1]][1] = route_graph[current_min[0]][current_min[1]][1] + to_add
    if current_min[0] < len(route_graph)-1:
        to_add = input_list[current_min[0]+1][current_min[1]]
        if route_graph[current_min[0]][current_min[1]][1] + to_add < route_graph[current_min[0]+1][current_min[1]][1] and route_graph[current_min[0]+1][current_min[1]][0] == 0:
            route_graph[current_min[0]+1][current_min[1]][1] = route_graph[current_min[0]][current_min[1]][1] + to_add
    if current_min[1] > 0:
        too_add = input_list[current_min[0]][current_min[1]-1]
        if route_graph[current_min[0]][current_min[1]][1] + to_add < route_graph[current_min[0]][current_min[1]-1][1] and route_graph[current_min[0]][current_min[1]-1][0] == 0:
            route_graph[current_min[0]][current_min[1]-1][1] = route_graph[current_min[0]][current_min[1]][1] + to_add
    if current_min[1] < len(route_graph[0])-1:
        to_add = input_list[current_min[0]][current_min[1]+1]
        if route_graph[current_min[0]][current_min[1]][1] + to_add < route_graph[current_min[0]][current_min[1]+1][1] and route_graph[current_min[0]][current_min[1]+1][0] == 0:
            route_graph[current_min[0]][current_min[1]+1][1] = route_graph[current_min[0]][current_min[1]][1] + to_add
    route_graph[current_min[0]][current_min[1]][0] = 1
    route_graph[current_min[0]][current_min[1]][1] = 10000

    if route_graph[len(route_graph)-1][len(route_graph[0])-1][1] != 10000:
        break

#Print final answer
print(route_graph[len(route_graph)-1][len(route_graph[0])-1][1])