from itertools import chain
from agent import Agent
from node_queue import AstarNodeQueue
from visit_registry import VisitNone, VisitAll
from pprint import pprint

edges = [
    ("Oradea", "Zerind", 71),
    ("Oradea", "Sibiu", 151),
    ("Zerind", "Arad", 75),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Sibiu", "Faragas", 99),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Rimnicu Vilcea", "Craiova", 146),
    ("Craiova", "Pitesti", 138),
    ("Pitesti", "Bucharest", 101),
    ("Faragas", "Bucharest", 211),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Urziceni", "Vaslui", 142),
    ("Hirsova", "Eforie", 86),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

def expand_city(city, h):
    return chain(
        ((city2, cost, h(city2)) for city1, city2, cost in edges if city1 == city),
        ((city1, cost, h(city1)) for city1, city2, cost in edges if city2 == city),
    )

visit_strategy = VisitNone()

city_queue = AstarNodeQueue(expand_city)
agent = Agent("Arad", "Bucharest", city_queue, visit_strategy)
path, cost = agent.go()

pprint(path)


def hline(city):
    return {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Dobreta": 242,
        "Eforie": 161,
        "Faragas": 178,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 98,
        "Rimnicu Vilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374,
    }[city]

city_queue = AstarNodeQueue(expand_city, hline)
agent = Agent("Arad", "Bucharest", city_queue, VisitNone())
path, cost = agent.go()

pprint(path)

