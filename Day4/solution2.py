#Convert input into list of bingo cards
def convert_input(filename):
    fp = open(filename)
    box_counter = 1
    for i, line in enumerate(fp):
        if len(line) == 1:
            box_counter += 1
    fp.close()

    input_list = []
    fp = open(filename)
    lines=fp.readlines()
    for i in range(0,box_counter):
        current_box = []
        for j in range(0,5):
            current_line = [
                int(lines[i*5 + i + j][0:2]),
                int(lines[i*5 + i + j][3:5]),
                int(lines[i*5 + i + j][6:8]),
                int(lines[i*5 + i + j][9:11]),
                int(lines[i*5 + i + j][12:14])
            ]
            current_box.append(current_line)
        input_list.append(current_box)
    fp.close()

    blank_list = []
    for item in input_list:
        blank_list.append(0)

    return [input_list, blank_list]


#Row checker
def row_checker(bingo_card, number_list, counter):
    for i in range(0,5):
        new_counter = 0
        for j in range(0, counter):
            if number_list[j] in bingo_card[i]:
                new_counter += 1
        if new_counter == 5:
            return bingo_card
    return False


#Column checker
def column_checker(bingo_card, number_list, counter):
    columns = [
        [bingo_card[0][0], bingo_card[1][0], bingo_card[2][0], bingo_card[3][0], bingo_card[4][0]],
        [bingo_card[0][1], bingo_card[1][1], bingo_card[2][1], bingo_card[3][1], bingo_card[4][1]],
        [bingo_card[0][2], bingo_card[1][2], bingo_card[2][2], bingo_card[3][2], bingo_card[4][2]],
        [bingo_card[0][3], bingo_card[1][3], bingo_card[2][3], bingo_card[3][3], bingo_card[4][3]],
        [bingo_card[0][4], bingo_card[1][4], bingo_card[2][4], bingo_card[3][4], bingo_card[4][4]]
    ]
    for i in range(0,5):
        new_counter = 0
        for j in range(0, counter):
            if number_list[j] in columns[i]:
                new_counter += 1
        if new_counter == 5:
            return bingo_card
    return False


#Play Bingo
def checker(number_list, bingo_cards, counter = 0):
    solved = []
    solved_at = []
    for num in number_list:
        counter += 1
        for i in range(0, len(bingo_cards)):
            if (row_checker(bingo_cards[i], number_list, counter) or column_checker(bingo_cards[i], number_list, counter)) and bingo_cards[i] not in solved:
                solved.append(bingo_cards[i])
                solved_at.append(counter)
    return[solved[len(solved)-1], solved_at[len(solved)-1]]


#Answer
def answer(matching_card, number_list):
    summer = 0
    for i in range(0,5):
        for j in range(0,5):
            if matching_card[i][j] not in number_list:
                summer += matching_card[i][j]
    return(summer * trunc_list[len(trunc_list)-1])



number_list = [91,17,64,45,8,13,47,19,52,68,63,76,82,44,28,56,37,2,78,48,32,58,72,53,9,85,77,89,36,22,49,86,51,99,6,92,80,87,7,25,31,66,84,4,98,67,46,61,59,79,0,3,38,27,23,95,20,35,14,30,26,33,42,93,12,57,11,54,50,75,90,41,88,96,40,81,24,94,18,39,70,34,21,55,5,29,71,83,1,60,74,69,10,62,43,73,97,65,15,16]
bingo_cards = convert_input('input.txt')[0]
numbers_matched = convert_input('input.txt')[1]

matching_card = checker(number_list, bingo_cards)[0]
trunc_list = number_list[0:checker(number_list, bingo_cards)[1]]

print(answer(matching_card, trunc_list))