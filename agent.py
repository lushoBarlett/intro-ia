class Node:

    def tracePath(node):
        path = [node.state]

        while node.parent is not None:
            node = node.parent
            path.append(node.state)

        path.reverse()
        return path

    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent

class Agent:

    def __init__(self, initial, final, nodeQueue):
        self.visits = set()
        self.final = final
        self.nodeQueue = nodeQueue
        self.moves = 0

    def visited(self, node):
        return node.state in self.visits

    def visit(self, node):
        return self.visits.add(node.state)

    def finalState(self, node):
        return node.state == self.final

    def transition(self):
        if self.nodeQueue.empty():
            return False

        node = self.nodeQueue.next()

        while self.visited(node):
            if self.nodeQueue.empty():
                return False

            node = self.nodeQueue.next()

        self.visit(node)

        if self.finalState(node):
            return Node.tracePath(node)

        self.nodeQueue.expand(node)

        return None
