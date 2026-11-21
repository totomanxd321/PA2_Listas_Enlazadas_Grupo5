import unittest
from itertools import permutations
from campus import (GRAFO, NOMBRES, ordenar, buscar, dfs, bfs, a_estrella,
                    heuristica, tiempo)


class CampusTest(unittest.TestCase):
    def test_orden(self):
        for entrada in permutations(NOMBRES):
            self.assertEqual(ordenar(list(entrada)), list("ABCELP"))

    def test_consulta(self):
        ids = ordenar(list(NOMBRES))
        for n, nombre in NOMBRES.items():
            self.assertEqual(buscar(ids, nombre), n)
        self.assertEqual(buscar(ids, "  ADMINISTRACION "), "A")
        self.assertIsNone(buscar(ids, "Auditorio"))
        self.assertIsNone(buscar(ordenar([]), "Entrada"))

    def test_recorrido(self):
        self.assertEqual(dfs(GRAFO, "E"), list("EALCBP"))

    def test_rutas(self):
        self.assertEqual(bfs(GRAFO, "E", "L"), list("EAL"))
        self.assertEqual(a_estrella(GRAFO, "E", "L"), list("EBCL"))

    def test_sin_paso(self):
        aislado = {"E": {}, "L": {}}
        for algoritmo in (bfs, a_estrella):
            self.assertEqual(algoritmo(aislado, "E", "L"), [])

    def test_consistencia(self):
        for meta in GRAFO:
            for a in GRAFO:
                for b, peso in GRAFO[a].items():
                    self.assertLessEqual(heuristica(a, meta), peso + heuristica(b, meta) + 1e-9)

    def test_optimos_todos_los_pares(self):
        # Oráculo independiente: enumeración exhaustiva de caminos simples.
        def caminos(actual, meta, camino):
            if actual == meta:
                yield camino
            else:
                for vecino in GRAFO[actual]:
                    if vecino not in camino:
                        yield from caminos(vecino, meta, camino + [vecino])

        for inicio in GRAFO:
            for meta in GRAFO:
                opciones = list(caminos(inicio, meta, [inicio]))
                self.assertEqual(tiempo(a_estrella(GRAFO, inicio, meta)), min(map(tiempo, opciones)))
                self.assertEqual(len(bfs(GRAFO, inicio, meta)), min(map(len, opciones)))


if __name__ == "__main__":
    unittest.main()
