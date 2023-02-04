from abc import ABC, abstractmethod
from collections import deque
from heapq import heappush, heappop
from node import Node

class NodeQueue(ABC):

    @abstractmethod
    def __init__(self, state, expander):
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

    def __init__(self, expander):
        self.nodes = deque([])
        self.expander = expander

    def start(self, state):
        self.nodes = deque([Node(state)])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.pop()

    def expand(self, parent):
        for s in self.expander(parent.state):
            self.nodes.append(parent.spawn_child(s))


class BFSNodeQueue(NodeQueue):

    def __init__(self, expander):
        self.nodes = deque([])
        self.expander = expander

    def start(self, state):
        self.nodes = deque([Node(state)])

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return self.nodes.popleft()

    def expand(self, parent):
        for s in self.expander(parent.state):
            self.nodes.append(parent.spawn_child(s))


class BestFirstNodeQueue(NodeQueue):

    def __init__(self, expander):
        self.nodes = []
        self.expander = expander

    def start(self, state):
        self.nodes = [Node(state)]

    def empty(self):
        return len(self.nodes) == 0

    def next(self):
        return heappop(self.nodes)

    def expand(self, parent):
        for s, c in self.expander(parent.state):
            heappush(self.nodes, parent.spawn_child(s, c))

