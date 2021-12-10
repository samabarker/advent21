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
illegal_lines = []
legal_lines = []
all_closers = []
points = [1,2,3,4]
scores = []

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
                if item not in illegal_lines:
                    illegal_lines.append(item)
                break       

#Get list of legal lines
for item in input_list:
    if item not in illegal_lines:
        legal_lines.append(item)

#Find which closers are needed based on number of openers left over
for item in legal_lines:
    closers = []
    for i in range(0, len(item)):
        current_item = item[i]
        if current_item in ['(','[','{','<']:
            if current_item == '(':
                closer = ')'
            if current_item == '[':
                closer = ']'
            if current_item == '{':
                closer = '}'
            if current_item == '<':
                closer = '>'
            number_of_openers = 0
            number_of_closers = 0
            for j in range(i, len(item)):
                if item[j] == current_item:
                    number_of_openers += 1
                if item[j] == closer:
                    number_of_closers += 1
                if number_of_closers == number_of_openers:
                    break
            if number_of_closers != number_of_openers:
                closers.append(closer)
    all_closers.append(closers)

#Calculate score for each closer, sort and print middle value   
for item in all_closers:
    score = 0
    for i in range(len(item)-1, -1, -1):
        score = score * 5 + points[symbol_position.index(item[i])]
    scores.append(score)
scores.sort()
print(scores[int((len(scores)-1)/2)])