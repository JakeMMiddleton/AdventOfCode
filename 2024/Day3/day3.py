import re

def get_input(input_path):
    f = open(input_path, "r")
    return f.read()

def ScanMemory(input_path, do_enabled = False):
    input = get_input(input_path)
    input = re.sub("\n", "", input)

    if do_enabled:
        do_texts = re.split("do\(\)", input)
        valid_text = ""
        for do_text in do_texts:
            valid_text += re.split("don\'t\(\)", do_text)[0]
    else:
        valid_text = input

    valid_muls = re.findall("mul\([0-9]+\,[0-9]+\)", valid_text)

    total = 0
    for mul in valid_muls:
        try:
            num_1, num_2 = [int(num) for num in re.findall("[0-9]+", mul)]
        except:
            print(f"More than 2 numbers found in {mul}. Check RegEx defining valid_muls.")
            return
        
        total += num_1*num_2

    return total

input_path = r"2024/Day3/input.txt"
print(f"Puzzle 1: {ScanMemory(input_path, do_enabled=False)}")
print(f"Puzzle 2: {ScanMemory(input_path, do_enabled=True)}")