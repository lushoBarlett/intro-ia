class Node:

    def tracePath(node):
        path = [node.state]

        while node.parent is not None:
            node = node.parent
            path.append(node.state)

        path.reverse()
        return path

    def __init__(self, state, cost = 0, parent = None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost
