from pprint import pformat

class Node:

    def trace_path(node):
        path = [node]

        while node.parent is not None:
            node = node.parent
            path.append(node)

        path.reverse()
        return path

    def __init__(self, state, cost = 0, hcost = 0, parent = None, depth = 0, expansion = 0):
        self.state = state
        self.cost = cost
        self.hcost = hcost
        self.parent = parent
        self.depth = depth
        self.expansion = expansion

    def __repr__(self):
        return f"{pformat(self.state).ljust(40, ' ')}[c:{self.cost} + h:{self.hcost} = {self.total_cost()} ({self.adjusted_cost()})] - E:{self.expansion}"

    def __lt__(self, other):
        return self.adjusted_cost() < other.adjusted_cost()

    def total_cost(self):
        return self.cost + self.hcost

    def parent_cost(self):
        return 0 if self.parent is None else self.parent.adjusted_cost()

    def adjusted_cost(self):
        return max(self.total_cost(), self.parent_cost())

    def spawn_child(self, state, cost, hcost, expansion):
        return Node(state, self.cost + cost, hcost, self, self.depth + 1, expansion)
