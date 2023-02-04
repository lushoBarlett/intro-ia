class Node:

    def trace_path(node):
        path = [node.state]

        while node.parent is not None:
            node = node.parent
            path.append(node.state)

        path.reverse()
        return path

    def __init__(self, state, cost = 0, parent = None, depth = 0):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost

    def spawn_child(self, state, cost = 1):
        return Node(state, self.cost + cost, self, self.depth + 1)
