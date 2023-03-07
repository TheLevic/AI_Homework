# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack        
    stack = Stack()
    startLoc = problem.getStartState() # (35, 16)
    if problem.isGoalState(startLoc): # if (x,y) == (1,1)
        return [] # return no directions
    visitedNodes = []
    stack.push((startLoc,[],0)) # ((x,y), 'east', 0)
    while (not stack.isEmpty()):
        currLoc, currDir, currCost = stack.pop() # state on top of stack
        if (currLoc not in visitedNodes):
            visitedNodes.append(currLoc) # don't check currLoc again
            if problem.isGoalState(currLoc):
                return currDir
            for location, direction, cost in problem.getSuccessors(currLoc):
                newDirections = currDir + [direction]
                stack.push((location, newDirections, cost))
    return "couldn't find"

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    visitedNodes = []    
    startNode = problem.getStartState()
    queue.push((startNode,[],0)) # ((x,y), dir, cost)
    while (not queue.isEmpty()):
        currNode, directions, cost = queue.pop() # checks the oldest element in the queue
        print(directions)
        if (currNode not in visitedNodes): # if it hasn't been checked before
            visitedNodes.append(currNode) # ...then add it
            if (problem.isGoalState(currNode)): # if this is the goal...
                return directions # ...then exit 
            for node, action, cost in problem.getSuccessors(currNode): # checks all of the children nodes
                nextAction = directions + [action] # updates route to the child node
                queue.push((node,nextAction,cost)) # adds item to queue


           
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    visitedNodes = []
    startNode = (problem.getStartState(), [], 0) # ((x,y), dir, cost)
    queue = PriorityQueue()
    queue.push((startNode), 0) # (node, cost)
    while (not queue.isEmpty()):
        currNode, directions, cost = queue.pop() # checks the oldest element in the queue
        if (currNode not in visitedNodes): # if it hasn't been checked before
            visitedNodes.append(currNode) # ...then add it
            if (problem.isGoalState(currNode)): # if this is the goal...
                return directions # ...then exit
            for node, action, cost in problem.getSuccessors(currNode): # check all of the children nodes
                nextAction = directions + [action] # updates route to the child node
                queue.push((node,nextAction,cost), cost) # adds item to queue
    return "couldn't find" 

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    from searchAgents import manhattanHeuristic
    visitedNodes = []
    queue = PriorityQueue()
    startNode = (problem.getStartState(), [],0) # ((x,y), dir, cost)
    queue.push(startNode,0) # node, cost

    while (not queue.isEmpty()):
        currNode, directions, cost = queue.pop() # checks the oldest item in queue
        if currNode not in visitedNodes: # if it hasn't been checked before
            visitedNodes.append(currNode)  # ...then add it
            if (problem.isGoalState(currNode)): # if this is the goal...
                return directions  # ...then exit
            for nextNode, nextDirection, nextCost in problem.getSuccessors(currNode): # check all of the children nodes
                previousCost = problem.getCostOfActions(directions) # cost to get to this child node
                totalRemainingCost = manhattanHeuristic(nextNode,problem) # cost to go from child to goal node
                totalDirections = directions + [nextDirection] # updates route to the child node
                queue.push((nextNode, totalDirections, nextCost), (previousCost + totalRemainingCost)) # (node, total cost)
    return "couldn't find"

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
