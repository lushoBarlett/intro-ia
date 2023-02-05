from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitNone
from pprint import pprint

stack = 7

def expand(stacks):
    expandable, ones, twos = stacks
    for i, s in enumerate(expandable):
        for cut in range(1, s // 2 + 1):
            if cut != s - cut:
                new = [cut, s - cut]
                cost = stack if 2 in new else 1
                new_expandable = expandable[:i] + [s for s in new if s > 2] + expandable[i+1:]
                new_ones = sum(s == 1 for s in new)
                new_twos = sum(s == 2 for s in new)
                yield (new_expandable, ones + new_ones, twos + new_twos), cost

def max_stack(stacks):
    expandable, ones, twos = stacks

    if expandable == []:
        return 0

    return max(0, max(expandable) - 2)

def final(stacks):
    expandable, ones, twos = stacks
    return expandable == []

initial = ([stack], 0, 0)
agent = Agent(initial, final, AstarNodeQueue(expand, max_stack), VisitNone())
path, cost = agent.go()

pprint(path)

