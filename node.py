from pprint import pformat

class Node:

    def trace_path(node):
        path = [node]

        while node.parent is not None:
            node = node.parent
            path.append(node)

        path.reverse()
        return path

    def __init__(self, state, cost = 0, hcost = 0, parent = None, depth = 0):
        self.state = state
        self.cost = cost
        self.hcost = hcost
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        return f"{pformat(self.state)} - [c:{self.cost} + h:{self.hcost} = {self.total_cost()}]"

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()

    def total_cost(self):
        return self.cost + self.hcost

    def spawn_child(self, state, cost, hcost):
        return Node(state, self.cost + cost, hcost, self, self.depth + 1)
