from node import Node

class Agent:

    def __init__(self, initial, final, node_queue, visit_registry, max_depth = None):
        self.initial = initial
        self.final = final
        self.node_queue = node_queue
        self.visit_registry = visit_registry
        self.max_depth = max_depth

    def final_state(self, node):
        return node.state == self.final

    def over_depth_limit(self, node):
        return self.max_depth is not None and self.max_depth < node.depth

    def next(self):
        if self.node_queue.empty():
            return None

        node = self.node_queue.next()

        while node in self.visit_registry or self.over_depth_limit(node):
            if self.node_queue.empty():
                return None

            node = self.node_queue.next()

        return node

    def go(self):

        self.node_queue.start(self.initial)

        current = None
        while current is None or not self.final_state(current):
            current = self.next()
            self.visit_registry.visit(current)
            self.node_queue.expand(current)

        return Node.trace_path(current), current.total_cost()
