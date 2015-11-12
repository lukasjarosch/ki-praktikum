#! /usr/bin/env python3
# coding: utf-8

class Node:
    """
    Represents a solver node and it's current state
   """

    def __init__(self, puzzle, parent=None, action=None):
        """
        :param puzzle: The puzzle instance
        :param parent: The parent node if any
        :param action: The action taken to produce this state, if any
        """
        self.puzzle = puzzle
        self.parent = parent
        self.action = action


    @property
    def state(self):
        """
        :return: Hashable self representation
        :rtype: string
        """
        return str(self)


    @property
    def path(self):
        """
        Reconstruct the path from the root node
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)


    @property
    def solved(self):
        """
        Wrapper for the Puzzle class

        :return: Check if puzzle is solved
        :rtype: boolean
        """
        return self.puzzle.solved


    @property
    def actions(self):
        """
        Wrapper for the Puzzle class

        :return: All possible actions
        :rtype: list
        """
        return self.puzzle.actions
