"""Orientación en un campus didáctico. Ejecutar con Python 3.8 o superior."""
from collections import deque
from heapq import heappop, heappush
from math import hypot, inf
from unicodedata import normalize, combining

NOMBRES = {"L": "Laboratorio", "E": "Entrada", "P": "Patio",
           "A": "Administración", "C": "Cafetería", "B": "Biblioteca"}
POS = {"E": (0, 0), "A": (0, 2), "B": (2, 0), "C": (3, 0),
       "L": (4, 0), "P": (1, 3)}
TRAMOS = [("E", "A", 6), ("A", "L", 8), ("E", "B", 2),
          ("B", "C", 1), ("C", "L", 1), ("A", "P", 2), ("P", "C", 5)]
GRAFO = {n: {} for n in NOMBRES}
for u, v, minutos in TRAMOS:
    GRAFO[u][v] = GRAFO[v][u] = minutos


def clave(texto):
    return "".join(c for c in normalize("NFD", texto.strip().casefold())
                   if not combining(c))


def ordenar(ids):
    if len(ids) <= 1:
        return ids[:]
    medio = len(ids) // 2
    izq, der = ordenar(ids[:medio]), ordenar(ids[medio:])
    i = j = 0
    salida = []
    while i < len(izq) and j < len(der):
        if clave(NOMBRES[izq[i]]) <= clave(NOMBRES[der[j]]):
            salida.append(izq[i])
            i += 1
        else:
            salida.append(der[j])
            j += 1
    return salida + izq[i:] + der[j:]


def buscar(ids, nombre):
    objetivo = clave(nombre)

    def visitar(inicio, fin):
        if inicio > fin:
            return None
        medio = (inicio + fin) // 2
        actual = clave(NOMBRES[ids[medio]])
        if objetivo == actual:
            return ids[medio]
        if objetivo < actual:
            return visitar(inicio, medio - 1)
        return visitar(medio + 1, fin)

    return visitar(0, len(ids) - 1)


def dfs(grafo, inicio):
    vistos, orden = set(), []

    def visitar(n):
        vistos.add(n)
        orden.append(n)
        for vecino in sorted(grafo[n]):
            if vecino not in vistos:
                visitar(vecino)

    visitar(inicio)
    return orden


def ruta(padres, n):
    camino = []
    while n is not None:
        camino.append(n)
        n = padres[n]
    return camino[::-1]


def bfs(grafo, inicio, meta):
    cola = deque([inicio])
    padres = {inicio: None}
    while cola:
        n = cola.popleft()
        if n == meta:
            return ruta(padres, n)
        for vecino in sorted(grafo[n]):
            if vecino not in padres:
                padres[vecino] = n
                cola.append(vecino)
    return []


def heuristica(n, meta):
    x, y = POS[n]
    a, b = POS[meta]
    return hypot(x - a, y - b)


def a_estrella(grafo, inicio, meta):
    costos, padres = {inicio: 0}, {inicio: None}
    cola = [(heuristica(inicio, meta), 0, inicio)]
    while cola:
        _, g, n = heappop(cola)
        if g != costos[n]:
            continue
        if n == meta:
            return ruta(padres, n)
        for vecino, peso in grafo[n].items():
            nuevo = g + peso
            if nuevo < costos.get(vecino, inf):
                costos[vecino], padres[vecino] = nuevo, n
                heappush(cola, (nuevo + heuristica(vecino, meta), nuevo, vecino))
    return []


def tiempo(camino):
    return sum(GRAFO[a][b] for a, b in zip(camino, camino[1:]))


if __name__ == "__main__":
    ids = ordenar(list(NOMBRES))
    print("Directorio:", ", ".join(NOMBRES[i] for i in ids))
    for nombre in ("laboratorio", "Auditorio"):
        print("Consulta", nombre, "=>", buscar(ids, nombre) or "Sin coincidencia")
    print("DFS desde Entrada:", " -> ".join(dfs(GRAFO, "E")))
    for etiqueta, algoritmo in [("BFS", bfs), ("A*", a_estrella)]:
        camino = algoritmo(GRAFO, "E", "L")
        print(etiqueta, " -> ".join(camino), "|", len(camino)-1, "tramos |", tiempo(camino), "min")
