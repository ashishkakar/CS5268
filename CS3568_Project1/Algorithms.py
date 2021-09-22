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

        #Trivial case: if start state=goal state then return empty
        if problem.isGoalState(problem.getStartState()):
            return []

        #Add start state to closed set
        closed = {problem.getStartState():(problem.getStartState(), '', 0)}

        #get successors of start state
        successors = problem.getSuccessors(problem.getStartState())

        #create fringe data structure (stack for DFS)
        fringe = util.Stack()

        #push successors to stack
        fringe.push(successors)

        #as long as fringe is not empty
        while not fringe.isEmpty():

            #extract the final layer of tree/graph
            nodes = fringe.pop()

            #if final layer has no nodes then drop the final layer and continue loop with upper layers
            if len(nodes)==0:
                continue

            #if final layer is not empty, extract the last node from final layer
            node = nodes.pop()

            #separate out position, direction and cost of the node
            (position, direction, cost) = node

            #if node is already in closed set, put the final layer back on fringe and continue with remaining nodes
            if position in closed:
                fringe.push(nodes)
                continue

            #if node is not in closed set, add it to the closed set
            closed[position] = node

            #if current node is goal state
            if problem.isGoalState(position):

                #create a stack of directioons and push all directions onto it from the final layer of tree/graph to the root
                directions = util.Stack()
                directions.push(direction)
                while not fringe.isEmpty():
                    nodes = fringe.pop()
                    node = nodes.pop()
                    (position, direction, cost) = node
                    directions.push(direction)

                #create a path variable that will hold the path to follow (directions in the reverse order)
                path = []

                #as long as directions is not empty, put the directions into path in the reverse order
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

                #return result
                return path

            #if the current node is not goal, get its successors
            successors = problem.getSuccessors(position)

            #put the nodes back on fringe
            nodes.append(node)
            fringe.push(nodes)

            #push the successors as the next layer on fringe
            fringe.push(successors)

        #FAILED to find the goal nodee. What to do?
        print("FAILED to find the goal node. What to do?")
        return []

class BFS(object):
    def breadthFirstSearch(self, problem):
        "*** TTU CS3568 YOUR CODE HERE ***"

        from game import Directions

        #Trivial case: if start state=goal state then return empty
        if problem.isGoalState(problem.getStartState()):
            return []

        #Add start state to closed set
        closed = {problem.getStartState():(problem.getStartState(), '', 0)}

        #get successors of start state
        #successors = problem.getSuccessors(problem.getStartState())

        #create fringe data structure (queue for BFS)
        fringe = util.Queue()

        #push successors to stack
        fringe.push([(problem.getStartState(), '', 0)])

        #as long as fringe is not empty
        while not fringe.isEmpty():

            #extract the final layer of tree/graph
            nodes = fringe.pop()

            #if final layer has no nodes then drop the final layer and continue loop with upper layers
            #if len(nodes)==0:
                #continue

            #if final layer is not empty, extract the last node from final layer
            node = nodes.pop()

            #separate out position, direction and cost of the node
            (position, direction, cost) = node

            successors = problem.getSuccessors(position)

            #if node is already in closed set, put the final layer back on fringe and continue with remaining nodes
            #if position in closed:
                #fringe.push(nodes)
                #continue

            for s in successors:
                (position, direction, cost) = s
                if position in closed:
                    continue
                n = nodes[:]
                n.append(node)
                n.append(s)
                fringe.push(n)
                closed[position] = s
                if problem.isGoalState(position):
                    path = []
                    while n:
                        node = n.pop(0)
                        (position, direction, cost) = node
                        if direction=='South':
                            path.append(Directions.SOUTH)
                        elif direction=='West':
                            path.append(Directions.WEST)
                        elif direction=='North':
                            path.append(Directions.NORTH)
                        elif direction=='East':
                            path.append(Directions.EAST)
                    return path


            #if node is not in closed set, add it to the closed set
            #closed[position] = node

            #if current node is goal state
            #if problem.isGoalState(position):

                #create a stack of directioons and push all directions onto it from the final layer of tree/graph to the root
                #directions = util.Stack()
                #directions.push(direction)
                #while not fringe.isEmpty():
                    #nodes = fringe.pop()
                    #node = nodes.pop()
                    #(position, direction, cost) = node
                    #directions.push(direction)

                #create a path variable that will hold the path to follow (directions in the reverse order)
                #path = []

                #as long as directions is not empty, put the directions into path in the reverse order
                #while not directions.isEmpty():
                    #direction = directions.pop()
                    #if direction=='South':
                        #path.append(Directions.SOUTH)
                    #elif direction=='West':
                        #path.append(Directions.WEST)
                    #elif direction=='North':
                        #path.append(Directions.NORTH)
                    #elif direction=='East':
                        #path.append(Directions.EAST)

                #return result
                #return path

            #if the current node is not goal, get its successors
            #successors = problem.getSuccessors(position)

            #put the nodes back on fringe
            #nodes.append(node)
            #fringe.push(nodes)

            #push the successors as the next layer on fringe
            #fringe.push(successors)

        #FAILED to find the goal nodee. What to do?
        print("FAILED to find the goal node. What to do?")
        return []

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
