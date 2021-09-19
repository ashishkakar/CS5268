import util

class DFS(object):
    def depthFirstSearch(self, problem):
        """
        Search the deepest nodes in the search tree first
        [2nd Edition: p 75, 3rd Edition: p 87]

        Your search algorithm needs to return a list of actions that reaches
        the goal.  Make sure to implement a graph search algorithm
        [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** TTU CS3568 YOUR CODE HERE ***"

        from game import Directions

        if problem.isGoalState(problem.getStartState()):
            return []
        closed = {problem.getStartState():(problem.getStartState(), '', 0)}
        successors = problem.getSuccessors(problem.getStartState())
        fringe = util.Stack()
        fringe.push(successors)
        while not fringe.isEmpty():
            nodes = fringe.pop()
            if len(nodes)==0:
                continue
            node = nodes.pop()
            (position, direction, cost) = node
            if position in closed:
                fringe.push(nodes)
                continue

            closed[position] = node
            if problem.isGoalState(position):
                directions = util.Stack()
                directions.push(direction)
                while not fringe.isEmpty():
                    nodes = fringe.pop()
                    node = nodes.pop()
                    (position, direction, cost) = node
                    directions.push(direction)
                path = []
                while not directions.isEmpty():
                    direction = directions.pop()
                    if direction=='South':
                        path.append(Directions.SOUTH)
                    elif direction=='West':
                        path.append(Directions.WEST)
                    elif direction=='North':
                        path.append(Directions.NORTH)
                    elif direction=='East':
                        path.append(Directions.EAST)
                return path
            successors = problem.getSuccessors(position)
            nodes.append(node)
            fringe.push(nodes)
            fringe.push(successors)


        util.raiseNotDefined()

class BFS(object):
    def breadthFirstSearch(self, problem):
        "*** TTU CS3568 YOUR CODE HERE ***"

        util.raiseNotDefined()

class UCS(object):
    def uniformCostSearch(self, problem):
        "*** TTU CS3568 YOUR CODE HERE ***"

        util.raiseNotDefined()

class aSearch (object):
    def nullHeuristic( state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0
    def aStarSearch(self,problem, heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        "*** TTU CS3568 YOUR CODE HERE ***"

        util.raiseNotDefined()
