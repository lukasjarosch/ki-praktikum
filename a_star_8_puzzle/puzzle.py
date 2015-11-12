#! /usr/bin/env python3
# coding: utf-8

class Puzzle:
	"""
	Represents the actual puzzle game
	"""

	def __init__(self, board):
		"""
		The board is represented like that:
			[[1,2,3],
			[4,5,6],
			[7,8,0]]

		:param board: The initial board state
		"""
		self.board = board
