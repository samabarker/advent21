def convert_input(filename):
    input_return = []
    fp = open(filename)
    for line in fp:
        first_comma = line.index(',')
        second_comma = first_comma + line[first_comma+1:].index(',') + 1
        arrow_point = line.index('>')
        current = [[int(line[0:first_comma]),int(line[first_comma+1:arrow_point-2])],[int(line[arrow_point+2:second_comma]), int(line[second_comma+1:])]]
        input_return.append(current)
    fp.close()
    return input_return


def check_ori(input_list):
    input_return = []
    for item in input_list:
        if (item[0][0] == item[1][0]):
            input_return.append('h')
        elif (item[0][1] == item[1][1]):
            input_return.append('v')
        else:
            input_return.append('d')
    return input_return


def get_max_numbs(input_list):
    max_x = 0
    max_y = 0
    for i in range(0,len(input_list)):
        if input_list[i][0][0] > max_x:
            max_x = input_list[i][0][0]
        if input_list[i][1][0] > max_x:
            max_x = input_list[i][1][0]
        if input_list[i][0][1] > max_y:
            max_y = input_list[i][0][1]
        if input_list[i][1][1] > max_y:
            max_y = input_list[i][1][1]
    return [max_x, max_y]


def create_map(input_coordinates):
    input_return = []
    for i in range(0,input_coordinates[1] + 1):
        rows = []
        for j in range(0, input_coordinates[0] + 1):
            rows.append(0)
        input_return.append(rows)
    return(input_return)


def add_routes(map, routes, v_h):
    for i in range(0, len(routes)):
        if v_h[i] == 'h':
            for j in range(routes[i][0][1],routes[i][1][1]+1):
                map[j][routes[i][1][0]] += 1
            for j in range(routes[i][1][1],routes[i][0][1]+1):
                map[j][routes[i][1][0]] += 1
        if v_h[i] == 'v':
            for j in range(routes[i][0][0],routes[i][1][0]+1):
                map[(routes[i][0][1])][j] += 1
            for j in range(routes[i][1][0],routes[i][0][0]+1):
                map[(routes[i][0][1])][j] += 1
        if v_h[i] == 'd':
            x_dir = 1
            y_dir = 1
            if routes[i][0][0] > routes[i][1][0]:
                x_dir = -1
            if routes[i][0][1] > routes[i][1][1]:
                y_dir = -1
            for j in range(0, abs(routes[i][0][0] - routes[i][1][0]) + 1):
                map[routes[i][0][1] + y_dir * j][routes[i][0][0] + x_dir * j] += 1
    return(map)


def check_map(map):
    counter = 0
    for i in range(0, len(map)):
        for j in range(0,len(map[i])):
            if map[i][j] > 1:
                counter += 1
    return counter


a = convert_input('input.txt')
b = check_ori(a)
c = get_max_numbs(a)
d = create_map(c)
e = add_routes(d,a,b)
f = check_map(e)

print(f)
