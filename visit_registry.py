from abc import ABC, abstractmethod


class VisitRegistry(ABC):

    @abstractmethod
    def visit(self, node):
        pass

    @abstractmethod
    def __contains__(self, node):
        pass


class VisitAll(VisitRegistry):

    def __init__(self):
        self.set = set()

    def visit(self, node):
        self.set.add(node.state)

    def __contains__(self, node):
        return node.state in self.set


class VisitNone(VisitRegistry):

    def visit(self, node):
        pass

    def __contains__(self, node):
        return False


class VisitParent(VisitRegistry):

    def visit(self, node):
        pass

    def __contains__(self, node):
        return (
            node.parent is not None and
            node.parent.parent is not None and
            node.state == node.parent.parent.state
        )


class VisitAncestors(VisitRegistry):

    def visit(self, node):
        pass

    def __contains__(self, node):

        ancestor = node.parent

        while ancestor is not None:
            if ancestor.state == node.state:
                return True

        return False
