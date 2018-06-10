from sudokill import *

# From https://en.wikipedia.org/wiki/Sudoku
clues = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

expected = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

solver, cells = solve(clues)
grid = get_solution(solver, cells)
solver.EndSearch()

assert(grid == expected)

clues = [
    [0,0,0,1,0,5,0,6,8],
    [0,0,0,0,0,0,7,0,1],
    [9,0,1,0,0,0,0,3,0],
    [0,0,7,0,2,6,0,0,0],
    [5,0,0,0,0,0,0,0,3],
    [0,0,0,8,7,0,4,0,0],
    [0,3,0,0,0,0,8,0,5],
    [1,0,5,0,0,0,0,0,0],
    [7,9,0,4,0,1,0,0,0]
]

solver, cells = solve(clues)
grid = get_solution(solver, cells)
solver.EndSearch()

colsums = [0] * 9
blocksum = defaultdict(int)
for i in range(9):
    assert(sum(grid[i]) == 45)
    for j in range(9):
        colsums[j] += grid[i][j]
        blocksum[(i // 3, j // 3)] += grid[i][j]
for j in range(9):
    assert(colsums[j] == 45)
for k in blocksum:
    assert(blocksum[k] == 45)
