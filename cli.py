import argparse
import csv
from sudokill import *

parser = argparse.ArgumentParser(description='Solves sudoku')
parser.add_argument('--csv', type=str,
        help='csv file with unsolved sudoku')
args = parser.parse_args()

with open(args.csv, 'r') as csvfile:
    clues = []
    filereader = csv.reader(csvfile)
    for row in filereader:
        clues.append(list(map(int, row)))

    solver, cells = solve(clues)
    grid = get_solution(solver, cells)
    solver.EndSearch()
    print_grid(grid)
