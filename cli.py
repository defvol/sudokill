import argparse
import csv
from sudokill import *

parser = argparse.ArgumentParser(description='Solves sudoku')
parser.add_argument('--csv', type=str,
        help='csv file with unsolved sudoku')
args = parser.parse_args()

with open(args.csv, 'rb') as csvfile:
    clues = []
    filereader = csv.reader(csvfile)
    for row in filereader:
        clues.append(map(int, row))

    solver, cells = solve(clues)
    grid = get_solution(solver, cells)
    solver.EndSearch()
    print_grid(grid)
