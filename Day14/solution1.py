#Convert inlet txt file into a list of strings
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    modified_list2 = []
    for item in content_list:
        separator_location = item.index('-')
        modified_list.append(item[:separator_location-1])
        modified_list2.append(item[separator_location+3:len(item)-1])
    return (modified_list, modified_list2)


instructions = get_input('input.txt')[0]
insertor = get_input('input.txt')[1]
input_str = 'KKOSPHCNOCHHHSPOBKVF'
itterations = 10

#Generate the string
for i in range(0,itterations):
    new_str = input_str[0]
    for i in range(0,len(input_str)-1):
        new_str += insertor[instructions.index(input_str[i]+input_str[i+1])] + input_str[i+1]
    input_str = new_str

#Calulate times each letter used
letters = []
times_used = []

for item in input_str:
    if item not in letters:
        letters.append(item)
        times_used.append(1)
    else:
        times_used[letters.index(item)] += 1

#Print answer
print(letters)
print(times_used)
print(max(times_used) - min(times_used))
