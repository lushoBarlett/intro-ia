def t(grid, i, j):
    return tuple([grid[j] if n == i else grid[i] if n == j else grid[n] for n in range(len(grid))])

def swap_up(pos, grid):
    if pos < 3:
        return []

    return [t(grid, pos, pos - 3)]

def swap_down(pos, grid):
    if pos > 5:
        return []

    return [t(grid, pos, pos + 3)]

def swap_left(pos, grid):
    if pos % 3 == 0:
        return []

    return [t(grid, pos, pos - 1)]

def swap_right(pos, grid):
    if pos % 3 == 2:
        return []

    return [t(grid, pos, pos + 1)]

def zeroPos(grid):
    for i, x in enumerate(grid):
        if x == 0:
            return i

from agent import Agent, Node

class DFSGridQueue:
    def __init__(self, state):
        self.nodes = [Node(state)]

    def empty(self):
        return self.nodes == []

    def next(self):
        return self.nodes.pop()

    def expand(self, parent):

        grid = parent.state

        z = zeroPos(grid)

        nextGrids = (
            swap_up(z, grid) +
            swap_right(z, grid) +
            swap_down(z, grid) +
            swap_left(z, grid)
        )

        self.nodes += [Node(g, parent) for g in nextGrids]

initial = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5,
)

final = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5,
)

agent = Agent(initial, final, DFSGridQueue(initial))

result = agent.transition()
while result is None:
    result = agent.transition()

print(f"Costo total: {len(result) - 1}")
