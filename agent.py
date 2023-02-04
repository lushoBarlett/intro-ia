from node import Node

class Agent:

    def __init__(self, initial, final, nodeQueue):
        self.visits = set()
        self.initial = initial
        self.final = final
        self.nodeQueue = nodeQueue

    def visited(self, node):
        return node.state in self.visits

    def visit(self, node):
        return self.visits.add(node.state)

    def finalState(self, node):
        return node.state == self.final

    def next(self):
        if self.nodeQueue.empty():
            return None

        node = self.nodeQueue.next()

        while self.visited(node):
            if self.nodeQueue.empty():
                return None

            node = self.nodeQueue.next()

        return node

    def go(self):

        self.nodeQueue.start(self.initial)

        current = None
        while current is None or not self.finalState(current):
            current = self.next()
            self.visit(current)
            self.nodeQueue.expand(current)

        return Node.tracePath(current), current.cost
