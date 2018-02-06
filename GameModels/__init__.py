#I represent maze's game with a matrix where in each cell we shold find:
# 0--> empty cell
# 1--> unreachable cell(wall)

import numpy as np


class MazeGameRepresentation:

    def __init__(self, matrix, pos, ending):

        self.matrix = matrix
        self.pos = pos
        self.ending = ending



class MazeState:
    def __init__(self, parent, matrix, pos, ending, heuristic):

        self.parent = parent
        self.H = heuristic
        self.representation = MazeGameRepresentation(matrix, pos, ending)

    def __eq__(self, other):
        return np.array_equal(self.representation.pos, other.representation.pos)

    def __ne__(self, other):
        return not np.array_equal(self.representation.pos, other.representation.pos)

    def __hash__(self):
        return hash(self.representation.pos[0]) ^ hash(self.representation.pos[1])


class Game:
    def __init__(self, initialState=None, heuristic=None):
        self.state = initialState
        self.heuristic = heuristic

    def neighbors(self, state):
        out = set([])
        return out

    def getState(self):
        return self.state

    def solutiion(self, state):
        return True


class MazeGame(Game):

    def __init__(self, matrix, pos, endingcell, heuristic):
        self.state = MazeState(None, matrix, pos, endingcell, heuristic)
        self.matrixDimension = (0, 0)
        self.matrixDimension = matrix.shape
        print("matrix dimension: ({},{})".format(self.matrixDimension[0], self.matrixDimension[1]))

    def neighbors(self, state):
        out = set([])
        rep = state.representation

        #I create these variables to handle the particular case where the algorithm examin the cells in first and last row or in a first and last column

        above = True
        below =True
        right = True
        left = True

        if rep.pos[0] == 0:
            above = False

        if rep.pos[0] == self.matrixDimension[0]-1:
            below = False

        if rep.pos[1] == 0:
           left = False

        if rep.pos[1] == self.matrixDimension[1]-1:
            right = False

        if right:
            if rep.matrix[rep.pos[0]][rep.pos[1]+1] != 1:
                print("It's possible to go right! So I'm in position ({},{}) now, next I may be in positon ({},{})".format(rep.pos[0], rep.pos[1], rep.pos[0], rep.pos[1]+1))
                proxpos=(rep.pos[0], rep.pos[1]+1)
                newState= MazeState(state, rep.matrix, proxpos, rep.ending, state.H)
                out.add(newState)

        if left:
            if rep.matrix[rep.pos[0]][rep.pos[1]-1] != 1:
                print("It's possible to go left! So I'm in position ({},{}) now, next I may be in positon ({},{})".format(rep.pos[0], rep.pos[1], rep.pos[0], rep.pos[1]-1))
                proxpos=(rep.pos[0], rep.pos[1]-1)
                newState= MazeState(state, rep.matrix, proxpos, rep.ending, state.H)
                out.add(newState)

        if below:
            if rep.matrix[rep.pos[0]+1][rep.pos[1]] != 1:
                print("It's possible to go below! So I'm in position ({},{}) now, next I may be in positon ({},{})".format(rep.pos[0], rep.pos[1], rep.pos[0]+1, rep.pos[1]))
                proxpos=(rep.pos[0]+1, rep.pos[1])
                newState= MazeState(state, rep.matrix, proxpos, rep.ending, state.H)
                out.add(newState)

        if above:
            if rep.matrix[rep.pos[0]-1][rep.pos[1]] != 1:
                print("It's possible to go above! So I'm in position ({},{}) now, next I may be in positon ({},{})".format(rep.pos[0], rep.pos[1], rep.pos[0]-1, rep.pos[1]))
                proxpos=(rep.pos[0]-1, rep.pos[1])
                newState= MazeState(state, rep.matrix, proxpos, rep.ending, state.H)
                out.add(newState)
        return out

    def solution(self, state):
        out = (state.representation.pos[0] == state.representation.ending[0]) and (state.representation.pos[1] == state.representation.ending[1])
        return out



























