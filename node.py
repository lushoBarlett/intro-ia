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

