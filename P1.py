def t(nodo, i, j):
    return tuple([nodo[j] if n == i else nodo[i] if n == j else nodo[n] for n in range(len(nodo))])

def swap_up(pos, nodo):
    if pos < 3:
        return []

    return [t(nodo, pos, pos - 3)]

def swap_down(pos, nodo):
    if pos > 5:
        return []

    return [t(nodo, pos, pos + 3)]

def swap_left(pos, nodo):
    if pos % 3 == 0:
        return []

    return [t(nodo, pos, pos - 1)]

def swap_right(pos, nodo):
    if pos % 3 == 2:
        return []

    return [t(nodo, pos, pos + 1)]

def zeroPos(nodo):
    for i, x in enumerate(nodo):
        if x == 0:
            return i

def expandir(nodo):
    z = zeroPos(nodo)
    return swap_up(z, nodo) + swap_right(z, nodo) + swap_down(z, nodo) + swap_left(z, nodo)

inicial = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5,
)

final = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5,
)

visitados = set()
nodos = [inicial]

camino = []

from pprint import pprint

while len(nodos) > 0:
    nodo = nodos.pop()

    if nodo in visitados:
        continue

    visitados.add(nodo)
    camino.append(nodo)

    if nodo == final:
        break

    nodos += expandir(nodo)

pprint(camino)
