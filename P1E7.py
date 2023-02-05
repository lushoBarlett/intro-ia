from itertools import chain
from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitAll
from pprint import pprint
from random import choice

forbidden = [(2, 1), (4, 1), (2, 2)]

def final(robot):
    x, y, o = robot
    return x == y == 5

"""
1,1  x->

y    .
|       .
v          .
             5,5
"""

def movement(robot):
    x, y, o = robot

    if o == 'N' and y > 1 and (x, y - 1) not in forbidden:
        yield (x, y - 1, o)

    if o == 'S' and y < 5 and (x, y + 1) not in forbidden:
        yield (x, y + 1, o)

    if o == 'O' and x > 1 and (x - 1, y) not in forbidden:
        yield (x - 1, y, o)

    if o == 'E' and x < 5 and (x + 1, y) not in forbidden:
        yield (x + 1, y, o)

def rotation(robot):
    x, y, o = robot

    if o == 'N':
        yield (x, y, 'E')

    if o == 'E':
        yield (x, y, 'S')

    if o == 'S':
        yield (x, y, 'O')

    if o == 'O':
        yield (x, y,'N')

def expand(robot):
    return chain(
        ((m, 2) for m in movement(robot)),
        ((r, 1) for r in rotation(robot)),
    )

def manhattan(robot):
    x, y, o = robot
    return abs(x - 5) + abs(y - 5)

agent = Agent((1, 1, 'N'), final, AstarNodeQueue(expand, manhattan), VisitAll())
path, cost = agent.go()

pprint(path)

agent = Agent((3, 4, choice("NSEO")), final, AstarNodeQueue(expand, manhattan), VisitAll())
path, cost = agent.go()

pprint(path)
