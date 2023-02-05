from itertools import chain
from agent import Agent
from node import Node
from node_queue import DFSNodeQueue, AstarNodeQueue
from visit_registry import VisitParent

def t(grid, i, j):
    grid = list(grid)
    grid[i], grid[j] = grid[j], grid[i]
    return tuple(grid)

def swap_up(pos, grid):
    if pos >= 3:
        yield t(grid, pos, pos - 3)

def swap_down(pos, grid):
    if pos < 6:
        yield t(grid, pos, pos + 3)

def swap_left(pos, grid):
    if pos % 3 > 0:
        yield t(grid, pos, pos - 1)

def swap_right(pos, grid):
    if pos % 3 < 2:
        yield t(grid, pos, pos + 1)

def expand_grid(grid, h):
    z = grid.index(0)

    grid_states = chain(
        swap_up(z, grid),
        swap_right(z, grid),
        swap_down(z, grid),
        swap_left(z, grid),
    )

    return ((s, 1, h(s)) for s in grid_states)

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

visit_strategy = VisitParent()
configurations = 9*8*7*6*5*4*3*2*1

grid_queue = DFSNodeQueue(expand_grid)
agent = Agent(initial, final, grid_queue, visit_strategy, max_depth=configurations)
path, cost = agent.go()

if path is None:
    print("No hay camino")
    exit(1)

print(f"Movimientos totales: {len(path) - 1}")
print(f"Costo: {cost}")


def h1(grid):
    return sum(int(i != grid.index(x)) for i, x in enumerate(final) if x != 0)


grid_queue = AstarNodeQueue(expand_grid, h1)
agent = Agent(initial, final, grid_queue, visit_strategy)
path, cost = agent.go()

if path is None:
    print("No hay camino")
    exit(1)

print(f"Movimientos totales: {len(path) - 1}")
print(f"Costo: {cost}")


def h2(grid):

    def mdist(i, j):
        hdist = abs(i % 3 - j % 3)
        vdist = abs(i // 3 - j // 3)
        return hdist + vdist

    return sum(mdist(i, grid.index(x)) for i, x in enumerate(final) if x != 0)


grid_queue = AstarNodeQueue(expand_grid, h2)
agent = Agent(initial, final, grid_queue, visit_strategy)
path, cost = agent.go()

if path is None:
    print("No hay camino")
    exit(1)

print(f"Movimientos totales: {len(path) - 1}")
print(f"Costo: {cost}")
