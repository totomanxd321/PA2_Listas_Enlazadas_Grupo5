import unittest
from app.estructuras import ListaSimple, ListaDoble, ListaCircular, Solicitud


def s(c):
    return Solicitud(c, "Asunto " + c)


class TestListaSimple(unittest.TestCase):
    def setUp(self):
        self.lista = ListaSimple()
        for codigo in ("A", "B", "C"):
            self.lista.insertar_final(s(codigo))

    def test_recorrido_y_tamano(self):
        self.assertEqual(self.lista.codigos(), ["A", "B", "C"])
        self.assertEqual(self.lista.tamano, 3)

    def test_insertar_inicio_final_y_despues(self):
        self.lista.insertar_inicio(s("X"))
        self.lista.insertar_final(s("Z"))
        self.assertTrue(self.lista.insertar_despues("B", s("Y")))
        self.assertEqual(self.lista.codigos(), ["X", "A", "B", "Y", "C", "Z"])
        self.assertEqual(self.lista.cola.dato.codigo, "Z")

    def test_insertar_despues_de_la_cola(self):
        self.assertTrue(self.lista.insertar_despues("C", s("D")))
        self.assertEqual(self.lista.cola.dato.codigo, "D")
        self.assertIsNone(self.lista.cola.siguiente)

    def test_insertar_despues_de_inexistente(self):
        self.assertFalse(self.lista.insertar_despues("NO", s("D")))
        self.assertEqual(self.lista.tamano, 3)

    def test_buscar_y_modificar(self):
        self.assertIsNone(self.lista.buscar("X"))
        self.assertTrue(self.lista.modificar("B", asunto="Resuelto", estado="Cerrado"))
        self.assertEqual(self.lista.buscar("B").dato.estado, "Cerrado")
        self.assertFalse(self.lista.modificar("X", estado="Cerrado"))

    def test_eliminar_cabeza_interior_y_cola(self):
        self.assertTrue(self.lista.eliminar("A"))
        self.assertTrue(self.lista.eliminar("B"))
        self.assertTrue(self.lista.eliminar("C"))
        self.assertEqual(self.lista.codigos(), [])
        self.assertIsNone(self.lista.cabeza)
        self.assertIsNone(self.lista.cola)
        self.assertEqual(self.lista.tamano, 0)

    def test_eliminar_interior_y_cola(self):
        self.assertTrue(self.lista.eliminar("B"))
        self.assertEqual(self.lista.codigos(), ["A", "C"])
        self.assertTrue(self.lista.eliminar("C"))
        self.assertEqual(self.lista.cola.dato.codigo, "A")
        self.assertIsNone(self.lista.cola.siguiente)
        self.assertFalse(self.lista.eliminar("NO"))

    def test_reubicar_cabeza_y_cola(self):
        self.assertTrue(self.lista.reubicar_despues("A", "C"))
        self.assertEqual(self.lista.codigos(), ["B", "C", "A"])
        self.assertEqual(self.lista.cola.dato.codigo, "A")
        self.assertTrue(self.lista.reubicar_despues("A", "B"))
        self.assertEqual(self.lista.codigos(), ["B", "A", "C"])
        self.assertEqual(self.lista.cola.dato.codigo, "C")

    def test_reubicar_posicion_actual_y_ausentes(self):
        self.assertTrue(self.lista.reubicar_despues("B", "A"))
        self.assertFalse(self.lista.reubicar_despues("A", "A"))
        self.assertFalse(self.lista.reubicar_despues("NO", "B"))
        self.assertFalse(self.lista.reubicar_despues("B", "NO"))
        self.assertEqual(self.lista.tamano, 3)

    def test_codigos_duplicados(self):
        with self.assertRaises(ValueError):
            self.lista.insertar_final(s("A"))
        with self.assertRaises(ValueError):
            self.lista.insertar_despues("A", s("B"))

    def test_vacia_y_un_nodo(self):
        l = ListaSimple()
        self.assertEqual(l.codigos(), [])
        self.assertFalse(l.eliminar("A"))
        l.insertar_inicio(s("A"))
        self.assertIs(l.cabeza, l.cola)
        self.assertTrue(l.eliminar("A"))
        self.assertEqual(l.tamano, 0)


class TestListaDoble(unittest.TestCase):
    def test_recorridos_vacia_y_tres_nodos(self):
        lista = ListaDoble()
        self.assertEqual(lista.recorrer_adelante(), [])
        self.assertEqual(lista.recorrer_atras(), [])
        for codigo in ("A", "B", "C"):
            lista.insertar_final(s(codigo))
        self.assertEqual(lista.recorrer_adelante(), ["A", "B", "C"])
        self.assertEqual(lista.recorrer_atras(), ["C", "B", "A"])
        self.assertIs(lista.cola.anterior.siguiente, lista.cola)
        self.assertIsNone(lista.cabeza.anterior)
        self.assertIsNone(lista.cola.siguiente)


class TestListaCircular(unittest.TestCase):
    def test_vacia_y_ciclos(self):
        lista = ListaCircular()
        self.assertEqual(lista.una_vuelta(), [])
        self.assertIsNone(lista.siguiente_revision())
        for codigo in ("A", "B", "C"):
            lista.insertar_final(s(codigo))
        self.assertEqual(lista.una_vuelta(), ["A", "B", "C"])
        self.assertIs(lista.cola.siguiente.siguiente.siguiente, lista.cola)
        self.assertEqual([lista.siguiente_revision() for _ in range(5)],
                         ["A", "B", "C", "A", "B"])


if __name__ == "__main__":
    unittest.main()
