#! /usr/bin/env python3
# coding: utf-8
import itertools

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
		self.width = len(board[0])
		self.board = board


	@property
	def solved(self):
		"""
		The puzzle is solved if the numbers of the flattened puzzle
		are in increasing order followed by a zero.
		
		:return: Solved state of the puzzle
		:rtype: boolean
		"""
		n = self.width * self.width
		return str(self) == ''.join(map(str, range(1, N))) + '0'
	

	@property
	def actions(self):
		"""
		Return a list of 'move', 'action' pairs. 'move' is a callback which
		returns a new puzzle with the following state that results in the
		movement of the '0' tile in the 'move' direction.
		"""
		def create_move(at, to):
			return lambda: self._move(at, to)

		moves = []
		for i, j in itertools.product(range(self.width), 
									range(self.width)):
			directions ={'R':(i, i-1),
						 'L':(i, j+1),
						 'D':(i-1, j),
						 'U':(i+1, j)} 
			for action, (r, c) in directions.items():
				if r >= 0 and c >= 0 and r < self.width and c < self.width and self.board[r][c] == 0:
						move = create_move((i, j), (r, c)), action
						moves.append(move)
		return moves

	def copy(self):

		"""
		copy 'self'
		"""
		board = []
		for row in self.board:
			board.append([x for x in row])
		return Puzzle(board)


	def _move(self, at, to):
		"""
		Returns a new puzzle where 'at' and 'to' tiles have been swapped.
		"""
		copy = self.copy()
		i, j = at
		r, c = to
		copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
		return copy


	def __str__(self):
		return ''.join(map(str, self))


	def __iter__(self):
		for row in self.board:
			yield from row
