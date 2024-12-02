"""
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

with open("reports.txt","r") as file:
    data = file.read()

rowsOfData : list[list[int]] = []

for row in data.splitlines():
    placeHolderList : list[int] = []
    for number in row.split():
        placeHolderList.append(int(number))
    rowsOfData.append(placeHolderList)

print(rowsOfData)

def multipleChecksOfSafeReports(listOfNumbers : list[int]):
    def figureOutSequence(numbers : list[int]):
        # Go through each pair of numbers in the sequence
        for i in range(1, len(numbers)):
            # Calculate the difference between the current and previous level
            diff = numbers[i] - numbers[i - 1]
            # If the difference is 0, it's not an increase or decrease
            if diff == 0:
                return False
            # If the difference is too large (more than 3) or too small (less than -3)
            if diff > 3 or diff < -3:
                return False
            # Check if the pattern changes between increasing and decreasing
            if i > 1:  # Make sure there's enough data to check a pattern
                prev_diff = numbers[i - 1] - numbers[i - 2]
                if (diff > 0 and prev_diff < 0) or (diff < 0 and prev_diff > 0):
                    return False
        # If no issues found, the sequence is safe
        return True

    if figureOutSequence(listOfNumbers):
        return "Safe"

    for i in range(len(listOfNumbers)):
        newListOfReportNumbers = listOfNumbers[:i] + listOfNumbers[i + 1:]
        if figureOutSequence(newListOfReportNumbers):
            return "Safe"
    return "Unsafe"

totalSafeReports : int = 0

for listOfNums in rowsOfData:
    checkIfSafeReport = multipleChecksOfSafeReports(listOfNums)
    if "Safe" in checkIfSafeReport:
        totalSafeReports += 1

print(totalSafeReports)