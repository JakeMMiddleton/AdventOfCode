def get_input(input_path):
    f = open(input_path, "r")

    input = f.read()
    input = input.split("\n\n")
    rules, pages = input[0].split("\n"), input[1].split("\n")
    rules = [rule.split("|") for rule in rules]
    pages = [page.split(",") for page in pages] 

    return rules, pages

def create_rule_dic(rules):
    #Rule dictionary lists any numbers that must appear before 
    rule_dic = {}
    for rulepair in rules:
        pre, post = rulepair[0], rulepair[1]

        if post in rule_dic:
            rule_dic[post].append(pre)
        else:
            rule_dic[post] = [pre]
    
    return rule_dic

def check_update_is_correct(update, rule_dic):

    for i in range(len(update) - 1):        
        curr_num = update[i]
        if curr_num not in rule_dic:
            continue

        rule_before_nums = rule_dic[curr_num] #List of numbers that, if present in the update, must come before our current number

        update_after_nums = update[i+1:] #List of numbers in the update that are after our current number

        failing_nums = set(rule_before_nums) & set(update_after_nums)
        if len(failing_nums) > 0:
            return [False, i, failing_nums]
            
    return [True, None, None]


def get_correct_middle_pages(input_path):
    rules, updates = get_input(input_path)
    rule_dic = create_rule_dic(rules) #This dictionary lays out the number and then lists any numbers that come before

    correct_middle_pages = 0
    fixed_middle_pages = 0

    for update in updates:
        result = check_update_is_correct(update, rule_dic)
        update_is_correct, failing_idx, failing_nums = result[0], result[1], result[2]

        if update_is_correct:
            mid_idx = len(update)//2
            correct_middle_pages += int(update[mid_idx])
            continue

        while not update_is_correct:
            max_fail_idx = failing_idx #This is where we move our failing number to
            for i, num in enumerate(update[failing_idx:]):
                if num in failing_nums:
                    max_fail_idx = failing_idx + i
        
            update = update[:failing_idx] + update[failing_idx+1:max_fail_idx+1] + [update[failing_idx]] + update[max_fail_idx+1:]

            result = check_update_is_correct(update, rule_dic)
            update_is_correct, failing_idx, failing_nums = result[0], result[1], result[2]

        mid_idx = len(update)//2
        fixed_middle_pages += int(update[mid_idx])

    print(f"Correct Middle Pages: {correct_middle_pages}. Fixed Middle Pages: {fixed_middle_pages}")
        
    return correct_middle_pages 


input_path = r"2024\Day5\input.txt"
get_correct_middle_pages(input_path)

