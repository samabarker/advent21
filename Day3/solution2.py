#Convert inlet txt file into a list of strings
def get_input(input_file):
    my_file = open(input_file, "r")
    content_list = my_file. readlines()
    modified_list = []
    for item in content_list:
        modified_list.append(item[:(len(item)-1)])
    return modified_list


#Convert binary to decimal
def bin_to_dec(bin):
    conversions = [2048,1024,512,256,128,64,32,16,8,4,2,1]
    current_val = 0
    for i in range(0, len(bin)):
        if bin[i] == '1':
            current_val += conversions[i]
    return current_val


#Reccursion function
def selection(position,lst, pos):
    
    #Escape clause
    if len(lst) == 1:
        return lst

    #Figure out whether we are using 1 or 0 as our maximum/minumum
    ones = 0
    zeros = 0
    for item in lst:
        if item[position] == '1':
            ones += 1
        else:
            zeros += 1
    if ones >= zeros and pos == 1:
        number = '1'
    elif ones < zeros and pos == 1:
        number = '0'
    elif ones >= zeros and pos == 0:
        number = '0'
    else:
        number = '1'
    
    #Create output list of correct answers
    output = []
    for item in lst:
        if item[position] == number:
            output.append(item)

    #If output of next itteration is a list of length 1, return this list of length 1, else do next itteration
    if len(selection(position+1,output,pos)) == 1:
        return selection(position+1,output,pos)
    else:
        selection(position+1,output,pos)


#Run the program
test_list = get_input('input.txt')
o2 = bin_to_dec(selection(0,test_list,1)[0])
co2 = bin_to_dec(selection(0,test_list,0)[0])
print(o2 * co2)

