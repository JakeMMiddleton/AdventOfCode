def ParseRecords(input):
    reports = list()
    for line in input:
        numbers = list()
        currentNumber = str()
        for character in line:
            if character == " " or character == "\n":
                numbers.append(int(currentNumber))
                currentNumber = str()
                continue

            currentNumber += character
        reports.append(numbers)
    return reports

def CheckSafetyScore(report):
    score = int()
    increasing = None
    for i, level in enumerate(report):
        if i == 0:
            continue

        previousLevel = report[i - 1]
        currentLevel = report[i]

        score = currentLevel - previousLevel
        if score < -3 or score > 3 or score == 0:
            return False
        if increasing == True and score < 0:
            return False
        if increasing == False and score > 0:
            return False
        
        if score < 0:
            increasing = False
        else: increasing = True
        
    return True

reports = ParseRecords(open(r"C:\Users\jakem\OneDrive\Documents\Coding Projects\advent_code\2024\Day 2\input.txt"))


report_analysis = {}
safeReportCount = 0
for report_idx, report in enumerate(reports):
    if CheckSafetyScore(report) == True:
        report_result = {"Report": report, "Result": "Safe with no Change"}
        report_analysis[report_idx] = report_result
        safeReportCount += 1 
    else: # Part 2
        for i, level in enumerate(report):
            reportCopy = report.copy()
            reportCopy.pop(i)
            if CheckSafetyScore(reportCopy) == True:
                report_result = {"Report": report, "Result": f"Safe after removing {report[i]}, (index {i})"}
                report_analysis[report_idx] = report_result
                safeReportCount += 1
                break
        if report_idx not in report_analysis:
            report_result = {"Report": report, "Result": "Unsafe"}
            report_analysis[report_idx] = report_result

print(report_analysis)
print(safeReportCount)