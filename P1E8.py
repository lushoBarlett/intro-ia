from itertools import chain
from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitAll
from pprint import pprint
from random import choice

def cut(string, i):
    extract = string[i:i+2]
    rest = string[:i] + string[i+2:]
    return extract, rest

def paste(s, target, i):
    return target[:i] + s + target[i:]

def expand(string):
    for i in range(len(string) - 1):
        s, rest = cut(string, i)
        for j in range(len(string) + 1):
            yield paste(s, rest, j), 1

def misplaced_os(string: str):
    return string.lstrip("O").count("O")

agent = Agent("OXOXOXOX", "OOOOXXXX", AstarNodeQueue(expand, misplaced_os), VisitAll())
path, cost = agent.go()

pprint(path)
