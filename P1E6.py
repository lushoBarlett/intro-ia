from itertools import chain
from agent import Agent
from node_queue import DFSNodeQueue, AstarNodeQueue, HillClimbing
from visit_registry import VisitAll
from pprint import pprint

edges = [
    ("A", "B", 1),
    ("B", "C", 2),
    ("B", "D", 5),
    ("B", "G1", 21),
    ("C", "E", 7),
    ("D", "F", 6),
    ("D", "G2", 11),
    ("E", "D", 3),
    ("E", "F", 10),
    ("F", "G2", 3),
    ("G1", "F", 7),
    ("G2", "F", 2),
    ("I", "B", 4),
    ("I", "C", 1),
]

def expand(state, h):
    return ((state2, cost, h(state2)) for state1, state2, cost in edges if state1 == state)

def final(state):
    return state in ("G1", "G2")

def h(state):
    return {
        "A": 13,
        "B": 11,
        "C": 14,
        "D": 4,
        "E": 14,
        "F": 3,
        "G1": 0,
        "G2": 0,
        "I": 15,
    }[state]

agent = Agent("I", final, DFSNodeQueue(expand), VisitAll())
path, cost = agent.go()

print("DFS")
pprint(path)

agent = Agent("I", final, AstarNodeQueue(expand, h), VisitAll())
path, cost = agent.go()

print("A*")
pprint(path)

agent = Agent("I", final, HillClimbing(expand, h), VisitAll())
path, cost = agent.go()

print("HC")
pprint(path)

