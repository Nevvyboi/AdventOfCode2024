"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
"""

with open("findWord.txt", "r") as file:
    data = file.readlines()

dataInGridFormat : list[list[str]] = []

for row in data:
    rowList: list[str] = []
    for letter in row.strip():
        rowList.append(letter)
    print(rowList)
    dataInGridFormat.append(rowList)

def search2DVector(grid : list[list[str]], row : int, column : int, wordToFind: str) -> bool:
    m, n = len(grid), len(grid[0])
    if grid[row][column] != wordToFind[0]:
        return 0
    lengthOfWord = len(wordToFind)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for directionX, directionY in directions:
        currentXPos, currentYPos = row, column
        k = 0
        while k < lengthOfWord:
            if not (0 <= currentXPos < m and 0 <= currentYPos < n):
                break
            if grid[currentXPos][currentYPos] != wordToFind[k]:
                break
            currentXPos += directionX
            currentYPos += directionY
            k += 1
        if k == lengthOfWord:
            count += 1
    return count

def searchWord(grid: list[list[str]], word: str) -> list:
    m, n = len(grid), len(grid[0])
    totalNoOfOccurrences = 0
    for i in range(m):
        for j in range(n):
            totalNoOfOccurrences += search2DVector(grid, i, j, word)

    return totalNoOfOccurrences

if __name__ == "__main__":
    result = searchWord(dataInGridFormat, "XMAS")
    print(result)
