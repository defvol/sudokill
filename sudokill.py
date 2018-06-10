from ortools.constraint_solver import pywrapcp
from collections import defaultdict


def solve(clues):
    solver = pywrapcp.Solver('sudokill')

    bloc = defaultdict(list)
    cell = [0] * 9
    cols = defaultdict(list)

    for i in range(9):
        cell[i] = [0] * 9
        for j in range(9):
            # Define lower and upper bounds per cell
            clue = clues[i][j]
            lb, ub = (clue, clue) if clue else (1, 9)
            cell[i][j] = solver.IntVar(lb, ub, 'cell[%i][%i]' % (i, j))
            # Collect vars for rules for blocks and columns
            bloc[(i // 3, j // 3)].append(cell[i][j])
            cols[j].append(cell[i][j])

    # Add constraints
    for n in range(9):
        # All elements in a row must be different and sum 45
        solver.Add(solver.AllDifferent(cell[n]))
        solver.Add(solver.Sum(cell[n]) == 45)
        # All elements in a col must be different and sum 45
        solver.Add(solver.AllDifferent(cols[n]))
        solver.Add(solver.Sum(cols[n]) == 45)

    # All elements in a block should be different and sum 45
    for q in bloc:
        solver.Add(solver.AllDifferent(bloc[q]))
        solver.Add(solver.Sum(bloc[q]) == 45)

    flat_cells = sum(cell, [])
    db = solver.Phase(flat_cells,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_MIN_VALUE)
    solver.NewSearch(db)
    return solver, cell


def get_solution(solver, cells):
    solver.NextSolution()
    grid = [0] * 9
    for i in range(9):
        grid[i] = [cells[i][j].Value() for j in range(9)]
    return grid


def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print grid[i][j],
            if j % 3 == 2:
                print '|',
        print ''
        if i % 3 == 2:
            print '- ' * 12
