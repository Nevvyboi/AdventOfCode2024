"""
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

with open("findWord.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

grid: list[list[str]] = [list(row) for row in data]

def isValid(grid: list[list[str]], x: int, y: int) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def findXShape(grid: list[list[str]], word: str) -> int:
    xShapes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != word[1]:
                continue
            diagonals = [
                [(-1, -1), (1, 1)],
                [(-1, 1), (1, -1)]
            ]
            validDiagonals = 0
            for dx, dy in diagonals:
                isValidDiagonal = True
                for k in range(len(word)):
                    x = i + dx[k]
                    y = j + dy[k]
                    if not isValid(grid, x, y) or grid[x][y] != word[k]:
                        isValidDiagonal = False
                        break
                if isValidDiagonal:
                    validDiagonals += 1
            if validDiagonals == 2:
                xShapes += 1
    return xShapes

if __name__ == "__main__":
    print(findXShape(grid, "MAS"))