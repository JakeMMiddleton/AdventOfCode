def get_input(input_path):
    f = open(input_path, "r")
    return f.read()

def find_xmas(input_path, cross=False):
    wordsearch = get_input(input_path)
    wordsearch_array = [[char for char in line] for line in wordsearch.split("\n")]

    num_xmas = 0

    for i in range(len(wordsearch_array)):
        for j in range(len(wordsearch_array[0])):

            # Puzzle 1
            if not cross:
                # Check if 'XMAS' is in each possible direction
                for direction in ["NW", "N", "NE", "E", "SE", "S", "SW", "W"]:
                    is_xmas = get_is_xmas(i, j, direction, wordsearch_array)
                    
                    if is_xmas:
                        num_xmas += 1

            #Puzzle 2
            if cross:
                is_cross_xmas = get_is_cross_xmas(i, j, wordsearch_array)

                if is_cross_xmas:
                    num_xmas += 1

    return num_xmas


def get_is_xmas(i, j, direction, wordsearch_array):
    max_i = len(wordsearch_array[0]) - 1
    max_j = len(wordsearch_array) - 1

    # Remove impossible values due to not enough values in that direction
    if direction in ["NW", "N", "NE"] and i <= 2:
        return False
    
    if direction in ["NE", "E", "SE"] and max_j - j <= 2:
        return False
    
    if direction in ["SE", "S", "SW"] and max_i - i <= 2:
        return False
    
    if direction in ["SW", "W", "NW"] and j <= 2:
        return False
        
    #Find if XMAS fits
    direction_addition_dic = {
        "NW": [-1, -1],
        "N": [-1, 0],
        "NE": [-1, 1],
        "E": [0, 1],
        "SE": [1, 1],
        "S": [1, 0],
        "SW": [1, -1],
        "W": [0, -1]
    }

    i_add, j_add = direction_addition_dic[direction]

    if (
        wordsearch_array[i][j] != "X"
        or wordsearch_array[i + i_add][j + j_add] != "M"
        or wordsearch_array[i + 2*i_add][j + 2*j_add] != "A"
        or wordsearch_array[i + 3*i_add][j + 3*j_add] != "S"
    ):
        return False
    
    return True

def get_is_cross_xmas(i, j, wordsearch_array):
    max_i = len(wordsearch_array[0]) - 1
    max_j = len(wordsearch_array) - 1

    # Make sure we are on an 'A'
    if wordsearch_array[i][j] != "A":
        return False
    
    # Make sure there are enough values in each direction
    if(
        i == 0
        or j == 0
        or i == max_i
        or j == max_j
    ):
        return False
        
    # Check if there are 2 MAS in cross direction
    num_mas = 0

    #Top left to bottom right
    if(
        (wordsearch_array[i-1][j-1] == "M"
        and wordsearch_array[i+1][j+1] == "S")
    ):
        num_mas += 1  

    # Top right to bottom left
    if(
        (wordsearch_array[i-1][j+1] == "M"
        and wordsearch_array[i+1][j-1] == "S")
    ):
        num_mas += 1

    # Bottom right to top left
    if(
        (wordsearch_array[i-1][j-1] == "S"
        and wordsearch_array[i+1][j+1] == "M")
    ):
        num_mas += 1  

    # Bottom left to Top right
    if(
        (wordsearch_array[i-1][j+1] == "S"
        and wordsearch_array[i+1][j-1] == "M")
    ):
        num_mas += 1 

    if num_mas >= 2:
        return True
    
    return False

input_path = r"2024\Day4\input.txt"
print(f"Puzzle 1: {find_xmas(input_path, cross=False)}")
print(f"Puzzle 2: {find_xmas(input_path, cross=True)}")
