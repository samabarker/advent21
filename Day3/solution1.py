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


#test_list = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
test_list = get_input('input.txt')
gamma = ''
epsilon = ''


#Determine gamma
for i in range(0,12):
    counter = 0
    for item in test_list:
        if item[i] == '1':
            counter += 1
    if counter > (len(test_list)/2):
        gamma += ('1')
    else:
        gamma += ('0')


#Determine epsilon from gamma
for item in gamma:
    if item == '1':
        epsilon += '0'
    else:
        epsilon += '1'


print(gamma, epsilon)
print(bin_to_dec(gamma), bin_to_dec(epsilon))
print(bin_to_dec(gamma) * bin_to_dec(epsilon))

