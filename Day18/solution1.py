from math import floor, ceil


def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[0:len(item)-1])
    return modified_list 


def concat(item1, item2):
    return '[' + item1 + ',' + item2 + ']'


def explode(string):
    while True:
        counter = 0
        pos = 0
        for i in range(0, len(string)):
            if string[i] == '[':
                counter += 1
            elif string[i] == ']':
                counter += -1
            if counter == 5:
                pos = i
                break
        if pos > 0:
            open_bracket = pos
            separator = open_bracket + string[open_bracket:].index(',')
            close_bracket = open_bracket + string[open_bracket:].index(']')
            first_num = int(string[open_bracket+1:separator])
            second_num = int(string[separator+1:close_bracket])
            left_num_pos = -1
            left_num_double = 0
            right_num_pos = -1
            right_num_double = 0
            for i in range(open_bracket,-1,-1):
                if string[i].isdigit():
                    left_num_pos = i
                    if string[i-1].isdigit():
                        left_num_double = 1
                    break
            for i in range(close_bracket+1,len(string)):
                if string[i].isdigit():
                    right_num_pos = i
                    if string[i+1].isdigit():
                        right_num_double = 1
                    break
            new_str = ''
            if left_num_pos == -1:
                new_str += string[0:open_bracket] + '0'
            elif left_num_pos != -1:
                new_str += string[0:left_num_pos-left_num_double] + str(first_num + int(string[left_num_pos-left_num_double:left_num_pos+1])) + string[left_num_pos+1:open_bracket] + '0'
            if right_num_pos == -1:
                new_str += string[close_bracket+1:]
            elif right_num_pos != -1:
                new_str += string[close_bracket+1:right_num_pos] + str(second_num + int(string[right_num_pos:right_num_pos+right_num_double+1])) + string[right_num_pos+right_num_double+1:]
            return (new_str)
        else:
            return False


def split(string):
    more_than_ten_pos = -1
    for i in range(0, len(string)-1):
        if string[i].isdigit() and string[i+1].isdigit():
            more_than_ten_pos = i
            break
    if more_than_ten_pos == -1:
        return False
    else:
        new_str = string[0:more_than_ten_pos] + '[' + str(floor((int(string[more_than_ten_pos:more_than_ten_pos+2])/2))) + ',' + str(ceil((int(string[more_than_ten_pos:more_than_ten_pos+2])/2))) + ']' + string[more_than_ten_pos+2:]
        return new_str
    

def magnitude(string):
    try:
        return(int(string))
    except:
        new_str = ''
        for i in range(0, len(string)-1):
            if string[i+1].isdigit():
                digit_len = 1
                for j in range(i+2,len(string)):
                    if string[j].isdigit():
                        digit_len += 1
                    else:
                        break
                if string[i+1+digit_len+1].isdigit():
                    second_digit_len = 1
                    for j in range(i+1+digit_len+1+1, len(string)):
                        if string[j].isdigit():
                            second_digit_len += 1
                        else:
                            break
                    break
        new_str = string[0:i] + str(3*int(string[i+1:i+1+digit_len]) + 2*int(string[i+1+digit_len+1:i+1+digit_len+1+second_digit_len])) + string[i+1+digit_len+1+second_digit_len+1:]
        
        if isinstance(magnitude(new_str),int):
            return magnitude(new_str)
        else:
            magnitude(new_str)
            

input_list = get_input('input.txt')
current_str = input_list[0]

for i in range(1,len(input_list)):
    current_str = concat(current_str, input_list[i])
    while True:
        if explode(current_str):
            current_str = explode(current_str)
        elif split(current_str):
            current_str = split(current_str)
        else:
            break

print(magnitude(current_str))
