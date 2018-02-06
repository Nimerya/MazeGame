import GameModels as Mg
import Heuristic as He
import numpy as np
import time as t


dictOfState = {}
heur = He.MazeHeuristic
h = 0

def search(game, state0):
    print("Starting the search")
    sHorizon = set([])
    sExplored = set([])
    #Add a first state to horizon
    sHorizon.add(state0)
    while len(sHorizon) > 0:

        print("length of horizon: {}".format(len(sHorizon)))
        print("length of explored: {}".format(len(sExplored)))

        #Put in view the state with min heuristic value associated(pick-->argMin)
        view = pick(sHorizon)
        #If view is not None
        if not (view is None):
            #check if view is the solution
            if game.solution(view):
                #in affermative case return the backpath to arrive to solution
                return backpath(view)

            #Add view in the list of explored state
            sExplored.add(view)
            print("View state added to explored: {} ".format(view.representation.pos))
            #Find the neighbors of view
            neighbors = game.neighbors(view)
            print("Size of neighbors: {} ".format(len(neighbors)))
            #Update Horizon with all the element in Horizon minus the element in the neighborhood that are alrady explored
            sHorizon = sHorizon | (neighbors - sExplored)
            print("New horizon size: {} ".format(len(sHorizon)))
            print("End iteration")
        #If in view ther's None
        else:
            return None

def backpath(state):
    padre = state.parent
    lStates = [state]
    while padre is not None:
        lStates.append(padre)
        padre = padre.parent
    return reversed(lStates)

def pick(setOfStates):
    return argMin(setOfStates)


def argMin(setOfState):
    localdict={}
    for s in setOfState:
        if s not in dictOfState:
            if h == 0:
                value = heur.HManhattan(s)
            elif h == 1:
                value = heur.Hchebyshev(s)
            else:
                value = heur.HEuclide(s)

            localdict[s] = value

    if len(localdict) > 0:
        out = min(localdict, key=localdict.get)
        print("Piked state value: {}".format(localdict[out]))
        dictOfState[out] = localdict[out]
    else:
        out = None

    return out


def main():

    # Insert the name of file that contains the input instance
    input_file = input("Insert the name of the file containing the input maze in this format \n 0,0,0,1\n 1,0,0,1\n 1,0,0,0\n 0,0,0,0\nwhere 0 is an empty cell and 1 is a wall;\nstarting point will be (0, 0), ending will be (n, m) of the matrix nxm: ")

    #Save in instance the name of file that was passed from input
    instance = open(input_file, "r")
    #Generate the matrix that represent the maze
    matrix = np.loadtxt(instance, delimiter=",")
    #Initial position
    pos = (0, 0)
    #Final position
    ending = (matrix.shape[0]-1, matrix.shape[1]-1)
    #Create the instance of maze's game
    game = Mg.MazeGame(matrix, pos, ending, heur)


    global h
    global dictOfState
    #Use this variable to store the time when the Manhattan heuristic start to work
    start0 = t.time()
    #Assign the value to choose the heuristc
    h = 0
    #Return the backpath of solution
    path0 = search(game, game.getState())
    #Calculate the time taken
    end0 = t.time()-start0
    len0 = len(dictOfState)


    dictOfState = {}
    #Use this variable to store the time when the Manhattan heuristic start to work
    start1 = t.time()
    #Assign the value to choose the heuristc
    h = 1
    #Return the backpath of solution
    path1 = search(game, game.getState())
    #Calculate the time taken
    end1 = t.time() - start1
    len1=len(dictOfState)

    
    dictOfState = {}
    #Use this variable to store the time when the Manhattan heuristic start to work
    start2 = t.time()
    #Assign the value to choose the heuristc
    h = 2
    #Return the backpath of solution
    path2 = search(game, game.getState())
    #Calculate the time taken
    end2 = t.time() - start2
    len2=len(dictOfState)

    print("Input maze is: \n{} ".format(matrix))

    #print the backpath using Manhattan distance
    if path0 is not None:
        move = 0
        for i in path0:
            print("Move {} of Manhattan: {}".format(move, i.representation.pos))
            move += 1
        print("\n")
    else:
        print("Something went wrong")

    #print the backpath using chebyshev distance
    if path1 is not None:
        move = 0
        for i in path1:
            print("Move {} of chebyshev: {}".format(move, i.representation.pos))
            move += 1
        print("\n")

    #print the backpath using Euclide distance
    if path2 is not None:
        move = 0
        for i in path2:
            print("Move {} of Euclide: {}".format(move, i.representation.pos))
            move += 1
        print("\n")

    #Print the time taken and the number of the states visited in each of three heuristic
    print("Solution reached in {} senconds, visiting {} states, using Manhattan heuristic".format(end0, len0))
    print("Solution reached in {} senconds,  visiting {} states, using chebyshev heuristic".format(end1, len1))
    print("Solution reached in {} senconds, visiting {} states, using Euclide heuristic".format(end2, len2))





#call the sunction main
if __name__ == "__main__":
    main()

