input_list = [
    [5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6]
    ]

input_list = [
    [5,6,5,1,3,4,1,4,5,2],
    [1,3,8,1,5,4,1,2,5,2],
    [1,8,7,8,4,3,5,2,2,4],
    [6,8,1,4,8,3,1,5,3,5],
    [3,8,8,3,5,4,7,3,8,3],
    [6,4,7,3,5,4,8,4,6,4],
    [1,8,8,5,8,3,3,6,5,8],
    [3,7,3,2,5,8,4,7,5,2],
    [1,8,8,1,5,4,6,1,2,8],
    [5,1,2,1,7,1,7,7,7,6]
    ]


flashes = 0
itterations = 100

def checker(counter = 1):
    global input_list, flashes
    if counter == 0:
        return True
    counter = 0
    for i in range(0,len(input_list)):
        for j in range(0, len(input_list[i])):
            if input_list[i][j] > 9:
                flashes += 1
                input_list[i][j] = 0
                try:
                    if input_list[i-1][j] != 0 and (i-1) >= 0: 
                        input_list[i-1][j] +=1
                except:
                    pass
                try:
                    if input_list[i-1][j+1] != 0 and (i-1) >= 0:
                        input_list[i-1][j+1] += 1
                except:
                    pass
                try:
                    if input_list[i][j+1] != 0:
                        input_list[i][j+1] += 1
                except:
                    pass
                try: 
                    if input_list[i+1][j+1] != 0:
                        input_list[i+1][j+1] += 1
                except:
                    pass
                try:
                    if input_list[i+1][j] != 0:
                        input_list[i+1][j] += 1
                except:
                    pass
                try:
                    if input_list[i+1][j-1] != 0 and (j-1) >= 0:
                        input_list[i+1][j-1] += 1
                except:
                    pass
                try:
                    if input_list[i][j-1] != 0 and (j-1) >= 0:
                        input_list[i][j-1] += 1
                except:
                    pass
                try:
                    if input_list[i-1][j-1] != 0 and (j-1) >= 0 and (i-1) >= 0:
                        input_list[i-1][j-1] += 1
                except:
                    pass
    for i in range(0,len(input_list)):
        for j in range(0, len(input_list[i])):
            if input_list[i][j] > 9:
                counter += 1
    if checker(counter):
        return True
    else:
        checker(counter)


for k in range(0, itterations):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            input_list[i][j] += 1
    checker()

print(flashes)
