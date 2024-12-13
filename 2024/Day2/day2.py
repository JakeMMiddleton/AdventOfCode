def get_input(input_path):
    f = open(input_path, "r")
    return f.read()


def get_direction(prev_num, curr_num):
    if prev_num < curr_num:
            return 1
    if prev_num > curr_num:
        return -1
    if prev_num == curr_num:
        return 0


def get_is_level_safe(prev_num, curr_num, direction):
    # Do numbers meet the direction?
    if (direction == -1 and curr_num > prev_num) or (direction == 1 and curr_num < prev_num) or (curr_num == prev_num):
        return False
    
    #Are they within 3 apart?
    if abs(curr_num - prev_num) > 3:
        return False
    
    return True


def puzzle1(input_path):
    #Get Reports
    input = get_input(input_path)
    reports = input.split('\n')

    #For each report, get the number of safe options
    num_safe = 0
    for report in reports:
        levels = report.split(' ')
        prev_num = int(levels[0])
        direction = 0
        is_level_safe = True

        for curr_num in levels[1:]:
            curr_num = int(curr_num)
            # Define Direction if not defined yet
            if (direction == 0):
                direction = get_direction(prev_num, curr_num)

            #Check if levels are safe
            is_level_safe = get_is_level_safe(prev_num, curr_num, direction)
            if not is_level_safe:
                break

            prev_num = curr_num
        
        if is_level_safe:
            num_safe += 1
        
    return num_safe


def get_is_report_safe(report):
    prev_num = int(report[0])
    direction = 0

    for i, curr_num in enumerate(report[1:]):
        curr_num = int(curr_num)
        # Define Direction if not defined yet
        if (direction == 0):
            direction = get_direction(prev_num, curr_num)

        #Check if levels are safe
        if not get_is_level_safe(prev_num, curr_num, direction):
            return False, [i, i+1]

        prev_num = curr_num

    return True, [None, None]



def puzzle2(input_path):
    input = get_input(input_path)
    reports = input.split('\n')
    
    num_safe_reports = 0
    report_analysis = {}

    for report_idx,  report in enumerate(reports):
        report = report.split(' ')
        report = [int(num) for num in report]

        is_report_safe = get_is_report_safe(report)

        #If original report is safe all the way through, add one to safe reports.
        if is_report_safe[0]:
            report_result = {"Report": report, "Result": "Safe with no Change"}
            report_analysis[report_idx] = report_result
            num_safe_reports += 1
            continue

        #If Original report is not safe, get the index pair that fails
        failing_idx_1, failing_idx_2 = is_report_safe[1]

        #Test if report is safe after removing the first failing index
        new_report = report.copy()
        del new_report[failing_idx_1]

        is_report_safe = get_is_report_safe(new_report)
        if is_report_safe[0]:
            num_safe_reports += 1
            report_result = {"Report": report, "Result": f"Safe after removing {report[failing_idx_1]}, (index {failing_idx_1})"}
            report_analysis[report_idx] = report_result
            continue

        #Test if the report is safe after removing the second failing index
        new_report = report.copy()
        del new_report[failing_idx_2]

        is_report_safe = get_is_report_safe(new_report)
        if is_report_safe[0]:
            num_safe_reports += 1
            report_result = {"Report": report, "Result": f"Safe after removing {report[failing_idx_2]}, (index {failing_idx_2})"}
            report_analysis[report_idx] = report_result
            continue

    
        report_result = {"Report": report, "Result": f"Unsafe"}
        report_analysis[report_idx] = report_result

    return num_safe_reports, report_analysis
        
        




path = r"C:\Users\jakem\OneDrive\Documents\Coding Projects\advent_code\2024\Day 2\input.txt"
#print(puzzle1(path))
num_safe_reports, report_analysis = puzzle2(path)
print(report_analysis)
print(num_safe_reports)