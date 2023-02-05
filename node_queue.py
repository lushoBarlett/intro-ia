from abc import ABC, abstractmethod
from collections import deque
from heapq import heappush, heappop
from node import Node

class NodeQueue(ABC):

    @abstractmethod
    def __init__(self, state, expander, heuristic):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def expand(self, parent):
        pass


class DFSNodeQueue(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.nodes = deque([])
        self.expander = expander
        self.heuristic = heuristic
        self.expansion = 0

    def start(self, state):
        self.nodes = deque([Node(state, hcost=self.heuristic(state))])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.pop()

    def expand(self, parent):
        self.expansion += 1
        for s, c in reversed(list(self.expander(parent.state))):
            h = self.heuristic(s)
            self.nodes.append(parent.spawn_child(s, c, h, self.expansion))


class BFSNodeQueue(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.nodes = deque([])
        self.expander = expander
        self.heuristic = heuristic
        self.expansion = 0

    def start(self, state):
        self.nodes = deque([Node(state, hcost=self.heuristic(state))])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.popleft()

    def expand(self, parent):
        self.expansion += 1
        for s, c in self.expander(parent.state):
            h = self.heuristic(s)
            self.nodes.append(parent.spawn_child(s, c, h, self.expansion))


class AstarNodeQueue(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.nodes = []
        self.expander = expander
        self.heuristic = heuristic
        self.expansion = 0

    def start(self, state):
        self.nodes = [Node(state, hcost=self.heuristic(state))]

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return heappop(self.nodes)

    def expand(self, parent):
        self.expansion += 1
        for s, c in self.expander(parent.state):
            h = self.heuristic(s)
            heappush(self.nodes, parent.spawn_child(s, c, h, self.expansion))


class HillClimbing(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.node = None
        self.expander = expander
        self.heuristic = heuristic
        self.expansion = 0

    def start(self, state):
        self.node = Node(state, hcost=self.heuristic(state))

    def empty(self):
        return self.node is None

    def next(self):
        node = self.node
        self.node = None
        return node

    def expand(self, parent):
        self.expansion += 1

        next_node = None
        for s, in self.expander(parent.state):
            h = self.heuristic(s)
            n = Node(s, 0, h, None, parent.depth + 1, self.expansion)

            if next_node is None or not next_node < n:
                next_node = n

        self.node = next_node
