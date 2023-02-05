from itertools import chain
from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitAll
from pprint import pprint
from random import choice

def swap(configuration, i, j):
    configuration = list(configuration)
    configuration[i], configuration[j] = configuration[j], configuration[i]
    return "".join(configuration)

def expand(configuration):
    v = configuration.index("V")
    for i in range(max(0, v - 3), min(len(configuration), v + 4)):
        if i != v:
            yield swap(configuration, i, v), abs(i - v)

def swap_distance(configuration: str):
    return max(0, configuration.rindex("B") - configuration.index("N") + 1)

def final(configuration):
    return configuration.lstrip("B").lstrip("V").lstrip("B").count("B") == 0

agent = Agent("NNBBV", final, AstarNodeQueue(expand, swap_distance), VisitAll())
path, cost = agent.go()

pprint(path)
