#! /usr/bin/env python3
# coding: utf-8

from puzzle import Puzzle
from solver import Solver

board = [[1,2,3],[4,0,6,],[7,5,8]]

puzzle = Puzzle(board)
s = Solver(puzzle)

p = s.solve_h1()

for node in p:
	print(node.action)
	#node.puzzle.pprint()
