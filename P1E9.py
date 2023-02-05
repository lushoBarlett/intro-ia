from itertools import chain
from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitAll
from pprint import pprint
from random import choice

def expand(register):
    if register % 3:
        yield 1, 1
        yield register * 2, register
        yield register + 1, 1
        yield register - 1, 1
    else:
        yield register // 3, 2 * register // 3

def distance(register):
    return abs(register - 7)

agent = Agent(1, 7, AstarNodeQueue(expand, distance), VisitAll())
path, cost = agent.go()

pprint(path)
