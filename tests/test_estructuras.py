import unittest

from app.estructuras import (Cola, ColaLlenaError, ColaVaciaError, Pila,
                             PilaLlenaError, PilaVaciaError)


class TestPila(unittest.TestCase):
    def test_vacia_al_inicio(self):
        self.assertTrue(Pila().esta_vacia())

    def test_lifo(self):
        p = Pila()
        for x in (1, 2, 3):
            p.apilar(x)
        self.assertEqual([p.desapilar() for _ in range(3)], [3, 2, 1])

    def test_ver_tope_no_elimina(self):
        p = Pila()
        p.apilar("a")
        self.assertEqual(p.ver_tope(), "a")
        self.assertEqual(p.tamano(), 1)

    def test_desapilar_vacia(self):
        with self.assertRaises(PilaVaciaError):
            Pila().desapilar()

    def test_tope_vacia(self):
        with self.assertRaises(PilaVaciaError):
            Pila().ver_tope()

    def test_desbordamiento(self):
        p = Pila(2)
        p.apilar(1)
        p.apilar(2)
        with self.assertRaises(PilaLlenaError):
            p.apilar(3)


class TestCola(unittest.TestCase):
    def test_vacia_al_inicio(self):
        self.assertTrue(Cola().esta_vacia())

    def test_fifo(self):
        c = Cola()
        for x in (1, 2, 3):
            c.encolar(x)
        self.assertEqual([c.desencolar() for _ in range(3)], [1, 2, 3])

    def test_ver_frente_no_elimina(self):
        c = Cola()
        c.encolar("a")
        c.encolar("b")
        self.assertEqual(c.ver_frente(), "a")
        self.assertEqual(c.tamano(), 2)

    def test_desencolar_vacia(self):
        with self.assertRaises(ColaVaciaError):
            Cola().desencolar()

    def test_frente_vacia(self):
        with self.assertRaises(ColaVaciaError):
            Cola().ver_frente()

    def test_cola_llena(self):
        c = Cola(2)
        c.encolar(1)
        c.encolar(2)
        with self.assertRaises(ColaLlenaError):
            c.encolar(3)

    def test_circularidad(self):
        c = Cola(3)
        for x in (1, 2, 3):
            c.encolar(x)
        c.desencolar()
        c.encolar(4)  # reutiliza la posición liberada
        self.assertEqual([c.desencolar() for _ in range(3)], [2, 3, 4])


if __name__ == "__main__":
    unittest.main()
