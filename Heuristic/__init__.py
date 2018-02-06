import math as m

class Heuristic:

    def __init__(self):
        pass

    @staticmethod
    def HManhattan(state):
        return 1

    @staticmethod
    def Hchebyshev(state):
        return 1

    @staticmethod
    def HEuclide(state):
        return 1


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def chebyshev_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Undefined for vectors of unequal length")
    return max(abs(e1-e2) for e1, e2 in zip(v1, v2))


def euclide_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Undefined for vectors of unequal length")
    dist = [(a-b)**2 for a, b in zip(v1, v2)]
    dist = m.sqrt(sum(dist))
    return dist

class MazeHeuristic(Heuristic):

    @staticmethod
    def HManhattan(state):
        print("State valuation:\n {}".format(state.representation.pos))
        result = manhattan_distance(state.representation.pos, state.representation.ending)
        print("State value: {}".format(result))
        return result

    @staticmethod
    def Hchebyshev(state):
        print("State valuation:\n {}".format(state.representation.pos))
        result = chebyshev_distance(state.representation.pos, state.representation.ending)
        print("State value: {}".format(result))
        return result

    @staticmethod
    def HEuclide(state):
        print("State valuation:\n {}".format(state.representation.pos))
        result = euclide_distance(state.representation.pos, state.representation.ending)
        print("State value: {}".format(result))
        return result





