input_list = [5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,
1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,
1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,
1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,
1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,
1,2,1,1,1,1,1,1,1,4,1,5]

#input_list = [3,4,3,1,2]
days = 256

number_of_fish_days = [0,0,0,0,0,0,0,0,0]

for item in input_list:
    number_of_fish_days[item] += 1

for i in range(0, days):
    new_list = [number_of_fish_days[1],
    number_of_fish_days[2],
    number_of_fish_days[3],
    number_of_fish_days[4],
    number_of_fish_days[5],
    number_of_fish_days[6],
    number_of_fish_days[7] + number_of_fish_days[0],
    number_of_fish_days[8],
    number_of_fish_days[0]]
    number_of_fish_days = new_list

print(number_of_fish_days)
print(sum(number_of_fish_days))