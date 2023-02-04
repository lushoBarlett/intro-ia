from abc import ABC, abstractmethod
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
        self.nodes = []
        self.expander = expander

    def start(self, state):
        self.nodes = [Node(state)]

    def empty(self):
        return self.nodes == []

    def next(self):
        return self.nodes.pop()

    def expand(self, parent):
        nextStates = self.expander(parent.state)
        self.nodes += [Node(s, parent) for s in nextStates]


class BFSNodeQueue(NodeQueue):

    def __init__(self, expander):
        self.nodes = []
        self.expander = expander

    def start(self, state):
        self.nodes = [Node(state)]

    def empty(self):
        return self.nodes == []

    def next(self):
        return self.nodes.pop(0)

    def expand(self, parent):
        nextStates = self.expander(parent.state)
        self.nodes += [Node(s, parent) for s in nextStates]

