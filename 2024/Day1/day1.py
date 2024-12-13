import re
def get_input(input_path):
    f = open(input_path, "r")
    return f.read()    

def get_lists(input_path):
    input = get_input(input_path)

    numbers = re.split('   |\n', input)
    list_1, list_2 = [], []

    for i,num in enumerate(numbers):
        if i%2 == 0:
            list_1.append(int(num))
        else:
            list_2.append(int(num))
    
    return list_1, list_2

def puzzle_1(input_path):
    list_1, list_2 = get_lists(input_path)

    output = 0
    for i in range(len(list_1)):
        output += abs(list_1[i] - list_2[i])
    
    return output

def puzzle_2(input_path):
    list_1, list_2 = get_lists(input_path)

    list_2_occurrences = {}
    for num in list_2:
        if num in list_2_occurrences:
            list_2_occurrences[num] += 1
        else:
            list_2_occurrences[num] = 1
    
    sim_score = 0
    for num in list_1:
        if num in list_2_occurrences:
            sim_score += num * list_2_occurrences[num]
    
    return sim_score

input_path = r"2024/Day1/input.txt"
print("Puzzle 1: " + str(puzzle_1(input_path)))
print("Puzzle 2: " + str(puzzle_2(input_path)))


