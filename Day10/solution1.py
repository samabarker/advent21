#Function to import the input and format into a list
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[:(len(item)-1)])
    return modified_list

#Define some vars
input_list = get_input('input.txt')
symbol_position = [')',']','}','>']
char_amounts = [3,57,1197,25137]
total = 0
illegal_chars = []

#Search each line to check if chunk is complete or not
for item in input_list:
    number_of_symbols = [0,0,0,0]
    for i in range(0, len(item)):
        if item[i] == ')' or item[i] == ']' or item[i] == '}' or item[i] == '>':
            while True:
                for j in range(i, -1, -1):
                    if item[j] == "(":
                        number_of_symbols[0] -= 1
                    if item[j] == ")":
                        number_of_symbols[0] += 1
                    if item[j] == "[":
                        number_of_symbols[1] -= 1
                    if item[j] == "]":
                        number_of_symbols[1] += 1
                    if item[j] == "{":
                        number_of_symbols[2] -= 1
                    if item[j] == "}":
                        number_of_symbols[2] += 1
                    if item[j] == "<":
                        number_of_symbols[3] -= 1
                    if item[j] == ">":
                        number_of_symbols[3] += 1
                        
                    if number_of_symbols[symbol_position.index(item[i])] == 0:
                        break
                break
            if sum(number_of_symbols) != 0:
                illegal_chars.append(item[i])
                break         

#Add amount for each illegal character and print
for item in illegal_chars:
    total += char_amounts[symbol_position.index(item)]
print(total)
