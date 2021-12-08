#Convert inlet txt file into a list of strings
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    modified_list1 = []
    for item in content_list:
        separator_location = item.index('|')
        modified_list.append(item[:separator_location-1])
        modified_list1.append(item[separator_location+2:len(item)-1])
    return [modified_list, modified_list1]

positions = ['','','','','','','']
#  1111
# 2    3 
# 2    3
#  4444
# 5    6
# 5    6
#  7777

#Summation for end result
total = 0

#Pattern for each number 0-9, corresponding to positions above
numbers = [
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [1,0,1,1,0,1,1],
    [0,1,1,1,0,1,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [1,0,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]
]

#Get input data lists - both the input for determining letter combinations for each number, and the 4 output letter combinations for determining the answer
input_list = get_input('input.txt')[0]
input_list_list = []
output_list = []
for item in input_list:
    input_list_list.append(item.split())
for item in get_input('input.txt')[1]:
    output_list.append(item.split())

#Sort alphabetically - needed for comparison purposes later
for item in input_list_list:
    for i in range(0, len(item)):
        b = sorted(item[i])
        item[i] = ''.join(b)

for j, item in enumerate(input_list_list):
    one_four_seven_eight = ['','','','']
    five_letter_numbs = []
    six_letter_nums = []
    for i in item:
        if len(i) == 2:
            one_four_seven_eight[0] = i
        elif len(i) == 4:
            one_four_seven_eight[1] = i
        elif len(i) == 3:
            one_four_seven_eight[2] = i
        elif len(i) == 7:
            one_four_seven_eight[3] = i
        elif len(i) == 5:
            five_letter_numbs.append(i)
        elif len(i) == 6:
            six_letter_nums.append(i)

    #If in 7 but not in 1, must be position 1
    for letter in one_four_seven_eight[2]:
        if letter not in one_four_seven_eight[0]:
            positions[0] = letter
    #If in 4 and in all three five letter numbers, must be position 4
    for letter in one_four_seven_eight[1]:
        if letter in five_letter_numbs[0] and letter in five_letter_numbs[1] and letter in five_letter_numbs[2]:
            positions[3] = letter
    #If in 4 and in only one of the five letter numbers, must be position 2
    for letter in one_four_seven_eight[1]:
        counter = 0
        for i in five_letter_numbs:
            if letter in i:
                counter += 1
        if counter == 1:
            positions[1] = letter
    #If in 1 and in only two six letter numbers, must be position 3
    for letter in one_four_seven_eight[0]:
        counter = 0
        for i in six_letter_nums:
            if letter in i:
                counter += 1
        if counter == 2:
            positions[2] = letter
    #If in 1 and in all three six letter numbers, must be position 6
    for letter in one_four_seven_eight[0]:
        if letter in six_letter_nums[0] and letter in six_letter_nums[1] and letter in six_letter_nums[2]:
            positions[5] = letter
    #If in all three six letter numbers but not in 4 or 7, must be position 7
    for letter in 'abcdefg':
        if letter in six_letter_nums[0] and letter in six_letter_nums[1] and letter in six_letter_nums[2] and letter not in one_four_seven_eight[1] and letter not in one_four_seven_eight[2]:
            positions[6] = letter
    #If not in any position, put final letter in position:
    for letter in 'abcdefg':
        if letter not in positions:
            positions[4] = letter

    #Get which number is where for current line
    current_line_nums = []
    for i in item:
        current_number = [0,0,0,0,0,0,0]
        for letter in i:
            current_number[positions.index(letter)] = 1
        current_line_nums.append(numbers.index(current_number))

    #Get ouput number (4 long) as a str, then convert to int to add to total
    output = ''
    for i in output_list[j]:
        i_sorted = sorted(i)
        i = ''.join(i_sorted)
        output += str(current_line_nums[item.index(i)])
    total += int(output)

print(total)