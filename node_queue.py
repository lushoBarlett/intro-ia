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

    def start(self, state):
        self.nodes = deque([Node(state, hcost=self.heuristic(state))])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.pop()

    def expand(self, parent):
        for s, c, h in self.expander(parent.state, self.heuristic):
            self.nodes.append(parent.spawn_child(s, c, h))


class BFSNodeQueue(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.nodes = deque([])
        self.expander = expander
        self.heuristic = heuristic

    def start(self, state):
        self.nodes = deque([Node(state, hcost=self.heuristic(state))])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.popleft()

    def expand(self, parent):
        for s, c, h in self.expander(parent.state, self.heuristic):
            self.nodes.append(parent.spawn_child(s, c, h))


class AstarNodeQueue(NodeQueue):

    def __init__(self, expander, heuristic = lambda s: 0):
        self.nodes = []
        self.expander = expander
        self.heuristic = heuristic

    def start(self, state):
        self.nodes = [Node(state, hcost=self.heuristic(state))]

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return heappop(self.nodes)

    def expand(self, parent):
        for s, c, h in self.expander(parent.state, self.heuristic):
            heappush(self.nodes, parent.spawn_child(s, c, h))

